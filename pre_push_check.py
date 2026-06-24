#!/usr/bin/env python3
"""发布前机械闸门 —— 扫描 git 追踪文件中的禁止模式，任一命中即阻断 push。

设计原则：
  - 确定性：正则匹配，不依赖 LLM 注意力
  - 边界尊重：只扫描 git 追踪的文件（.gitignore 已定义发布边界）
  - 可扩充：每次裸审/审查发现新类型 → 回写进 FORBIDDEN 列表
  - 零误报占位符：C:/Users/X 等已知占位符显式排除

用法：
  python pre_push_check.py           # 扫描全部规则
  python pre_push_check.py --quiet   # 仅输出命中（给 git hook 用）
  python pre_push_check.py --list    # 列出当前规则但不扫描

集成 git pre-push hook：
  .git/hooks/pre-push:
    #!/bin/sh
    PYTHONIOENCODING=utf-8 python pre_push_check.py || exit 1
"""

import sys
import os
import re
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

# 自排除 —— 本脚本自身的正则定义中包含模式示例，不是泄露
SELF_EXCLUDE = {'pre_push_check.py'}

# ── 本机特定值（从环境变量读取，不在代码中硬编码）───────
# 用法：PRE_PUSH_PATH_PREFIX="<PATH_PREFIX>" PRE_PUSH_USERNAME="<USERNAME>" python pre_push_check.py
# 真实值从私有 shell 环境注入，不在代码中硬编码
# 传纯文本前缀和用户名，脚本自动构造覆盖多种斜杠方向的正则
_USER_PATH_ROOT = re.compile(
    r'[A-Z]:/Users/(?!X\b)[^/\\\s"\']+|'
    r'[A-Z]:\\Users\\(?!X\\b)[^/\\\s"\']+|'
    r'/c/Users/(?!X\b)[^/\\\s"\']+'
)

def _build_path_re(prefix: str) -> str:
    """从纯文本前缀构造匹配正/反斜杠的正则。"""
    if not prefix:
        return r'(?!)'
    p = re.escape(prefix)
    return p.replace(r'/', r'[/\\\\]')

_PATH_RAW = os.environ.get('PRE_PUSH_PATH_PREFIX', '')
_USER_RAW = os.environ.get('PRE_PUSH_USERNAME', '')
_PROJECT_PATH = re.compile(_build_path_re(_PATH_RAW) if _PATH_RAW else r'(?!)')
_USERNAME_PATTERN = re.compile(r'\b' + re.escape(_USER_RAW) + r'\b' if _USER_RAW else r'(?!)')

# ── 禁止模式 ───────────────────────────────────────────
# 格式: (编译后的正则, 规则名, 严重度: BLOCKER/WARN)
# 每次裸审发现新泄露类型 → 在此追加规则
# 注意：本机特定值通过环境变量注入，不在代码中硬编码
FORBIDDEN = [
    # === 本机绝对路径（特定值来自环境变量） ===
    (_PROJECT_PATH,                                                '本机项目绝对路径',                 'BLOCKER'),
    (_USER_PATH_ROOT,                                              'Windows用户目录',                  'BLOCKER'),

    # === 个人标识（特定值来自环境变量） ===
    (_USERNAME_PATTERN,                                            'Windows用户名',                    'BLOCKER'),

    # === 联系方式 ===
    (re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'), '邮箱地址',                         'BLOCKER'),

    # === 敏感凭据 ===
    (re.compile(r'(?i)(api[_-]?key|api[_-]?secret|access[_-]?token|auth[_-]?token|private[_-]?key)\s*[:=]\s*["\'][A-Za-z0-9_\-]{8,}["\']'),
                                                                   '疑似API凭据硬编码',                  'BLOCKER'),
    (re.compile(r'(?i)(password|passwd|pwd)\s*[:=]\s*["\'][^"\']+["\']'), '疑似密码硬编码',             'BLOCKER'),
    (re.compile(r'(?i)\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,}\b'), 'GitHub个人访问令牌',              'BLOCKER'),

    # === 环境文件 ===
    (re.compile(r'\.env$'),                                        '.env文件',                          'BLOCKER'),
]

# 已知安全占位符 —— 这些命中不报
KNOWN_PLACEHOLDERS = [
    re.compile(r'C:/Users/X\b'),        # retrospect 中的转义层级示例
    re.compile(r'C:\\Users\\X\b'),
]


def _is_excluded_placeholder(line: str) -> bool:
    """判断整行是否仅是已知安全占位符的合法使用。"""
    return any(p.search(line) for p in KNOWN_PLACEHOLDERS)


def get_tracked_files() -> list[str]:
    """返回 git 追踪的文件列表（相对路径）。优先用 git add --dry-run。"""
    # git add --dry-run 最可靠 —— 它就是 git 实际会追踪的文件集合
    result = subprocess.run(
        ['git', 'add', '--dry-run', '.'],
        capture_output=True, text=True, cwd=str(PROJECT_ROOT),
        encoding='utf-8', errors='replace'
    )
    lines = result.stdout.strip().split('\n')
    files = []
    for line in lines:
        if line.startswith("add '") and line.endswith("'"):
            files.append(line[5:-1])
        elif line.startswith('add "') and line.endswith('"'):
            files.append(line[5:-1])
    return files


def scan_file(filepath: str, quiet: bool) -> list[tuple[int, str, str, str]]:
    """扫描单个文件，返回命中列表 [(行号, 行内容, 规则名, 严重度), ...]."""
    hits = []
    full_path = PROJECT_ROOT / filepath

    # 跳过二进制/大文件
    if filepath.endswith(('.docx', '.png', '.jpg', '.emf', '.pdf', '.svg', '.pyc')):
        return hits

    try:
        with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
    except (OSError, UnicodeDecodeError):
        return hits

    for lineno, line in enumerate(lines, 1):
        if _is_excluded_placeholder(line):
            continue
        for pattern, rule_name, severity in FORBIDDEN:
            if pattern.search(line):
                hits.append((lineno, line.rstrip('\n'), rule_name, severity))

    return hits


def main():
    quiet = '--quiet' in sys.argv

    if '--list' in sys.argv:
        print("当前禁止规则：")
        for _, name, sev in FORBIDDEN:
            print(f"  [{sev}] {name}")
        print(f"\n已知占位符（不触发）：")
        for p in KNOWN_PLACEHOLDERS:
            print(f"  {p.pattern}")
        return 0

    if not quiet:
        print("=" * 60)
        print("pre_push_check —— 发布前机械闸门")
        print(f"项目: {PROJECT_ROOT}")
        print("=" * 60)

    # 获取 git 追踪文件
    tracked = get_tracked_files()
    if not quiet:
        print(f"\n扫描范围: {len(tracked)} 个 git 追踪文件")
        print(f"禁止规则: {len(FORBIDDEN)} 条\n")

    all_hits: dict[str, list] = {}  # filepath -> hits
    total = 0
    blocker_count = 0

    for filepath in tracked:
        if filepath in SELF_EXCLUDE:
            continue
        hits = scan_file(filepath, quiet)
        if hits:
            all_hits[filepath] = hits
            total += len(hits)
            blocker_count += sum(1 for _, _, _, s in hits if s == 'BLOCKER')

    # 输出结果
    if not all_hits:
        if not quiet:
            print("✅ 零命中 —— 机械闸门通过")
        return 0

    print(f"\n❌ 发现 {total} 处命中（{blocker_count} BLOCKER）分布在 {len(all_hits)} 个文件：\n")

    for filepath, hits in sorted(all_hits.items()):
        print(f"  📄 {filepath}")
        for lineno, line, rule_name, severity in hits:
            tag = "🔴" if severity == 'BLOCKER' else "🟡"
            preview = line[:120] + ("…" if len(line) > 120 else "")
            print(f"     {tag} L{lineno} [{rule_name}]")
            if not quiet:
                print(f"        {preview}")
        print()

    # 区分 WARN 和 BLOCKER
    if blocker_count > 0:
        print(f"⛔ 机械闸门阻断：{blocker_count} 个 BLOCKER 项必须修复后才能 push。")
        print(f"   如确认为误报，请在 pre_push_check.py 的 KNOWN_PLACEHOLDERS 中添加排除规则。")
        return 1
    else:
        print(f"⚠️  {total} 个 WARN 项（不阻断 push，但建议处理）。")
        return 0


if __name__ == '__main__':
    sys.exit(main())

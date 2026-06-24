#!/usr/bin/env python
"""版本一致性验证脚本 —— 发布前硬门

验证范围：
  Layer 1（框架版本一致性——必须全部 PASS）：
    - VERSION 文件
    - 主 MD 版本头
    - 主 JSON metadata.version
    - README.md 版本声明
    - project.yaml version.number
    - reference_files.md 版本引用
    - project_status.md 阶段声明
    - docx core.xml 版本（如可读）

  Layer 2（配套文件 md/json 版本一致性——必须全部 PASS）：
    - _protocols-and-tools/ 下所有 .md/.json 配对文件
    - _research/ 下所有 .md/.json 配对文件
    - _archive/ 下所有 .md/.json 配对文件（可选，--skip-archive 跳过）

用法: python verify_version_consistency.py [--fix] [--skip-archive] [--verbose]
  --fix           尝试自动修复可修复的不一致（实验性，默认仅报告）
  --skip-archive  跳过 _archive/ 目录的配对检查
  --verbose       显示所有 PASS 项详情（默认只显示 FAIL 和摘要）

变更记录:
  2026-06-24 (Claude Opus 4.8 via Claude Code CLI): project_status.md 版本检测正则
    `v?(\\d+\\.\\d+\\.\\d+)` → `v(\\d+\\.\\d+\\.\\d+)`（v 前缀改为必需），
    修复章节号（如 §13.1.2）被误判为版本号导致的假 FAIL。
"""

import sys, os, re, json, zipfile
from pathlib import Path

# 强制 UTF-8 输出，解决 Windows/PowerShell GBK 编码问题
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PROJECT = Path(__file__).parent
EXPECTED_VERSION = None
VERBOSE = False


def read_file(path):
    try:
        return (PROJECT / path).read_text(encoding='utf-8')
    except Exception as e:
        return f"<ERROR: {e}>"


def find_version_in_text(text, patterns=None):
    """在文本中搜索版本号，返回 (行号, 匹配行, 版本号) 列表"""
    if patterns is None:
        patterns = [
            r'v?(\d+\.\d+(?:\.\d+)?)',       # 语义版本 (X.Y 或 X.Y.Z)
            r'version[:\s]+"?v?(\d+\.\d+(?:\.\d+)?)',  # version字段
        ]
    results = []
    for i, line in enumerate(text.split('\n'), 1):
        for pat in patterns:
            m = re.search(pat, line, re.IGNORECASE)
            if m:
                ver = m.group(1)
                results.append((i, line.strip(), ver))
                break
    return results


def extract_md_version(text):
    """从 .md 文件中提取文档自身版本号（非框架版本引用）"""
    ver_two = r'v?(\d+\.\d+)'           # X.Y
    ver_three = r'v?(\d+\.\d+\.\d+)'    # X.Y.Z

    # 优先级1：显式 "版本" 声明行（表格或键值格式）
    decl_patterns = [
        # 表格格式：| **版本** | v1.0.4 |
        rf'\|\s*\*\*版本\*\*\s*\|\s*({ver_three}(?:\+)?)',
        rf'\|\s*\*\*版本\*\*\s*\|\s*({ver_two}(?:\+)?)',
        # 键值格式：**版本**：v1.0.4
        rf'\*\*版本\*\*[：:]\s*({ver_three}(?:\+)?)',
        rf'\*\*版本\*\*[：:]\s*({ver_two}(?:\+)?)',
        # 简化格式：版本：v0.4
        rf'版本[：:]\s*({ver_three}(?:\+)?)',
        rf'版本[：:]\s*({ver_two}(?:\+)?)',
    ]
    for pat in decl_patterns:
        m = re.search(pat, text[:3000])
        if m:
            return m.group(1)

    # 优先级2：表格第一列为版本号
    for vp in [ver_three, ver_two]:
        m = re.search(rf'^\|\s*{vp}(?:\+)?\s*\|', text[:3000], re.MULTILINE)
        if m:
            return m.group(1)

    # 回退：取第一个版本号，跳过明显是框架/模型引用
    for lineno, line in enumerate(text[:2000].split('\n'), 1):
        m = re.search(rf'({ver_three}|{ver_two})', line)
        if not m:
            continue
        ver = m.group(1)
        # 跳过框架更新/配套引用（"v1.6.4 框架配套更新"）
        if re.search(r'框架.*(?:更新|配套)', line):
            continue
        # 跳过模型版本（"GPT-5.5"、"v5.5" 单独出现）
        if re.search(r'GPT|ChatGPT|模型.*版本', line, re.IGNORECASE):
            continue
        # 跳过纯数字型版本引用（如 §9.2 被误提取为 v9.2）
        if re.match(r'^\d+\.\d+$', ver) and '§' in line:
            continue
        return ver

    return None


def check_version(expected, found, source_name, detail=""):
    """检查版本是否一致（容忍前导v和后缀+）"""
    found_n = found.lstrip('v').rstrip('+')
    expected_n = expected.lstrip('v').rstrip('+')
    if found_n == expected_n:
        flags = []
        if found != expected:
            if found.lstrip('v') != found_n:
                flags.append('v-prefix')
            if found.endswith('+') != expected.endswith('+'):
                flags.append('+-suffix')
            detail = f" ({', '.join(flags)} diff OK)" + detail
        return True, f"  PASS: {source_name} = {found}{detail}"
    else:
        return False, f"  FAIL: {source_name} = {found} (expected {expected}){detail}"


def check_paired_files(directory, results):
    """检查目录下 .md/.json 配对文件的版本一致性"""
    dir_path = PROJECT / directory
    if not dir_path.exists():
        return

    md_files = {}
    json_files = {}

    for f in dir_path.rglob("*.md"):
        rel = str(f.relative_to(PROJECT))
        stem = f.stem
        md_files[stem] = rel
    for f in dir_path.rglob("*.json"):
        rel = str(f.relative_to(PROJECT))
        stem = f.stem
        json_files[stem] = rel

    # 查找配对
    paired = set(md_files.keys()) & set(json_files.keys())

    for stem in sorted(paired):
        md_rel = md_files[stem]
        json_rel = json_files[stem]

        # 读取 .md 版本
        md_text = read_file(md_rel)
        md_ver = extract_md_version(md_text)

        # 读取 .json 版本
        try:
            with open(PROJECT / json_rel, 'r', encoding='utf-8') as f:
                jd = json.load(f)
            json_ver = jd.get('metadata', {}).get('version', None)
        except Exception as e:
            results.append((f"{md_rel} ↔ {json_rel}", False, f"  FAIL: JSON读取失败: {e}"))
            continue

        # 检查
        if md_ver and json_ver:
            ok, msg = check_version(md_ver, json_ver, f"{md_rel} (v{md_ver}) ↔ {json_rel} ({json_ver})")
        elif md_ver and not json_ver:
            ok, msg = False, f"  FAIL: {md_rel}=v{md_ver} but {json_rel} has NO version in metadata"
        elif not md_ver and json_ver:
            ok, msg = False, f"  FAIL: {json_rel}=v{json_ver} but {md_rel} has NO detectable version"
        else:
            ok, msg = False, f"  FAIL: {md_rel} ↔ {json_rel}: neither has detectable version"

        results.append((f"pair:{stem}", ok, msg))
        if VERBOSE or not ok:
            print(msg)

    # 报告未配对的
    md_only = set(md_files.keys()) - paired
    json_only = set(json_files.keys()) - paired
    if VERBOSE and (md_only or json_only):
        for stem in sorted(md_only):
            print(f"  INFO: {md_files[stem]} has no .json counterpart (skip)")
        for stem in sorted(json_only):
            print(f"  INFO: {json_files[stem]} has no .md counterpart (skip)")


def main():
    global EXPECTED_VERSION, VERBOSE

    skip_archive = '--skip-archive' in sys.argv
    VERBOSE = '--verbose' in sys.argv

    # Step 0: 读取 VERSION
    version_file = PROJECT / "VERSION"
    if not version_file.exists():
        print("FATAL: VERSION file missing")
        return 1

    EXPECTED_VERSION = version_file.read_text(encoding='utf-8').strip()
    print(f"Expected framework version: {EXPECTED_VERSION}")
    print(f"Project root: {PROJECT}\n")

    results = []

    # ============================================================
    # Layer 1: 框架版本一致性
    # ============================================================
    print("─" * 60)
    print("Layer 1: 框架版本一致性（全部必须与 VERSION 匹配）")
    print("─" * 60)

    # 1. 主 MD 版本头
    md_text = read_file("AI协作项目全生命周期框架.md")
    md_hits = find_version_in_text(md_text[:2000])
    if md_hits:
        ok, msg = check_version(EXPECTED_VERSION, md_hits[0][2], "主MD版本头")
    else:
        ok, msg = False, "  FAIL: 主MD版本头: 未找到版本号"
    results.append(("L1:主MD版本头", ok, msg))
    print(msg)

    # 2. JSON metadata.version
    try:
        with open(PROJECT / "AI协作项目全生命周期框架.json", 'r', encoding='utf-8') as f:
            j = json.load(f)
        json_ver = j.get('metadata', {}).get('version', 'MISSING')
        ok, msg = check_version(EXPECTED_VERSION, json_ver, "主JSON metadata.version")
    except Exception as e:
        ok, msg = False, f"  FAIL: 主JSON metadata.version: {e}"
    results.append(("L1:主JSON", ok, msg))
    print(msg)

    # 3. JSON revision
    json_rev = j.get('metadata', {}).get('revision', 'N/A')
    if json_rev != 'N/A':
        rev_ver_match = re.search(r'v?(\d+\.\d+\.\d+)', str(json_rev))
        if rev_ver_match:
            ok, msg = check_version(EXPECTED_VERSION, rev_ver_match.group(1), "主JSON metadata.revision")
            results.append(("L1:主JSON.revision", ok, msg))
            print(msg)

    # 4. README.md
    readme_text = read_file("README.md")
    readme_ver = re.search(r'\*\*版本\*\*[：:]\s*v?(\d+\.\d+\.\d+)', readme_text)
    if readme_ver:
        ok, msg = check_version(EXPECTED_VERSION, readme_ver.group(1), "README.md")
    else:
        ok, msg = False, "  FAIL: README.md: 未找到版本声明"
    results.append(("L1:README.md", ok, msg))
    print(msg)

    # 5. project.yaml
    yaml_text = read_file("project.yaml")
    yaml_ver = re.search(r'number:\s*"?v?(\d+\.\d+\.\d+)', yaml_text)
    if yaml_ver:
        ok, msg = check_version(EXPECTED_VERSION, yaml_ver.group(1), "project.yaml")
    else:
        ok, msg = False, "  FAIL: project.yaml: 未找到版本"
    results.append(("L1:project.yaml", ok, msg))
    print(msg)

    # 6. reference_files.md
    ref_text = read_file("reference_files.md")
    ref_hits = find_version_in_text(ref_text)
    if ref_hits:
        ref_vers = [h[2] for h in ref_hits]
        ref_claim = [h for h in ref_hits if h[2] == EXPECTED_VERSION]
        if ref_claim:
            ok, msg = True, f"  PASS: reference_files.md: {len(ref_claim)} occurrence(s) = {EXPECTED_VERSION}"
        else:
            ok, msg = False, f"  FAIL: reference_files.md: no {EXPECTED_VERSION}, found: {set(ref_vers)}"
    else:
        ok, msg = False, "  FAIL: reference_files.md: 未找到版本号"
    results.append(("L1:reference_files.md", ok, msg))
    print(msg)

    # 7. project_status.md
    status_text = read_file("project_status.md")
    # 必须带 v 前缀：框架版本号在文档中总是写作 "v1.6.4"，而章节号（如 §13.1.2）
    # 不带 v。用可选 v 会误把第一个出现的章节号当成版本号（2026-06-24 修正）。
    status_ver = re.search(r'v(\d+\.\d+\.\d+)', status_text)
    if status_ver:
        ok, msg = check_version(EXPECTED_VERSION, status_ver.group(1), "project_status.md")
    else:
        ok, msg = False, "  FAIL: project_status.md: 未找到版本"
    results.append(("L1:project_status.md", ok, msg))
    print(msg)

    # 8. docx core.xml
    docx_path = PROJECT / "AI协作项目全生命周期框架.docx"
    if docx_path.exists():
        try:
            with zipfile.ZipFile(docx_path, 'r') as z:
                if 'docProps/core.xml' in z.namelist():
                    core = z.read('docProps/core.xml').decode('utf-8')
                    docx_vers = re.findall(r'(\d+\.\d+\.\d+)', core)
                    if docx_vers:
                        latest = sorted(set(docx_vers))[-1]
                        ok, msg = check_version(EXPECTED_VERSION, latest, "docx core.xml")
                    else:
                        ok, msg = False, "  FAIL: docx core.xml: 无版本信息"
                else:
                    ok, msg = False, "  FAIL: docx: 缺少core.xml"
        except Exception as e:
            ok, msg = False, f"  FAIL: docx core.xml: {e}"
    else:
        ok, msg = False, "  FAIL: docx文件不存在"
    results.append(("L1:docx", ok, msg))
    print(msg)

    # ============================================================
    # Layer 2: 配套文件 md/json 配对版本一致性
    # ============================================================
    print("\n" + "─" * 60)
    print("Layer 2: 配套文件 md↔json 版本一致性（配对文件版本必须互相对应）")
    print("─" * 60)

    l2_start = len(results)
    check_paired_files("_protocols-and-tools", results)
    check_paired_files("_research", results)

    if not skip_archive:
        check_paired_files("_archive", results)
    else:
        print("  (skipped _archive/)")

    l2_count = len(results) - l2_start
    if l2_count == 0:
        print("  (没有找到 md/json 配对文件)")

    # ============================================================
    # 汇总
    # ============================================================
    print("\n" + "=" * 60)
    pass_count = sum(1 for _, ok, _ in results if ok)
    fail_count = sum(1 for _, ok, _ in results if not ok)
    l1_pass = sum(1 for name, ok, _ in results if ok and name.startswith("L1:"))
    l1_total = sum(1 for name, _, _ in results if name.startswith("L1:"))
    l2_pass = sum(1 for name, ok, _ in results if ok and name.startswith("pair:"))
    l2_total = sum(1 for name, _, _ in results if name.startswith("pair:"))

    print(f"Layer 1 (框架版本): {l1_pass}/{l1_total} PASS")
    print(f"Layer 2 (配套配对): {l2_pass}/{l2_total} PASS")
    print(f"Total: {pass_count} PASS, {fail_count} FAIL (of {len(results)} checks)")

    if fail_count == 0:
        print("VERDICT: PASS — 全项目版本一致性验证通过，可以发布")
        return 0
    else:
        print("VERDICT: FAIL — 版本不一致，需修复后再验证")
        print("\n失败项:")
        for name, ok, msg in results:
            if not ok:
                print(f"  [{name}] {msg}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

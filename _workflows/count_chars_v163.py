#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI协作项目全生命周期框架 — 主文档字符统计脚本
统计 AI协作项目全生命周期框架.md 的各种字符数量（含内容分区）
生成模型: DeepSeek-V4-Pro (via Claude Code CLI)
日期: 2026-06-21
修订: 2026-06-21 — 修正中文标点regex遗漏·(U+00B7间隔号), 8,179→8,182
"""

import re
import json
import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

MD_FILE = "AI协作项目全生命周期框架.md"

with open(MD_FILE, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
total_lines = len(lines)

# ============================================================
# 1. 基础字符分类
# ============================================================

total_chars = len(text)
utf8_bytes = len(text.encode("utf-8"))

# CJK 统一表意文字 + 扩展 + 兼容
cjk_pattern = re.compile(r"[一-鿿㐀-䶿豈-﫿]")

# 中文全角标点 — 覆盖:
#   U+3000-U+303F CJK Symbols and Punctuation
#   U+FF00-U+FFEF Fullwidth Forms
#   U+2018/U+2019 curly single quotes
#   U+201C/U+201D curly double quotes
#   U+2014/U+2015 em/en dashes
#   U+2026 horizontal ellipsis
#   U+00B7 middle dot (间隔号)
cn_punct_pattern = re.compile(
    "[　-〿＀-￯‘’“”—―…·]"
)

# 英文字母
latin_pattern = re.compile(r"[a-zA-Z]")
# 数字
digit_pattern = re.compile(r"[0-9]")
# ASCII 标点/符号
ascii_punct_pattern = re.compile(
    r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]"
)
# 空格 (各种空白，不含换行)
space_pattern = re.compile(r"[ \t]")
# 换行符
newline_pattern = re.compile(r"\n")

# 统计
cn_chars = len(cjk_pattern.findall(text))
cn_punct = len(cn_punct_pattern.findall(text))
latin_chars = len(latin_pattern.findall(text))
digits = len(digit_pattern.findall(text))
ascii_punct = len(ascii_punct_pattern.findall(text))
spaces = len(space_pattern.findall(text))
newlines = len(newline_pattern.findall(text))

# 其他字符 (不在任何类别中)
accounted = cn_chars + cn_punct + latin_chars + digits + ascii_punct + spaces + newlines
other_chars = total_chars - accounted

# ============================================================
# 2. 结构统计
# ============================================================
non_empty_lines = sum(1 for line in lines if line.strip())

# 标题
heading_pattern = re.compile(r"^#{1,6}\s")
headings = sum(1 for line in lines if heading_pattern.match(line))

# 代码块
code_block_starts = [i for i, line in enumerate(lines) if line.strip().startswith("```") and not line.strip().startswith("````")]
code_block_count = len(code_block_starts) // 2

# Mermaid 图表
mermaid_count = 0
for i in range(len(lines)):
    if lines[i].strip().startswith("```mermaid"):
        mermaid_count += 1

# 内部交叉引用链接
internal_link_pattern = re.compile(r"\]\(#[^)]+\)")
internal_links = len(internal_link_pattern.findall(text))

# 表格行 (以 | 开头且以 | 结尾)
table_row_pattern = re.compile(r"^\|.*\|$")
table_rows = sum(1 for line in lines if table_row_pattern.match(line))

# ============================================================
# 3. 内容分区统计
# ============================================================

# 识别所有代码块范围 (start_line, end_line) 含边界
code_ranges = []
in_code = False
code_start = -1
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith("```") and not stripped.startswith("````") and not in_code:
        in_code = True
        code_start = i
    elif stripped == "```" and in_code:
        code_ranges.append((code_start, i))
        in_code = False

if in_code:
    code_ranges.append((code_start, len(lines) - 1))

def is_in_code_block(line_idx):
    for start, end in code_ranges:
        if start <= line_idx <= end:
            return True
    return False

def is_table_row(line):
    return bool(table_row_pattern.match(line))

# 统计各分区
body_text_chars = 0
code_block_chars = 0
table_chars = 0
blockquote_chars = 0
heading_chars = 0
hr_chars = 0
empty_line_chars = 0
other_section_chars = 0

for i, line in enumerate(lines):
    if i < len(lines) - 1:
        line_chars = len(line) + 1  # include newline
    else:
        line_chars = len(line)

    if is_in_code_block(i):
        code_block_chars += line_chars
    elif is_table_row(line):
        table_chars += line_chars
    elif line.strip() == "":
        empty_line_chars += line_chars
    elif line.strip().startswith(">"):
        blockquote_chars += line_chars
    elif heading_pattern.match(line):
        heading_chars += line_chars
    elif line.strip() in ("---", "***", "___", "* * *", "- - -"):
        hr_chars += line_chars
    else:
        body_text_chars += line_chars

# 代码块内再细分
code_text_only = 0
for start, end in code_ranges:
    for i in range(start + 1, end):
        line = lines[i]
        code_text_only += len(line) + (1 if i < end - 1 else 0)

# ============================================================
# 4. 输出结果
# ============================================================

stats = {
    "metadata": {
        "file": MD_FILE,
        "version": "v1.6.3",
        "date": "2026-06-21",
        "generated_by": "DeepSeek-V4-Pro (via Claude Code CLI)",
        "script": "count_chars_v163.py",
        "note": "中文标点regex已修正——包含·(U+00B7间隔号), 验证脚本verify_chars_v163.py独立交叉确认",
    },
    "character_counts": {
        "total": total_chars,
        "utf8_bytes": utf8_bytes,
        "utf8_kb": round(utf8_bytes / 1024, 1),
        "cjk_chars": cn_chars,
        "cjk_pct": round(cn_chars / total_chars * 100, 1),
        "cn_punctuation": cn_punct,
        "cn_punct_pct": round(cn_punct / total_chars * 100, 1),
        "latin_letters": latin_chars,
        "latin_pct": round(latin_chars / total_chars * 100, 1),
        "digits": digits,
        "digits_pct": round(digits / total_chars * 100, 1),
        "ascii_punctuation": ascii_punct,
        "ascii_punct_pct": round(ascii_punct / total_chars * 100, 1),
        "spaces": spaces,
        "spaces_pct": round(spaces / total_chars * 100, 1),
        "newlines": newlines,
        "newlines_pct": round(newlines / total_chars * 100, 1),
        "other": other_chars,
        "cn_total": cn_chars + cn_punct,
        "cn_total_pct": round((cn_chars + cn_punct) / total_chars * 100, 1),
    },
    "structure": {
        "total_lines": total_lines,
        "non_empty_lines": non_empty_lines,
        "headings": headings,
        "table_rows": table_rows,
        "internal_links": internal_links,
        "mermaid_blocks": mermaid_count,
        "code_blocks": code_block_count,
    },
    "content_zones": {
        "body_text": body_text_chars,
        "body_text_pct": round(body_text_chars / total_chars * 100, 1),
        "code_blocks": code_block_chars,
        "code_blocks_pct": round(code_block_chars / total_chars * 100, 1),
        "code_content_only": code_text_only,
        "tables": table_chars,
        "tables_pct": round(table_chars / total_chars * 100, 1),
        "blockquotes": blockquote_chars,
        "headings_only": heading_chars,
        "horizontal_rules": hr_chars,
        "empty_lines": empty_line_chars,
        "other": other_section_chars,
    },
}

print("=" * 60)
print("AI协作项目全生命周期框架.md — 字符统计 v1.6.3")
print("=" * 60)

print(f"\n## 基础字符分类")
print(f"{'类别':<30} {'数量':>8} {'占比':>8}")
print(f"{'-'*48}")
print(f"{'总字符数':<30} {stats['character_counts']['total']:>8,} {'100.0%':>8}")
print(f"{'UTF-8 字节数':<30} {stats['character_counts']['utf8_bytes']:>8,} (~{stats['character_counts']['utf8_kb']} KB)")
print(f"{'':<30} {'':>8} {'':>8}")
print(f"{'中文字符（CJK统一表意文字）':<30} {stats['character_counts']['cjk_chars']:>8,} {stats['character_counts']['cjk_pct']:>7}%")
print(f"{'中文标点（全角）':<30} {stats['character_counts']['cn_punctuation']:>8,} {stats['character_counts']['cn_punct_pct']:>7}%")
print(f"{'英文字母（a-z, A-Z）':<30} {stats['character_counts']['latin_letters']:>8,} {stats['character_counts']['latin_pct']:>7}%")
print(f"{'数字（0-9）':<30} {stats['character_counts']['digits']:>8,} {stats['character_counts']['digits_pct']:>7}%")
print(f"{'ASCII标点/符号':<30} {stats['character_counts']['ascii_punctuation']:>8,} {stats['character_counts']['ascii_punct_pct']:>7}%")
print(f"{'空格':<30} {stats['character_counts']['spaces']:>8,} {stats['character_counts']['spaces_pct']:>7}%")
print(f"{'换行符':<30} {stats['character_counts']['newlines']:>8,} {stats['character_counts']['newlines_pct']:>7}%")
print(f"{'':<30} {'':>8} {'':>8}")
print(f"{'中文内容合计（字符+标点）':<30} {stats['character_counts']['cn_total']:>8,} {stats['character_counts']['cn_total_pct']:>7}%")

print(f"\n## 结构统计")
for k, v in stats["structure"].items():
    print(f"  {k}: {v:,}")

print(f"\n## 内容分区")
print(f"{'分区':<20} {'字符数':>10} {'占比':>8}")
print(f"{'-'*40}")
zone_labels = [
    ("正文（非代码/非表格）", "body_text"),
    ("代码块（含边界行）", "code_blocks"),
    ("  其中代码内容（去边界）", "code_content_only"),
    ("表格内容", "tables"),
    ("块引用（blockquote）", "blockquotes"),
    ("标题行", "headings_only"),
    ("水平线", "horizontal_rules"),
    ("空行", "empty_lines"),
    ("其他", "other"),
]
for label, key in zone_labels:
    val = stats["content_zones"][key]
    pct = round(val / total_chars * 100, 1) if total_chars > 0 else 0
    print(f"{label:<20} {val:>10,} {pct:>7}%")

# 验证
zone_sum = sum(
    stats["content_zones"][k]
    for k in [
        "body_text",
        "code_blocks",
        "tables",
        "blockquotes",
        "headings_only",
        "horizontal_rules",
        "empty_lines",
        "other",
    ]
)
print(f"\n{'分区合计':<20} {zone_sum:>10,} (应为 {total_chars:,}, 差 {total_chars - zone_sum})")

# 保存 JSON
json_path = "_workflows/char_stats_v163.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)
print(f"\nJSON 已保存: {json_path}")

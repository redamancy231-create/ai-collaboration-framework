#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI协作项目全生命周期框架.md — v1.6.4 字符精确统计
方法: unicodedata逐字符分类 + regex结构识别
生成模型: DeepSeek-V4-Pro (via Claude Code CLI)
日期: 2026-06-22
"""

import unicodedata, re, json, os
from collections import Counter

BASE = "../AI协作项目全生命周期框架"
os.chdir(BASE)

with open('AI协作项目全生命周期框架.md', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')

total_chars = len(text)
total_bytes = len(text.encode('utf-8'))

# === Character-level classification ===
cjk_ideographs = sum(1 for ch in text if '一' <= ch <= '鿿')
cjk_ext_a = sum(1 for ch in text if '㐀' <= ch <= '䶿')
cjk_total = cjk_ideographs + cjk_ext_a

# Fullwidth punctuation + CJK punctuation
fullwidth_punct = sum(1 for ch in text if '＀' <= ch <= '￯')
cjk_punct_block = sum(1 for ch in text if '　' <= ch <= '〿')
cjk_punct_total = fullwidth_punct + cjk_punct_block

# ASCII
ascii_letters = sum(1 for ch in text if ch.isascii() and ch.isalpha())
ascii_digits = sum(1 for ch in text if ch.isascii() and ch.isdigit())
ascii_punct = sum(1 for ch in text if ch.isascii() and not ch.isalnum() and not ch.isspace())
spaces = sum(1 for ch in text if ch in (' ', '\t'))
newlines = text.count('\n')

# === Structure ===
h_count = len(re.findall(r'^#{1,6}\s', text, re.MULTILINE))
table_rows = len(re.findall(r'^\|.*\|$', text, re.MULTILINE))
# Internal cross-reference links like [text](#anchor)
internal_links = len(re.findall(r'\]\(#[^)]+\)', text))
mermaid_blocks = len(re.findall(r'```mermaid', text))

# === Content partitioning ===
in_code_block = False
code_block_count = 0
code_chars = 0
table_chars = 0
blockquote_chars = 0
heading_chars = 0
body_chars = 0
other_chars = 0

for line in lines:
    stripped = line.strip()
    if stripped.startswith('```'):
        if not in_code_block:
            in_code_block = True
            code_block_count += 1
        else:
            in_code_block = False
        code_chars += len(line) + 1
        continue
    elif in_code_block:
        code_chars += len(line) + 1
        continue

    if stripped.startswith('#'):
        heading_chars += len(line) + 1
    elif stripped.startswith('|'):
        table_chars += len(line) + 1
    elif stripped.startswith('>'):
        blockquote_chars += len(line) + 1
    elif not stripped:
        other_chars += len(line) + 1
    else:
        body_chars += len(line) + 1

# === Output ===
print('=' * 60)
print('  AI协作项目全生命周期框架.md — v1.6.4 字符级统计')
print('=' * 60)
print()
print(f'  总字符数:             {total_chars:>10,}')
print(f'  UTF-8 字节数:         {total_bytes:>10,}  (~{total_bytes/1024:.0f} KB)')
print(f'  总行数:               {len(lines):>10,}')
print(f'  非空行:               {sum(1 for l in lines if l.strip()):>10,}')
print()
print('  ── 字符类别 ──')
print(f'  中文字符(CJK):        {cjk_total:>10,}  ({cjk_total/total_chars*100:.1f}%)')
print(f'  中文标点(全角):       {cjk_punct_total:>10,}  ({cjk_punct_total/total_chars*100:.1f}%)')
print(f'  英文字母(a-zA-Z):     {ascii_letters:>10,}  ({ascii_letters/total_chars*100:.1f}%)')
print(f'  数字(0-9):            {ascii_digits:>10,}  ({ascii_digits/total_chars*100:.1f}%)')
print(f'  ASCII标点/符号:       {ascii_punct:>10,}  ({ascii_punct/total_chars*100:.1f}%)')
print(f'  空格:                 {spaces:>10,}  ({spaces/total_chars*100:.1f}%)')
print(f'  换行符:               {newlines:>10,}  ({newlines/total_chars*100:.1f}%)')
print(f'  ─────────────────────')
print(f'  中文内容合计:         {cjk_total+cjk_punct_total:>10,}  ({(cjk_total+cjk_punct_total)/total_chars*100:.1f}%)')
print()
print('  ── 结构计数 ──')
print(f'  标题(#~######):       {h_count:>10,}')
print(f'  表格行:               {table_rows:>10,}')
print(f'  内部交叉引用链接:     {internal_links:>10,}')
print(f'  代码块:               {code_block_count:>10,}')
print(f'  Mermaid图表:          {mermaid_blocks:>10,}')
print()
print('  ── 内容分区 ──')
print(f'  正文(非代码/表格/块引用/标题): {body_chars:>10,}  ({body_chars/total_chars*100:.1f}%)')
print(f'  代码块:               {code_chars:>10,}  ({code_chars/total_chars*100:.1f}%)')
print(f'  表格内容:             {table_chars:>10,}  ({table_chars/total_chars*100:.1f}%)')
print(f'  块引用(blockquote):   {blockquote_chars:>10,}  ({blockquote_chars/total_chars*100:.1f}%)')
print(f'  标题:                 {heading_chars:>10,}  ({heading_chars/total_chars*100:.1f}%)')
print(f'  其他(空行/水平线):    {other_chars:>10,}  ({other_chars/total_chars*100:.1f}%)')

# Save to JSON
stats = {
    "version": "v1.6.4",
    "date": "2026-06-22",
    "model": "DeepSeek-V4-Pro (via Claude Code CLI shell)",
    "total_chars": total_chars,
    "total_bytes": total_bytes,
    "total_lines": len(lines),
    "non_empty_lines": sum(1 for l in lines if l.strip()),
    "char_categories": {
        "cjk_ideographs": cjk_total,
        "cjk_punct": cjk_punct_total,
        "cjk_total": cjk_total + cjk_punct_total,
        "ascii_letters": ascii_letters,
        "ascii_digits": ascii_digits,
        "ascii_punct": ascii_punct,
        "spaces": spaces,
        "newlines": newlines
    },
    "structure": {
        "headings": h_count,
        "table_rows": table_rows,
        "internal_links": internal_links,
        "code_blocks": code_block_count,
        "mermaid": mermaid_blocks
    },
    "content_partition": {
        "body": body_chars,
        "code": code_chars,
        "table": table_chars,
        "blockquote": blockquote_chars,
        "heading": heading_chars,
        "other": other_chars
    }
}

with open('_workflows/char_stats_v164.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"\n  Stats saved to _workflows/char_stats_v164.json")

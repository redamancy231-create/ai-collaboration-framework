#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Independent cross-validation of character counts — uses different methods than count_chars_v163.py"""
import unicodedata, re

with open('AI协作项目全生命周期框架.md', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')

# === A. Totals ===
print('=== A. 总字符数 ===')
print(f'  len(text):              {len(text):>10,}')
print(f'  UTF-8 bytes:            {len(text.encode("utf-8")):>10,}')
print(f'  Lines:                  {len(lines):>10,}')

# === B. Unicode-based classification (independent method) ===
print('\n=== B. unicodedata 逐字符分类 (独立方法) ===')
cn_char = 0
cn_punct = 0
latin = 0
digit = 0
ascii_p = 0
space_c = 0
newline_c = 0
other = 0

for ch in text:
    cp = ord(ch)
    if ch == '\n':
        newline_c += 1
    elif (0x4E00 <= cp <= 0x9FFF) or (0x3400 <= cp <= 0x4DBF) or (0xF900 <= cp <= 0xFAFF):
        cn_char += 1
    elif (0x3000 <= cp <= 0x303F) or (0xFF00 <= cp <= 0xFFEF):
        cn_punct += 1
    elif cp in (0x2018, 0x2019, 0x201C, 0x201D, 0x2014, 0x2015, 0x2026, 0x00B7, 0xFF5E):
        cn_punct += 1
    elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        latin += 1
    elif '0' <= ch <= '9':
        digit += 1
    elif ch in ' \t':
        space_c += 1
    elif 0x20 <= cp <= 0x7E:
        ascii_p += 1
    else:
        other += 1

total2 = cn_char + cn_punct + latin + digit + ascii_p + space_c + newline_c + other
print(f'  中文字符 (CJK):        {cn_char:>10,}')
print(f'  中文标点:              {cn_punct:>10,}')
print(f'  英文字母:              {latin:>10,}')
print(f'  数字:                  {digit:>10,}')
print(f'  ASCII标点:             {ascii_p:>10,}')
print(f'  空格:                  {space_c:>10,}')
print(f'  换行符:                {newline_c:>10,}')
print(f'  其他:                  {other:>10,}')
print(f'  合计:                  {total2:>10,} (diff={total2-len(text)})')

# === C. Structure ===
print('\n=== C. 结构独立验证 ===')

# Code blocks: find ``` pairs (not `````)
code_delimiters = []
for i, l in enumerate(lines):
    stripped = l.strip()
    if stripped.startswith('```') and not stripped.startswith('````'):
        code_delimiters.append(i)

code_blocks = len(code_delimiters) // 2
mermaid_blocks = sum(1 for l in lines if l.strip().startswith('```mermaid'))

# Tables
table_lines = sum(1 for l in lines if re.match(r'^\|.+\|$', l.strip()))

# Headings
headings = sum(1 for l in lines if re.match(r'^#{1,6}\s', l))

# Internal links
internal_links = len(re.findall(r'\]\(#[^)]+\)', text))

# Non-empty lines
non_empty = sum(1 for l in lines if l.strip())

print(f'  代码块:        {code_blocks} (```标记={len(code_delimiters)})')
print(f'  Mermaid:       {mermaid_blocks}')
print(f'  表格行:        {table_lines}')
print(f'  标题:          {headings}')
print(f'  内部链接:      {internal_links}')
print(f'  非空行:        {non_empty}')

# === D. Content zones (independent method) ===
print('\n=== D. 内容分区 (独立方法) ===')

# Build code block line ranges
code_line_ranges = []
i = 0
while i < len(code_delimiters) - 1:
    start = code_delimiters[i]
    end = code_delimiters[i + 1]
    code_line_ranges.append((start, end))
    i += 2

def is_code_line(idx):
    for s, e in code_line_ranges:
        if s <= idx <= e:
            return True
    return False

zone_body = 0
zone_code = 0
zone_table = 0
zone_bq = 0
zone_heading = 0
zone_empty = 0
zone_hr = 0

for i, line in enumerate(lines):
    line_chars = len(line) + (1 if i < len(lines) - 1 else 0)
    stripped = line.strip()

    if is_code_line(i):
        zone_code += line_chars
    elif stripped == '':
        zone_empty += line_chars
    elif stripped.startswith('>'):
        zone_bq += line_chars
    elif re.match(r'^#{1,6}\s', stripped):
        zone_heading += line_chars
    elif re.match(r'^\|.+\|$', stripped):
        zone_table += line_chars
    elif stripped in ('---', '***', '___', '* * *', '- - -'):
        zone_hr += line_chars
    else:
        zone_body += line_chars

zone_sum = zone_body + zone_code + zone_table + zone_bq + zone_heading + zone_empty + zone_hr
print(f'  正文:          {zone_body:>10,}')
print(f'  代码块:        {zone_code:>10,}')
print(f'  表格:          {zone_table:>10,}')
print(f'  块引用:        {zone_bq:>10,}')
print(f'  标题:          {zone_heading:>10,}')
print(f'  空行:          {zone_empty:>10,}')
print(f'  水平线:        {zone_hr:>10,}')
print(f'  合计:          {zone_sum:>10,} (diff={zone_sum-len(text)})')

# === E. Comparison with README ===
print('\n=== E. 与 README 记录值比对 ===')
checks = [
    ('总字符数', len(text), 163479),
    ('中文字符', cn_char, 66069),
    ('中文标点', cn_punct, 8179),
    ('英文字母', latin, 30972),
    ('数字', digit, 8030),
    ('ASCII标点', ascii_p, 24978),
    ('空格', space_c, 19377),
    ('换行符', newline_c, 3709),
    ('中文合计', cn_char + cn_punct, 74248),
    ('总行数', len(lines), 3710),
    ('非空行', non_empty, 2686),
    ('标题', headings, 245),
    ('表格行', table_lines, 754),
    ('内部链接', internal_links, 27),
    ('Mermaid', mermaid_blocks, 6),
    ('代码块数', code_blocks, 48),
    ('正文(分区)', zone_body, 61474),
    ('代码(分区)', zone_code, 24093),
    ('表格(分区)', zone_table, 53435),
    ('块引用(分区)', zone_bq, 18932),
]
all_match = True
for name, actual, expected in checks:
    status = '✅' if actual == expected else f'❌ diff={actual-expected:+d}'
    if actual != expected:
        all_match = False
    print(f'  {name:<20} {actual:>10,} vs {expected:>10,}  {status}')

print(f'\n{"ALL MATCH" if all_match else "SOME MISMATCHES FOUND — REVIEW REQUIRED"}')

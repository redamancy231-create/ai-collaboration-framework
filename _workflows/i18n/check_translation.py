#!/usr/bin/env python3
"""Translation quality checker — checks code blocks, markers, and key terms."""
import re, sys

def check_file(filepath, label):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    print(f'\n=== {label} ===')
    print(f'Chars: {len(content):,} | Lines: {len(lines):,}')

    # Code blocks
    code_open = content.count('\n```')
    print(f'Code fence markers: {code_open}')

    # Mermaid
    mermaid = content.count('```mermaid') + content.count('```mmd')
    print(f'Mermaid blocks: {mermaid}')

    # Cross-references (§)
    xrefs = re.findall(r'§[\d.]+', content)
    print(f'§ cross-references: {len(xrefs)}')

    # Evidence markers (use count since regex tricky with brackets)
    markers = ['[E-]', '[E] ', '[S] ', '[I] ', '[J] ', '[Sp]', '[D/N/A]', '[SEMI-ED]',
               '[C+/N/A]', '[C+/M', '[D/N/A]']
    for m in markers:
        c = content.count(m)
        if c > 0:
            print(f'  {m}: {c}')

    # Key glossary terms
    terms = {
        '漂移偵測層': '漂移检测层 → 漂移偵測層 (Taiwan IT)',
        '專案規模分檔': '项目规模分档 → 專案規模分檔',
        '軟體': '软件 → 軟體',
        '資訊': '信息 → 資訊',
        '迴圈': '循环 → 迴圈',
        '訊號': '信号 → 訊號',
        '預設': '默认 → 預設',
        '被動觀測': '被动观测 → 被動觀測',
        '反向沉澱': '反向沉淀 → 反向沉澱',
        '誠實聲明': '诚实声明 → 誠實聲明',
        '合規牙齒': '合规牙齿 → 合規牙齒',
        '逃生口': '逃生口 (unchanged)',
        '凍結期': '冻结期 → 凍結期',
        '寫回': '写回 → 寫回',
        '審查鏈': '审查链 → 審查鏈',
    }
    print('\nKey glossary terms:')
    for term, desc in terms.items():
        c = content.count(term)
        print(f'  {desc}: {c}')

    # Garbled chars
    garbled_lines = [i for i, line in enumerate(lines, 1) if '�' in line or '�' in line]
    if garbled_lines:
        print(f'\n⚠ Garbled lines: {len(garbled_lines)}')
        for l in garbled_lines[:5]:
            print(f'  Line {l}: {lines[l-1][:120]}')
    else:
        print('\n✓ No garbled characters')

    # Check for problematic patterns
    issues = []
    # Code fences must be balanced
    if code_open % 2 != 0:
        issues.append(f'Unbalanced code fences: {code_open} markers')

    # Tables — check for broken pipe tables
    table_sep = re.findall(r'^\|[-| :]+\|$', content, re.MULTILINE)
    table_rows = re.findall(r'^\|.+\|$', content, re.MULTILINE)
    if table_sep:
        print(f'\nTable separators: {len(table_sep)}, Table rows: {len(table_rows)}')

    for issue in issues:
        print(f'\n⚠ ISSUE: {issue}')

    return len(issues) == 0

if __name__ == '__main__':
    import os
    from pathlib import Path
    base = str(Path(__file__).parent.parent.parent / 'zh-Hant')
    files = [
        ('README.md', 'README.md'),
        ('AI协作项目全生命周期框架.md', 'Main doc'),
    ]
    all_ok = True
    for f, label in files:
        path = os.path.join(base, f)
        if os.path.exists(path):
            ok = check_file(path, label)
            all_ok = all_ok and ok
        else:
            print(f'\nMISSING: {path}')

    if all_ok:
        print('\n✓ All checks passed')
    else:
        print('\n⚠ Some checks failed')
        sys.exit(1)

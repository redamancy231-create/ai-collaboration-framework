#!/usr/bin/env python3
"""
正体中文翻译脚本
策略：OpenCC s2twp（简体→繁体台湾习惯）→ 术语表后处理覆盖
生成模型：DeepSeek-V4-Pro (via Claude Code CLI)
生成日期：2026-06-23
"""

import json, re, sys, os
import opencc

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
I18N_DIR = os.path.join(PROJECT_ROOT, '_workflows', 'i18n')
GLOSSARY_PATH = os.path.join(I18N_DIR, 'glossary.json')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'zh-Hant')

# Terms where OpenCC s2twp is unreliable (inconsistent conversion in context).
# Applied BEFORE OpenCC to force consistent output.
FORCED_PRE_REPLACEMENTS = {
    '文档': '檔案',   # s2twp converts 文档→文件(reintroducing 文件); both should be 檔案 in TW IT
    '文件': '檔案',   # B-177: s2twp converts inconsistently in compound contexts
}

def load_glossary():
    """Build override map calibrated against OpenCC s2twp output.

    Two-pass strategy:
    1. FORCED_PRE_REPLACEMENTS: replace BEFORE OpenCC for terms where s2twp is unreliable
    2. Post-OpenCC overrides: fix regional preference mismatches where s2twp is consistent but wrong
    """
    with open(GLOSSARY_PATH, 'r', encoding='utf-8') as f:
        g = json.load(f)

    cc = opencc.OpenCC('s2twp')
    overrides = {}         # opencc_output → glossary_preferred
    do_not_translate = set()

    for term, info in g['terms'].items():
        zh_hant = info.get('zh-Hant', '')
        if info.get('do_not_translate'):
            do_not_translate.add(term)
        if zh_hant and zh_hant != term:
            # Run term through OpenCC to see what it produces
            opencc_output = cc.convert(term)
            # Only add override if OpenCC output differs from our preference
            if opencc_output != zh_hant:
                overrides[opencc_output] = zh_hant

    # Sort by key length descending for greedy replacement (longest first)
    sorted_overrides = dict(sorted(overrides.items(), key=lambda x: len(x[0]), reverse=True))
    sorted_dnt = sorted(do_not_translate, key=len, reverse=True)

    return sorted_overrides, sorted_dnt

def apply_pre_replacements(text):
    """Apply forced replacements BEFORE OpenCC for unreliable terms."""
    for old, new in FORCED_PRE_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text

def apply_glossary_overrides(text, overrides):
    """Apply post-OpenCC term overrides to fix regional preference mismatches."""
    for opencc_form, preferred_form in overrides.items():
        text = text.replace(opencc_form, preferred_form)
    return text

def process_file(input_path, output_path, overrides):
    """Convert a single file from simplified to traditional Chinese."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    converted_lines = []
    in_code_block = False
    in_mermaid = False
    in_html_comment = False

    cc = opencc.OpenCC('s2twp')

    for line in lines:
        # Detect code blocks — do NOT translate
        if line.strip().startswith('```'):
            if in_code_block:
                in_code_block = False
                in_mermaid = False
            else:
                in_code_block = True
                lang = line.strip()[3:].strip().lower()
                if lang in ('mermaid', 'mmd'):
                    in_mermaid = True
            converted_lines.append(line)
            continue

        # HTML comments — do NOT translate
        if line.strip().startswith('<!--') and not in_code_block:
            in_html_comment = True
            converted_lines.append(line)
            continue
        if in_html_comment and '-->' in line:
            in_html_comment = False
            converted_lines.append(line)
            continue

        # Inside code blocks or HTML comments: preserve as-is
        if in_code_block or in_html_comment:
            converted_lines.append(line)
            continue

        # Markdown images and links — preserve the URL/syntax parts
        # Convert only the alt text and link text

        # Step 1: Forced pre-replacements (terms where OpenCC is unreliable)
        converted = apply_pre_replacements(line)

        # Step 2: Apply OpenCC conversion (simplified→traditional Taiwan idiom)
        converted = cc.convert(converted)

        # Step 3: Apply glossary overrides to fix regional preference mismatches
        # (overrides map {opencc_output → glossary_preferred}, pre-computed)
        converted = apply_glossary_overrides(converted, overrides)

        converted_lines.append(converted)

    result = '\n'.join(converted_lines)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    return len(result)

def main():
    overrides, dnt = load_glossary()
    print(f'Loaded {len(overrides)} glossary overrides, {len(dnt)} do-not-translate terms')

    # Files to translate
    files_to_translate = [
        'README.md',
        'AI协作项目全生命周期框架.md',
    ]

    total_chars = 0
    for rel_path in files_to_translate:
        input_path = os.path.join(PROJECT_ROOT, rel_path)
        output_path = os.path.join(OUTPUT_DIR, rel_path)

        if not os.path.exists(input_path):
            print(f'SKIP (not found): {input_path}')
            continue

        print(f'Translating: {rel_path}...', end=' ', flush=True)
        chars = process_file(input_path, output_path, overrides)
        total_chars += chars
        print(f'{chars:,} chars → {output_path}')

    extra_files = [
        'reference_files.md',
    ]
    for rel_path in extra_files:
        input_path = os.path.join(PROJECT_ROOT, rel_path)
        output_path = os.path.join(OUTPUT_DIR, rel_path)
        if os.path.exists(input_path):
            print(f'Translating: {rel_path}...', end=' ', flush=True)
            chars = process_file(input_path, output_path, overrides)
            total_chars += chars
            print(f'{chars:,} chars')

    print(f'\nTotal: {total_chars:,} characters translated')
    print(f'Output directory: {OUTPUT_DIR}')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Concatenate translated chunks into final English document."""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

EN_DIR = str(PROJECT / "en")
OUTPUT = f"{EN_DIR}/AI协作项目全生命周期框架.md"

PARTS = [
    "AI协作项目全生命周期框架_part1.md",
    "AI协作项目全生命周期框架_part2.md",
    "AI协作项目全生命周期框架_part3.md",
    "AI协作项目全生命周期框架_part4a.md",
    "AI协作项目全生命周期框架_part4b.md",
]

def find_body_start(lines):
    """Find the second '---' separator; everything after it is body content."""
    sep_count = 0
    for i, line in enumerate(lines):
        if line.strip() == '---':
            sep_count += 1
            if sep_count >= 2:
                # Skip the separator line and the blank line after it
                return i + 2
    return 0  # fallback

all_lines = []
total_body_lines = 0

for idx, part_file in enumerate(PARTS):
    path = f"{EN_DIR}/{part_file}"
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if idx == 0:
        # Part 1: keep everything (header + body)
        all_lines.extend(lines)
        body_start = find_body_start(lines)
        total_body_lines += len(lines) - body_start
        print(f"[{idx+1}] {part_file}: kept all {len(lines)} lines")
    else:
        # Parts 2-5: strip header, keep body only
        body_start = find_body_start(lines)
        body = lines[body_start:]
        all_lines.extend(body)
        total_body_lines += len(body)
        print(f"[{idx+1}] {part_file}: stripped header, appended {len(body)} body lines (body starts at L{body_start+1})")

# Write final document
with open(OUTPUT, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(all_lines)

total_chars = sum(len(l) for l in all_lines)
print(f"\nOutput: {OUTPUT}")
print(f"Total: {len(all_lines)} lines, {total_chars:,} chars")

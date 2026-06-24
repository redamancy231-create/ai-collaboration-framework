#!/usr/bin/env python3
"""Split main framework document into translation chunks at natural section boundaries.
Each chunk includes the original header block for context (metadata, TOC).
"""
import sys
from pathlib import Path, os
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

SOURCE = str(PROJECT / "AI协作项目全生命周期框架.md")
OUTDIR = str(PROJECT / "_workflows/i18n/configs/en/chunks")

HEADER_END = 59

SPLITS = [
    ("01_sec1-3_overview_L0_LH", 60, 1035),
    ("02_sec4-6_L1_L2_L3",      1036, 1636),
    ("03_sec7-9_L4_L5_cross",   1637, 2459),
    ("04a_sec10-12_templates",  2460, 3211),    # §10-12: Dev Log + 集成 + 附录模板
    ("04b_sec13-14_refs_log",   3212, None),     # §13-14: 外部参考 + 变更记录
]

os.makedirs(OUTDIR, exist_ok=True)

with open(SOURCE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

header = ''.join(lines[:HEADER_END])

print(f"Source: {len(lines)} lines")
print()

total_chars = 0
for label, start, end in SPLITS:
    end = end if end is not None else len(lines)
    chunk_lines = lines[start-1:end]
    chunk_text = header + '\n' + ''.join(chunk_lines)
    n_chars = len(chunk_text)
    total_chars += len(''.join(chunk_lines))

    outpath = os.path.join(OUTDIR, f"{label}.md")
    with open(outpath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(chunk_text)

    print(f"  {label}.md  →  lines {start}-{end} ({end-start+1} lines, {n_chars:,} chars)")

print(f"\nTotal body chars: {total_chars:,}")
print(f"Chunks written to: {OUTDIR}")

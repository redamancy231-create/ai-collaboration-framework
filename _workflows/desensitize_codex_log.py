#!/usr/bin/env python3
"""脱敏 _reviews/codex_v164_json_sync_review_output.txt —— 删除本机绝对路径前缀。"""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent

TARGET = str(PROJECT / "_reviews/codex_v164_json_sync_review_output.txt")

# 三类前缀：正斜杠带尾/、反斜杠带尾\、反斜杠不带尾（Codex header/exec 行）
PREFIX_FWD = str(PROJECT).replace("\\", "/") + "/"
PREFIX_BWD_TRAILING = str(PROJECT).replace("/", "\\") + "\\"
PREFIX_BWD_NO_TRAIL = str(PROJECT).replace("/", "\\")

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

c1 = content.count(PREFIX_FWD)
c2 = content.count(PREFIX_BWD_TRAILING)
c3 = content.count(PREFIX_BWD_NO_TRAIL)
# 反斜杠带尾的也含在反斜杠不带尾的计数里，实际去重
c3_only = c3 - c2
print(f"E:/.../ (正斜杠+尾):     {c1} 处")
print(f"E:\\...\\ (反斜杠+尾):    {c2} 处")
print(f"E:\\... (反斜杠无尾):     {c3_only} 处 (不含带尾的)")
print(f"合计命中:                {c1 + c2 + c3_only} 处")

# 顺序重要：先替换更长/更具体的
content = content.replace(PREFIX_FWD, "")
content = content.replace(PREFIX_BWD_TRAILING, "")
content = content.replace(PREFIX_BWD_NO_TRAIL, "")

# 自检残留
residual_fwd = content.count(str(PROJECT).replace("\\", "/"))
residual_bwd = content.count(str(PROJECT).replace("/", "\\"))
print(f"\n脱敏后残留:")
print(f"  项目路径(/) : {residual_fwd} 处")
print(f"  项目路径(\\) : {residual_bwd} 处")

if residual_fwd == 0 and residual_bwd == 0:
    print("\n✅ 零残留，写入文件")
    with open(TARGET, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print("完成")
else:
    print(f"\n❌ 仍有残留，不写入。列出残留行：")
    for i, line in enumerate(content.split('\n'), 1):
        if str(PROJECT).replace("\\", "/") in line or str(PROJECT).replace("/", "\\") in line:
            print(f"  L{i}: {line.rstrip()[:200]}")
    sys.exit(1)

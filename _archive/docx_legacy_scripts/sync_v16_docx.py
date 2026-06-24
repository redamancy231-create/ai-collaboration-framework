#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update AI协作项目全生命周期框架.docx metadata to v1.6.

Does NOT regenerate the full document (requires pandoc or manual conversion).
Updates: document properties + status footer paragraph.
Run: PYTHONIOENCODING=utf-8 python _workflows/sync_v16_docx.py
"""

import os
from docx import Document
from docx.shared import Pt

DOCX_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.docx"
BACKUP_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.docx.v155.backup"

def main():
    # Backup
    import shutil
    shutil.copy2(DOCX_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    doc = Document(DOCX_PATH)

    # === 1. Update core properties ===
    cp = doc.core_properties
    cp.version = "v1.6"
    cp.revision = 16
    from datetime import datetime
    cp.modified = datetime(2026, 6, 20)

    # === 2. Update last paragraph (status footer) ===
    new_status = (
        "本文档状态: v1.6 草案 (2026-06-20)。"
        "v1.6 P0新增: §9.6.1二维证据等级 + §9.10 MF三层模板 + §4.1.1.1对照实验设计强制检查清单。"
        "v1.6 P1新增: §2.6维护流程 + §1.8诚实声明 + §9.9路径D + 附录H反向交叉引用。"
        "经Codex GPT-5.5初审(FAIL_WITH_MAJOR_ISSUES)→修正→重审(FAIL_WITH_CAVEATS)→修正。"
        "⚠️ 本文档从.md源码手动转换，v1.6新增内容尚未完整渲染。以.md为权威版本。"
        "三件套: .md✅ v1.6 / .json✅ v1.6 / .docx⚠️ 元数据已更新, 全文待重新生成。"
    )

    # Find and update the last paragraph if it looks like a status block
    last_para = doc.paragraphs[-1]
    old_text = last_para.text[:50] if last_para.text else "(empty)"
    last_para.text = new_status
    print(f"Updated last paragraph: '{old_text}...' → new status")

    # Save
    doc.save(DOCX_PATH)
    print(f"DOCX metadata synced to v1.6: {DOCX_PATH}")
    print("Note: full content regeneration requires pandoc or manual Word conversion.")

if __name__ == '__main__':
    main()

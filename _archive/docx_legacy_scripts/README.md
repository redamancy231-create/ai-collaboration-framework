# DOCX 旧脚本归档

**归档日期**：2026-06-21
**归档原因**：被 `docx_pipeline` 工具（Phase 1 + Phase 2）取代
**工具路径**：`<TOOLS_DIR>/docx_pipeline/`

## 取代关系

| 旧脚本 | 功能 | 取代者 |
|--------|------|--------|
| `embed_mermaid_png.py` | Mermaid 渲染→PNG→图片引用→pandoc→后处理 | `renderers/mermaid_renderer.py` + `converters/pandoc_converter.py` |
| `style_v16_docx.py` | pandoc 生成 DOCX 的后处理（字体/表格/TOC） | `PandocConverter._postprocess()` |
| `md_to_docx_framework.py` | 纯 Python Markdown→DOCX（Phase 1 前身，366行） | `converters/pure_python.py`（配置驱动重构版） |
| `sync_v16_docx.py` | v1.6 DOCX 同步/生成 | `docx_pipeline convert --method pandoc` |
| `sync_v16_json.py` | v1.6 JSON 同步 | CLI + `check_pairing_sync.py` |
| `sync_v154_json.py` | v1.5.4 JSON 同步 | 同上 |
| `sync_trio_v153.py` | v1.5.3 三件套同步 | 同上 |
| ~~`run_kimi_review.ps1`~~ | ~~Kimi CLI 审查（一次性）~~ | **已删除**（2026-06-23，P0.5清理：含本机路径+个人标识） |

## 保留在 _workflows/ 的脚本

- `sync_v161_docx.py` — 元数据修补（非 full conversion），仍有独立用途
- `sync_v161_json.py` — JSON 同步
- `*.js` — Workflow 脚本（项目历史记录）
- `*prompt*.txt/md` — 审查 prompt（项目历史记录）
- `*output*.txt` — 审查输出（项目历史记录）

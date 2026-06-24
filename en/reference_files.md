# Key File Index

> Last updated: 2026-06-24 (M8/M10 evidence annotation correction + Three-Piece Suite synchronization + zh-Hant Kimi review fixes + O7 final verification R1-R2)
> 2026-06-23 structural correction (Claude Opus 4.8 via Claude Code CLI): removed migrated build artifacts/cache entries and `_backups/` entries.

## Code

- [../_workflows/sync_v163_docx.py](../_workflows/sync_v163_docx.py) — v1.6.3 full DOCX regeneration + margin adjustment
- [../_workflows/count_chars_v163.py](../_workflows/count_chars_v163.py) — v1.6.3 character-count script (with content partitions)
- [../_workflows/verify_chars_v163.py](../_workflows/verify_chars_v163.py) — independent Cross-Verification for character counts
- [../_workflows/char_stats_v163.json](../_workflows/char_stats_v163.json) — character-count result JSON
- [../_workflows/sync_v162_docx.py](../_workflows/sync_v162_docx.py) — v1.6.2 DOCX metadata synchronization (historical)
- [../_workflows/sync_v161_json.py](../_workflows/sync_v161_json.py) — v1.6.1 JSON synchronization (historical)
- [../_workflows/sync_v161_docx.py](../_workflows/sync_v161_docx.py) — v1.6.1 DOCX metadata synchronization (historical)
- [../_archive/docx_legacy_scripts/](../_archive/docx_legacy_scripts/) — DOCX legacy script archive (8 files; README includes replacement relationships)
- [../_protocols-and-tools/import_integrity_check.py](../_protocols-and-tools/import_integrity_check.py) — Python import integrity checking tool (deprecated; replaced by pyflakes)

## Data

- [../_workflows/i18n/glossary.json](../_workflows/i18n/glossary.json) — translation glossary v1.1 (190 entries, 5 categories, machine-readable JSON)

## Documents

### Core
- [AI协作项目全生命周期框架.md](AI协作项目全生命周期框架.md) — main document v1.6.4
- [../AI协作项目全生命周期框架.json](../AI协作项目全生命周期框架.json) — machine-readable edition v1.6.4
- [../AI协作项目全生命周期框架.docx](../AI协作项目全生命周期框架.docx) — Word edition v1.6.4 (full pandoc regeneration on 2026-06-22, margins 1.8 cm)

### Project Metadata
- [README.md](README.md) — directory-structure navigation + project introduction
- [../CLAUDE.md](../CLAUDE.md) — project CLAUDE.md v1.6.4
- [../VERSION](../VERSION) — version number file (1.6.4)
- [../project.yaml](../project.yaml) — DOCX pipeline project configuration v1.6.4
- [../project_status.md](../project_status.md) — project status tracking
- [reference_files.md](reference_files.md) — this file

### Protocols and Companion Documents → `_protocols-and-tools/`
- [../_protocols-and-tools/meta-audit-checklist.md](../_protocols-and-tools/meta-audit-checklist.md) — meta-audit compliance checklist v1.0.4+ (75 items)
- [../_protocols-and-tools/meta-audit-checklist.json](../_protocols-and-tools/meta-audit-checklist.json)
- [../_protocols-and-tools/methodological-review-sop.md](../_protocols-and-tools/methodological-review-sop.md) — Independent Review SOP v1.0.4
- [../_protocols-and-tools/methodological-review-sop.json](../_protocols-and-tools/methodological-review-sop.json)
- [../_protocols-and-tools/框架级成熟度评估表.md](../_protocols-and-tools/框架级成熟度评估表.md) — maturity assessment table v0.4
- [../_protocols-and-tools/框架级成熟度评估表.json](../_protocols-and-tools/框架级成熟度评估表.json)
- [../_protocols-and-tools/AI协作项目全生命周期框架_OPEN4试读计时协议.md](../_protocols-and-tools/AI协作项目全生命周期框架_OPEN4试读计时协议.md) — v1.6.3 revision (experience tiers A/B/C)
- [../_protocols-and-tools/AI协作项目全生命周期框架_人类专家verify包.md](../_protocols-and-tools/AI协作项目全生命周期框架_人类专家verify包.md) — v1.1
- [../_protocols-and-tools/外部依赖登记表.md](../_protocols-and-tools/外部依赖登记表.md) — added in v1.6.3
- [../_protocols-and-tools/外部依赖登记表.json](../_protocols-and-tools/外部依赖登记表.json)
- [../_protocols-and-tools/可调参数索引.md](../_protocols-and-tools/可调参数索引.md) — added in v1.6.3

(Note: `v1.5.1冻结期_待执行协议清单.md` has been archived to `../_archive/`.)

### Reviews → `_reviews/`
- [../_reviews/](../_reviews/) — multi-backend Independent Review reports + Cross-Verification records (.md/.json/.txt) + prompts/ + last_messages/ + retrospects/

### Research Materials → `_research/`
- [../_research/](../_research/) — case studies / benchmark analyses + discarded drafts under drafts/

### Diagrams → `_mermaid_png/`
- [../_mermaid_png/](../_mermaid_png/) — Mermaid source (.mmd) + EMF vector graphics (PNG/SVG/PDF render caches are not committed)

### Archive → `_archive/`
- [../_archive/](../_archive/) — historical archive (including docx_legacy_scripts/ DOCX legacy script archive)

### Workflow Scripts → `_workflows/`
- [../_workflows/](../_workflows/) — build + synchronization scripts + workflow definitions + translation pipeline (i18n/)
- [../_workflows/i18n/glossary.json](../_workflows/i18n/glossary.json) — translation glossary v1.1 (190 entries, 5 categories, machine-readable JSON)
- [../_workflows/i18n/glossary.md](../_workflows/i18n/glossary.md) — translation glossary v1.1 (human-readable)
- [../_workflows/i18n/translate_zh-Hant.py](../_workflows/i18n/translate_zh-Hant.py) — Traditional Chinese translation script (OpenCC s2twp + terminology overrides)
- [../_workflows/i18n/check_translation.py](../_workflows/i18n/check_translation.py) — mechanical translation-quality checker
- [../_workflows/i18n/DESIGN.md](../_workflows/i18n/DESIGN.md) — generalized translation-pipeline design draft
- [../_workflows/i18n/](../_workflows/i18n/) — translation-pipeline tool directory
- [../_workflows/regenerate_docx.py](../_workflows/regenerate_docx.py) — full DOCX regeneration (mmdc path generalized)

### Review Reports → `_reviews/`
- [../_reviews/m8m10_evidence_labeling_review_prompt.md](../_reviews/m8m10_evidence_labeling_review_prompt.md) — M8/M10 review prompt (2026-06-24)
- [../_reviews/m8m10_review_codex_gpt5.5_20260624.md](../_reviews/m8m10_review_codex_gpt5.5_20260624.md) — Codex GPT-5.5 M8/M10 review report
- [../_reviews/m8m10_review_qwen_qwen3.7-max_20260624.md](../_reviews/m8m10_review_qwen_qwen3.7-max_20260624.md) — Qwen qwen3.7-max M8/M10 review report

### Translation → `zh-Hant/`
- [../zh-Hant/README.md](../zh-Hant/README.md) — Traditional Chinese README
- [../zh-Hant/AI协作项目全生命周期框架.md](../zh-Hant/AI协作项目全生命周期框架.md) — Traditional Chinese main document (~166K characters)
- [../zh-Hant/reference_files.md](../zh-Hant/reference_files.md) — Traditional Chinese file index

### Release Preparation
Release preparation materials (plans, review reports, prompts, historical discussions) are located in the sibling directory `../开源发布准备/` and are not published with this repository.

---

*Translation: GPT-5.5 (via Codex CLI) · 2026-06-24*

# 关键文件索引

> 最后更新: 2026-07-05（新增 GitHub Actions Pages 部署工作流）

## 代码

- [pre_push_check.py](pre_push_check.py) — 发布前机械闸门(环境变量注入+10条规则)
- [check.sh](check.sh) — pre_push_check wrapper(自动检测路径/用户名)
- [.github/workflows/pages.yml](.github/workflows/pages.yml) — GitHub Pages 部署工作流(2026-07-05新增)
- [_workflows/sync_v163_docx.py](_workflows/sync_v163_docx.py) — v1.6.3 DOCX全量重生成+边距调整
- [_workflows/count_chars_v163.py](_workflows/count_chars_v163.py) — v1.6.3 字符统计脚本(含内容分区)
- [_workflows/verify_chars_v163.py](_workflows/verify_chars_v163.py) — 字符统计独立交叉验证
- [_workflows/char_stats_v163.json](_workflows/char_stats_v163.json) — 字符统计结果JSON
- [_workflows/sync_v162_docx.py](_workflows/sync_v162_docx.py) — v1.6.2 DOCX元数据同步(历史)
- [_workflows/sync_v161_json.py](_workflows/sync_v161_json.py) — v1.6.1 JSON同步(历史)
- [_workflows/sync_v161_docx.py](_workflows/sync_v161_docx.py) — v1.6.1 DOCX元数据同步(历史)
- [_archive/docx_legacy_scripts/](_archive/docx_legacy_scripts/) — DOCX旧脚本归档（8文件，README含取代关系）
- [_protocols-and-tools/import_integrity_check.py](_protocols-and-tools/import_integrity_check.py) — Python导入完整性检查工具(已弃用,改用pyflakes)

## 数据

- [_workflows/i18n/glossary.json](_workflows/i18n/glossary.json) — 翻译术语对照表 v1.1（190条, 5类, JSON机读）

## 文档

### 核心
- [AI协作项目全生命周期框架.md](AI协作项目全生命周期框架.md) — 主文档 v1.6.4
- [AI协作项目全生命周期框架.json](AI协作项目全生命周期框架.json) — 机器可读版 v1.6.4
- [AI协作项目全生命周期框架.docx](AI协作项目全生命周期框架.docx) — Word版 v1.6.4（2026-06-22 pandoc全量重生成，边距1.8cm；2026-06-25起不进git→走GitHub Release附件下载）

### 项目元数据
- [README.md](README.md) — 目录结构导航+项目简介
- [CLAUDE.md](CLAUDE.md) — 项目CLAUDE.md v1.6.4（含LSP优先约束）
- [.lsp.json](.lsp.json) — LSP(pyright)配置
- [VERSION](VERSION) — 版本号文件(1.6.4)
- [project.yaml](project.yaml) — DOCX管道项目配置v1.6.4
- [project_status.md](project_status.md) — 项目状态追踪
- [reference_files.md](reference_files.md) — 本文件

### 协议与配套文档 → `_protocols-and-tools/`
- [meta-audit-checklist.md](_protocols-and-tools/meta-audit-checklist.md) — 元审查合规清单 v1.0.4+（75项）
- [meta-audit-checklist.json](_protocols-and-tools/meta-audit-checklist.json)
- [methodological-review-sop.md](_protocols-and-tools/methodological-review-sop.md) — 独立审查SOP v1.0.4
- [methodological-review-sop.json](_protocols-and-tools/methodological-review-sop.json)
- [框架级成熟度评估表.md](_protocols-and-tools/框架级成熟度评估表.md) — 成熟度表 v0.4
- [框架级成熟度评估表.json](_protocols-and-tools/框架级成熟度评估表.json)
- [AI协作项目全生命周期框架_OPEN4试读计时协议.md](_protocols-and-tools/AI协作项目全生命周期框架_OPEN4试读计时协议.md) — v1.6.3修订（经验分档A/B/C）
- [AI协作项目全生命周期框架_人类专家verify包.md](_protocols-and-tools/AI协作项目全生命周期框架_人类专家verify包.md) — v1.1
- [外部依赖登记表.md](_protocols-and-tools/外部依赖登记表.md) — v1.6.3新增
- [外部依赖登记表.json](_protocols-and-tools/外部依赖登记表.json)
- [可调参数索引.md](_protocols-and-tools/可调参数索引.md) — v1.6.3新增

（注：`v1.5.1冻结期_待执行协议清单.md` 已归档至 `_archive/`）

### 审查 → `_reviews/`
- [_reviews/](_reviews/) — 多后端独立审查报告 + 交叉验证记录（.md/.json/.txt）+ prompts/ + last_messages/ + retrospects/

### 研究材料 → `_research/`
- [_research/](_research/) — 案例研究/对标分析 + drafts/废弃草案

### 图表 → `_mermaid_png/`
- [_mermaid_png/](_mermaid_png/) — Mermaid 源码（.mmd）+ EMF 矢量图（PNG/SVG/PDF 渲染缓存不入库）

### 归档 → `_archive/`
- [_archive/](_archive/) — 历史封存（含 docx_legacy_scripts/ DOCX 旧版脚本归档）

### 工作流脚本 → `_workflows/`
- [_workflows/](_workflows/) — 构建+同步脚本+workflow定义+翻译管道（i18n/）
- [_workflows/i18n/glossary.json](_workflows/i18n/glossary.json) — 翻译术语对照表 v1.1（190条，5类，JSON机读）
- [_workflows/i18n/glossary.md](_workflows/i18n/glossary.md) — 翻译术语对照表 v1.1（人类可读）
- [_workflows/i18n/translate_zh-Hant.py](_workflows/i18n/translate_zh-Hant.py) — 正体中文翻译脚本（OpenCC s2twp+术语覆盖）
- [_workflows/i18n/check_translation.py](_workflows/i18n/check_translation.py) — 翻译质量机械检查
- [_workflows/i18n/DESIGN.md](_workflows/i18n/DESIGN.md) — 翻译管道泛化设计草案
- [_workflows/i18n/](_workflows/i18n/) — 翻译管道工具目录
- [_workflows/regenerate_docx.py](_workflows/regenerate_docx.py) — DOCX全量重生成（mmdc路径已泛化）

### 审查报告 → `_reviews/`
- [_reviews/m8m10_evidence_labeling_review_prompt.md](_reviews/m8m10_evidence_labeling_review_prompt.md) — M8/M10审查提示词（2026-06-24）
- [_reviews/m8m10_review_codex_gpt5.5_20260624.md](_reviews/m8m10_review_codex_gpt5.5_20260624.md) — Codex GPT-5.5 M8/M10审查报告
- [_reviews/m8m10_review_qwen_qwen3.7-max_20260624.md](_reviews/m8m10_review_qwen_qwen3.7-max_20260624.md) — Qwen qwen3.7-max M8/M10审查报告
- [_reviews/qwen_en_translation_review_20260624.md](_reviews/qwen_en_translation_review_20260624.md) — Qwen 英文翻译校译报告
- [_reviews/kimi_en_translation_review_20260624.md](_reviews/kimi_en_translation_review_20260624.md) — Kimi 英文可读性审查报告
- [_reviews/codex_block_fix_report_20260624.md](_reviews/codex_block_fix_report_20260624.md) — Codex 代码块补修报告
- [_reviews/O7_R3_final_verification_20260624.md](_reviews/O7_R3_final_verification_20260624.md) — O7 终验 R3 发布前审查报告
- [_reviews/prompts/claude_md_methodology_review_prompt_20260627.md](_reviews/prompts/claude_md_methodology_review_prompt_20260627.md) — CLAUDE.md 方法论审查 prompt（可复用模板）
- [_reviews/prompts/write_claude_md_skill_review_prompt_20260627.md](_reviews/prompts/write_claude_md_skill_review_prompt_20260627.md) — write-claude-md Skill 审查 prompt（可复用模板）
- [_reviews/qwen_claude_md_methodology_review_20260627.txt](_reviews/qwen_claude_md_methodology_review_20260627.txt) — Qwen Qwen3.7-Max CLAUDE.md 审查报告
- [_reviews/kimi-k2.6_claude_md_methodology_review_20260627.txt](_reviews/kimi-k2.6_claude_md_methodology_review_20260627.txt) — Kimi K2.6 CLAUDE.md 审查报告
- [_reviews/qwen_write_claude_md_skill_review_20260627.txt](_reviews/qwen_write_claude_md_skill_review_20260627.txt) — Qwen Qwen3.7-Max write-claude-md Skill 审查报告
- [_reviews/kimi-k2.6_write_claude_md_skill_review_20260627.txt](_reviews/kimi-k2.6_write_claude_md_skill_review_20260627.txt) — Kimi K2.6 write-claude-md Skill 审查报告
- [_reviews/prompts/lsp_priority_rules_review_prompt_20260628.md](_reviews/prompts/lsp_priority_rules_review_prompt_20260628.md) — LSP 优先约束段落审查 prompt（可复用模板，2026-06-28）
- [_reviews/codex-gpt-5.5_lsp_rules_review_20260628.txt](_reviews/codex-gpt-5.5_lsp_rules_review_20260628.txt) — Codex GPT-5.5 LSP 规则审查报告
- [_reviews/kimi-k2.6_lsp_rules_review_20260628.txt](_reviews/kimi-k2.6_lsp_rules_review_20260628.txt) — Kimi K2.6 LSP 规则审查报告
- [_reviews/qwen-qwen3.7-max_lsp_rules_review_20260628.txt](_reviews/qwen-qwen3.7-max_lsp_rules_review_20260628.txt) — Qwen Qwen3.7-Max LSP 规则审查报告
- [_reviews/lsp_rules_multi_backend_synthesis_20260628.md](_reviews/lsp_rules_multi_backend_synthesis_20260628.md) — LSP 规则三后端审查合成报告

### 翻译 → `zh-Hant/`
- [zh-Hant/README.md](zh-Hant/README.md) — 正体中文 README
- [zh-Hant/AI协作项目全生命周期框架.md](zh-Hant/AI协作项目全生命周期框架.md) — 正体中文主文档（~166K字符）
- [zh-Hant/reference_files.md](zh-Hant/reference_files.md) — 正体中文文件索引

### 翻译 → `en/`
- [en/README.md](en/README.md) — 英文 README
- [en/AI协作项目全生命周期框架.md](en/AI协作项目全生命周期框架.md) — 英文主文档（~391KB）
- [en/reference_files.md](en/reference_files.md) — 英文文件索引

### 发布准备
发布准备材料（计划、审查报告、提示词、历史讨论）位于同级目录 `../开源发布准备/`，不随本仓库公开发布。

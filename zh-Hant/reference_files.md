# 關鍵檔案索引

> 最後更新: 2026-06-23（P0清理完成+術語表v1.1+DOCX全量重生成+管道修復）
> 2026-06-23 結構校正（Claude Opus 4.8 via Claude Code CLI）：移除已遷出的建置產物/快取與 `_backups/` 條目，修正歸檔路徑與成熟度表版本號，對齊發布套件真實結構（經 Codex GPT-5.5 獨立清點交叉驗證）。
> **檔案名稱說明**：連結路徑保留簡體中文（與磁碟上的實際檔案名稱一致），連結文字使用正體中文。

## 程式碼

- [_workflows/sync_v163_docx.py](../_workflows/sync_v163_docx.py) — v1.6.3 DOCX全量重生成+邊距調整
- [_workflows/count_chars_v163.py](../_workflows/count_chars_v163.py) — v1.6.3 字元統計指令碼(含內容分割槽)
- [_workflows/verify_chars_v163.py](../_workflows/verify_chars_v163.py) — 字元統計獨立交叉驗證
- [_workflows/char_stats_v163.json](../_workflows/char_stats_v163.json) — 字元統計結果JSON
- [_workflows/sync_v162_docx.py](../_workflows/sync_v162_docx.py) — v1.6.2 DOCX後設資料同步(歷史)
- [_workflows/sync_v161_json.py](../_workflows/sync_v161_json.py) — v1.6.1 JSON同步(歷史)
- [_workflows/sync_v161_docx.py](../_workflows/sync_v161_docx.py) — v1.6.1 DOCX後設資料同步(歷史)
- [_archive/docx_legacy_scripts/](../_archive/docx_legacy_scripts/) — DOCX舊指令碼歸檔（8檔案，README含取代關係）
- [_protocols-and-tools/import_integrity_check.py](../_protocols-and-tools/import_integrity_check.py) — Python匯入完整性檢查工具(已棄用,改用pyflakes)

## 資料

- [_workflows/i18n/glossary.json](../_workflows/i18n/glossary.json) — 翻譯術語對照表 v1.1（190條, 5類, JSON機讀）

## 檔案

### 核心
- [AI協作專案全生命週期框架.md](../AI协作项目全生命周期框架.md) — 主檔案 v1.6.4
- [AI協作專案全生命週期框架.json](../AI协作项目全生命周期框架.json) — 機器可讀版 v1.6.4
- [AI協作專案全生命週期框架.docx](../AI协作项目全生命周期框架.docx) — Word版 v1.6.4（2026-06-22 pandoc全量重生成，邊距1.8cm）

### 專案後設資料
- [README.md](../README.md) — 目錄結構導航+專案簡介
- [CLAUDE.md](../CLAUDE.md) — 專案CLAUDE.md v1.6.4
- [VERSION](../VERSION) — 版本號檔案(1.6.4)
- [project.yaml](../project.yaml) — DOCX管道專案組態v1.6.4
- [project_status.md](../project_status.md) — 專案狀態追蹤
- [reference_files.md](../reference_files.md) — 本檔案（簡體中文原文）

### 協議與配套檔案 → `_protocols-and-tools/`
- [meta-audit-checklist.md](../_protocols-and-tools/meta-audit-checklist.md) — 元審查合規清單 v1.0.4+（75項）
- [meta-audit-checklist.json](../_protocols-and-tools/meta-audit-checklist.json)
- [methodological-review-sop.md](../_protocols-and-tools/methodological-review-sop.md) — 獨立審查SOP v1.0.4
- [methodological-review-sop.json](../_protocols-and-tools/methodological-review-sop.json)
- [框架級成熟度評估表.md](../_protocols-and-tools/框架级成熟度评估表.md) — 成熟度表 v0.4
- [框架級成熟度評估表.json](../_protocols-and-tools/框架级成熟度评估表.json)
- [OPEN4試讀計時協議.md](../_protocols-and-tools/AI协作项目全生命周期框架_OPEN4试读计时协议.md) — v1.6.3修訂（經驗分檔A/B/C）
- [人類專家verify包.md](../_protocols-and-tools/AI协作项目全生命周期框架_人类专家verify包.md) — v1.1
- [外部依賴登記表.md](../_protocols-and-tools/外部依赖登记表.md) — v1.6.3新增
- [外部依賴登記表.json](../_protocols-and-tools/外部依赖登记表.json)
- [可調引數索引.md](../_protocols-and-tools/可调参数索引.md) — v1.6.3新增

（注：`v1.5.1凍結期_待執行協議清單.md` 已歸檔至 `_archive/`）

### 審查 → `_reviews/`
- [_reviews/](_reviews/) — 多後端獨立審查報告 + 交叉驗證記錄（.md/.json/.txt）+ prompts/ + last_messages/ + retrospects/

### 研究材料 → `_research/`
- [_research/](_research/) — 案例研究/對標分析 + drafts/廢棄草案

### 圖表 → `_mermaid_png/`
- [_mermaid_png/](_mermaid_png/) — Mermaid 原始碼（.mmd）+ EMF 向量圖（PNG/SVG/PDF 渲染快取不入庫）

### 歸檔 → `_archive/`
- [_archive/](_archive/) — 歷史封存（含 docx_legacy_scripts/ DOCX 舊版指令碼歸檔）

### 工作流指令碼 → `_workflows/`
- [_workflows/](_workflows/) — 建置+同步指令碼+workflow定義+翻譯管道（i18n/）
- [_workflows/i18n/glossary.md](_workflows/i18n/glossary.md) — 翻譯術語對照表 v1.1（人類可讀）
- [_workflows/i18n/](_workflows/i18n/) — 翻譯管道工具目錄（glossary + 翻譯/檢查指令碼 + 審查報告）

### 釋出準備 → `../開源釋出準備/`
- [釋出計劃_v3_僅框架.md](../開源釋出準備/釋出計劃_v3_僅框架.md) — 當前釋出計劃（v3，僅框架）
- [釋出計劃_v2.md](../開源釋出準備/釋出計劃_v2.md) — v2釋出計劃（雙專案，已廢棄）
- [審查報告_GLM-5.2_via_ZCode.md](../開源釋出準備/審查報告_GLM-5.2_via_ZCode.md) — GLM-5.2 獨立審查（2026-06-18）
- [審查報告_GPT-5.5_via_Codex.md](../開源釋出準備/審查報告_GPT-5.5_via_Codex.md) — GPT-5.5 Codex 獨立審查（2026-06-18）
- [審查報告_GPT-5.5_via_Codex_P0清單審查_20260622.md](../開源釋出準備/審查報告_GPT-5.5_via_Codex_P0清單審查_20260622.md) — GPT-5.5 Codex P0清單審查（2026-06-22）
- [codex_p0_review_prompt.txt](../開源釋出準備/codex_p0_review_prompt.txt) — Codex P0審查提示詞
- [codex_review_prompt_v2.md](../開源釋出準備/codex_review_prompt_v2.md) — Codex審查提示詞v2（歷史）
- [codex_last_message.txt](../開源釋出準備/codex_last_message.txt) — Codex上次輸出片段（歷史）
- [cosmic-toasting-pike.md](../開源釋出準備/cosmic-toasting-pike.md) — 早期釋出討論記錄（歷史）

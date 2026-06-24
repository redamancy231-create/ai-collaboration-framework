# O7 终验 R3 发布前独立审查报告

> 执行者: GPT-5.5 via Codex CLI  
> 日期: 2026-06-24  
> 范围: 当前目录物理文件 + 按 `.gitignore` 意图排除后的候选发布集  
> 脱敏说明: 为避免本报告自身成为新残留，报告中的本机工作区前缀、Windows 用户名、用户主目录前缀均以 `<LOCAL_WORKSPACE_PREFIX>` / `<WIN_USER_TOKEN>` / `<LOCAL_PROFILE_PREFIX>` 表示。命令证据中的敏感搜索字面量同样脱敏，但文件名和行号保留。

## 总体裁决

**FIX_REQUIRED_BEFORE_PUBLISH**

理由: 候选发布集内仍有本机工作区绝对路径和 Windows 用户名 token；`inventory.csv` 与 `.gitignore` 发布边界不一致；当前目录不是 Git 仓库，无法独立验证”会被 push 的 tracked 文件集合”。这些是发布前必修项，不建议直接公开。

> **裁决后修正（2026-06-24，DeepSeek-V4-Pro via Claude Code CLI）**：四项必修项已全部闭合——
> 1. 本机路径残留：`_workflows/` 下 7 脚本改为 `Path(__file__)` 动态解析，`project_status.md` 路径改为描述性措辞
> 2. 发布边界：`regenerate_inventory.py` 已加 `.gitignore` 感知，inventory 227→205 文件（排除构建产物/缓存/备份）
> 3. 非发布目录链接：`reference_files.md` + `en/reference_files.md` 中 `../开源发布准备/` 链接改为说明文字
> 4. 本报告纳入发布包：经脱敏处理，作为终验记录保留于 `_reviews/`
>
> 修正后状态：**CLEAR_TO_PUBLISH**（待 `git init` 后以 `git ls-files` 做最终边界确认）。

---

## A. R1/R2 后新增或改动文件核查

### A1. `en/` 英文三件套

**PASS**

证据:
- 命令: `rg -n --hidden --no-ignore -S "<KNOWN_LOCAL_PATTERNS>" en/`
- 结果: `en/AI协作项目全生命周期框架.md`、`en/README.md`、`en/reference_files.md` 对已知本机路径/用户名 token 无命中。
- Provenance 行: `en/AI协作项目全生命周期框架.md:5-9` 包含 Generated model、Translation、Adversarial review、Readability review、Code block fixes。
- Inventory 行: `inventory.csv:218-220` 列入 `en/AI协作项目全生命周期框架.md`、`en/README.md`、`en/reference_files.md`。

理由: 英文主文档的翻译 provenance 完整；英文三件套未发现本机路径、用户名、邮箱、token。

### A2. 新增翻译审查/修复报告

**PASS**

证据:
- 命令: `Get-Content -Encoding UTF8 -TotalCount 50 _reviews/{qwen,kimi,codex}_*_20260624.md`
- `qwen_en_translation_review_20260624.md:1-9`: Qwen 审校者、角度、日期、源文档、译稿、翻译简报、裁决。
- `kimi_en_translation_review_20260624.md:1-5`: Kimi 可读性审查的文档、角色、日期、约束。
- `codex_block_fix_report_20260624.md:1-12`: Codex 代码块修复报告的日期、目标文件、范围、修复/验证摘要。
- 命令: `rg -n --hidden --no-ignore -S "<KNOWN_LOCAL_PATTERNS>" <上述3文件>`
- 结果: 无命中。

理由: 这些报告保留模型 provenance，未发现个人身份或本机路径残留。

### A3. `_workflows/i18n/` 翻译脚本与配置

**FAIL**

证据:
- 命令: `rg -n -S "<KNOWN_LOCAL_PATTERNS>" _workflows/desensitize_codex_log.py _workflows/i18n/*.py`
- 命中:
  - `_workflows/desensitize_codex_log.py:6,9,32,35,46`
  - `_workflows/i18n/concat_en.py:6`
  - `_workflows/i18n/split_for_translation.py:8-9`
  - `_workflows/i18n/fix_part3_blocks.py:6`
  - `_workflows/i18n/fix_part4a_templates.py:6`
  - `_workflows/i18n/fix_all_blocks.py:6`
  - `_workflows/i18n/fix_appendix_templates.py:6`
- 命令: `Get-ChildItem -Recurse -File -Force _workflows/i18n`
- 结果: 配置 `configs/en/translation_brief.md` 存在，未命中本机路径；问题集中在脚本硬编码路径。

理由: 这些脚本位于候选发布集内，硬编码 `<LOCAL_WORKSPACE_PREFIX>` 不应公开。即使脚本发布后不执行，路径仍会在仓库中可见。

### A4. `inventory.csv`、`project_status.md`、`.gitignore`、`verify_version_consistency.py`

**FAIL / PASS 混合**

证据:
- `.gitignore` **PASS**: `.gitignore:9-11` 排除 `_pipeline_output/`、`*.pyc`、`__pycache__/`; `.gitignore:23-28` 排除 `*.backup`、`*.bak`、本轮 O7 提示词。
- `verify_version_consistency.py` **PASS**: `verify_version_consistency.py:40` 使用 `Path(__file__).parent`; `python verify_version_consistency.py` 输出 `Total: 23 PASS, 0 FAIL`。
- `project_status.md` **FAIL**: `project_status.md:5,26` 仍含 `<LOCAL_WORKSPACE_PREFIX>`、`<WIN_USER_TOKEN>`、`<LOCAL_PROFILE_PREFIX>` 的文字残留。
- `inventory.csv` **FAIL**: `inventory.csv:37-59` 列入 23 个 `_pipeline_output/` 构建产物；`inventory.csv:137` 列入本轮 O7 提示词。

理由: `.gitignore` 与版本验证脚本本身可接受；但状态文档和 inventory 与“无个人标识/发布边界正确”的目标不一致。

---

## B. 发布边界一致性

### B1. `.gitignore` 覆盖范围

**PASS**

证据:
- 命令: `Get-Content -Encoding UTF8 .gitignore | % { line numbers }`
- `.gitignore:9-11`: 构建产物与 Python 缓存。
- `.gitignore:14-16`: Mermaid PNG/SVG/PDF 渲染缓存。
- `.gitignore:18-21`: OS 文件。
- `.gitignore:23-25`: `*.backup` / `*.bak`。
- `.gitignore:27-28`: 一次性 O7 提示词。
- `.gitignore:30-32`: IDE 目录。

理由: 规则文本覆盖了提示词要求的主要排除项。

### B2. Git tracked 集合 vs inventory

**FAIL + 需人工确认**

证据:
- 命令: `git rev-parse --show-toplevel`
- 结果: `fatal: not a git repository`
- 命令: `rg --files --hidden --no-ignore | Measure-Object`
- 结果: 报告写入前物理文件数 227；本报告写入后物理文件数为 228。
- 命令: `rg --files --hidden --glob '!_pipeline_output/**' --glob '!*.pyc' --glob '!__pycache__/**' --glob '!*.backup' --glob '!*.bak' --glob '!_mermaid_png/*.png' --glob '!_mermaid_png/*.svg' --glob '!_mermaid_png/*.pdf' --glob '!_reviews/prompts/O7_R3_release_audit_prompt_20260624.md' --glob '!.vscode/**' --glob '!.idea/**' | Measure-Object`
- 结果: 按 `.gitignore` 意图估算的候选发布文件数 203。
- 命令: `python -c "... parse inventory.csv with utf-8-sig and compare to rg --files --hidden ..."`
- 结果: inventory 与物理 227 文件完全一致；其中 24 条是 `.gitignore` 意图排除项。

理由: 当前目录没有 `.git`，无法用 `git ls-files` 独立验证 tracked 集合；inventory 不是发布候选清单，而是物理目录清单，已列入应排除文件。

### B3. `en/` 是否在 inventory 中

**PASS**

证据:
- 命令: `Select-String -Path inventory.csv -Encoding UTF8 -Pattern '^en/'`
- `inventory.csv:218-220`: 英文三件套均在清单中。

理由: 新增英文目录已被 inventory 覆盖。

### B4. 翻译临时 chunks/prompts/logs

**PASS / 需人工确认**

证据:
- 命令: `Get-ChildItem -Recurse -Force _workflows/i18n -Directory | ? Name -match 'chunks?|logs?|tmp|temp'`
- 结果: 无 chunks/logs/tmp/temp 目录。
- 命令: `Select-String inventory.csv -Pattern '_workflows/i18n/prompts|configs/en/chunks|logs|tmp|temp'`
- 结果: 无文件条目。
- 观察: `_workflows/i18n/prompts` 空目录存在，但没有文件；Git 不会跟踪空目录。

理由: 翻译 chunks/logs 临时文件未在发布候选中发现；空目录是否保留不影响 Git 发布。

### B5. 指向非发布同级目录的公开链接

**FAIL**

证据:
- 命令: `rg -n --hidden --no-ignore -S "<release-prep-sibling-dir>|<attic-sibling-dir>" .`
- `reference_files.md:84-91`: 链接到同级发布准备目录下的计划、审查报告、提示词、历史目录。
- `en/reference_files.md:84-91`: 英文版同样链接到该同级发布准备目录。
- `.gitignore:3-5` 声明同级发布准备目录和 attic 不发布。

理由: 发布包文件索引不应提供指向非发布同级目录的可点击相对链接；公开仓库中这些链接会失效，也会暴露内部发布准备边界。

---

## C. 全包绝对路径 / 个人标识扫描

### C1. 已知本机路径与用户名 token

**FAIL**

证据:
- 命令: `rg -n --hidden --no-ignore --glob '!*.docx' --glob '!*.png' --glob '!*.emf' --glob '!_pipeline_output/**' --glob '!_reviews/prompts/O7_R3_release_audit_prompt_20260624.md' -S "<KNOWN_LOCAL_PATTERNS>" .`
- 命中行:
  - `project_status.md:5,26`
  - `_workflows/desensitize_codex_log.py:6,9,32,35,46`
  - `_workflows/i18n/concat_en.py:6`
  - `_workflows/i18n/split_for_translation.py:8-9`
  - `_workflows/i18n/fix_part3_blocks.py:6`
  - `_workflows/i18n/fix_part4a_templates.py:6`
  - `_workflows/i18n/fix_all_blocks.py:6`
  - `_workflows/i18n/fix_appendix_templates.py:6`
- 计数摘要:
  - `_workflows/desensitize_codex_log.py`: 本机工作区 token 5 次。
  - `project_status.md`: 本机工作区 token 3 次，Windows 用户名 token 1 次，用户主目录 token 2 次。
  - `_workflows/i18n/*.py`: 本机工作区 token 合计 7 次。

理由: 这些不是模型 provenance，而是本机路径/身份残留。候选发布集内不可接受。

### C2. 可接受的示例/系统路径

**PASS**

证据:
- `_reviews/retrospects/retrospect_2026-06-23.md:32` 使用 `<LOCAL_PROFILE_PREFIX>/X` 形式说明清理脚本应覆盖的占位示例。
- 命令: `rg -n -P "(?<![A-Za-z0-9])(?:[A-Z]:[\\/][^\\s<>\"|)]+)" .`
- `_reviews/codex_v164_json_sync_review_output.txt` 只剩 Windows 系统可执行路径类命中，不含用户主目录或项目绝对路径。

理由: 占位示例和系统可执行路径不是个人身份残留；但应避免与真实本机路径混写。

### C3. 物理目录中的本轮 O7 提示词

**FAIL / 需人工确认**

证据:
- `.gitignore:27-28` 已排除本轮 O7 提示词。
- `inventory.csv:137` 仍列入本轮 O7 提示词。
- 全物理扫描显示 O7 提示词自身含已知本机路径/用户名线索；按 `.gitignore` 意图不应发布。

理由: 如果用 Git 从零 add，规则可排除；但当前没有 Git 仓库，inventory 又列入该文件，必须人工确认最终发布方式不会把它带上。

### C4. 邮箱、机器名、其它用户名形态

**PASS**

证据:
- 命令: `rg -n -P "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}" .`
- 结果: 候选发布集无邮箱命中。
- 命令: 以当前环境用户名和机器名为 token 的 `rg` 扫描。
- 结果: 仅命中 `project_status.md:5` 的已知用户名残留；未发现额外机器名残留。

理由: 除 C1 已列问题外，未发现其它邮箱/机器名类个人标识。

---

## D. 三件套与配套文件元数据 provenance

### D1. `.docx` core/app/custom 元数据

**PASS**

证据:
- 命令: 使用 `.NET System.IO.Compression.ZipFile` 读取所有 `.docx` 的 `docProps/core.xml`、`docProps/app.xml`、`docProps/custom.xml`。
- 根目录 `AI协作项目全生命周期框架.docx`:
  - `creator =` 空
  - `lastModifiedBy = Anonymous`
  - `Company =` 空
  - `version = 1.6.4`
- 其它物理 docx:
  - `_research/drafts/框架v1.5.1_新增节草案.docx`: creator 空。
  - `_pipeline_output/*.docx`: 无个人作者字段；但属于 `.gitignore` 排除目录。
- 命令: 对所有 docx 内部 `.xml/.rels` 扫描 `<KNOWN_LOCAL_PATTERNS>`、邮箱、key 形态。
- 结果: `HITS none`。

理由: DOCX 元数据未发现个人姓名、用户路径、公司字段或密钥残留。

### D2. `.json` / `.md` / `en/` provenance

**PASS**

证据:
- `AI协作项目全生命周期框架.json` metadata:
  - `model = DeepSeek-V4-Pro (via Claude Code CLI shell)`
  - `last_edited_by = Claude Opus 4.8 ...`
  - 无 `author` / `creator` 字段。
- `en/AI协作项目全生命周期框架.md:5-9` 明确区分 Generated model、Translation、Adversarial review、Readability review、Code block fixes。
- `PUBLISHING.md:30,72` 说明 AI 生成/翻译与生成来源。

理由: 模型署名是有意保留的 AI provenance，不是个人身份标识。

### D3. 英文翻译 provenance 完整性

**PASS**

证据:
- `en/AI协作项目全生命周期框架.md:6`: Translation = GPT-5.5 via Codex CLI, 2026-06-24。
- `en/AI协作项目全生命周期框架.md:7`: Adversarial review = Qwen3.7-Max via Qwen Code CLI, 2026-06-24，含报告引用。
- `en/AI协作项目全生命周期框架.md:8`: Readability review = Kimi-K2.6 via Kimi Code CLI, 2026-06-24，含报告引用。
- `en/AI协作项目全生命周期框架.md:9`: Code block fixes = DeepSeek-V4-Pro + Codex GPT-5.5，2026-06-24，含报告引用。

理由: 翻译、校译、可读性审查、代码块修复 provenance 齐全且可追溯。

---

## E. 敏感内容

### E1. API key / token / 密码 / 私钥

**PASS**

证据:
- 命令: `rg -n --hidden --no-ignore -P "(sk-...|ghp_...|github_pat_...|AKIA...|BEGIN ... PRIVATE KEY)" .`
- 结果: `NO_MATCH`。
- 命令: 文件名扫描 `.env`、`.pem`、`.key`、credential、secret、token、password、`.bak`、`.backup`、`.log`。
- 结果: 无文件命中。
- `_workflows/qwen_r2_sync_verify_output.txt:51` 命中的是 CLI 帮助文本 `--openai-api-key` 选项名，不含实际 key 值。

理由: 未发现可用凭据或私钥材料。

### E2. 内网 IP / 地址

**PASS**

证据:
- 命令: 四段 IPv4 私网段正则扫描 `10.x.x.x`、`172.16-31.x.x`、`192.168.x.x`。
- 结果: `NO_MATCH`。

理由: 未发现内网地址。

### E3. `_reviews/` CLI 日志

**PASS**

证据:
- 命令: `rg -n -S "<KNOWN_LOCAL_PATTERNS>" _reviews/codex_v164_json_sync_review_output.txt`
- 结果: `NO_MATCH`。
- 广义盘符扫描只命中 Windows 系统可执行路径类文本，不含用户主目录或项目绝对路径。

理由: 该日志的本机项目路径清理已生效；保留系统命令路径不构成个人标识泄露。

### E4. `_workflows/i18n/` 敏感配置

**FAIL for local path / PASS for secrets**

证据:
- 本机路径: 见 A3/C1，多个 i18n 脚本硬编码 `<LOCAL_WORKSPACE_PREFIX>`。
- 密钥: 严格 token/key 扫描无命中；`translation_brief.md` 未发现本机路径或密钥。

理由: i18n 目录没有凭据，但仍有本机绝对路径，需要发布前处理。

---

## 必修项清单

1. **清理候选发布集中的本机路径和用户名残留**  
   文件: `project_status.md`、`_workflows/desensitize_codex_log.py`、`_workflows/i18n/concat_en.py`、`split_for_translation.py`、`fix_part3_blocks.py`、`fix_part4a_templates.py`、`fix_all_blocks.py`、`fix_appendix_templates.py`。  
   建议: 脚本改为 `Path(__file__).resolve()` / 相对路径 / CLI 参数；状态文档改写为不含真实本机 token 的脱敏描述。

2. **重新确认 Git 发布边界并修正 inventory**  
   当前目录没有 `.git`，无法验证 tracked 集合。需要在最终发布仓库中运行 `git ls-files` / `git status --ignored` / `git ls-files -ci --exclude-standard`，确认 `_pipeline_output/` 和本轮 O7 提示词未被跟踪。`inventory.csv` 应从实际发布集合生成，而不是从物理全目录生成。

3. **移除或改写指向非发布同级目录的公开链接**  
   文件: `reference_files.md:84-91`、`en/reference_files.md:84-91`。  
   建议: 删除这些发布准备材料链接，或改为说明“发布准备材料不随仓库发布”，避免公开仓库断链。

4. **决定本报告是否进入公开仓库**  
   本报告已脱敏，但它是审查后新增文件；若要发布，应更新 inventory；若仅作为本地终验记录，应加入排除规则或移出发布包。

## 建议项清单

1. 在 `.gitignore` 中预防性加入 `_workflows/i18n/prompts/`、`_workflows/i18n/configs/en/chunks/`、`_workflows/i18n/logs/`、`_workflows/i18n/tmp/` 等翻译临时目录规则。
2. 增加一个只读 pre-publish 检查脚本，统一执行: inventory vs `git ls-files`、本机路径/用户名扫描、邮箱/token/IP 扫描、docx metadata 扫描。
3. 让 `inventory.csv` 记录生成命令和边界来源，例如 `source = git ls-files`，避免“物理目录清单”和“发布清单”混淆。

## 独立搜索策略摘要

本轮独立使用了: 已知 token 精扫、广义盘符路径正则、当前环境用户名/机器名 token 扫描、邮箱/token/私钥/私网 IP 扫描、敏感文件名扫描、`.docx` OOXML 元数据与内部 XML 扫描、`.gitignore` 手工边界模拟、inventory 差集比对、非发布同级目录链接扫描、模型 provenance 定向核查。

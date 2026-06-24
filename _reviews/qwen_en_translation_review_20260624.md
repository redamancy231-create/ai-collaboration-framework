# Qwen3.7-Max 对抗式校译报告

> **审校者**: Qwen3.7-Max (Qwen Code CLI)
> **审校角度**: Accuracy & Consistency（准确性与一致性）
> **日期**: 2026-06-24
> **中文源文档**: `AI协作项目全生命周期框架.md` (v1.6.4)
> **英文译稿**: `en/AI协作项目全生命周期框架.md`
> **翻译简报**: `_workflows/i18n/configs/en/translation_brief.md`
> **总体裁决**: **FIX_REQUIRED**（1 MEDIUM + 2 LOW）

---

## 1. 术语一致性

**PASS**

高频术语在全文中一致使用，对照翻译简报 §5 术语表逐项核查：

| 术语 | 一致性 | 备注 |
|------|--------|------|
| Three-Piece Suite | ✅ | 19处一致，无变体 |
| Write-Back | ✅ | 大写+连字符一致 |
| Independent Review | ✅ | 17+处一致 |
| Cross-Backend Review | ✅ | 一致 |
| Review Chain | ✅ | 一致 |
| Adversarial Review | ✅ | 一致 |
| Honesty Statement | ✅ | 17处一致 |
| Kill Criteria / Kill Conditions | ✅ | 一致 |
| Ceiling Effect | ✅ | 一致 |
| Opportunistic Observation | ✅ | 30处一致 |
| Reverse Precipitation | ✅ | 一致 |
| Evidence Level | ✅ | 一致 |
| Cross-Model Generalizability | ✅ | 一致 |
| Cross-Model Replication | ✅ | 一致 |
| Methodology Fragment (MF) | ✅ | 一致 |
| Compliance Teeth | ✅ | 低频但一致 |
| Failure Space | ✅ | 一致 |
| Rule Sunset | ✅ | 一致 |
| Closed-Loop Curation | ✅ | 一致 |
| OPEN Items Registry | ✅ | 一致 |
| Negative Result / Negative Conclusion | ✅ | 一致 |
| Single-Model Evidence Dominance | ✅ | 一致 |
| Claim Calibration | ✅ | 一致 |

无替代翻译或拼写变体被发现。

---

## 2. 保护元素完整性

**PASS_WITH_MINOR_ISSUES**

| 类别 | 结果 | 发现 |
|------|------|------|
| 证据标注 | ⚠️ | EN=157 vs ZH=158，缺失1处 `[B+/M1*]` |
| 版本号 | ✅ | v1.6.4~v1.1 全部保留 |
| 层/闸门/等级标签 | ✅ | L0-L5, L-H, HG-0~3, M0-M3, OPEN-1~5 全部保留 |
| Mermaid 代码块 | ✅ | EN=7, ZH=7，逐字一致 |
| 项目名 | ✅ | prompt-tdd/PocketFlow/GitNexus/Evolver/Small_Scale/BDC2026 未翻译 |
| 可执行代码块 | ✅ | 一致 |
| 文件路径 | ✅ | `_workflows/`/`_reviews/`/`_research/`/`_protocols-and-tools/`/`_archive/` 未翻译 |
| 检查点 ID | ✅ | CK1-CK6, PF-A1-001, PF-8, PF-9 保留 |

### 发现 #1

- **文件**: `en/AI协作项目全生命周期框架.md`, ~L1073（§4.1.1 交叉引用段）
- **问题**: 中文源 §4.1.1 交叉引用段末尾有 "**v1.6.4 发布前订正**：证据标注从 [B+/M2] 修正为 [B+/M1*]（Codex+Qwen 双后端独立审查裁决，2026-06-24）。" 该句在英文中**整句遗漏**，导致丢失 1 处 `[B+/M1*]` 证据标注。
- **建议修正**: 在 §4.1.1 cross-reference 段末尾（"Methodology fragments PT-M1..." 之前）添加：
  `**v1.6.4 pre-release correction**: Evidence label corrected from [B+/M2] to [B+/M1*] (Codex+Qwen dual-backend Independent Review adjudication, 2026-06-24).`

---

## 3. 完整性

**PASS_WITH_MINOR_ISSUES**

- **目录结构**: 中英文完全对应，14 章 + 所有子节无遗漏
- **表格完整性**: 769 行（EN）vs 769 行（ZH），列数一致
- **段落覆盖**: 头部元数据块（~30行）、§1.5 死亡判据表、§1.6 OPEN Items 表、§2.2 Spec 内容表、§2.4 映射表、所有 blockquote 段落均完整翻译
- **遗漏**: 仅上述 §4.1.1 交叉引用段缺失 v1.6.4 订正句（与检查 #2 发现 #1 为同一问题）

---

## 4. 准确性

**PASS**

### 技术概念

- "复盘" → "Retrospect" / "Post-Mortem Analysis" ✅（无 generic "review" 或 "retrospective" 误用）
- "三件套" → "Three-Piece Suite" ✅（无 "three-piece set" / "triple suite"）
- "闸门" → "Gate" ✅（无 "floodgate" / "sluice"）
- "写回" → "Write-Back" ✅（大写连字符一致）

### 否定逻辑抽查

| 中文原文 | 英文译文 | 判定 |
|---------|---------|------|
| 框架失败永远会被解释成"执行不到位"而非"框架无效" | framework failure will always be explained as "poor execution" rather than "the framework is invalid" | ✅ 方向正确 |
| 不并入任何复扩表 | not merged into any re-expansion table | ✅ |
| 不接受新增 [Sp] / 机制节 | no new [Sp] / mechanism sections are accepted | ✅ |
| 上层弱不能靠下层强来弥补 | A weak upper layer cannot be compensated for by a strong lower layer | ✅ |
| 框架自身也必须有——否则… | The framework itself must also have them. Otherwise… | ✅ |

### 数字/百分比/统计量抽查

| 中文源 | 英文译文 | 判定 |
|--------|---------|------|
| 30% 复杂度 | 30% Complexity | ✅ |
| 15%（维护成本阈值） | 15% | ✅ |
| 70%（HG 过载阈值） | 70% | ✅ |
| n=24/arm | n=24/arm | ✅ |
| n=20/arm | n=20/arm | ✅ |
| ΔF1=0.000 | ΔF1=0.000 | ✅ |
| 0.954（correctness_rate） | 0.954 | ✅ |
| 7 轮双后端审查链 | 7-round dual-backend Review Chain | ✅ |
| 58 项发现 | 58 findings | ✅ |
| 42K星 | 42K-star | ✅ |

未发现数字错误。

---

## 5. 风格违规

**PASS**

### 英式拼写

搜索 `organise` / `realise` / `normalise` / `recognise` / `analyse` / `behaviour` / `colour` / `favour` / `honour` / `centre` / `metre` / `theatre` → **0 匹配**

### 营销语言

搜索 `groundbreaking` / `revolutionary` / `cutting-edge` / `state-of-the-art` / `game-changing` / `innovative` / `unprecedented` → **0 匹配**

### 语气软化抽查

- "必须" → "must" ✅（未降级为 "should" / "may"）
- "不要一上来就全量启用" → "Do not enable everything at once" ✅
- "不是必做清单" → "not a mandatory checklist" ✅
- 作者直接/坦率语气保持良好，未见不当软化

---

## 6. 交叉引用

**PASS_WITH_MINOR_ISSUES**

- §X.X 节号引用全部保留，编号未改动 ✅
- 文件路径引用完整 ✅
- 6 处 Mermaid 图引用正确 ✅

### 发现 #2

- **文件**: `en/AI协作项目全生命周期框架.md`, L1075
- **问题**: HTML 锚点 `<a id="4111-对照实验设计强制检查清单"></a>` 仍为中文 ID，与英文目录链接不匹配
- **建议修正**: `<a id="4111-mandatory-checklist-for-controlled-experiment-design"></a>`

### 发现 #3

- **文件**: `en/AI协作项目全生命周期框架.md`, L1636
- **问题**: Markdown 锚点引用 `(#附录-h-反模式清单)` 指向中文 ID
- **建议修正**: `(#appendix-h-anti-pattern-catalog)`

---

## 7. 中文残留

**PASS_WITH_MINOR_ISSUES**

全文扫描结果（3790 行中 432 行含 CJK 字符），分类如下：

| 类别 | 行数（估） | 判定 |
|------|-----------|------|
| Mermaid 代码块内中文 | ~60 行 × 7 块 | ✅ 受保护 |
| 代码块/模板块内中文 | ~200 行 | ✅ 受保护 |
| 反引号内文件名 | ~30 行 | ✅ 受保护（文件名不翻译） |
| §13.1.2 项目代号表（形态匹配/并购重组/ETF 项目 V3.6） | 3 行 | ✅ 可接受（项目原始中文标识符，紧邻列有英文描述） |
| HTML 锚点中文（L1075） | 1 行 | ⚠️ 见发现 #2 |
| Markdown 锚点引用中文（L1636） | 1 行 | ⚠️ 见发现 #3 |

**无正文散文中的未译中文段落或句子。**

---

## 8. 核心格言

**PASS**

10 条核心格言均在英文中找到，保持警句力度：

| # | 中文 | 英文实际用词 | 位置 | 力度 |
|---|------|------------|------|------|
| 1 | 方向盘 > 发动机 | **Steering Wheel > Engine** | L70 | ✅ 简洁 |
| 2 | 分层不互相替代 | **Layers Are Not Interchangeable** | L71 | ✅ 断言式 |
| 3 | AI 内部闭环 ≠ 人类审查 | **AI Internal Closed Loop ≠ Human Review** | L73 | ✅ 符号保留 |
| 4 | 从失败中反向沉淀 | **Reverse Precipitation from Failures** | L72 | ✅ 有力 |
| 5 | 离散审查测不出连续漂移 | **Discrete Reviews Cannot Detect Continuous Drift** | L23, L202 | ✅ 全称否定 |
| 6 | 30% 复杂度就能跑 | **Runs at 30% Complexity** | L173 | ✅ 口语化 |
| 7 | 加复杂度比减复杂度容易 | **Adding Complexity Is Easier Than Removing It** | L19 | ✅ 格言式 |
| 8 | 沉默省略仍是弱实践 | **Silent Omission Is Still Weak Practice** | — | ✅ |
| 9 | 规则只增不减 | **Rules Only Increase, Never Decrease** | — | ✅ |
| 10 | 新增观测，不新增阻断 | **Add Observability, Not Blocking** | L203 | ✅ 祈使式 |

---

## 总体裁决：FIX_REQUIRED

翻译整体质量高。术语一致、保护元素完好、无英式拼写/营销语言、核心格言有力。

仅有 **3 处需修正的问题**：

| # | 严重性 | 位置 | 问题 | 修正建议 |
|---|--------|------|------|----------|
| 1 | **MEDIUM** | en/ ~L1073（§4.1.1 交叉引用段） | v1.6.4 发布前订正句整句遗漏，丢失 `[B+/M1*]` 证据标注 | 在段末 "Methodology fragments..." 前补入 v1.6.4 pre-release correction 句 |
| 2 | LOW | en/ L1075 | HTML 锚点 ID 残留中文 `4111-对照实验设计强制检查清单` | 改为 `4111-mandatory-checklist-for-controlled-experiment-design` |
| 3 | LOW | en/ L1636 | Markdown 锚点引用残留中文 `#附录-h-反模式清单` | 改为 `#appendix-h-anti-pattern-catalog` |

---

> **审校说明**: 本报告为翻译审查链中第一个对照中文源文档的审校。后续 Kimi-K2.6 可读性审查将独立评估英文文本的流畅度和学术可发表性（不对照中文源）。

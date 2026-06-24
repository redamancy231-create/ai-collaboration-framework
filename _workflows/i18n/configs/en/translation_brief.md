# English Translation Brief — AI协作项目全生命周期框架 v1.6.4

> **Date**: 2026-06-24 | **Prepared by**: DeepSeek-V4-Pro (via Claude Code CLI)
> **Workflow**: GPT-5.5 (Codex CLI) initial translation → Qwen3.7-Max (Qwen Code CLI) adversarial review → Kimi-K2.6 (Kimi Code CLI) readability & publishability review

---

## 1. Scope

Three files, output to `en/` directory:

| File | Approx. Size | Notes |
|------|-------------|-------|
| `AI协作项目全生命周期框架.md` | ~166K chars / ~310KB | Main framework document; 14 sections + appendices |
| `README.md` | ~9KB | Repository landing page |
| `reference_files.md` | ~7KB | File index with descriptions |

Filenames remain in Chinese (cross-references from `en/` use `../` relative links to root).

---

## 2. Translation Workflow

```
GPT-5.5 initial translation
        ↓
Qwen3.7-Max adversarial review (focus: accuracy, terminology, completeness)
        ↓
Kimi-K2.6 readability review (focus: native fluency, academic publishability)
        ↓
Back-translation spot-check (sample 3-5 paragraphs)
```

### GPT-5.5 (Initial Translator)

- Translate the **full body text** of all three files
- Preserve all protected elements (see §4) exactly as-is
- Follow terminology table (§5) for consistency
- Follow style conventions (§3)
- Translate section by section; do NOT skip any section
- When uncertain about a term, flag it with `<!-- TRANSLATOR-NOTE: ... -->` HTML comment

### Qwen3.7-Max (Adversarial Reviewer — Angle: Accuracy & Consistency)

- **Adversarial stance**: assume errors exist, actively hunt for them
- Check terminology consistency across all three files (cross-reference with §5 term table)
- Verify protected elements are untouched (code blocks, Mermaid, evidence annotations, cross-references, version numbers)
- Flag: mistranslations, inconsistent terminology, missed/untranslated Chinese text, style violations (British spellings, marketing tone)
- Do NOT rewrite for elegance — only fix errors; preserve the author's direct voice
- Output: list of findings with file/line/error-type/fix

### Kimi-K2.6 (Readability Reviewer — Angle: Native Fluency & Academic Publishability)

**This is a DIFFERENT angle from Qwen.** Qwen hunted for bugs; you evaluate whether the English reads as **credible academic-technical prose** to a native English speaker.

- **Role**: You are a native English-speaking academic editor evaluating whether this translated methodology document is publishable on GitHub as a serious reference work.
- **Read the English output as if you've never seen the Chinese original.** Ask:
  1. Does it flow naturally, or does it "sound translated"? Flag unnatural phrasing, calques, awkward constructions.
  2. Would an English-speaking ML/AI researcher find the prose credible, or does it undermine the author's authority?
  3. Are there passages where you literally cannot understand what is being said without reading the Chinese source? (opacity check)
  4. Do the invented concepts (Three-Piece Suite, Reverse Precipitation, Compliance Teeth, etc.) come across as deliberate terminology or as translation errors?
  5. Are the maxims (§5 core maxims) punchy and memorable in English, or did they lose their force?
- **Constraints**:
  - Do NOT re-translate from scratch — only suggest improvements to the existing translation
  - Do NOT check against the Chinese source (that was Qwen's job) — evaluate the English as a standalone text
  - Flag passages where you suspect a translation error based on internal inconsistency, even without checking the source
  - Preserve the author's direct/blunt tone — don't soften for politeness
- **Output**: list of findings with file/line/issue-type/suggested-fix. Categorize as: AWKWARD (unnatural phrasing), OPAQUE (incomprehensible), CREDIBILITY (undermines authority), STYLE (tone violation), SUSPECTED-ERROR (probable mistranslation based on internal inconsistency).

---

## 3. Style Conventions

### American English
- Spelling: `-ize` (not `-ise`), `-or` (not `-our`), `behavior` (not `behaviour`)
- Punctuation: double quotes `"..."` for quoted text; serial (Oxford) comma
- Dates: `YYYY-MM-DD` (keep existing format)

### Tone & Voice
- **Academic-technical**, not marketing-speak
- **Clarity > elegance** — prioritize unambiguous meaning over idiomatic flow
- **Preserve the alien quality** of invented concepts — they are NOT standard English terms; don't force them into idiomatic English
- The author uses a direct, sometimes blunt tone — preserve it, don't soften
- First-person plural ("我们") → "we" when referring to the framework's normative stance; use "the author" when clearly referring to the individual
- Second-person ("你") → "you" in instructional context; rewrite to neutral third-person in narrative passages

### Structural Conventions
- Chinese section references `§X.X` → keep as `§X.X`
- Chinese bullet points `-` → keep as `-`
- Table alignment: preserve column count and structure
- Footnotes: preserve numbering and placement

---

## 4. Protection Rules — DO NOT TRANSLATE

These elements must pass through **unchanged** to the English output:

### Always Protected
| Category | Examples | Rule |
|----------|----------|------|
| Executable code blocks | ` ```python ... ``` `, ` ```bash ... ``` `, ` ```shell ... ``` ` | Entire block unchanged |
| Template code blocks | ` ```markdown ... ``` ` in §12 (Appendix templates) | **Translate labels and placeholder descriptions** inside the block; keep structure (headings, indentation, `____` blanks) intact |
| Inline code | `` `VERSION` ``, `` `metadata.version` `` | Backtick content unchanged |
| Mermaid diagrams | ` ```mermaid ... ``` ` | Entire block unchanged |
| HTML comments | `<!-- ... -->` | Unchanged (use for translator notes) |
| File paths | `_workflows/`, `_reviews/`, `../_attic/` | Unchanged |
| URLs | `https://...`, `arXiv:...` | Unchanged (text part may translate) |
| Project names | `prompt-tdd`, `PocketFlow`, `GitNexus`, `Evolver`, `Small_Scale`, `PilotDeck`, `BDC2026` | Unchanged |

### Evidence & Notation
| Category | Symbols | Rule |
|----------|---------|------|
| Evidence annotations | `[S]` `[E]` `[E-]` `[I]` `[J]` `[Sp]` `[D/N/A]` `[SEMI-ED]` `[C+/N/A]` `[B+/M1*]` etc. | Never translate; never add/remove spaces around brackets |
| Layer labels | `L0` `L1` `L2` `L3` `L4` `L5` `L-H` | Keep exactly |
| Gate labels | `HG-0` `HG-1` `HG-2` `HG-3` | Keep exactly |
| Evidence strength | `A` `B+` `B` `C+` `C` `D` | Keep exactly |
| Cross-model grades | `M0` `M1` `M1*` `M2` `M3` `N/A` | Keep exactly; `M1*` asterisk is meaningful |
| OPEN items | `OPEN-1` through `OPEN-5` | Keep exactly |
| Version numbers | `v1.6.4`, `v1.5.5`, etc. | Keep exactly |
| Checkpoint IDs | `CK1`–`CK6`, `PF-A1-001`, `PF-8`, `PF-9` | Keep exactly |
| Protocol labels | `Protocol 3`, `C1`–`C8` | Keep exactly |

### Framework-Specific Terms (keep as-is)
| Term | Reason |
|------|--------|
| `Dev Log` | Framework artifact name; keep capitalized |
| `Spec` | Framework layer name; always capitalized |
| `provenance` | Operational term; always lowercase |
| `CLAUDE.md` | File naming convention |
| `checkpoint` / `gate` / `agent` / `pipeline` / `workflow` | When used as framework operational terms (not generic English) |
| `kill-test-first` | Skill name |
| `prompt-tdd` | Project name; always lowercase with hyphen |

---

## 5. Key Terminology Reference

Full glossary: `_workflows/i18n/glossary.json` (190 terms). Below are the **high-frequency terms** that must be consistent across all three files:

### Framework Architecture
| 中文 | English |
|------|---------|
| 框架 | framework |
| 层 | layer |
| 跨层关切 | cross-layer concern |
| 核心 vs 外挂 | core vs companion |
| 最小可行 Prompt 六要素 | Six Elements of a Minimum Viable Prompt |
| 使用强度分档 | Usage Intensity Tier |
| 最低强制版/默认版/完整版 | Minimum Mandatory / Default / Full Edition |
| 项目规模分档 | Project Scale Tier |

### Layers
| 中文 | English |
|------|---------|
| Spec（项目宪法） | Spec (Project Constitution) |
| L-H Human Gate（人类闸门） | L-H Human Gate |
| L1 Context（上下文管理）/ Prompt（任务规格） | L1 Context (Context Management) / Prompt (Task Specification) |
| L2 Execute（执行）/ Loop（执行迭代） | L2 Execute (Execution) / Loop (Execution Iteration) |
| L3 Review（审查）/ Workflow（多任务编排） | L3 Review (Review) / Workflow (Multi-Task Orchestration) |
| L4 Retrospect（复盘） | L4 Retrospect (Post-Mortem Analysis) |
| L5 Closure（封存） | L5 Closure (Archival & Sunset Determination) |
| 漂移检测层 | Drift Detection Layer |

### Key Concepts
| 中文 | English |
|------|---------|
| 三件套 | Three-Piece Suite |
| 三件套同步协议 | Three-Piece Suite Synchronization Protocol |
| 独立审查 | Independent Review |
| 异后端审查 | Cross-Backend Review |
| 审查链 | Review Chain |
| 审查门 | Review Gate |
| 写回 | Write-Back |
| 写回审查门 | Write-Back Review Gate |
| 魔鬼代言人审查 | Adversarial Review |
| 交叉验证 | Cross-Verification |
| 冻结期 | Freeze Period |
| 反向沉淀 | Reverse Precipitation |
| 被动观测 | Opportunistic Observation |
| 诚实声明 | Honesty Statement |
| 死亡判据 | Kill Criteria |
| 否决条件 | Kill Conditions |
| 逃生口 | Escape Hatch |
| 分级逃生口 | Tiered Escape Hatch |
| 合规牙齿 | Compliance Teeth |
| 声称校准 | Claim Calibration |
| 天花板效应 | Ceiling Effect |
| 规则退役 | Rule Sunset |
| 闭环策展 | Closed-Loop Curation |
| 已知待决项登记（OPEN items） | OPEN Items Registry |
| 已知反例 | Known Counterexamples |
| 失效空间 | Failure Space |
| 方法论片段（MF） | Methodology Fragment (MF) |
| 作者-读者同构假设 | Author-Reader Structural Isomorphism Assumption |
| 外部依赖漂移风险 | External Dependency Drift Risk |

### Evidence System
| 中文 | English |
|------|---------|
| 证据二维矩阵 | Two-Dimensional Evidence Matrix |
| 证据等级 | Evidence Level |
| 内部强度 | Internal Strength |
| 跨模型推广性 | Cross-Model Generalizability |
| 阴性结果 | Negative Result |
| 阴性结论 | Negative Conclusion |
| 单模型证据主导 | Single-Model Evidence Dominance |
| 跨模型复现 | Cross-Model Replication |

### Experimentation
| 中文 | English |
|------|---------|
| 对照实验 | Controlled Experiment |
| 预登记（pre-registration） | Pre-Registration |
| 双评分者盲评协议 | Dual-Rater Blinded Scoring Protocol |
| 格式效应 | Format Effect |
| 结构效应 | Structure Effect |
| 路由声明 | Routing Declaration |
| 屏障并行（barrier parallel） | Barrier Parallel |
| 迭代至枯竭（loop-until-dry） | Loop-Until-Dry |
| 评委团（judge panel） | Judge Panel |
| 对抗验证（adversarial verify） | Adversarial Verification |
| 完备性审查（completeness critic） | Completeness Critic |

### Drift Detection
| 中文 | English |
|------|---------|
| 五类漂移信号 | Five Categories of Drift Signals |
| 漂移信号（句法/语义/程序/对齐/绩效） | Drift Signals (Syntactic / Semantic / Procedural / Alignment / Performance) |
| 静默失效 | Silent Failure |
| 静默失效信号 | Silent Failure Signal |
| 四级告警 | Four-Level Alerting |
| 信号聚合与告警规则 | Signal Aggregation & Alert Rules |
| 难度分层漂移 | Difficulty-Stratified Drift |
| 事件流健康度监测 | Event Stream Health Monitoring |
| 自适应权重淘汰 | Adaptive Weight Pruning |

### Workflow Patterns
| 中文 | English |
|------|---------|
| 嵌套工作流 | Nested Workflow |
| 流水线（pipeline） | Pipeline |
| 声明式管道执行（Pipeline DAG） | Declarative Pipeline Execution (Pipeline DAG) |
| 结构化多角色审查（Structured Multi-Role Review） | Structured Multi-Role Review |
| 会话交接（Session Handoff） | Session Handoff |
| 多后端审查链 | Multi-Backend Review Chain |
| 审查维度互补设计 | Complementary Review-Dimension Design |
| 双轴独立性 | Dual-Axis Independence |
| 上下文隔离 | Context Isolation |
| 路径隔离原则 | Path Isolation Principle |

### Meta / Maintenance
| 中文 | English |
|------|---------|
| 版本号规则 | Versioning Rules |
| 语义化版本 | Semantic Versioning |
| 版本时间线 | Version Timeline |
| 硬关卡（hard gate） | Hard Gate |
| 科学门（science gates） | Science Gates |
| 强制启用清单 | Mandatory Activation Checklist |
| 框架级成熟度评估表 | Framework-Level Maturity Assessment Table |
| 反模式清单（附录H） | Anti-Pattern Catalog (Appendix H) |
| 自指涉节 | Self-Referential Section |

### Other Common Terms
| 中文 | English |
|------|---------|
| 后端 | backend |
| 审查 | review |
| 模板 | template |
| 源码 | source code |
| 配置 | configuration |
| 默认 | default |
| 命令行 | command line |
| 软件 | software |
| 数据 | data |
| 日志 | log |
| 服务器 | server |
| 接口 | interface |
| 实现 | implementation |
| 质量 | quality |
| 网络 | network |
| 框架 | framework |

### Core Maxims (translate for meaning, preserve punchiness)
| 中文 | English |
|------|---------|
| 方向盘 > 发动机 | Steering Wheel > Engine |
| 分层不互相替代 | Layers Are Not Interchangeable |
| AI 内部闭环 ≠ 人类审查 | AI Internal Closed Loop ≠ Human Review |
| 从失败中反向沉淀 | Reverse Precipitation from Failures |
| 离散审查测不出连续漂移 | Discrete Reviews Cannot Detect Continuous Drift |
| 30% 复杂度就能跑 | Runs at 30% Complexity |
| 加复杂度比减复杂度容易 | Adding Complexity Is Easier Than Removing It |
| 沉默省略仍是弱实践 | Silent Omission Is Still Weak Practice |
| 规则只增不减 | Rules Only Increase, Never Decrease |
| 新增观测，不新增阻断 | Add Observability, Not Blocking |

---

## 6. Known Tricky Areas

### Section References
Chinese `§X.X` format is identical to English — keep as-is. The section numbers must remain unchanged.

### Chinese Parenthetical Notes
Pattern: `中文术语（English translation）` → becomes `English Translation` on first occurrence, with parenthetical Chinese if needed for disambiguation.

### Table Cell Alignment
Tables may use Chinese-width characters that affect alignment in plaintext. After translation, verify all tables have the same column count and structure.

### Mermaid Diagrams
Six Mermaid diagrams in the main document — ALL protected. Do NOT translate labels inside Mermaid code blocks (they're part of the diagram source).

### Template Markdown Blocks (§12 Appendices)
The Spec template, Prompt template, Retrospect template, Closure template, Session template, and Risk Register template are in ` ```markdown ` fenced code blocks (§12). These are **NOT executable code** — they are templates meant for human readers to copy and adapt. **Translate the labels and placeholder descriptions** inside these blocks. For example:
- `## S1: 项目状态` → `## S1: Project Status`
- `## 任务: [一句话描述]` → `## Task: [one-line description]`
- `- 输出物: ____` → `- Deliverable: ____`

Keep intact: heading levels, indentation, `____` blanks, `[ ]` checkboxes, and template structure markers.

### Version Timeline Table
§14 version timeline — translate event descriptions and evidence notes, but keep version numbers, dates, and confidence indicators (`✅`, `🟡`, `⚠️`) exactly as-is.

### Errata / Corrections Notes
The document contains self-referential errata notes (e.g., "v1.6.4 发布前订正"). Translate these but preserve the version number references.

### Deeply Nested Lists
Some sections have 3-4 levels of nested lists. Preserve the nesting structure exactly.

---

## 7. Review Criteria Summary

### Qwen3.7-Max Checklist (Accuracy & Consistency)

When reviewing GPT-5.5's translation, check:

1. **Terminology Consistency**: Same Chinese term → same English translation across all three files
2. **Protected Elements**: Zero modification to code blocks, Mermaid, evidence annotations, cross-references
3. **Completeness**: No skipped sections, no dropped sentences
4. **Accuracy**: No mistranslations of technical concepts
5. **Style**: American English conventions; no British spellings
6. **Voice**: Academic-technical tone preserved; no marketing-speak introduced
7. **Table Integrity**: Same row/column counts as source
8. **Cross-References**: `§X.X` links still point to correct sections (section numbers unchanged)
9. **Residual Chinese**: Scan for untranslated Chinese text outside protected elements
10. **Maxim Punchiness**: Core maxims (§5) retain their aphoristic quality

### Kimi-K2.6 Checklist (Readability & Publishability)

Evaluate the English output as a **standalone text** (do not compare against Chinese source):

1. **Natural Flow**: Does prose read like original English, not translated English? Flag calques, awkward constructions, unnatural word order.
2. **Academic Credibility**: Would this pass as serious academic-technical writing in English? Flag anything that undermines authorial authority.
3. **Opacity**: Any passages genuinely incomprehensible without the Chinese source? Flag and suggest clarification.
4. **Terminology Feel**: Do invented concepts read as deliberate coinages or as translation errors? Flag the latter.
5. **Maxim Force**: Do the core maxims land with punch in English? Suggest alternatives if they fell flat.
6. **Tone**: Is the author's direct/blunt voice preserved? Flag unintended softening or marketing-speak creep.
7. **Internal Consistency**: Flag probable errors detectable from English text alone (e.g., a term used two different ways, a contradiction between sections).

**Output categories**: AWKWARD / OPAQUE / CREDIBILITY / STYLE / SUSPECTED-ERROR — each with file, line, and suggested fix.

---

## 8. Output

Place translated files in `en/`:
```
en/
├── AI协作项目全生命周期框架.md
├── README.md
└── reference_files.md
```

Internal cross-references within `en/` should use relative paths to root (e.g., `../_reviews/...`), same as the Chinese originals.

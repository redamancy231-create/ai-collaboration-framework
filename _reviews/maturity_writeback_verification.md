# 成熟度表写回核查

## 结论

- 通过：10 项
- 存疑：5 项
- 不通过：1 项
- 需要修正：有。主要是 §9 的 C1/C5 表述、审查轮数口径、以及 L5 闭合行对 Protocol 3 PASS / 闭合检查“全部通过”的表述过于干净。

本轮核查范围为 `框架级成熟度评估表.md` 中标注“试跑1”的 8 行和 §9；主要依据 `方法论提取方法论` 项目文件、Kimi Phase 8 事实核查报告和相关审查报告。

## 发现

### F1 存疑：14/20 loops 与“最终值”口径需注明

位置：`框架级成熟度评估表.md:7,20,170,183`

成熟度表写“14/20 loops”。这与项目闭合时记录一致：`DEV_LOG.md:222` 写明 20:22 项目闭合，C7 为 14/20；Loop 汇总表也为总计 14（`DEV_LOG.md:33`），C7 指标行为 14/20（`DEV_LOG.md:48`）。

但闭合后 Kimi Phase 8 事实核查被记录为追加 loop，`DEV_LOG.md:224` 写 “C7: 14->15/20”。因此若“最终值”指包含闭合后事实核查，则成熟度表的 14/20 不是最新 DEV_LOG 末尾值；若指项目闭合时 Protocol 3 试跑值，则成立。

建议修正：将“14/20 loops”改为“闭合时 14/20 loops；闭合后 Kimi 核查追加至 15/20”。

### F2 存疑：审查轮数存在 10 / 11 两种口径

位置：`框架级成熟度评估表.md:61,167,184,193`

成熟度表在不同位置同时写“reviews/ 含 11 轮审查报告”“10 轮”“11 轮审查”。文件证据支持两种口径，但需要说明：

- `project_spec.md:35` 写 10 轮异后端审查，不含 Phase 3.5 Codex 复编码。
- `CLAUDE.md:10` 列出 11 项，包含 Phase 3.5 Codex 复编码。
- `reviews/` 目录实际有 12 个 `.md` 文件，其中包含 `qwen_phase4_reverify_report.md` 和 `kimi_phase8_factcheck_report.md`，不等于简单“11 轮审查报告”。
- `DEV_LOG.md:49` 的 C8 当前值仍写“8轮审查完成”，已明显滞后于后续记录。

建议修正：统一口径为“10 轮异后端审查，不含复编码；若计入 Phase 3.5 复编码为 11 项审查/核查活动”。避免把 `reviews/` 目录文件数直接等同审查轮数。

### F3 通过：58 项发现、0 CRITICAL 遗留与最终框架文档 header 一致

位置：`框架级成熟度评估表.md:187`

最终框架文档 header 写：R5 Phase 7.6 为 7.7/10 GO，4 MAJOR 已修正；五轮合计 58 项发现，0 CRITICAL 遗留，0 MAJOR 遗留（`framework_output/main/方法论提取框架_v0.1_trial.md:14-15`）。DEV_LOG 也在 21:15 记录 Phase 7.6 4 MAJOR 遗留修正完成，并写“58 项发现，0 CRITICAL，0 MAJOR 遗留”（`DEV_LOG.md:226-232`）。

注意：Retrospect 正文仍保留“4 MAJOR 已知遗留”的历史口径（`archive/phase8_retrospect_report.md:137,154`），但后续 DEV_LOG 与最终框架文档已补修。成熟度表引用“试跑项目最终状态”时成立。

### F4 通过：最高 7.7 与 Phase 7.6 报告一致

位置：`框架级成熟度评估表.md:159,184`

`reviews/phase7.6_codex_targeted_review_report.md:11-15` 明确写综合评分 7.7/10，判定 GO。DEV_LOG 的 Phase 7 系列汇总也把 Phase 7.6 Codex 标为 7.7 GO（`DEV_LOG.md:206,216`）。

### F5 不通过：C1/C5 “未定义测量方法”表述不准确

位置：`框架级成熟度评估表.md:165`

成熟度表写“指标定义了目标值但未定义测量方法（C1 ‘中位数 <=20min/条’ 但未指定如何计时）”。这与 `spec/success_criteria.md` 不一致：C1 的测量方式为“每 phase 首条 prompt 计时；复杂任务允许例外记录”，C5 的测量方式为“Dev Log 记录框架相关操作时间；首次试跑不稳定，记录为基线数据”（`spec/success_criteria.md:31-38`）。

真实问题是执行计时不完整：`DEV_LOG.md:41,46` 记录 C1/C5 未完整计量/计时；Retrospect 也写 C1/C5 未完整计时（`archive/phase8_retrospect_report.md:38-44,76-81`）。Kimi 已指出“测量方法已定义，但具体计时工具未指定/执行不完整”。

建议修正：改为“C1/C5 计时执行缺失：有粗略测量口径，但未指定可靠计时工具，且 DEV_LOG 未完整记录”。

### F6 通过：审查频率从 Phase 7 一次演变为持续审查有证据

位置：`框架级成熟度评估表.md:167`

原计划证据成立：`spec/evaluation_plan.md:14-18` 将独立模型审查列为 Phase 7；`spec/evaluation_plan.md:75-76` 的 Phase 7 交付物为 Codex CLI 审查报告。项目执行中，`project_spec.md:22,82` 明确记录独立审查从“Phase 7 一次”演变为“每 Phase 后一次/持续模式”。

建议微调：成熟度表写“10 轮”时应按 F2 明确口径。

### F7 通过：Phase 5 Codex+Qwen 零重叠有报告自证

位置：`框架级成熟度评估表.md:168`

Codex Phase 5 报告列 17 项发现（`reviews/phase5_codex_crosscheck.md:23-43`）。Qwen Phase 5 报告写 16 项发现全部为 Codex 未覆盖的增量发现，统计为 0 CRITICAL / 13 MAJOR / 3 MINOR（`reviews/phase5_qwen_independent_review.md:192-213`），并在互补关系表写“两轮审查维度正交，发现无重叠”“33 项发现”（`reviews/phase5_qwen_independent_review.md:227-240`）。

### F8 存疑：提取者效应 22% / 9.4% 的引用文件需拆开

位置：`框架级成熟度评估表.md:169`

22% 显著分歧率和 ~65% inflation 在 `synthesis/phase3_recoding_comparison.md:55-76` 有直接证据。9.4% 不在该 Phase 3 复编码文件中，而是在 Qwen 复验证后合并到 `synthesis/phase4_validated_pattern_catalog.md:20,41-47`。

建议修正：写为“Phase 3 复编码得到显著分歧率 22% 与独有特征 inflation ~65%；Phase 4/Qwen 复验证将纯效应修正为 ~9.4%”。

### F9 通过：8 行升级所引文件路径均存在

位置：`框架级成熟度评估表.md:44-61`

本轮抽查涉及的关键路径均存在：`project_spec.md`、`DEV_LOG.md`、`CLAUDE.md`、`archive/phase8_retrospect_report.md`、`reviews/phase5_*`、`reviews/phase7*`、`reviews/kimi_phase8_factcheck_report.md`、`synthesis/phase3_recoding_comparison.md`、`synthesis/phase4_validated_pattern_catalog.md`、`framework_output/main/方法论提取框架_v0.1_trial.md`。

### F10 通过但需限缩：L0 Spec 维护机制升级为“部分验证”合理

位置：`框架级成熟度评估表.md:44`

`project_spec.md` 和 `CLAUDE.md` 均为 v1.0 闭合状态，且记录初始 plan/spec 未审、持续审查、闭合状态等写回信息（`project_spec.md:3-36`）。Phase 5/7/7.5 的审查发现及修正也在 DEV_LOG 和 CLAUDE 版本记录中可追踪。

“部分验证”合理，但“反向沉淀频率：每 Phase 后”略强。实际是 Phase 2/3/4/5/6/7/8 均有审查或同步记录，但并非每个 Phase 都有同等框架级反向沉淀。

### F11 通过：HG-0/HG-1 与 AI 未越权两行升级合理

位置：`框架级成熟度评估表.md:45-46`

HG-0 触发及 Codex 7.2/10、5 项强制修订见 `DEV_LOG.md:61-69`。HG-1 决策 OPEN-2/OPEN-3 选项 B/B、用户确认但交互内容未留存见 `DEV_LOG.md:167-169`。成熟度表已保留“HG-2/3 未触发”“交互记录留存需改进”“仅 1 次 HG-1”的限制，升级到部分验证不过度。

### F12 通过：L4 Retrospect 模板与最小发现数升级合理

位置：`框架级成熟度评估表.md:56-57`

Retrospect 按深度版模板执行，说明覆盖失效清单、意外发现、Protocol 3 实测、成熟度写回等字段（`archive/phase8_retrospect_report.md:12-14`），并产出 3 失效 + 3 意外（`DEV_LOG.md:220`；`archive/phase8_retrospect_report.md:20,38,50` 等）。Kimi 核查也认可大部分事实，但指出若干修正项。成熟度表将其限为 N=1 的“部分验证”合理。

### F13 存疑：L5 闭合条件/清单的“全部通过”应改为“条件闭合后补修”

位置：`框架级成熟度评估表.md:59-60`

成熟度表写“Protocol 3 PASS”“全部 7 项通过”。但 Retrospect 经 Kimi 修正后，总裁决为“IMPROVE→条件PASS”，不是严格 PASS（`archive/phase8_retrospect_report.md:86,152-154`）。闭合检查中也明确写 Phase 7.6 4 MAJOR 为已知遗留（`archive/phase8_retrospect_report.md:137,154`）。这些 MAJOR 后来在 21:15 补修完成（`DEV_LOG.md:226-232`）。

因此“L5 Closure 部分验证”可以成立，但成熟度表当前叙述过于乐观。

建议修正：改为“Retrospect 时为 IMPROVE→条件PASS，Phase 7.6 4 MAJOR 作为已知遗留；闭合后 21:15 已补修为 0 MAJOR 遗留”。闭合清单不应写“试跑1 未发现缺失项”，因为 Kimi 明确指出过闭合条件表述和发现数口径问题。

### F14 存疑：归档路径规范的“11 轮审查报告”需按目录实际情况改写

位置：`框架级成熟度评估表.md:61`

归档目录结构成立：`archive/`、`reviews/`、`synthesis/`、`explorations/` 均存在，且含对应产物。但 `reviews/` 实际 `.md` 文件为 12 个，项目文档口径为 10 轮审查或 11 项活动。此行应避免写死“11 轮审查报告”。

建议修正：改为“reviews/ 含 HG-0、Phase 2/3/4/5/6/7/7.5/7.6/8 等审查、复验证和事实核查报告；轮数口径见 §9 注释”。

### F15 通过：负面结果没有完全省略，但成熟度表应更显式保留

位置：`框架级成熟度评估表.md:56-61,165-187`

负面结果在 §9 中已有记录：C1/C5 未完整计时、C4 交互记录不足、总裁决为 IMPROVE→条件PASS、Phase 7.6 曾有 4 MAJOR 遗留。成熟度表的问题不是完全省略，而是 L5 行的措辞把这些条件和补修过程压平了。

建议：在 L5 三行补一句“本验证包含一次条件闭合后的事实核查与补修，非首次闭合即完全无遗留”。

### F16 通过：从待实证/零数据升级为“部分验证”总体不过度

位置：`框架级成熟度评估表.md:44-61,130`

8 行均有真实试跑文件支撑，且成熟度表没有升级为“已验证”，而是“部分验证”。考虑到 N=1、单项目、同一操作者、闭合后补修等局限，升级到“部分验证”总体合理。需要下调的不是等级，而是叙述精确度，尤其是 C1/C5、审查轮数、L5 闭合状态三处。

#!/usr/bin/env python3
"""Comprehensive fix: translate all remaining CJK in non-Mermaid code blocks."""
import sys
from pathlib import Path, re
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

TARGET = str(PROJECT / "en/AI协作项目全生命周期框架.md")

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
all_fixes = []

def add(old, new):
    global count, content
    if old in content:
        content = content.replace(old, new)
        count += 1

# === §4.1.1.1 INVENTORY protocol ===
for o, n in [
    ("设计者自评（全部标记 ✓/✗）", "Designer self-assessment (mark all ✓/✗)"),
    ("异后端非设计者独立审查（不知道设计者自评结果）", "Cross-backend non-designer Independent Review (blinded to designer self-assessment)"),
    ("差异逐项仲裁（设计者 + 审查者面对面核对每一项 ✗）", "Discrepancy arbitration item by item (designer + reviewer compare each ✗ face-to-face)"),
    ("等价声明中标注验证后端和审查者身份", "Equivalence declaration records verification backend and reviewer identity"),
    ("1. 目标（做什么）", "1. Objective (what to do)"),
    ("   - 一句话描述输出物", "   - One-line description of deliverable"),
    ("   - 如果有多个输出物，列优先级", "   - If multiple deliverables, list priority"),
    ("2. 输入（从哪里开始）", "2. Input (where to start)"),
    ("   - 数据/文件/上次产出的路径", "   - Paths to data/files/previous output"),
    ("   - 相关 Spec 的引用", "   - References to relevant Spec"),
    ("3. 完成标准（什么算做完）", "3. Completion Criteria (what counts as done)"),
    ("   - 可验证的完成条件", "   - Verifiable completion conditions"),
    ("   - 反例：什么不算完成", "   - Counter-example: what does NOT count as completion"),
    ("4. 否决条件（什么算失败）", "4. Kill Conditions (what counts as failure)"),
    ("   - 来自 kill-test-first 门1 的红线", "   - Red lines from kill-test-first gate 1"),
    ("   - 来自 Spec 的约束", "   - Constraints from Spec"),
    ("5. 特殊约束", "5. Special Constraints"),
    ("   - 语言/格式要求", "   - Language/format requirements"),
    ("   - 工具限制", "   - Tool restrictions"),
    ("   - 时间上限", "   - Time limit"),
    ("6. 输出格式", "6. Output Format"),
    ("7. 确认项（Agent 执行前自检）", "7. Confirmation Items (Agent self-check before execution)"),
    ("8. Agent 自评（执行后填写）", "8. Agent Self-Assessment (fill in after execution)"),
    ("否决条件（来自 kill-test-first 门1）：", "Kill Conditions (from kill-test-first gate 1):"),
    ("- [ ] 独立性声明：本任务不依赖未验证的外部假设 ____", "- [ ] Independence declaration: this task does not depend on unverified external assumptions: ____"),
    ("- [ ] 可证伪命题：如果 ____ 不成立，本任务结论无效", "- [ ] Falsifiable proposition: if ____ does not hold, this task's conclusion is invalid"),
    ("- [ ] 先验对标：已知 ____ 做过类似工作，本任务差异在于 ____", "- [ ] Prior benchmark: ____ has done similar work; this task differs in ____"),
    ("- [ ] 死亡判据：如果 ____（可测量阈值），停止并不再尝试", "- [ ] Kill Criteria: if ____ (measurable threshold), stop and do not retry"),
    ("- [ ] 质量门槛：交付前必须通过 ____", "- [ ] Quality bar: must pass ____ before delivery"),
    ("- [ ] 三态输出：GO / STOP / REDESIGN（最多 2 次）", "- [ ] Three-state output: GO / STOP / REDESIGN (max 2 attempts)"),
]: add(o, n)

# === §6 Workflow patterns ===
for o, n in [
    ("             并行)        并行)        并行)", "             parallel)     parallel)     parallel)"),
    ("   特点：无阶段间 barrier。A 在 Stage 3 时 B 可能还在 Stage 1。", "   Trait: no inter-stage barrier. A can be in Stage 3 while B is still in Stage 1."),
    ("   适用：绝大多数多阶段任务。", "   Use: most multi-stage tasks."),
    ("   反例：不要因为\"想先看完所有 Stage 1 结果\"就用 barrier——写成 Stage 2 的开头逻辑。", '   Anti-pattern: don\'t use a barrier just because you "want to see all Stage 1 results first" — make that the opening logic of Stage 2.'),
    ("   Items ──▶ [所有 Finder 并行] ──▶ barrier（等全部完成）──▶ 全局去重/排序 ──▶ [精选项目并行处理]", "   Items ──▶ [All Finders parallel] ──▶ barrier (wait for all) ──▶ global dedup/sort ──▶ [selected items parallel processing]"),
    ("   适用：需要跨所有结果做去重、排序、或判断\"有没有结果\"的场景。", '   Use: scenarios requiring cross-result dedup, sorting, or "are there any results?" checks.'),
    ("   反例：\"我想先整理一下结果再继续\"——这是 pipeline 中间的 transform stage。", '   Anti-pattern: "I want to organize results before continuing" — that\'s a transform stage inside a pipeline.'),
    ("   产出 ──▶ [验证者A: 正确性视角] ──┐", "   Output ──▶ [Verifier A: Correctness lens] ──┐"),
    ("          ├─▶ [验证者B: 安全性视角] ──┼──▶ 投票 ──▶ 存活/淘汰", "          ├─▶ [Verifier B: Security lens] ──┼──▶ vote ──▶ survive/eliminate"),
    ("          └─▶ [验证者C: 可复现视角] ──┘", "          └─▶ [Verifier C: Reproducibility lens] ──┘"),
    ("   适用：重要产出需要多视角独立审查。", "   Use: important outputs requiring multi-perspective Independent Review."),
    ("   注意：验证者必须用不同的 prompt 角度（不是同一 prompt 跑 N 次）。", "   Note: verifiers MUST use different prompt angles (not the same prompt run N times)."),
    ("   （提示：多数情况 3 就够了。投票超半数存活通过；全票淘汰才放弃。）", "   (Tip: 3 is enough in most cases. Majority vote survives; only unanimous rejection kills.)"),
    ("   [找出所有Bug] ──▶ [验证者 ×3] ──▶ 投票 2/3 ──▶ 存活（确认是 Bug）", "   [Find all bugs] ──▶ [Verifier ×3] ──▶ vote 2/3 ──▶ survive (confirmed as bug)"),
    ("   同一个问题 ──▶ [方案A: MVP优先] ──┐", "   Same problem ──▶ [Approach A: MVP-first] ──┐"),
    ("               ├─▶ [方案B: 风险优先] ──┼──▶ 独立评分 ──▶ 选最优 + 嫁接其他优点", "               ├─▶ [Approach B: Risk-first] ──┼──▶ independent scoring ──▶ pick best + graft other strengths"),
    ("               └─▶ [方案C: 用户优先] ──┘", "               └─▶ [Approach C: User-first] ──┘"),
    ("   适用：有多种合理解法，不确定哪个最好。", "   Use: multiple reasonable approaches; unclear which is best."),
    ("   成本高，仅在单次尝试大概率不够时使用。", "   Costly; use only when a single attempt is unlikely to suffice."),
    ("   适用：未知数量的发现型任务（找 Bug、找边缘情况）。", "   Use: discovery tasks with unknown quantity (bug finding, edge-case hunting)."),
    ("   K=2：连续两轮无新发现即停止。", "   K=2: stop after two consecutive rounds with zero new findings."),
    ("   产出 ──▶ Critic Agent: \"什么缺失了？——哪些维度没覆盖？哪些来源没读？哪些假设没检验？\"", '   Output ──▶ Critic Agent: "What is missing? — Which dimensions uncovered? Which sources unread? Which assumptions untested?"'),
    ("          ──▶ 缺失项清单 ──▶ 如果非空 ──▶ 派发新一轮任务", "          ──▶ missing-items list ──▶ if non-empty ──▶ dispatch new round of tasks"),
    ("   产出 ──▶ [Creator: 生成产出]", "   Output ──▶ [Creator: generate output]"),
    ("          ──▶ [Verifier: 独立后端模型 + 隔离上下文，从正确性/安全性/可复现性三视角审查]", "          ──▶ [Verifier: independent backend model + isolated context, review from correctness/security/reproducibility lenses]"),
    ("          ──▶ 若 Verifier 驳回 → Creator 修订 → 重新验证（最多 3 轮）", "          ──▶ if Verifier rejects → Creator revises → re-verify (max 3 rounds)"),
    ("   适用：任何正式交付物或关键决策产出。", "   Use: any formal deliverable or critical-decision output."),
    ("   强制：Verifier 必须满足双轴独立性（后端模型不同 + 上下文隔离），否则降级为普通自评。", "   Mandatory: Verifier MUST satisfy Dual-Axis Independence (different backend model + Context Isolation); otherwise downgraded to standard self-assessment."),
    ("   注意：Creator-Verifier 是审查模式，零人类参与的纯 AI 闭环不能独立做出关键决策。", "   Note: Creator-Verifier is a review pattern; a purely AI closed loop with zero human involvement cannot independently make critical decisions."),
    ("   人类定位：Creator-Verifier 终态意见 + 结果 → 给人类决策；人做最终裁决。", "   Human role: Creator-Verifier final opinion + results → presented to human for decision; human makes the final call."),
    ("   反例：把 Creator-Verifier 3 轮结果直接当作\"已验证\"而不经过 HG-2。", '   Anti-pattern: treating 3 Creator-Verifier rounds as "verified" without passing through HG-2.'),
    ("   阶段 A (scan) ────┐", "   Stage A (scan) ────┐"),
    ("   阶段 B (structure) ─┤ 依赖声明", "   Stage B (structure) ─┤ dependency declaration"),
    ("   阶段 C (parse) ─────┤ deps: ['structure', 'scan']", "   Stage C (parse) ─────┤ deps: ['structure', 'scan']"),
    ("   阶段 D (resolve) ───┤ deps: ['parse']", "   Stage D (resolve) ───┤ deps: ['parse']"),
    ("   Runner: Kahn 拓扑排序 → 检测循环/缺依赖/重复 → 顺序执行", "   Runner: Kahn topological sort → detect cycles/missing deps/duplicates → sequential execution"),
    ("   适用：大任务拆成 DAG 子任务，维持声明式（写依赖、不写步骤）。", "   Use: decompose large tasks into DAG sub-tasks; stay declarative (write dependencies, not steps)."),
    ("   PR/产出 ──▶ [角色1: 事实历史学家] ──┐", "   PR/output ──▶ [Role 1: Fact Historian] ──┐"),
    ("            ├─▶ [角色2: 分支/过程卫生] ──┤ 依赖DAG", "            ├─▶ [Role 2: Branch/Process Hygiene] ──┤ dependency DAG"),
    ("            ├─▶ [角色3: 风险架构师] ─────┤ (角色1,2完成", "            ├─▶ [Role 3: Risk Architect] ─────┤ (Roles 1,2 done"),
    ("            ├─▶ [角色4: 测试/CI验证者] ──┤  后并行)", "            ├─▶ [Role 4: Test/CI Verifier] ──┤  then parallel)"),
    ("            ├─▶ [角色5: 安全边界审查] ───┤", "            ├─▶ [Role 5: Security Boundary Reviewer] ───┤"),
    ("            ├─▶ [角色6: 架构影响分析] ──┤", "            ├─▶ [Role 6: Architecture Impact Analyst] ──┤"),
    ("            └─▶ [角色7: Diff 自解释审查] ┘", "            └─▶ [Role 7: Diff Self-Explanation Reviewer] ┘"),
    ("   适用：多维度审查（代码、架构、安全、测试），需要每个维度有固定审查协议。", "   Use: multi-dimensional review (code, architecture, security, testing) where each dimension needs a fixed review protocol."),
    ("   协议：每个角色输出一个结构化裁定（PASS/FAIL+证据），不是长段落意见。", "   Protocol: each role outputs a structured verdict (PASS/FAIL + evidence), not a long-form opinion."),
    ("   反例：让同一个模型扮演所有 7 个角色然后\"综合\"——这等同于单次审查。", '   Anti-pattern: having the same model play all 7 roles and then "synthesize" — this is equivalent to a single review.'),
]: add(o, n)

# === §10 Dev Log ===
for o, n in [
    ("项目根/", "project-root/"),
    ("├── DEV_LOG.md              ← 主脉络索引（只记\"什么时间改了哪，导航到哪\"）", '├── DEV_LOG.md              ← Main-thread index ("when, what changed, navigate to where")'),
    ("│   ├── 2026-06-10_添加余弦预筛选.md", "│   ├── 2026-06-10_added-cosine-pre-filter.md"),
    ("│   ├── 2026-06-09_修复波动率过滤单位Bug.md", "│   ├── 2026-06-09_fixed-volatility-filter-unit-bug.md"),
    ("│   ├── 2026-06-08_V3.6架构重构.md", "│   ├── 2026-06-08_V3.6-architecture-refactor.md"),
    ("形态匹配ETF策略/", "morphology-matching-ETF-strategy/"),
    ("├── strategy.py          ← [6/9 Bug修复] [6/8 重构] [5/17 BUGFIX-001]", "├── strategy.py          ← [6/9 Bugfix] [6/8 Refactor] [5/17 BUGFIX-001]"),
    ("├── backtest.py          ← [6/9 波动率单位修复] [5/18 BUGFIX-004]", "├── backtest.py          ← [6/9 Volatility unit fix] [5/18 BUGFIX-004]"),
    ("├── signals.py           ← [6/10 余弦预筛选]", "├── signals.py           ← [6/10 Cosine pre-filter]"),
    ("├── config.py            ← [6/10 参数调整] [6/8 参数调整]", "├── config.py            ← [6/10 Parameter tuning] [6/8 Parameter tuning]"),
    ("├── timing.py            ← [6/8 新增文件]", "├── timing.py            ← [6/8 New file]"),
    ("├── 设计文档_V2.9.md      ← [5/16 V2.8修改意见]", "├── design-doc_V2.9.md   ← [5/16 V2.8 revision notes]"),
    ("└── 编码方案_V2.9.md      ← [5/16 编码方案修改]", "└── encoding-scheme_V2.9.md ← [5/16 Encoding scheme revision]"),
    ("### 2026-06-10 14:23 — 添加余弦预筛选", "### 2026-06-10 14:23 — Added cosine pre-filter"),
    ("- **文件**: signals.py (+120行), config.py (+3行)", "- **Files**: signals.py (+120 lines), config.py (+3 lines)"),
    ("- **原因**: 全量DTW计算太慢（1.5h → 优化到20min）", "- **Reason**: full DTW computation was too slow (1.5h → optimized to 20min)"),
    ("- **详情**: → [dev-logs/2026-06-10_添加余弦预筛选.md]", "- **Details**: → [dev-logs/2026-06-10_added-cosine-pre-filter.md]"),
    ("- **关联变更**: 依赖 2026-06-08_V3.6架构重构 中的解耦设计", "- **Related changes**: depends on decoupling design from 2026-06-08_V3.6-architecture-refactor"),
    ("- **关联审阅**: —", "- **Related review**: —"),
    ("### 2026-06-09 22:15 — 修复 VOL_ABSOLUTE_CAP 单位Bug", "### 2026-06-09 22:15 — Fixed VOL_ABSOLUTE_CAP unit bug"),
    ("- **症状**: 波动率过滤100%触发，仓位被永久压制≤70%", "- **Symptom**: volatility filter triggered 100%; positions permanently capped ≤70%"),
    ("- **根因**: 年化波动率(0.15~0.40)与日度CAP(0.022)单位不匹配", "- **Root cause**: annualized volatility (0.15~0.40) and daily CAP (0.022) had mismatched units"),
    ("- **修复**: 删除年化(×√252)，恢复日度标准差单位", "- **Fix**: removed annualization (×√252), restored daily standard deviation unit"),
    ("- **详情**: → [dev-logs/2026-06-09_修复波动率过滤单位Bug.md]", "- **Details**: → [dev-logs/2026-06-09_fixed-volatility-filter-unit-bug.md]"),
    ("- **日期时间**: ____", "- **Date/time**: ____"),
    ("- **涉及文件**: ____", "- **Files involved**: ____"),
    ("- **变更类型**: [Bug修复 / 功能新增 / 架构重构 / 参数调整 / 设计修订]", "- **Change type**: [Bugfix / Feature / Architecture refactor / Parameter tuning / Design revision]"),
    ("- **严重级别**: [P0/P1/P2]（仅 Bug 修复）", "- **Severity**: [P0/P1/P2] (Bugfix only)"),
    ("- **关联版本**: ____", "- **Associated version**: ____"),
    ("- **关联变更**: ____", "- **Related changes**: ____"),
    ("### 变更内容", "### Changes Made"),
    ("### 影响分析", "### Impact Analysis"),
    ("- **影响范围**: ____", "- **Scope of impact**: ____"),
    ("- **破坏性**: [是 / 否]", "- **Breaking**: [Yes / No]"),
    ("- **向后兼容**: [是 / 否]", "- **Backward compatible**: [Yes / No]"),
    ("### 教训", "### Lessons Learned"),
    ("- **原因**: ____", "- **Cause**: ____"),
    ("- **预防**: ____", "- **Prevention**: ____"),
    ("- **值得推广**: ____（可能跨项目有效）", "- **Worth generalizing**: ____ (potentially cross-project valid)"),
    ("已验证 (3)          待实证 (6)           零数据 (1)", "Verified (3)          Needs evidence (6)    No data (1)"),
    ("   ├── Bug记录格式    ├── AI自动追加       └── AI追溯效果", "   ├── Bug record format  ├── AI auto-append       └── AI traceability effect"),
    ("   ├── 注释不可靠前提 ├── 双视图结构", "   ├── Comment-unreliable premise ├── Dual-view structure"),
    ("   └── 独立持久化方向 ├── FK导航健壮性", "   └── Independent persistence direction ├── FK navigation robustness"),
    ("                       ├── 轻量vs分支分界", "                       ├── Lightweight vs branch boundary"),
    ("                       ├── 过时声明清理", "                       ├── Stale statement cleanup"),
    ("                       └── Log随代码迁移", "                       └── Log migration with code"),
]: add(o, n)

# === §11 Integration table ===
for o, n in [
    ("本框架层         现有系统                         集成方式", "Framework Layer   Existing System                    Integration Method"),
    ("L0: Spec        CLAUDE.md + memory/              已是 Spec 载体，补 S5/S6/S8", "L0: Spec         CLAUDE.md + memory/               Already Spec carriers; add S5/S6/S8"),
    ("                kill-test-first 门1              Spec 的否决条件组件", "                 kill-test-first gate 1            Kill Conditions component of Spec"),
    ("L-H: Human Gate feedback_independent_           框架化——显式闸门 + Trigger condition", "L-H: Human Gate  feedback_independent_           Formalized — explicit gate + Trigger condition"),
    ("L1: Prompt      kill-test-first 门1              嵌入 Prompt 模板的\"否决条件\"栏", 'L1: Prompt       kill-test-first gate 1            Embedded in Prompt template "Kill Conditions" field'),
    ("                 headroom 三组件                  可借鉴的架构原则（非直接方", "                 headroom three components         Borrowable architectural principle (not direct methodology)"),
    ("L2: Loop        形态匹配ETF项目                   循环收敛 + 失败模式实证来源", "L2: Loop         morphology-matching ETF project    Loop convergence + failure-mode empirical source"),
    ("                并购重组案例研究                  八阶段流水线 + 开卷/盲答对照", "                 M&A case study research           Eight-stage pipeline + open-book/blind-answer control"),
    ("L3: Workflow    BDC2026                           5/30 误传zip→不可用→复盘", "L3: Workflow     BDC2026                           5/30 mis-sent zip → unusable → post-mortem"),
    ("                prompt-tdd                        对照实验 ×3 → [E-] ×3 → §4.1.1/§6.3", "                prompt-tdd                        Controlled experiment ×3 → [E-] ×3 → §4.1.1/§6.3"),
    ("                PocketFlow                        A 类方法论资产 ×3 → §1.7/§9.9/附录H", "                PocketFlow                        Class A methodology assets ×3 → §1.7/§9.9/Appendix H"),
    ("                GitNexus + Small_Scale +         多项目分析链 + 多后端独立审", "                GitNexus + Small_Scale +          Multi-project analysis chain + multi-backend Independent Review → v1.5"),
    ("L4: Retrospect  Protocol 3 试跑1                  C1-C8 方法论反馈 → §", "L4: Retrospect   Protocol 3 Trial Run 1            C1-C8 methodology feedback → §"),
    ("                被动观测三事件                    §7.7 跨案例分析", "                Three Opportunistic Observation events  §7.7 cross-case analysis"),
    ("                框架 v1.3.2 纠正路线图            \"双重确认偏误\"教训 → §", '                Framework v1.3.2 correction roadmap     "Double-confirmation bias" lesson → §'),
    ("L5: Closure     方法论提取方法论                  M-tier 闭合案例（14/20→15/20）→ §", "L5: Closure      methodology extraction methodology  M-tier closure case (14/20→15/20) → §"),
    ("                形态匹配ETF项目                   S-tier 闭合案例（17 版本）→ ", "                morphology-matching ETF project    S-tier closure case (17 versions) → "),
    ("跨层: 可复现性  reference_python_versions.md      按项目类型分档要求", "Cross: Reproducibility  reference_python_versions.md    Tiered by project type"),
    ("              VERSION + verify_version_consistency.py 版本一致性硬验证", "              VERSION + verify_version_consistency.py   Version consistency hard verification"),
    ("跨层: 证据标注  框架级成熟度评估表                  三维证据标注 [内部强度/跨模型/设计", "Cross: Evidence labels  Framework-Level Maturity Assessment  Two-dimensional evidence labels [Internal Strength/Cross-Model"),
    ("              方法论片段三层模板                  问题→方案→失效的端到端记", "              Methodology Fragment three-layer template  End-to-end recording: problem→solution→failure"),
    ("跨层: 审查     methodological-review-sop.md       独立审查标准操作程序（配套审查维度", "Cross: Review    methodological-review-sop.md       Independent Review SOP (companion review-dimension design)"),
    ("               meta-audit-checklist.md            框架自身合规审查（75 项）", "               meta-audit-checklist.md            Framework self-compliance review (75 items)"),
]: add(o, n)

# === §12 Appendix templates ===
for o, n in [
    ("- 所需工具/数据不可用（bash失效/读不到文件/数据缺失）→ 停止并报告，绝不用替代数据继续",
     "- Required tools/data unavailable (bash broken / can't read files / data missing) → stop and report; never continue with substitute data"),
    ("> 关联项目Version: ____", "> Associated project version: ____"),
    ("- ____ （至少 1 条；找不到标注原因）", "- ____ (at least 1; if none found, note the reason)"),
    ("### 3. 意外发现（Surprises）", "### 3. Surprises"),
    ("- ____ （至少 1 条；找不到标注原因）", "- ____ (at least 1; if none found, note the reason)"),
    ("### 4. Spec 更新候选", "### 4. Spec Update Candidates"),
    ("### 5. 下次改进（Action items）", "### 5. Next Improvements (Action items)"),
    ("> 触发事件: [重大错误 / 否决触发 / 闭合前]", "> Trigger event: [Major error / Kill Condition triggered / Pre-closure]"),
    ("- ____ （至少 1 条）", "- ____ (at least 1)"),
    ("- 正面意外: ____", "- Positive surprise: ____"),
    ("- 负面意外: ____", "- Negative surprise: ____"),
    ("### 4. 根因分析（Root cause）", "### 4. Root Cause Analysis"),
    ("### 5. 系统性影响评估", "### 5. Systemic Impact Assessment"),
    ("### 6. Spec 更新候选", "### 6. Spec Update Candidates"),
    ("### 7. 跨项目方法论候选", "### 7. Cross-Project Methodology Candidates"),
    ("### 8. Protocol 3 / 框架层反馈", "### 8. Protocol 3 / Framework-Level Feedback"),
    ("> 如是\"发现替代\"——三项证据门槛确认: □可验证记录 □同等标准更优 □独立模型确认",
     '> If "Alternative found" — three evidence thresholds confirmed: □ Verifiable record □ Better under equal or stricter standards □ Independent model confirmation'),
    ("- [ ] 代码归档 (Git tag + 最后 commit hash: ____)", "- [ ] Code archived (Git tag + last commit hash: ____)"),
    ("- [ ] 数据归档 (快照路径: data/raw/)", "- [ ] Data archived (snapshot path: data/raw/)"),
    ("### 知识提取", "### Knowledge Extraction"),
    ("- [ ] 可复用代码模块提取 (路径: ____)", "- [ ] Reusable code module extraction (path: ____)"),
    ("- [ ] 方法论片段提取 (存入 _protocols-and-tools/)", "- [ ] Methodology fragment extraction (store in _protocols-and-tools/)"),
    ("- [ ] 失败模式记录 (存入 _research/ 或 memory/)", "- [ ] Failure pattern recording (store in _research/ or memory/)"),
    ("- [ ] 数据资产说明 (README in data/raw/)", "- [ ] Data asset description (README in data/raw/)"),
    ("### 交付物", "### Deliverables"),
    ("- [ ] .md 版（主交付物）", "- [ ] .md version (primary deliverable)"),
    ("- [ ] .json 版（机读配套）", "- [ ] .json version (machine-readable companion)"),
    ("- [ ] .docx 版 [学术项目必须]", "- [ ] .docx version [Mandatory for academic projects]"),
    ("- [ ] 终期报告经至少 1 个独立模型审阅", "- [ ] Final report reviewed by at least 1 independent model"),
    ("- [ ] 审阅报告存入 _reviews/", "- [ ] Review report stored in _reviews/"),
    ("### 公告（如适用）", "### Announcement (if applicable)"),
    ("- [ ] README 更新（标记 CLOSED）", "- [ ] README updated (marked CLOSED)"),
    ("- [ ] CHANGELOG 更新", "- [ ] CHANGELOG updated"),
    ("- [ ] 逐条检查 memory 时效性：超过 30 天的条目提醒\"需验证\"",
     '- [ ] Check memory timeliness item by item: entries older than 30 days prompt "verification needed"'),
    ("- [ ] 读本项目 project_status.md", "- [ ] Read this project's project_status.md"),
    ("- [ ] 读上次 Retrospect（如果有）", "- [ ] Read previous Retrospect (if exists)"),
    ("- [ ] 更新 project_status.md:", "- [ ] Update project_status.md:"),
    ("  - 当前版本/阶段", "  - Current version/phase"),
    ("  - 本次完成", "  - Completed this session"),
    ("  - 下次计划", "  - Next plan"),
    ("  - 新发现的 OPEN 项", "  - Newly discovered OPEN items"),
    ("- [ ] 更新 CLAUDE.md（如有重要变更）", "- [ ] Update CLAUDE.md (if significant changes)"),
    ("- [ ] Retrospect（如适用，轻量模板）", "- [ ] Retrospect (if applicable, lightweight template)"),
    ("- [ ] 更新 memory/（跨项目经验）", "- [ ] Update memory/ (cross-project experience)"),
    ("- [ ] 确认 .gitignore 覆盖所有不该提交的文件", "- [ ] Confirm .gitignore covers all files that should not be committed"),
    ("- [ ] 清理临时文件（测试产物/调试脚本/中间文件）", "- [ ] Clean up temporary files (test artifacts / debug scripts / intermediate files)"),
    ("| R001 | ____ | ____ | ____ | ____ | ____ | ____ | 监控中 |", "| R001 | ____ | ____ | ____ | ____ | ____ | ____ | Monitoring |"),
    ("| R002 | ____ | ____ | ____ | ____ | ____ | ____ | 已触发 |", "| R002 | ____ | ____ | ____ | ____ | ____ | ____ | Triggered |"),
    ("| R003 | ____ | ____ | ____ | ____ | ____ | ____ | 已缓解 |", "| R003 | ____ | ____ | ____ | ____ | ____ | ____ | Mitigated |"),
    ("**HG触发规则**: 影响=H 且 概率≥M → 必须触发 Human Gate", "**HG trigger rule**: Impact=H AND Probability≥M → MUST trigger Human Gate"),
    ("**更新频率**: 每次 Retrospect 时顺带检查", "**Update frequency**: check during each Retrospect"),
    ("> 维护方式: AI 自动追加，人在 HG-1 时抽查", "> Maintenance method: AI auto-appends; human spot-checks at HG-1"),
    ("[项目名称]/", "[Project-Name]/"),
    ("├── strategy.py          ← [日期 变更简述] [日期 变更简述]", "├── strategy.py          ← [date Change summary] [date Change summary]"),
    ("├── backtest.py          ← [日期 变更简述]", "├── backtest.py          ← [date Change summary]"),
    ("├── signals.py           ← [日期 变更简述]", "├── signals.py           ← [date Change summary]"),
    ("├── config.py            ← [日期 变更简述]", "├── config.py            ← [date Change summary]"),
    ("├── 设计文档_VX.X.md      ← [日期 变更简述]", "├── design-doc_VX.X.md   ← [date Change summary]"),
    ("└── 编码方案_VX.X.md      ← [日期 变更简述]", "└── encoding-scheme_VX.X.md ← [date Change summary]"),
    ("├── dev-logs/             ← [日期 变更简述] [日期 变更简述]", "├── dev-logs/             ← [date Change summary] [date Change summary]"),
    ("│   ├── YYYY-MM-DD_变更简述.md", "│   ├── YYYY-MM-DD_change-summary.md"),
    ("│   └── YYYY-MM-DD_变更简述.md", "│   └── YYYY-MM-DD_change-summary.md"),
    ("├── _reviews/             ← [日期 审查简述]", "├── _reviews/             ← [date Review summary]"),
    ("├── _archive/             ← [日期 归档]", "├── _archive/             ← [date Archived]"),
    ("├── README.md             ← [日期 最后更新]", "├── README.md             ← [date Last updated]"),
    ("└── CLAUDE.md             ← [日期 最后更新]", "└── CLAUDE.md             ← [date Last updated]"),
    ("# [YYYY-MM-DD] — [变更标题]", "# [YYYY-MM-DD] — [Change title]"),
    ("### 症状（仅 Bug 修复）", "### Symptoms (Bugfix only)"),
    ("### 根因（仅 Bug 修复）", "### Root Cause (Bugfix only)"),
    ("### 变更内容", "### Changes Made"),
    ("### 影响分析", "### Impact Analysis"),
    ("- **严重级别**: [P0/P1/P2]（仅 Bug 修复）", "- **Severity**: [P0/P1/P2] (Bugfix only)"),
]: add(o, n)

# Regex cleanup
content = re.sub(r'（仅 Bug 修复）', '(Bugfix only)', content)
content = re.sub(r'（仅 Bug）', '(Bug only)', content)

with open(TARGET, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

# Final audit
lines = content.split('\n')
in_block = False; in_mermaid = False; residual = []
for i, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('```mermaid'): in_mermaid = True; in_block = True; continue
    elif s.startswith('```') and not in_mermaid and not in_block: in_block = True; continue
    elif s.startswith('```') and in_block: in_mermaid = False; in_block = False; continue
    if in_block and not in_mermaid:
        if any('一' <= c <= '鿿' for c in line):
            residual.append((i, line.rstrip()[:140]))

print(f"Explicit replacements: {count}")
print(f"Residual non-Mermaid code block CJK: {len(residual)}")
for ln, txt in residual:
    print(f"  L{ln}: {txt}")

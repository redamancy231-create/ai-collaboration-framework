#!/usr/bin/env python3
"""Fix untranslated Chinese text inside non-executable code blocks in part3."""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

TARGET = str(PROJECT / "en/AI协作项目全生命周期框架_part3.md")

REPLACEMENTS = [
    # === §7.4 Retrospect 轻量/深度模板 ===
    ("1. 生效清单（Keep doing）", "1. What Worked (Keep doing)"),
    ("2. 失效清单（Stop doing / Change）", "2. What Didn't Work (Stop doing / Change)"),
    ("3. 意外发现（Surprises）", "3. Surprises"),
    ("4. Spec 更新候选", "4. Spec Update Candidates"),
    ("5. 下次改进（Action items）", "5. Action Items"),
    ("3. 意外发现（Surprises）—— 每条可选标注：发现方式 / 复核状态 / 适用边界（详见 §7.7.5）",
     "3. Surprises — each may optionally note: discovery method / verification status / applicability boundary (see §7.7.5)"),
    ("4. 根因分析（Root cause —— 为什么失效？系统性还是偶发？）",
     "4. Root Cause Analysis (Why did it fail? Systematic or incidental?)"),
    ("5. 系统性影响评估（这个发现对其他项目/模块的影响？）",
     "5. Systemic Impact Assessment (Impact of this finding on other projects/modules?)"),
    ("6. Spec 更新候选（→ 提给 Human Gate HG-2）",
     "6. Spec Update Candidates (→ submit to Human Gate HG-2)"),
    ("7. 跨项目方法论候选（→ 写回 memory/）",
     "7. Cross-Project Methodology Candidates (→ write back to memory/)"),
    ("8. Protocol 3 / 框架层反馈（如适用：C1-C8 裁决、证据缺口、HG/审查频率教训）",
     "8. Protocol 3 / Framework-Level Feedback (if applicable: C1-C8 verdicts, evidence gaps, HG/review frequency lessons)"),
    ("9. 下次改进（具体 action items）", "9. Next Improvements (concrete action items)"),

    # === §7.4 写回流程 ===
    ("1. AI 跑 Retrospect → 出草稿（按轻量/深度模板）",
     "1. AI runs Retrospect → produces draft (using lightweight or full template)"),
    ("2. Human Gate：草稿给人过目，确认或修改",
     "2. Human Gate: human reviews draft, confirms or modifies"),
    ("3. 人确认后 → AI 执行写回：",
     "3. After human confirmation → AI executes Write-Back:"),
    ("   ├── 项目级 Spec 更新 → 本项目 Spec 文件",
     "   ├── Project-level Spec update → this project's Spec file"),
    ("   ├── 跨项目方法论 → memory/（全局 lessons learned）",
     "   ├── Cross-project methodology → memory/ (global lessons learned)"),
    ("   └── 本阶段记录 → 项目 Retrospect 日志（备查）",
     "   └── This-phase record → project Retrospect log (for reference)"),

    # === §7.7.5 深度版模板增强 ===
    ("3. 意外发现（Surprises）",
     "3. Surprises"),
    ("    - 发现内容：[原有字段，必填]",
     "    - Finding: [existing field, required]"),
    ("    - 发现方式：[冗余暴露 / 一致维护暴露 / 审查附带暴露 / 比较型 / 维护型 /",
     "    - Discovery method: [Redundancy-Driven / Consistency-Maintenance / Review-Incidental / Comparative / Maintenance /"),
    ("                 审查型 / 执行型 / 失败型 / 使用型 / 时漂型 / 缺失型 / 其他]",
     "                 Review / Execution / Failure / Usage / Temporal-Drift / Absence / Other]"),
    ("    - 复核状态：[未复核 / 复核确认（附证据）/ 复核驳回（附原因）/ 待异后端确认]",
     "    - Verification status: [Unverified / Confirmed (with evidence) / Rejected (with reason) / Pending cross-backend confirmation]"),
    ("    - 适用边界：[该洞察在什么条件下可能不成立；边界未知则标注\"未确定\"]",
     "    - Applicability boundary: [Under what conditions might this insight not hold; mark \"undetermined\" if unknown]"),

    # === §8.4 Closure Checklist ===
    ("□ 闭合条件确认（基于哪个条件 + 证据）",
     "□ Closure condition confirmed (which condition + evidence)"),
    ("□ 终期总结报告（.md）",
     "□ Final summary report (.md)"),
    ("□ 终期总结报告（.docx）[学术项目必须]",
     "□ Final summary report (.docx) [mandatory for academic projects]"),
    ("□ 项目评估分析（.md + .json）",
     "□ Project evaluation analysis (.md + .json)"),
    ("□ 可复用遗产提取（代码模块/方法论/失败模式/数据资产）",
     "□ Reusable legacy extraction (code modules / methodology / failure patterns / data assets)"),
    ("□ 跨项目方法论写回 memory/（至少 3 条）",
     "□ Cross-project methodology write-back to memory/ (at least 3 items)"),
    ("□ Retrospect 终期回顾（深度版）",
     "□ Retrospect final review (full template)"),
    ("□ 归档（三级分层，见下）",
     "□ Archive (three-tier structure, see below)"),
    ("□ 外部审阅（终期报告至少经 1 个独立模型审阅）",
     "□ External review (final report reviewed by at least 1 independent model)"),
    ("□ 项目状态更新（project_status.md 标记 CLOSED + 封存基线 + 重启门槛）",
     "□ Project status update (mark CLOSED in project_status.md + archive baseline + restart threshold)"),
    ("□ 交付物双件生成（md + json）",
     "□ Dual-format artifact generation (md + json)"),
    ("□ 人最终确认（HG-3 闭合闸门）",
     "□ Final human confirmation (HG-3 closure gate)"),
    ("□ 临时文件清理 + 敏感信息检查",
     "□ Temporary file cleanup + sensitive information check"),

    # === §8.5 归档目录结构 ===
    ("├── archive/                    ← 终期报告 + 评估分析 + Retrospect",
     "├── archive/                    ← Final report + evaluation analysis + Retrospect"),
    ("│   ├── 终期总结报告_v1.0.md",
     "│   ├── final_report_v1.0.md"),
    ("│   ├── 终期总结报告_v1.0.docx",
     "│   ├── final_report_v1.0.docx"),
    ("│   ├── 项目评估分析.md",
     "│   ├── project_evaluation.md"),
    ("│   ├── 项目评估分析.json",
     "│   ├── project_evaluation.json"),
    ("│   └── Retrospect_终期回顾.md",
     "│   └── Retrospect_final_review.md"),
    ("├── code/                       ← 最终版代码",
     "├── code/                       ← Final version of code"),
    ("│   └── raw/                    ← 原始数据快照（标注获取日期和来源）",
     "│   └── raw/                    ← Raw data snapshot (annotate acquisition date and source)"),
    ("├── docs/                       ← 设计文档、审查报告",
     "├── docs/                       ← Design documents, review reports"),
    ("└── project_spec.md             ← 项目 Spec（终版，随项目归档）",
     "└── project_spec.md             ← Project Spec (final version, archived with project)"),

    # === §9.6.1 证据公式 ===
    ("[证据等级] = [内部证据强度] × [跨模型推广性]",
     "[Evidence Level] = [Internal Strength] × [Cross-Model Generalizability]"),
    ("[内部强度 / 跨模型推广性]  例如: [B+ / M0]  [C+ / M2]  [A / N/A]  [D / N/A]",
     "[Internal Strength / Cross-Model Generalizability]  e.g.: [B+ / M0]  [C+ / M2]  [A / N/A]  [D / N/A]"),

    # === §9.10 MF三层模板结构 ===
    ("[Fragment ID] — [名称] — [分类]",
     "[Fragment ID] — [Name] — [Category]"),
    ("第一层：问题识别（Problem Space）",
     "Layer 1: Problem Identification (Problem Space)"),
    ("├── 核心问题描述",
     "├── Core problem description"),
    ("├── 问题识别条件：何时应警惕此问题",
     "├── Problem identification conditions: when to watch for this problem"),
    ("└── 检测方法：如何确认问题确实存在（而非类似但不同的问题）",
     "└── Detection method: how to confirm the problem genuinely exists (not a similar but different problem)"),
    ("第二层：解决方案（Solution Space）",
     "Layer 2: Solution (Solution Space)"),
    ("├── 推荐解决方案",
     "├── Recommended solution"),
    ("├── 解决方案适用条件（关键新增）：方案在什么前提下可用",
     "├── Solution applicability conditions (key addition): under what preconditions the solution is usable"),
    ("├── 替代方案（当首选方案不适用时）",
     "├── Alternatives (when the recommended solution is not applicable)"),
    ("├── 方案选择决策树（可选）",
     "├── Solution selection decision tree (optional)"),
    ("第三层：已知反例与失效模式（Failure Space）（关键新增）",
     "Layer 3: Known Counterexamples and Failure Modes (Failure Space) (key addition)"),
    ("├── 已知反例：方案在什么情况下被观察到失效",
     "├── Known counterexamples: under what circumstances the solution has been observed to fail"),
    ("├── 失效模式：方案为什么会失效（机制层面）",
     "├── Failure modes: why the solution fails (mechanism level)"),
    ("├── 静默失效信号：如何检测方案正在失效但未报告错误",
     "├── Silent failure signals: how to detect the solution is failing without an error being reported"),
    ("└── 与其他 MF 的冲突/交互（可选）",
     "└── Conflicts/interactions with other MFs (optional)"),

    # === PT-M1 示例 ===
    ("[PT-M1] — 天花板效应预警与解决方案 — [设计审查]",
     "[PT-M1] — Ceiling Effect Warning and Mitigation — [Design Review]"),
    ("第一层：问题识别",
     "Layer 1: Problem Identification"),
    ("- 核心问题：对照实验中的天花板效应——所有实验条件表现一致接近满分，没有方差可供区分条件",
     "- Core problem: Ceiling Effect in controlled experiments — all conditions perform near-perfect, leaving no variance to discriminate between conditions"),
    ("- 识别条件：(a) 任一条件的准确率/得分接近满分（>95%）；(b) 或条件间方差趋零",
     "- Identification conditions: (a) any condition's accuracy/score is near-ceiling (>95%); (b) or between-condition variance approaches zero"),
    ("- 检测方法：Tier 0 试点测试（n≥8/条件），计算每个条件的得分均值和方差，若 >95% 天花板 → 正式实验前必须调整",
     "- Detection method: Tier 0 pilot test (n≥8/condition), compute mean and variance of scores per condition; if >95% ceiling → must adjust before formal experiment"),
    ("第二层：解决方案",
     "Layer 2: Solution"),
    ("- 推荐方案：切换替代因变量（DV）——找到有足够方差且与原始DV正相关的替代测量维度",
     "- Recommended solution: switch to an alternative dependent variable (DV) — find an alternative measurement dimension with sufficient variance that is positively correlated with the original DV"),
    ("- 适用条件：(a) 任务存在 ≥2 个正交评估维度；(b) 替代维度在实验条件下有足够的期望方差（需在 Tier 0 中预检验）；(c) 替代维度的测量误差可接受",
     "- Applicability conditions: (a) the task has ≥2 orthogonal evaluation dimensions; (b) the alternative dimension has sufficient expected variance under experimental conditions (must be pre-tested in Tier 0); (c) measurement error of the alternative dimension is acceptable"),
    ("- 替代方案：(a) 增加任务难度（仅当任务可供性 >1 个维度时有效）；(b) 降级为描述性实验（当任务可供性=1 且无替代DV时）",
     "- Alternatives: (a) increase task difficulty (only effective when task affordance >1 dimension); (b) downgrade to descriptive experiment (when task affordance=1 and no alternative DV exists)"),
    ("- 方案选择决策树：连续DV + 多维度 → 切换替代DV / 二分类DV + 多维度 → 引入辅助连续指标 / 任何DV + 单维度 → 禁止仅靠增加难度",
     "- Solution selection decision tree: Continuous DV + multiple dimensions → switch to alternative DV / Binary DV + multiple dimensions → introduce auxiliary continuous metric / Any DV + single dimension → increasing difficulty alone is prohibited"),
    ("第三层：已知反例与失效模式",
     "Layer 3: Known Counterexamples and Failure Modes"),
    ("- 已知反例（A3 静默失效）：A3 的路由任务是二分类单维度任务——PT-M1 的标准方案（切换替代DV）不可用，但设计者未收到警告 → 选用了无效缓解方案（Hard Mode）",
     "- Known counterexample (A3 Silent Failure): A3's routing task was a binary single-dimension task — PT-M1's standard solution (switch alternative DV) was not applicable, but the designer received no warning → chose an ineffective mitigation (Hard Mode)"),
    ("- 失效机制：不是 PT-M1 \"错误\"——是它的知识表示不完整。当任务可供性=1 时，\"切换DV\"的前提不成立，但模板未独立声明这一前提",
     "- Failure mechanism: not a PT-M1 \"error\" — rather, its knowledge representation was incomplete. When task affordance=1, the precondition for \"switch DV\" does not hold, but the template did not independently declare this precondition"),
    ("- 静默失效信号：若任务可供性=1（单一评估维度），设计者仍选择\"增加任务难度/Hard Mode\"作为天花板缓解方案（而非降级为描述性实验）→ 触发静默失效告警。A3 的问题不是\"选了非标准方案\"——是选了形式上像替代方案（增加难度）、前提条件上不适用的方案（单维度任务上增加难度不增加区分度）",
     "- Silent failure signal: If task affordance=1 (single evaluation dimension) and the designer still chooses \"increase task difficulty / Hard Mode\" as the ceiling mitigation (rather than downgrading to a descriptive experiment) → trigger silent failure alert. A3's problem was not \"choosing a non-standard solution\" — it was choosing a solution that formally resembled an alternative (increase difficulty) but failed its preconditions (increasing difficulty on a single-dimension task does not increase discriminability)"),
    ("- 跨模型推广性：PT-M1 的失效机制（任务可供性=1）是任务结构层面的约束，不依赖特定模型——预期跨模型可推广（待验证）",
     "- Cross-model generalizability: PT-M1's failure mechanism (task affordance=1) is a task-structure-level constraint independent of specific models — expected to be cross-model generalizable (pending verification)"),

    # === 零星中文术语 ===
    ("每次AI协作会话开始时人工执行以下检查:",
     "At the start of each AI collaboration session, manually execute the following checks:"),
    ("每次AI协作会话结束时的人工执行检查:",
     "At the end of each AI collaboration session, manually execute the following checks:"),
]

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for old, new in REPLACEMENTS:
    if old in content:
        content = content.replace(old, new)
        count += 1

# 残留检测
lines = content.split('\n')
in_block = False
residual = []
for i, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('```') and not in_block:
        in_block = True
        continue
    elif s.startswith('```') and in_block:
        in_block = False
        continue
    if in_block:
        has_cjk = any('一' <= c <= '鿿' for c in line)
        if has_cjk:
            residual.append((i, line.rstrip()[:120]))

with open(TARGET, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"Applied {count}/{len(REPLACEMENTS)} replacements")
print(f"Residual Chinese lines in code blocks: {len(residual)}")
if residual:
    for ln, text in residual[:20]:
        print(f"  L{ln}: {text}")

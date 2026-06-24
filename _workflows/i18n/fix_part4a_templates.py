#!/usr/bin/env python3
"""Fix untranslated template labels inside markdown code blocks in part4a."""
import sys
from pathlib import Path, re
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

TARGET = str(PROJECT / "en/AI协作项目全生命周期框架_part4a.md")

# Mapping: Chinese template label → English
REPLACEMENTS = [
    # Spec template (Appendix A)
    ("# [项目名称] — 项目 Spec", "# [Project Name] — Project Spec"),
    ("版本: v__", "Version: v__"),
    ("创建日期: ____", "Created: ____"),
    ("最后更新: ____", "Last updated: ____"),
    ("状态: [活跃 / 封存 / 闭合]", "Status: [Active / Archived / Closed]"),
    ("S1: 项目状态", "S1: Project Status"),
    ("当前阶段: ____", "Current phase: ____"),
    ("当前版本: ____", "Current version: ____"),
    ("封存基线: ____", "Archive baseline: ____"),
    ("最近完成: ____", "Recently completed: ____"),
    ("下一步: ____", "Next step: ____"),
    ("S2: 关键文件路径", "S2: Key File Paths"),
    ("项目根目录: ____", "Project root: ____"),
    ("代码: ____", "Code: ____"),
    ("数据: ____", "Data: ____"),
    ("文档: ____", "Documents: ____"),
    ("产出: ____", "Output: ____"),
    ("S3: 技术约定", "S3: Technical Conventions"),
    ("语言/版本: ____", "Language/version: ____"),
    ("关键依赖: ____", "Key dependencies: ____"),
    ("核心约束: ____", "Core constraints: ____"),
    ("绩效基准: ____", "Performance baseline: ____"),
    ("S4: 否决条件（红线）", "S4: Kill Conditions (Red Lines)"),
    ("如果触发 → STOP", "If triggered → STOP"),
    ("如果触发 → REDESIGN，最多 2 次", "If triggered → REDESIGN, max 2 attempts"),
    ("如果触发 → 回到上一基线", "If triggered → revert to previous baseline"),
    ("S5: 成功标准", "S5: Success Criteria"),
    ("主指标: ____  目标: ____  最低可接受: ____", "Primary metric: ____  Target: ____  Minimum acceptable: ____"),
    ("辅指标: ____  目标: ____", "Secondary metric: ____  Target: ____"),
    ("反例（什么不算成功）: ____", "Counter-example (what does NOT count as success): ____"),
    ("S6: 评估计划", "S6: Evaluation Plan"),
    ("三层分工：AI自评每轮 + 独立模型里程碑 + 人类关键决策", "Three-layer division: AI self-assessment each round + independent model milestone + human key decisions"),
    ("默认指标集：[量化: 夏普+Calmar+ICIR+回撤+盈亏比 / 学术: 创新性+严谨性+表达+文献覆盖 / 工程: 功能+性能+可维护性+测试覆盖]", "Default metric sets: [Quant: Sharpe+Calmar+ICIR+drawdown+profit-loss ratio / Academic: novelty+rigor+expression+literature coverage / Engineering: functionality+performance+maintainability+test coverage]"),
    ("评估点1 (____): 指标____  通过阈值____", "Evaluation point 1 (____): Metric____  Pass threshold____"),
    ("评估点2 (____): 指标____  通过阈值____", "Evaluation point 2 (____): Metric____  Pass threshold____"),
    ("最终评估: ____", "Final evaluation: ____"),
    ("S7: 重启门槛（封存项目）", "S7: Restart Threshold (Archived Projects)"),
    ("门槛0: ____", "Threshold 0: ____"),
    ("门槛1: ____", "Threshold 1: ____"),
    ("S8: 风险登记", "S8: Risk Register"),
    ("见风险登记表（附录 F）。H影响+M及以上概率 → 触发 Human Gate。", "See Risk Register (Appendix F). H-impact + M-or-higher probability → triggers Human Gate."),
    ("S9: 可复现性声明", "S9: Reproducibility Statement"),
    ("[学术/量化] Python完整版本+来源: ____", "[Academic/Quant] Complete Python version + source: ____"),
    ("[学术/量化] pip freeze: ____", "[Academic/Quant] pip freeze: ____"),
    ("[学术/量化] 数据快照: data/raw/ (获取日期: ____, 来源: ____)", "[Academic/Quant] Data snapshot: data/raw/ (Date acquired: ____, Source: ____)"),
    ("随机种子: ____", "Random seed: ____"),
    ("[工程/探索最低] Python主版本: ____", "[Engineering/Exploration minimum] Python major version: ____"),
    ("S10: 命名与文件约定", "S10: Naming & File Conventions"),
    ("版本号规则: ____", "Versioning rules: ____"),
    ("文件命名: ____", "File naming: ____"),
    ("目录结构: ____", "Directory structure: ____"),

    # Prompt template (Appendix B)
    ("任务: [一句话描述]", "Task: [one-line description]"),
    ("1. 目标", "1. Objective"),
    ("输出物: ____", "Deliverable: ____"),
    ("优先级: [P0必须 / P1尽量 / P2锦上添花]", "Priority: [P0 Must / P1 Should / P2 Nice-to-have]"),
    ("2. 输入", "2. Input"),
    ("数据/文件: ____", "Data/files: ____"),
    ("相关 Spec: ____", "Relevant Spec: ____"),
    ("参考上下文: ____", "Reference context: ____"),
    ("3. 完成标准", "3. Completion Criteria"),
    ("(可验证)", "(verifiable)"),
    ("反例: ____ 不算完成", "Counter-example: ____ does NOT count as completion"),
    ("4. 否决条件", "4. Kill Conditions"),
    ("[ ] 绝对禁止: ____ (触发即 STOP)", "[ ] Absolutely prohibited: ____ (STOP immediately if triggered)"),
    ("[ ] 上限: ____ (超过即 STOP)", "[ ] Upper limit: ____ (STOP if exceeded)"),
    ("5. 特殊约束", "5. Special Constraints"),
    ("时间上限: ____ 分钟", "Time limit: ____ minutes"),
    ("工具限制: ____", "Tool restrictions: ____"),
    ("风格/格式: ____", "Style/format: ____"),
    ("语言: ____", "Language: ____"),
    ("6. 输出格式", "6. Output Format"),
    ("7. 确认项（Agent 执行前自检）", "7. Confirmation Items (Agent self-check before execution)"),
    ("我已读取所有相关 Spec 和上下文文件: [ ]", "I have read all relevant Spec and context files: [ ]"),
    ("我理解否决条件和完成标准: [ ]", "I understand Kill Conditions and Completion Criteria: [ ]"),
    ("我有所有必需的输入文件/数据: [ ]", "I have all required input files/data: [ ]"),
    ("我将使用指定的工具和格式: [ ]", "I will use the specified tools and format: [ ]"),
    ("8. Agent 自评（执行后填写）", "8. Agent Self-Assessment (fill in after execution)"),
    ("完成标准全部满足: [ ]", "All Completion Criteria met: [ ]"),
    ("无否决条件触发: [ ]", "No Kill Conditions triggered: [ ]"),
    ("主要成功点: ____", "Key successes: ____"),
    ("主要失败/不足: ____", "Key failures/shortcomings: ____"),
    ("下次应改进: ____", "Improvements for next time: ____"),
    ("需要升级为 Spec 的经验: ____", "Experience worth upgrading to Spec: ____"),

    # Retrospect template (Appendix C)
    ("Retrospect: [事件/里程碑名称]", "Retrospect: [event/milestone name]"),
    ("触发日期", "Trigger date"),
    ("参与模型", "Participating models"),
    ("审查独立性", "Review independence"),
    ("事实层: 发生了什么？", "Factual layer: What happened?"),
    ("背景（触发前状态）", "Background (pre-trigger state)"),
    ("事件流（按时间顺序）", "Event flow (chronological)"),
    ("关键决策点（+ 谁做的决策）", "Key decision points (+ who made the decision)"),
    ("偏离预期的地方", "Deviations from expectation"),
    ("因果层: 为什么发生？", "Causal layer: Why did it happen?"),
    ("根本原因（Root Cause, 用 5-Why）", "Root Cause (use 5-Why)"),
    ("直接原因（Proximate Cause）", "Proximate Cause"),
    ("贡献因素（Contributing Factors）", "Contributing Factors"),
    ("假设层: 暴露了什么差距？", "Assumption layer: What gap was exposed?"),
    ("被打破的假设", "Broken assumption"),
    ("假设为什么会被持有（来源、强度、验证状态）", "Why was the assumption held (source, strength, verification status)"),
    ("这个假设在其他场景下是否也被（错误地）持有？", "Is this assumption also (incorrectly) held in other scenarios?"),
    ("教训层: 应该记住什么？", "Lesson layer: What should be remembered?"),
    ("行为教训（做什么/不做什么）", "Behavioral lesson (what to do / what not to do)"),
    ("模式教训（可跨项目迁移）", "Pattern lesson (transferable across projects)"),
    ("约束教训（应变成规则或检查项）", "Constraint lesson (should become a rule or checklist item)"),
    ("行动层: 具体改什么？", "Action layer: What concretely changes?"),
    ("立即修复（本次）", "Immediate fix (this round)"),
    ("短期改进（下一个项目）", "Short-term improvement (next project)"),
    ("长期预防（框架/MF 升级）", "Long-term prevention (framework/MF upgrade)"),
    ("不做什么（明确记录避免重复发明）", "What NOT to do (explicitly recorded to avoid reinvention)"),

    # Full Retrospect template (Appendix C enhanced)
    ("触发日期: ____", "Trigger date: ____"),
    ("参与模型: ____", "Participating models: ____"),
    ("审查独立性: [独立/半独立/自审]", "Review independence: [Independent / Semi-independent / Self-review]"),
    ("发现方法: [主动审查/被动观测/偶然发现/用户反馈/外部输入/其他: ____]", "Discovery method: [Active review / Opportunistic observation / Accidental discovery / User feedback / External input / Other: ____]"),
    ("验证状态: [已确认/部分确认/未验证/无法验证]", "Verification status: [Confirmed / Partially confirmed / Unverified / Unverifiable]"),
    ("可推广性: [单项目/本框架领域内/可能跨领域/未知]", "Applicability: [Single project / Within framework domain / Potentially cross-domain / Unknown]"),

    # Closure checklist (Appendix D)
    ("Closure 检查清单: [项目名称]", "Closure Checklist: [Project Name]"),
    ("C1. 所有 P0 项已完成", "C1. All P0 items completed"),
    ("C2. 所有重大 Bug 已修复或记录为已知问题", "C2. All major bugs fixed or documented as known issues"),
    ("C3. 所有 OPEN 项已裁决", "C3. All OPEN items resolved"),
    ("C4. Retrospect 已完成", "C4. Retrospect completed"),
    ("C5. 关键教训已写回 Spec", "C5. Key lessons written back to Spec"),
    ("C6. 文件结构已清理", "C6. File structure cleaned up"),
    ("C7. README/CLAUDE.md 已更新", "C7. README/CLAUDE.md updated"),
    ("C8. 构建/运行指令已验证（至少一次干净运行）", "C8. Build/run instructions verified (at least one clean run)"),
    ("C9. 归档包已生成（如适用）", "C9. Archive package generated (if applicable)"),

    # Session Start/End templates (Appendix E)
    ("Session Start", "Session Start"),
    ("日期: ____", "Date: ____"),
    ("模型: ____", "Model: ____"),
    ("项目: ____", "Project: ____"),
    ("本次目标: ____", "This session's goal: ____"),
    ("注意事项: ____", "Notes: ____"),
    ("Session End", "Session End"),
    ("完成项: ____", "Completed: ____"),
    ("未完成项: ____", "Unfinished: ____"),
    ("下次计划: ____", "Next plan: ____"),
    ("值得记录的经验: ____", "Experience worth recording: ____"),
    ("需要升级为 Spec 的经验: ____（同 Prompt 模板）", "Experience worth upgrading to Spec: ____ (same as Prompt template)"),

    # Risk Register (Appendix F)
    ("风险登记: [项目名称]", "Risk Register: [Project Name]"),
    ("风险描述", "Risk description"),
    ("影响 (H/M/L)", "Impact (H/M/L)"),
    ("概率 (H/M/L)", "Probability (H/M/L)"),
    ("缓解措施", "Mitigation"),
    ("触发条件", "Trigger condition"),
    ("状态 [活跃/已解除/已发生]", "Status [Active / Resolved / Occurred]"),
    ("这是一个模板（待填充）—— 实际使用时会记录具体风险条目。", "This is a template (to be filled) — actual risk entries are recorded during use."),

    # Dev Log template (Appendix G)
    ("开发手册：[项目名称]", "Development Manual: [Project Name]"),
    ("项目文件树地图", "Project File Tree Map"),
    ("变更时间轴", "Change Timeline"),
    ("[日期] — [变更标题]", "[YYYY-MM-DD] — [Change Title]"),
    ("基本信息", "Basic Information"),
    ("日期: ____", "Date: ____"),
    ("模型: ____", "Model: ____"),
    ("版本: ____", "Version: ____"),
    ("变更类型: [Bug修复/功能新增/重构/文档/配置/其他]", "Change type: [Bug fix / Feature / Refactor / Documentation / Configuration / Other]"),
    ("严重性: [P0/P1/P2]", "Severity: [P0 / P1 / P2]"),
    ("症状（仅 Bug）", "Symptoms (Bug only)"),
    ("根因（仅 Bug）", "Root Cause (Bug only)"),
    ("变更内容", "Changes Made"),
    ("影响分析", "Impact Analysis"),
    ("影响范围: ____", "Scope of impact: ____"),
    ("破坏性: [是/否]", "Breaking: [Yes / No]"),
    ("测试: ____", "Tests: ____"),
    ("教训", "Lessons Learned"),
    ("变更历史详见: DEV_LOG.md", "See change history: DEV_LOG.md"),
    ("关键变更: [6/9 BUGFIX-001 波动率单位] [6/8 V3.6解耦重构]", "Key changes: [6/9 BUGFIX-001 volatility units] [6/8 V3.6 decoupling refactor]"),
]

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for old, new in REPLACEMENTS:
    if old in content:
        content = content.replace(old, new)
        count += 1

# Verify no residual Chinese in template blocks
# Find all markdown code blocks and check for Chinese
import unicodedata
lines = content.split('\n')
in_md_block = False
residual = []
for i, line in enumerate(lines, 1):
    if line.strip().startswith('```markdown'):
        in_md_block = True
        continue
    elif line.strip().startswith('```') and in_md_block:
        in_md_block = False
        continue
    if in_md_block:
        has_cjk = any('一' <= c <= '鿿' for c in line)
        if has_cjk:
            residual.append((i, line.rstrip()[:120]))

if residual:
    print(f"⚠ {len(residual)} lines with residual Chinese in template blocks:")
    for ln, text in residual[:20]:
        print(f"  L{ln}: {text}")

with open(TARGET, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"\nApplied {count}/{len(REPLACEMENTS)} replacements")
print(f"Residual Chinese lines in template blocks: {len(residual)}")

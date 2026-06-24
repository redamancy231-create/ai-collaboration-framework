#!/usr/bin/env python3
"""Fix remaining untranslated Chinese in appendix template code blocks (Appendices B-G)."""
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

PROJECT = Path(__file__).resolve().parent.parent

TARGET = str(PROJECT / "en/AI协作项目全生命周期框架.md")

REPLACEMENTS = [
    # === Appendix B: Prompt Template — Kill Conditions section ===
    ("### 4. Kill Conditions（来自 kill-test-first 门1）", "### 4. Kill Conditions (from kill-test-first gate 1)"),
    ("- 独立性声明: ____", "- Independence declaration: ____"),
    ("- 可证伪命题: 如果 ____ 不成立，结论无效", "- Falsifiable proposition: If ____ does not hold, the conclusion is invalid"),
    ("- 先验对标: 已知 ____ 做过类似，本任务差异 ____", "- Prior benchmark: ____ has done similar work; this task differs in ____"),
    ("- 死亡判据: 如果 ____ → STOP", "- Kill Criteria: If ____ → STOP"),
    ("- 质量门槛: 交付前通过 ____", "- Quality bar: Must pass ____ before delivery"),
    ("- 三态: GO / STOP / REDESIGN（最多 2 次）", "- Three states: GO / STOP / REDESIGN (max 2 attempts)"),
    ("### 5. 约束", "### 5. Constraints"),
    ("- 来自 Spec: ____", "- From Spec: ____"),
    ("- 本轮特有: ____", "- This-round specific: ____"),
    ("### 6. 逃生口", "### 6. Escape Hatch"),
    ("- 发现需改 Spec → 触发 HG-2", "- Discovery that Spec needs changing → trigger HG-2"),
    ("- 前提假设不成立 → 停止并报告", "- Precondition assumption fails → stop and report"),
    ("- 超出 scope → 记录但不执行，下轮讨论", "- Out of scope → record but do not execute; discuss next round"),

    # === Appendix C: Lightweight Retrospect Template ===
    ("> 触发事件: [里程碑完成 / 外部审查]", "> Trigger event: [Milestone completed / External review]"),
    ("> 参与方: [AI / 人 / 混合]", "> Participants: [AI / Human / Mixed]"),
    ("> 审查类型: [独立 / 半独立 / 自审]", "> Review type: [Independent / Semi-independent / Self-review]"),
    ("### 1. 生效清单（Keep doing）", "### 1. What Worked (Keep doing)"),
    ("### 2. 失效清单（Stop doing / Change）", "### 2. What Didn't Work (Stop doing / Change)"),
    ("- 数据/工具就绪检查", "- Data/tool readiness check"),
    ("- Spec 一致性检查", "- Spec consistency check"),
    ("- 可复现性检查", "- Reproducibility check"),

    # === Appendix D: Closure Checklist ===
    ("> 闭合Date: ____", "> Closure Date: ____"),
    ("> 闭合条件: [目标达成 / 红线触发 / 预算耗尽 / 发现替代 / 优先级变更 / 人决定]",
     "> Closure condition: [Goal achieved / Red line triggered / Budget exhausted / Alternative found / Priority changed / Human decision]"),
    ("> 闭合触发证据: ____", "> Closure trigger evidence: ____"),
    ("### 终期产物", "### Final Deliverables"),
    ("- [ ] 终期总结报告 (.md)", "- [ ] Final summary report (.md)"),
    ("- [ ] 终期总结报告 (.docx) [学术项目必须]", "- [ ] Final summary report (.docx) [Mandatory for academic projects]"),
    ("- [ ] 项目评估分析 (.md + .json)", "- [ ] Project evaluation analysis (.md + .json)"),
    ("### 可复用遗产提取", "### Reusable Legacy Extraction"),
    ("- [ ] 代码模块: ____", "- [ ] Code modules: ____"),
    ("- [ ] 方法论片段: ____", "- [ ] Methodology fragments: ____"),
    ("- [ ] 失败模式: ____", "- [ ] Failure patterns: ____"),
    ("- [ ] 数据资产: ____", "- [ ] Data assets: ____"),
    ("### 跨项目写回", "### Cross-Project Write-Back"),
    ("- [ ] memory/ 新增/更新（至少 3 条）", "- [ ] memory/ additions/updates (at least 3 items)"),
    ("- [ ] 框架级教训写回（如适用）", "- [ ] Framework-level lesson write-back (if applicable)"),
    ("### 归档", "### Archive"),
    ("- [ ] 项目文件按 §8.5 三级分层归档", "- [ ] Project files archived per §8.5 three-tier structure"),
    ("### 外部审阅", "### External Review"),
    ("- [ ] 终期报告经至少 1 个独立模型审阅", "- [ ] Final report reviewed by at least 1 independent model"),
    ("### 项目状态更新", "### Project Status Update"),
    ("- [ ] project_status.md 标记 CLOSED", "- [ ] project_status.md marked CLOSED"),
    ("- [ ] 记录封存基线 + 重启门槛", "- [ ] Archive baseline + restart threshold recorded"),
    ("### 最终确认", "### Final Confirmation"),
    ("- [ ] 人最终确认（HG-3 闭合闸门）", "- [ ] Final human confirmation (HG-3 closure gate)"),
    ("### 清理", "### Cleanup"),
    ("- [ ] 临时文件清理", "- [ ] Temporary file cleanup"),
    ("- [ ] 敏感信息检查", "- [ ] Sensitive information check"),
    ("- [ ] 交付物双件生成（md + json）", "- [ ] Dual-format artifact generation (md + json)"),

    # === Appendix E: Session Handoff ===
    ("### Session Start 检查清单", "### Session Start Checklist"),
    ("- [ ] 读 CLAUDE.md（自动）", "- [ ] Read CLAUDE.md (automatic)"),
    ("- [ ] 读 memory/MEMORY.md（自动）", "- [ ] Read memory/MEMORY.md (automatic)"),
    ("- 逐条检查 memory 时效性：超过 30 天的条目提醒\"需验证\"",
     "- Check memory timeliness item by item: entries older than 30 days prompt \"verification needed\""),
    ("- [ ] 读本项目的 project_status.md", "- [ ] Read this project's project_status.md"),
    ("- [ ] 检查未完成的 Next Steps", "- [ ] Check unfinished Next Steps"),
    ("- [ ] 读上一次 Retrospect（如有）", "- [ ] Read previous Retrospect (if exists)"),
    ("- [ ] 确认当前环境：Python 版本、工作目录、数据可用性",
     "- [ ] Confirm current environment: Python version, working directory, data availability"),
    ("### Session End 检查清单", "### Session End Checklist"),
    ("- [ ] 更新 project_status.md（本会话完成项 + 下次计划）",
     "- [ ] Update project_status.md (completed this session + next plan)"),
    ("- [ ] 更新 CLAUDE.md（如有重要新发现）", "- [ ] Update CLAUDE.md (if important new findings)"),
    ("- [ ] 更新 memory/（跨项目经验写回）", "- [ ] Update memory/ (cross-project experience write-back)"),
    ("- [ ] Retrospect（如适用，按轻量模板）", "- [ ] Retrospect (if applicable, lightweight template)"),
    ("- [ ] 确认 .gitignore 与发布边界一致", "- [ ] Confirm .gitignore matches release boundary"),
    ("- [ ] 确认无临时文件/敏感信息残留", "- [ ] Confirm no temporary files / sensitive info residual"),

    # === Appendix F: Risk Register ===
    ("| ID | Risk description | 影响(H/M/L) | 概率(H/M/L) | Mitigation | 触发信号 | Plan B | 状态 |",
     "| ID | Risk description | Impact (H/M/L) | Probability (H/M/L) | Mitigation | Trigger signal | Plan B | Status |"),
    ("| ID | 风险描述 | 影响(H/M/L) | 概率(H/M/L) | 缓解措施 | 触发条件 | Plan B | 状态 [活跃/已解除/已发生] |",
     "| ID | Risk description | Impact (H/M/L) | Probability (H/M/L) | Mitigation | Trigger condition | Plan B | Status [Active/Resolved/Occurred] |"),

    # === Appendix G: Dev Log Template (additional) ===
    ("### 项目文件树地图（自动生成）", "### Project File Tree Map (auto-generated)"),
    ("### 变更时间轴（反向时间序）", "### Change Timeline (reverse chronological)"),
    ("### 基本信息", "### Basic Information"),
    # "症状" could be ambiguous - keep searching context
    ("- 症状: ____", "- Symptoms: ____"),
    ("- 根因: ____", "- Root cause: ____"),
    ("- 触发: ____", "- Trigger: ____"),
    ("- 修复: ____", "- Fix: ____"),
    ("- 教训: ____", "- Lesson: ____"),
    ("### 关联变更", "### Related Changes"),
    ("- 前置依赖: ____", "- Prerequisite: ____"),
    ("- 后续影响: ____", "- Subsequent impact: ____"),
    ("### 审阅", "### Review"),
    ("- [ ] 自审", "- [ ] Self-review"),
    ("- [ ] 异后端审阅", "- [ ] Cross-backend review"),
    ("- [ ] 人确认", "- [ ] Human confirmation"),

    # Missing pieces in the Extended Prompt Template (after Appendix B main body)
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

    # Additional items from the expanded template sections
    ("### 特殊约束", "### Special Constraints"),
    ("- 时间上限: ____ 分钟", "- Time limit: ____ minutes"),
    ("- 工具限制: ____", "- Tool restrictions: ____"),
    ("### 输出格式", "### Output Format"),
    ("### 独立审查", "### Independent Review"),
    ("- [ ] 至少 1 个异后端独立审查", "- [ ] At least 1 cross-backend Independent Review"),
    ("- [ ] 审查报告存入 _reviews/", "- [ ] Review report stored in _reviews/"),
    ("### 交付物", "### Deliverables"),
    ("- [ ] .md", "- [ ] .md"),
    ("- [ ] .json [学术项目必须]", "- [ ] .json [Mandatory for academic projects]"),

    # Additional cleanup: catch remaining CJK line-by-line in appendix region
    ("| 风险描述", "| Risk description"),
    ("| 影响(H/M/L)", "| Impact (H/M/L)"),
    ("| 概率(H/M/L)", "| Probability (H/M/L)"),
    ("| 缓解措施", "| Mitigation"),
    ("| 触发条件", "| Trigger condition"),
    ("| 状态", "| Status"),
    ("### 8. Agent 自评（执行后填写）", "### 8. Agent Self-Assessment (fill in after execution)"),
    ("### 9. 独立审查（如适用）", "### 9. Independent Review (if applicable)"),
]

with open(TARGET, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for old, new in REPLACEMENTS:
    if old in content:
        content = content.replace(old, new)
        count += 1

# Residual check: count CJK lines in non-Mermaid code blocks
lines = content.split('\n')
in_block = False
in_mermaid = False
residual = []
for i, line in enumerate(lines, 1):
    s = line.strip()
    if s.startswith('```mermaid'):
        in_mermaid = True; in_block = True; continue
    elif s.startswith('```') and not in_mermaid and not in_block:
        in_block = True; continue
    elif s.startswith('```') and in_block:
        in_mermaid = False; in_block = False; continue
    if in_block and not in_mermaid:
        has_cjk = any('一' <= c <= '鿿' for c in line)
        if has_cjk:
            residual.append((i, line.rstrip()[:130]))

with open(TARGET, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print(f"Applied {count}/{len(REPLACEMENTS)} replacements")
print(f"Residual non-Mermaid code block CJK: {len(residual)}")
for ln, txt in residual[:15]:
    print(f"  L{ln}: {txt}")

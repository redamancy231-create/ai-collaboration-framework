#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync AI协作项目全生命周期框架.json to v1.6 — evidence system upgrade + maintenance enhancements.

Targeted update: metadata + changelog + version_timeline + structural nodes for 7 new sections.
Run: PYTHONIOENCODING=utf-8 python _workflows/sync_v16_json.py
"""

import json
import os
import sys

JSON_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.json"
BACKUP_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.json.v155.backup"

def load_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path=None):
    target = path or JSON_PATH
    with open(target, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    data = load_json()
    save_json(data, BACKUP_PATH)
    print(f"Backup saved to: {BACKUP_PATH}")

    md = data['metadata']

    # === 1. Core metadata ===
    md['version'] = "1.6"
    md['date'] = "2026-06-20"
    md['model'] = "DeepSeek-V4-Pro (via Claude Code CLI shell)"
    md['revision'] = "v1.6 (2026-06-20)"
    md['revision_source'] = (
        "A2+A3深度复盘(5-agent Workflow, A2×A3跨实验综合, 10模式2推翻8修订) + "
        "Codex v1.5.5交叉验证(MAJOR #1/#3) + "
        "prompt-tdd A2+A3实验写回 + "
        "跨版本维护实践规范化(P1维护性增强) + "
        "PocketFlow三轮独立分析(A类资产写回) + "
        "Evolver项目分析(Protocol 3试跑1回写) + "
        "GitNexus分析项目 + Small_Scale项目分析"
    )

    # === 2. Status ===
    md['status'] = (
        "草案, v1.6 (证据体系升级+维护性增强). "
        "v1.6 P0新增: §9.6.1(二维证据等级: 内部强度A-D × 跨模型推广性M0-M3/N/A) + "
        "§9.10(MF三层模板: 问题识别+解决方案适用条件+已知反例/失效模式) + "
        "§4.1.1.1(对照实验设计强制检查清单CK1-CK6, Tier 1硬门+条件触发). "
        "v1.6 P1新增: §2.6(框架维护流程: 版本号规则/审查门/三件套同步/冻结期) + "
        "§1.8(已知局限与诚实声明: 8条系统性局限) + "
        "§9.9路径D(方法论迁移者30-45min) + 附录H反向交叉引用. "
        "v1.5.5新增: §6.3.1路由声明格式对照证据[E-](A3实验写回). "
        "v1.5.4新增: §4.1.1执行合约[E-](A2实验写回). "
        "v1.5.3新增: §1.7(最小核心+示例外挂)+§9.9(阅读导航)+附录H(反模式清单). "
        "v1.5.2写回: Protocol 3试跑1的6项改进. "
        "v1.5.1新增: §3.7.0+§3.7.4.1+§9.7+§9.8(四个[Sp]节). "
        "方法论来源: prompt-tdd A2+A3深度复盘+Evolver项目(4.1-4.2/10)+"
        "PocketFlow(DeepSeek/ChatGPT-5.5/GLM-5.2)+GitNexus+Small_Scale. "
        "v1.6经Codex GPT-5.5初审(FAIL_WITH_MAJOR_ISSUES)→修正→重审(FAIL_WITH_CAVEATS)→修正. "
        "审查独立性: [SEMI]——后端不同但提示词由作者撰写."
    )

    # === 3. Changelog — prepend v1.6 entry ===
    v16_changelog = {
        "version": "v1.6",
        "date": "2026-06-20",
        "trigger": (
            "A2+A3深度复盘§7 + Codex v1.5.5交叉验证MAJOR #1/#3 + "
            "跨版本维护实践规范化(P1维护性增强来自Codex/Qwen审查中反复出现的组织/导航/可维护性关切)"
        ),
        "summary": (
            "v1.6 Minor升级——7项新增/增强写回. "
            "P0(证据体系升级): §9.6.1二维证据等级 + §9.10 MF三层模板 + §4.1.1.1对照实验设计强制检查清单. "
            "P1(维护性/导航增强): §2.6框架维护流程 + §1.8诚实声明(8条局限) + §9.9路径D + 附录H反向交叉引用."
        ),
        "changes": [
            {"id": "v1.6-1", "type": "新增", "desc": "§9.6.1证据等级二维表示——内部强度A-D × 跨模型推广性M0-M3/N/A", "location": "§9.6.1"},
            {"id": "v1.6-2", "type": "新增", "desc": "§9.10 MF三层模板——问题识别+解决方案适用条件+已知反例/失效模式, 含PT-M1完整示例", "location": "§9.10"},
            {"id": "v1.6-3", "type": "新增", "desc": "§4.1.1.1对照实验设计强制检查清单CK1-CK6 (Tier 1硬门CK1-CK3 + 条件触发CK4-CK6)", "location": "§4.1.1.1"},
            {"id": "v1.6-4", "type": "新增", "desc": "§2.6框架维护流程——版本号规则/审查门/三件套同步/冻结期+过渡条款", "location": "§2.6"},
            {"id": "v1.6-5", "type": "新增", "desc": "§1.8已知局限与诚实声明——8条系统性局限集中声明", "location": "§1.8"},
            {"id": "v1.6-6", "type": "扩展", "desc": "§9.9新增路径D(方法论迁移者30-45min)", "location": "§9.9"},
            {"id": "v1.6-7", "type": "扩展", "desc": "附录H 4条反模式各添加反向交叉引用", "location": "附录H"},
        ],
        "evidence_level": "[C+/N/A]——跨项目模式识别, 非LLM实验来源",
        "codex_reviews": [
            "Codex GPT-5.5初审(FAIL_WITH_MAJOR_ISSUES, 2 MAJOR + 7 MEDIUM)→全量修正",
            "Codex GPT-5.5重审(FAIL_WITH_CAVEATS, 0 MAJOR + 5 MEDIUM)→全量修正",
        ],
        "three_piece_sync": "2026-06-20: .md已更新(v1.6); .json本次同步; .docx待生成",
        "unadopted_downgraded": [
            "复盘§7.3 多轮异后端审查收益管理 → v1.7+ (N=2实验数据不足)",
            "复盘§7.4 阴性实验价值评估与归档标准 → v1.7+ (体量大, 独立成章)",
            "复盘§7.5 实验间方法论传递审计 → v1.7+ (PT-M1单一断裂案例不足)",
            "复盘§7.6 Tier 0/Tier 1升级标准 → v1.7+ (已部分吸收至CK1)",
        ],
    }
    md['changelog'].insert(0, v16_changelog)

    # === 4. Version timeline — append v1.6 row ===
    if 'version_timeline' not in md:
        md['version_timeline'] = []
    md['version_timeline'].append({
        "date": "2026-06-20",
        "version": "v1.6",
        "event": "Minor升级: P0证据体系升级(§9.6.1/§9.10/§4.1.1.1)+P1维护性增强(§2.6/§1.8/§9.9路径D/附录H反向引用)",
        "evidence": "今日操作; 7项新增/增强写回; 经Codex GPT-5.5初审→修正→重审→修正",
        "confidence": "🟡 较可信(本日操作, Codex重审FAIL_WITH_CAVEATS已修正, 待三件套全量同步验证)",
    })

    # === 5. Independent reviews — append Codex v1.6 reviews ===
    if 'independent_reviews' not in md:
        md['independent_reviews'] = []
    md['independent_reviews'].append({
        "version": "v1.6",
        "reviewer": "Codex GPT-5.5 (Codex CLI)",
        "date": "2026-06-20",
        "type": "异后端交叉验证(初审+重审)",
        "verdict_initial": "FAIL_WITH_MAJOR_ISSUES",
        "verdict_rereview": "FAIL_WITH_CAVEATS",
        "report": "_reviews/codex_v16_crosscheck_20260620.txt",
        "rereview_report": "_reviews/codex_v16_crosscheck_rereview_20260620.txt",
    })

    # === 6. Add structural nodes for new sections ===

    # §1.8 已知局限与诚实声明
    data['known_limitations'] = {
        "section": "§1.8",
        "title": "已知局限与诚实声明",
        "added_in": "v1.6",
        "evidence_level": "[C+/N/A]",
        "source": "Codex v1.5.5 MAJOR #1精神 + 复盘§9已知局限(PM-1~PM-6 + §9.3/§9.4)",
        "limitations": [
            "单模型证据主导——A2/A3均基于GPT-5.5 temp=0",
            "单团队实验者效应——设计/执行/审查未分离",
            "无独立人类专家校准——评分体系全程LLM-LLM",
            "二维证据体系未试跑——v1.6新增的二维等级待验证",
            "N=2实验的统计基础——量化数字不可参数化推广",
            "探索性vs确认性框架张力——Tier 0/Tier 1边界模糊",
            "测试集区分度未分析——有效样本量可能远小于名义样本量",
            "框架自身审查链局限——审查者池固定/停止规则内生/学习效应未控制",
        ],
    }

    # §2.6 框架维护流程
    data['framework_maintenance'] = {
        "section": "§2.6",
        "title": "框架自身的维护流程",
        "added_in": "v1.6",
        "evidence_level": "[D/N/A]",
        "source": "跨版本维护实践规范化 + Codex/Qwen审查中反复出现的可维护性关切",
        "key_rules": {
            "versioning": "语义化版本(Major.Minor.Patch), Major需≥3后端审查+试跑, Minor需≥2后端审查, Patch可单后端",
            "changelog": "每版记录触发事件/修改节/来源/证据等级, 版本时间线同步更新, 保留独立快照",
            "writeback_review_gate": "新[Sp]节≥2后端+冻结期, 新[E-]节≥2后端0 MAJOR, 修订≥1后端, 重组≥1后端",
            "three_piece_sync": "Minor+升级后.md/.json/.docx全量同步, ≥1轮异后端检查一致性",
            "freeze_rules": "≥50%新[Sp]节完成试跑前不接受新[Sp]机制节",
        },
        "transition_clause": "§2.6审查门自v1.6审查通过后的下一版起生效; v1.6自身为pre-release draft",
    }

    # §4.1.1.1 对照实验设计检查清单 (P0 portion)
    data['experiment_design_checklist'] = {
        "section": "§4.1.1.1",
        "title": "对照实验设计强制检查清单",
        "added_in": "v1.6",
        "evidence_level": "[C+/M1]",
        "source": "A2+A3深度复盘§7.1",
        "tier1_hard_gates": {
            "CK1": "效能分析/最小可检测效应量——Tier 1必须有, 事后报告MDE",
            "CK2": "GT预定义完整性——边缘用例规则/多标签可接受集合/争议仲裁流程",
            "CK3": "DV×天花板解决方案适用性矩阵——单维度任务禁止仅靠增加难度",
        },
        "conditional_items": {
            "CK4": "测试集捷径审计+反编造测试——条件触发(强模型+prompt文本匹配), 可豁免",
            "CK5": "INVENTORY等价性异后端验证——条件触发(≥2 prompt变体), 可豁免",
            "CK6": "修复-回归循环审查门——条件触发(组件级以上结构性变更), 可豁免",
        },
        "usage": "Tier 1硬门(CK1-CK3)任一项FAIL→禁止进入Tier 1; 条件触发项(CK4-CK6)FAIL时记录豁免理由后可进入",
    }

    # §9.6.1 二维证据等级
    data['two_dimensional_evidence'] = {
        "section": "§9.6.1",
        "title": "证据等级的二维表示: 内部强度 × 跨模型推广性",
        "added_in": "v1.6",
        "evidence_level": "[C+/N/A]",
        "source": "Codex v1.5.5 MAJOR #3 + 复盘跨实验综合",
        "dimension_1_internal": {
            "A": "多源交叉验证——≥2独立实验/项目/方法方向一致",
            "B+": "单实验强证据——严谨设计+≥6轮审查+0未闭合MAJOR",
            "B": "单实验中等证据——基本合理, 已知局限存在",
            "C+": "多项目模式识别——≥2项目, 经≥2后端审查",
            "C": "单项目观察——单个项目中发现的现象",
            "D": "专家判断/推测——基于领域经验但无系统证据",
        },
        "dimension_2_cross_model": {
            "M3": "跨≥3模型家族验证",
            "M2": "跨2模型家族验证",
            "M1": "两实验单模型家族(≥2独立实验, 同家族)",
            "M0": "单实验单模型(1实验, 1家族)",
            "N/A": "非LLM来源",
        },
        "notation": "[内部强度 / 跨模型推广性], e.g. [B+/M0], [C+/M1]",
    }

    # §9.10 MF三层模板
    data['methodological_fragment_three_layer_template'] = {
        "section": "§9.10",
        "title": "方法论片段模板: 三层模型",
        "added_in": "v1.6",
        "evidence_level": "[C+/N/A]",
        "source": "A2+A3深度复盘§6.1(PT-M1迁移断裂)",
        "layers": {
            "layer_1": "问题识别(Problem Space)——核心问题描述+问题识别条件+检测方法",
            "layer_2": "解决方案(Solution Space)——推荐方案+适用条件+替代方案+选择决策树",
            "layer_3": "已知反例与失效模式(Failure Space)——已知反例+失效机制+静默失效信号+与其他MF的冲突",
        },
        "key_rules": [
            "三层回答不同的问题, 不可互相替代",
            "第三层是第二层的测试覆盖——每个适用条件须有对应已知反例",
            "静默失效信号是强制字段——对于有自动化检测潜力的失效模式",
            "三层可独立更新——某层证据增强不要求其他层同步更新",
        ],
        "pt_m1_example": "PT-M1三层示例见§9.10正文——A3的Hard Mode是任务可供性=1时选了前提不适用的方案",
    }

    save_json(data)
    print(f"JSON synced to v1.6: {JSON_PATH}")
    print("Done. Next: verify with diff, then sync .docx")

if __name__ == '__main__':
    main()

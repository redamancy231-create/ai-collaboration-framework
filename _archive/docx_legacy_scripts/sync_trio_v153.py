#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync AI协作项目全生命周期框架.json to v1.5.3 based on the md source of truth.

This script updates metadata, changelog, edit_history, independent_reviews,
and adds new structural sections (§1.7, §9.9, Appendix H) that were added
in v1.5.2 (Protocol 3 writeback) and v1.5.3 (PocketFlow A-class assets).

Run: PYTHONIOENCODING=utf-8 python _workflows/sync_trio_v153.py
"""

import json
import os
import sys

JSON_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.json"
VERSION_PATH = "<PROJECT_ROOT>/VERSION"

def load_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path=None):
    target = path or JSON_PATH
    with open(target, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    data = load_json()

    md = data['metadata']

    # === 1. Update core metadata ===
    md['version'] = "1.5.3"
    md['date'] = "2026-06-18"
    md['model'] = "DeepSeek-v4-pro (via Claude Code CLI shell)"
    md['revision'] = "v1.5.3 (2026-06-18)"
    md['revision_source'] = (
        "Evolver项目分析(Protocol 3试跑1回写) + PocketFlow三轮独立分析(A类资产写回) "
        "+ GitNexus分析项目 + Small_Scale项目分析 + ChatGPT-5.5独立审查"
    )

    # Update name to reflect current version
    md['name'] = "AI协作项目全生命周期框架"

    # Update status and description
    md['status'] = (
        "草案, v1.5.3 (PocketFlow方法论转化A类资产写回 + Protocol 3试跑1回写). "
        "v1.5.3新增: §1.7(最小核心+示例外挂)+§9.9(阅读导航与难度分层)+附录H(反模式清单). "
        "v1.5.2写回: Protocol 3试跑1的6项改进(C1/C5测量方法/HG-0双检查点/审查频率适应性上调/"
        "HG交互留存/C8≥2轮异后端建议/S-tier降级阈值备注). "
        "v1.5.1新增: §3.7.0(事件流健康度监测[Sp])+§3.7.4.1(自适应权重淘汰[Sp])"
        "+§9.7(经验注入上下文预算规则[Sp])+§9.8(研究经验对象REO[Sp]). "
        "方法论来源=Evolver项目分析(arXiv:2604.15097,综合评分4.1-4.2/10,四轮独立审查跨三个后端)"
        "+PocketFlow三轮独立分析(DeepSeek-V4-Pro/ChatGPT-5.5/GLM-5.2). "
        "v1.5.1草案经Codex ChatGPT-5.5 R3→R4审查(R3驳回4.3→R4修改后通过7.2/10, Δ+2.9). "
        "v1.5新增: §6.2模式8/9+§9.2+§9.6, 经ChatGPT-5.5审查C+(5.43/10). "
        "v1.4新增: §3.7.2.6/§5.3.1/§6.5.1/§9.1/§1.5/§9.4/附录H(已取消), "
        "经三轮审查(ChatGPT-5.5 5.50+5.37+Kimi-K2.7-Code 5.00). "
        "审查独立性: [SEMI]——后端不同但提示词由作者撰写. "
        "仍待验证: 四个[Sp]节的行为有效性; §9.7 A/B测试; REO Phase 0-3实施; "
        "S-tier Protocol 3降级阈值; §1.7/§9.9/附录H的读者验证."
    )

    md['status_note'] = (
        "草案冻结已解除(Protocol 3试跑1 Retrospect完成, 条件满足). "
        "v1.5.2写回Protocol 3试跑1反馈(6项改进). "
        "v1.5.3写回PocketFlow A类资产(3项: §1.7+§9.9+附录H). "
        "仍待多项目验证. "
        "v1.5.1新增: §3.7.0事件流健康度监测[Sp]+§3.7.4.1自适应权重淘汰[Sp]"
        "+§9.7经验注入上下文预算规则[Sp]+§9.8研究经验对象(REO)[Sp]. "
        "方法论来源=Evolver项目分析(arXiv:2604.15097,综合评分4.1-4.2/10,四轮独立审查跨三个后端). "
        "完整规格见_research/框架v1.5.1_新增节草案.md. "
        "v1.5新增: §6.2模式8/9+§9.2+§9.6. "
        "v1.4新增: §3.7.2.6/§5.3.1/§6.2/§6.5.1/§9.1/§1.5/§9.4/附录H. "
        "v1.3遗留OPEN-1~4状态不变(OPEN-5已于v1.5.1冻结期关闭→§8.8). "
        "v1.3新增§3.7漂移检测层(五类信号+告警聚合+规则退役+宪法审计+闭环策展+监测模板)——"
        "将OPEN-1从候选草案升级为正式操作化方案. "
        "经ChatGPT-5.5独立审查全件(加权6.1/10,修改后通过), 10项修订已执行. "
        "21个决策点已拍板, 但Dev Log 7/10组件待实证、框架整体已经1次真实试跑(Protocol 3)."
    )

    # Update description to include v1.5.2/v1.5.3
    md['description'] = (
        "AI协作项目的完整操作化框架——从Spec到Closure的七层+四跨层关切+开发手册产物. "
        "v1.1新增Dev Log(开发手册). v1.2经三模型独立审查链校准. "
        "v1.3新增§3.7漂移检测层(五类信号+四级告警+规则退役+宪法审计+闭环策展+监测模板). "
        "v1.4新增§3.7.2.6难度分层监测+§5.3.1能力获取vs行为塑造+§6.5.1文件系统IPC反面模式"
        "+§9.1训练-评估对齐/Import完整性/配置验证/接口退化. "
        "v1.5新增§6.2模式8(Pipeline DAG)+模式9(Structured Multi-Role Review)"
        "+§9.2多轮多后端独立审查编排+§9.6证据分类(S/E/I/J/Sp). "
        "v1.5.1新增§3.7.0事件流健康度监测+§3.7.4.1自适应权重淘汰"
        "+§9.7经验注入上下文预算规则+§9.8研究经验对象(REO). "
        "v1.5.2写回Protocol 3试跑1的6项改进(C1/C5测量方法/HG-0双检查点/"
        "审查频率适应性上调/HG交互留存/C8≥2轮异后端建议/S-tier降级阈值). "
        "v1.5.3新增§1.7(最小核心+示例外挂)+§9.9(阅读导航与难度分层)+附录H(反模式清单). "
        "方法论来源=Evolver项目分析(GitNexus→Small_Scale→PilotDeck→Evolver四项目链)"
        "+PocketFlow三轮独立分析. 基于ETF项目V3.6代码头部注释实践提炼."
    )

    # === 2. Update freeze_status ===
    md['freeze_status'] = {
        "frozen": False,
        "was_frozen": True,
        "frozen_since": "2026-06-14",
        "unfrozen_date": "2026-06-16",
        "unfreeze_reason": "Protocol 3试跑1 Retrospect完成, 满足解除条件. v1.5.2为试跑回写版, v1.5.3为PocketFlow A类资产写回版.",
        "original_reason": "框架5版本0试跑；加复杂度倾向已被自身记录但未变成执行约束. 冻结把教训文字变成纪律.",
        "allowed_during_freeze": [
            "修确凿bug(版本漂移/引用失效/编辑错乱)",
            "执行已设计未跑协议(OPEN-4试读/OPEN-1 verify降级替代)",
            "补零试跑即可做的诚实性产物(框架级成熟度表)"
        ],
        "forbidden_during_freeze": [
            "新增[Sp]节",
            "新增机制节"
        ],
        "unfreeze_condition": "首次真实试跑(A类半天或B类一周)完成+Retrospect回写至框架级成熟度表——已满足",
        "note": "v1.5.2和v1.5.3均基于试跑反馈或独立分析产出, 非'加新机制'. 冻结已解除."
    }

    # Update companion_md
    md['companion_md'] = "AI协作项目全生命周期框架.md"

    # Update companion_reviews to include recent reviews
    md['companion_reviews'] = [
        {
            "file": "_reviews/AI协作项目全生命周期框架_对ChatGPT-5.5回应的再再审查.json",
            "status": "legacy",
            "relevant_version": "v1.2"
        },
        {
            "file": "_reviews/框架v1.5.1_Codex审查报告.md",
            "status": "current",
            "relevant_version": "v1.5.1"
        },
        {
            "file": "_reviews/codex_review_v1.5.1_sync.md",
            "status": "current",
            "relevant_version": "v1.5.1"
        },
        {
            "file": "_reviews/codex_review_v1.5.1_三件套同步审查.md",
            "status": "current",
            "relevant_version": "v1.5.1"
        }
    ]

    # Update derived_from to include PocketFlow
    if "PocketFlow三轮独立分析" not in str(md.get('derived_from', [])):
        md['derived_from'] = [
            "13.txt (Prompt/Loop/Workflow/Spec四层讨论，源文件已删除)",
            "kill-test-first skill (事前否决+预登记+先验对标+魔鬼代言人)",
            "形态匹配ETF策略17版本实践经验",
            "并购重组案例研究八阶段流水线经验",
            "LIT项目四轮AI评估教训",
            "BDC2026提交失败教训",
            "多模型对照实验治理审计经验",
            "GitNexus分析项目(2026-06-14: 9-agent workflow+三轮独立审查+证据分类实战)",
            "Evolver项目分析(2026-06-14: arXiv:2604.15097, 综合评分4.1-4.2/10, 四轮独立审查跨三个后端, 方法论提取5项:4项→框架v1.5.1四节+1项→memory/methodology_obfuscated_code_evaluation.md)",
            "PocketFlow三轮独立分析(2026-06-16~18: DeepSeek-V4-Pro/ChatGPT-5.5/GLM-5.2, 方法论提取A类资产3项→框架v1.5.3三节)"
        ]

    # Update JSON sync note in freeze_status
    if 'note_json_sync' in md.get('freeze_status', {}):
        md['freeze_status']['note_json_sync'] = (
            "R4审查指出的'json停v1.4'问题在v1.5.1时已同步修复(version/revision/description/模式8/模式9均已对齐v1.5.1). "
            "v1.5.3全域同步: 包括v1.5.2(Protocol 3试跑1回写)和v1.5.3(PocketFlow A类资产写回)的全部变更. "
            "2026-06-16: 6处ASCII图→Mermaid(F12), json同步补edit_history+rendering元数据. "
            "2026-06-18: 三件套全量同步至v1.5.3."
        )

    # === 3. Add edit_history entries for v1.5.2 and v1.5.3 ===
    edit_history = md.get('edit_history', [])

    # v1.5.2 edit
    edit_history.append({
        "date": "2026-06-16",
        "editor_model": "DeepSeek-v4-pro",
        "editor_cli": "Claude Code CLI shell",
        "editor_house": "Claude house",
        "editor_role": "编辑者（框架作者，自编辑）",
        "independence_level": "[SELF]",
        "independence_note": "作者自编辑，基于Protocol 3首次试跑(方法论提取方法论项目)Retrospect+Phase 7系列审查反馈。C1-C8指标裁决经Codex ChatGPT-5.5独立审查验证(Phase 7.5)。属试跑回写，所有变更来源标注为'[Protocol 3试跑1反馈，2026-06-16]'",
        "scope": "Protocol 3试跑1回写——非冻结期新增机制，而是试跑后对已有框架的测量方法/频率/留存要求的操作性强化",
        "changes": [
            {
                "id": "P3-0",
                "type": "状态更新",
                "desc": "版本头与文档状态更新为v1.5.2 'Protocol 3试跑1回写'，记录本次回写范围",
                "location": "版本头"
            },
            {
                "id": "P3-1",
                "type": "修正",
                "desc": "C1/C5增加可操作测量方法：C1以DEV_LOG HH:MM时间戳计loop耗时；C5维护'框架操作耗时'计数器；首次试跑未完整计时标注为预期内基线问题",
                "location": "§5.2/C1, §9.1/DEV_LOG"
            },
            {
                "id": "P3-2",
                "type": "新增",
                "desc": "HG-0双检查点：Plan阶段(审查项目计划) + Spec阶段(审查Spec)，不是只审写完的Spec",
                "location": "§3.2 HG-0"
            },
            {
                "id": "P3-3",
                "type": "新增",
                "desc": "独立审查频率适应性上调：若项目含≥3概念判断Phase或方法论/概念归类或前期MAJOR密度>3/Phase，可从闭合前一次上调为每Phase后一次",
                "location": "§9.2"
            },
            {
                "id": "P3-4",
                "type": "新增",
                "desc": "HG交互留存要求：每次HG触发时DEV_LOG须记录三项证据——人工响应时间戳/响应内容摘要/AI是否如实传达选项",
                "location": "§3.2"
            },
            {
                "id": "P3-5",
                "type": "新增",
                "desc": "C8≥2轮异后端审查建议写入审查编排规则",
                "location": "§9.2 C8"
            },
            {
                "id": "P3-6",
                "type": "备注",
                "desc": "S档Protocol 3适配备注：C6降为'≥1失效或≥1意外'，C8降为'1轮异后端审查≥6.0/10'，并标注为待S档试跑验证",
                "location": "§5.2/§7/§8.8"
            },
            {
                "id": "P3-7",
                "type": "强化",
                "desc": "深度版Retrospect模板新增'Protocol 3/框架层反馈'项，用于显式记录C1-C8裁决、证据缺口、HG/审查频率教训",
                "location": "§7"
            }
        ],
        "reviewer_guidance": "所有变更均基于首次真实试跑数据(闭合时14/20 loops, 58项发现, 0 CRITICAL/MAJOR遗留)。后续独立审查者应验证：(a)测量方法是否可操作；(b)频率上调条件是否合理；(c)降级阈值是否在试跑中验证。",
        "companion_md_section": "§14「v1.5.2 Protocol 3试跑1回写（2026-06-16）」"
    })

    # v1.5.3 edit
    edit_history.append({
        "date": "2026-06-18",
        "editor_model": "DeepSeek-v4-pro",
        "editor_cli": "Claude Code CLI shell",
        "editor_house": "Claude house",
        "editor_role": "编辑者（框架作者，自编辑）",
        "independence_level": "[SELF]",
        "independence_note": "作者自编辑，基于PocketFlow三轮独立分析(DeepSeek-V4-Pro/ChatGPT-5.5/GLM-5.2, 2026-06-16~18)产出的A类资产——可直接写回框架的方法论改进，无需额外验证实验。共3项A类资产(B2/B1/C1-C3)，经三个并行agent独立规划后统一执行写回。A类满足条件：(a)方法论来源可追溯；(b)≥2后端独立确认可迁移性；(c)不依赖PocketFlow特有实现。写回后经ChatGPT-5.5交叉验证确认一致性",
        "scope": "PocketFlow A类资产写回——新增3节(§1.7+§9.9+附录H)，均为[Sp]推测级，待试跑验证",
        "changes": [
            {
                "id": "PF-1",
                "type": "新增",
                "desc": "新增§1.7「框架自身的架构原则：最小核心+示例外挂」——定义核心(主文档强制规则)vs外挂(配套目录参考实现)的区分标准(普遍性/强制性/稳定性三条判定规则)+4种反模式警示+边界案例默认进外挂原则",
                "location": "§1.7",
                "source": "PocketFlow B1资产——'最小核心+示例外挂架构'"
            },
            {
                "id": "PF-2",
                "type": "新增",
                "desc": "新增§9.9「阅读导航与难度分层」——按☆☆☆/★☆☆/★★☆/★★★标注11个章节难度+3条推荐阅读路径(A最小启动/B标准实践/C完整方法论)+使用说明5条",
                "location": "§9.9",
                "source": "PocketFlow B2资产——cookbook难度分层体系"
            },
            {
                "id": "PF-3",
                "type": "新增",
                "desc": "新增「附录H:反模式清单」——集中收纳4条经独立审查确认可迁移性的反模式(H.1文件系统作IPC/H.2极简主义的隐性成本/H.3继承层次膨胀/H.4重试逻辑与并发状态耦合)。原§6.5.1文件系统作IPC条目迁移至此并新增PocketFlow来源的3条",
                "location": "附录H",
                "source": "PocketFlow C1-C3反模式资产组"
            },
            {
                "id": "PF-4",
                "type": "修正",
                "desc": "§1.4末尾新增对§9.9和§1.7的交叉引用；§1.6末尾新增对§1.7的交叉引用",
                "location": "§1.4/§1.6"
            },
            {
                "id": "PF-5",
                "type": "版本",
                "desc": "版本号升级v1.5.2→v1.5.3；日期更新→2026-06-18；版本头新增PocketFlow标注段落",
                "location": "版本头"
            }
        ],
        "reviewer_guidance": "所有新增节均为[Sp]推测级——方法论来源可追溯(PocketFlow三轮独立分析)，但应用于本框架的有效性待试跑验证。B1 §1.7的N=2证据仅为方向性指示；B2 §9.9的难度分级基于框架设计者单一视角；C1-C3附录H的4条反模式满足收录标准(≥2独立后端审查确认可迁移性)，但在本框架场景中的实际触发频率待观察。",
        "companion_md_section": "§14「v1.5.3 PocketFlow方法论转化A类资产写回（2026-06-18）」"
    })

    md['edit_history'] = edit_history

    # === 4. Add PocketFlow independent reviews ===
    independent_reviews = md.get('independent_reviews', [])
    independent_reviews.extend([
        {
            "reviewer": "DeepSeek-V4-Pro",
            "backend": "DeepSeek",
            "object": "PocketFlow R1审查",
            "role": "R1初始审查(作者侧)",
            "independence_level": "AUTHOR_SIDE",
            "scored": False,
            "verdict": "not_applicable",
            "date": "2026-06-16",
            "note": "作者侧审查，非独立——仅供后续独立审查参照。产出包括源码结构分析和方法论转化建议初稿"
        },
        {
            "reviewer": "ChatGPT-5.5",
            "backend": "GPT-5.5",
            "object": "PocketFlow R2审查",
            "role": "R2独立审查(Codex CLI)",
            "independence_level": "IND",
            "scored": True,
            "score": 5.5,
            "date": "2026-06-17",
            "verdict": "passed_with_revisions",
            "note": "独立后端+隔离上下文审查。确认B1/B2/C1-C3资产的可迁移性，指出需补充§1.7判定规则的具体性"
        },
        {
            "reviewer": "GLM-5.2",
            "backend": "GLM-5",
            "object": "PocketFlow R3审查",
            "role": "R3独立审查(ZCode CLI)",
            "independence_level": "SEMI",
            "scored": True,
            "score": 5.0,
            "date": "2026-06-18",
            "verdict": "passed_with_revisions",
            "note": "GLM-5.2自报但待确认(见memory/todo_verify_glm5_identity.md)。确认反模式H.2-H.4的可迁移性，建议补充正向替代规则——已执行"
        }
    ])
    md['independent_reviews'] = independent_reviews

    # === 5. Update mermaid_conversion (already mostly correct, minor update) ===
    if 'mermaid_conversion' not in md:
        md['mermaid_conversion'] = {
            "date": "2026-06-16",
            "blocks_count": 6,
            "sections": [
                "§1.2 完整生命周期视图 (flowchart TD)",
                "§3.2 闸门位置与触发条件 (flowchart TD)",
                "§3.7.4 规则退役流程 (stateDiagram-v2)",
                "§3.7.6 闭环策展决策树 (flowchart TD)",
                "§5.2 Loop工作模式 (flowchart TD)",
                "§6.3 模式选择决策树 (flowchart TD)"
            ],
            "reviewed_by": "ChatGPT-5.5 (Codex CLI, GPT-5.5)",
            "review_method": "方案审阅 + mermaid-cli实际渲染6图SVG + 忠实性抽查(图1+图5) + 结构完整性检查(14章+84围栏配对)",
            "issues_fixed": [
                "图4: LowFreq标签内英文双引号导致解析失败 → 改用「低频」",
                "图5: Guard1→Guard2→Guard3串行链暗示固定顺序 → GuardCheck单节点四分支并行分派"
            ],
            "principle": "选择性转换: 流程/决策/状态→Mermaid; 伪代码/表格/目录树→保留原样。此为展示格式变更，不改机制内容。"
        }

    # === 6. Add new top-level sections to JSON ===

    # §1.7: Framework architecture principle
    data['framework_architecture_principle'] = {
        "_section": "§1.7",
        "_added": "v1.5.3",
        "_evidence_level": "[Sp]",
        "_source": "PocketFlow B1资产 '最小核心+示例外挂架构', 经DeepSeek/ChatGPT-5.5/GLM-5.2三轮独立确认可迁移性 [PocketFlow方法论转化，2026-06-18]",
        "_comment": "框架自身的架构原则：定义核心(主文档强制规则)vs外挂(配套目录参考实现)的区分标准。防止两类根本性误用：把参考实现当强制规则，或把强制规则当可选附录跳过。",
        "core_definition": {
            "description": "主文档(本文件)——框架的canonical source of truth，不等于每句话都强制",
            "minimum_mandatory_core": [
                "七层+四跨层关切定义(§1.3速览表)",
                "强制启用清单(§1.4最低强制版列): S1-S4/HG-0/HG-1/HG-3/Workflow三模式/Dev Log单时间轴",
                "死亡判据(§1.5): 框架自身有效性的可测量判定标准",
                "闸门触发条件与决策规则(§3.2-§3.5)",
                "逃生口规则(§4.3+附录B): 工具/数据不可用时停，不用替代数据",
                "闭合条件与分档(§8+§8.8)",
                "可复现性/评估/会话交接的最低标准(§9)"
            ],
            "normative_reference": "[Sp]推测机制(§3.7.0/§9.7/§9.8)、模板附录A-G、变更记录§14、候选profile(§3.7.2.6)——在主文档中以便查阅，标注了证据等级和启用条件",
            "navigation_and_meta": "§9.9、§13、本文档元数据——辅助读者高效使用框架，不产生合规义务",
            "core_characteristic": "有合规牙齿——违反它会被框架的死亡判据或审查标准捕获。核心不回答'可以怎么做'，只回答'必须怎么做'和'什么情况下可以豁免'"
        },
        "external_plugins": {
            "description": "配套目录提供场景化的应用模板、参考实现和治理记录。不是强制规则——'这里有已验证的做法，你可以直接用、改、或参考后自己设计'",
            "directories": {
                "_reviews": {
                    "role": "独立审查报告与提示词存档",
                    "analogy": "审查类cookbook(如pocketflow-judge)",
                    "usage": "做独立审查时参考提示词结构和评分维度；不要求每个项目产出等量审查"
                },
                "_research": {
                    "role": "对标分析、版本草案、方法论研究",
                    "analogy": "设计文档类cookbook(如各cookbook的docs/design.md)",
                    "usage": "需要理解某条原则的'为什么'时查阅；不要求每个项目做同等深度的对标研究"
                },
                "_protocols-and-tools": {
                    "role": "协议包、执行手册、verify工具",
                    "analogy": "工具集成类cookbook(如pocketflow-mcp)",
                    "usage": "执行特定协议时按手册操作；不要求每个项目跑全部协议"
                },
                "_archive": {
                    "role": "旧版归档——被取代但保留供追溯",
                    "analogy": "N/A(框架治理特有)",
                    "usage": "查历史版本或旧审查结论时翻阅；日常不读"
                }
            },
            "plugin_characteristic": "无合规牙齿——跳过它不会触发死亡判据或导致审查FAIL。外挂的价值在于'别人踩过的坑你不用再踩'，而非'你必须这样踩'"
        },
        "distinction_rules": {
            "description": "三条判定规则决定一项内容应进入核心文档还是配套目录",
            "rules": [
                {
                    "criterion": "普遍性",
                    "core": "任何项目类型(量化/学术/工程/探索)都适用",
                    "external": "仅特定类型或特定阶段适用"
                },
                {
                    "criterion": "强制性",
                    "core": "不遵守会导致框架死亡判据触发或审查FAIL",
                    "external": "参考实现，不遵守仅损失效率而非合规"
                },
                {
                    "criterion": "稳定性",
                    "core": "跨版本稳定，修改需走HG-2(Spec变更闸门)",
                    "external": "可按需增删，新增/删除走Dev Log记录即可"
                }
            ],
            "boundary_default": "当一项内容无法确定该进核心还是外挂时，默认进外挂。理由：从外挂升级到核心只需一次编辑(且有HG-2闸门把关)，从核心移除到外挂则需要证明'之前的强制要求是错的'——成本不对称"
        },
        "anti_patterns": {
            "description": "防止四类根本性架构误用",
            "list": [
                {
                    "pattern": "核心膨胀",
                    "description": "把每个cookbook里的最佳实践都升级为核心规则——核心变百科全书，合规成本爆炸",
                    "prevention": "§1.4使用强度分档+§1.7核心vs外挂区分标准——两套机制共同防止单一主文档无限增长"
                },
                {
                    "pattern": "外挂遗忘",
                    "description": "有价值的参考实现沉在配套目录里，新读者不知道它们存在——'花了时间做但没人用'",
                    "prevention": "§9.9阅读导航在难度分层表中标注配套目录位置；§1.7在框架总览中说明配套目录结构"
                },
                {
                    "pattern": "核心虚无",
                    "description": "不敢把任何规则写进核心(因为怕'过度约束')——核心只剩目录，实际规则全在外挂(pocketflow-case-studies教训)",
                    "prevention": "死亡判据(§1.5)+最低强制启用清单(§1.4)——若核心为空，死亡判据因无对象可评估而自动触发"
                },
                {
                    "pattern": "外挂强制化",
                    "description": "配套目录的参考实现被认为'最佳实践====必须遵守'——外挂变相夺权，审查时被当作合规标准",
                    "prevention": "§1.7显式声明'无合规牙齿'+HG-2闸门限定合规范围仅限核心文档——外挂不进入审查rubric"
                }
            ]
        },
        "relationship_with_other_sections": {
            "§1.4_usage_tiers": "§1.4管用多少(使用强度分档)，§1.7管在哪找(核心vs外挂组织逻辑)。两者正交互补——§1.4回答'30%复杂度就能跑——是哪30%'，§1.7回答'那30%就在这份主文档里，其余70%在配套目录'",
            "§9.9_reading_navigation": "§1.7说明框架材料分布在主文档和4个配套目录，§9.9在此结构上叠加难度分层导航——§1.7管'在哪找'，§9.9管'从哪开始读'",
            "§1.6_open_items": "§1.7描述了框架材料自身的组织逻辑，其中配套目录_reviews/和_protocols-and-tools/的部分内容与OPEN-4(最低上手时间未测)直接相关"
        }
    }

    # §9.9: Reading navigation and difficulty stratification
    data['reading_navigation'] = {
        "_section": "§9.9",
        "_added": "v1.5.3",
        "_evidence_level": "[Sp]",
        "_source": "PocketFlow B2资产——cookbook难度分层体系(☆☆☆→★★★) [PocketFlow方法论转化，2026-06-18]",
        "_comment": "跨层关切——降低框架入门门槛，帮助不同背景的读者按难度梯度选择入口路径，而非被迫逐节通读。难度标注为[Sp]推测级，基于框架设计者单一视角，待读者反馈校准。",
        "difficulty_levels": {
            "☆☆☆_entry": {
                "meaning": "概念定义/清单类，可独立阅读，无前置依赖",
                "typical_reader": "无需AI协作经验"
            },
            "★☆☆_basic": {
                "meaning": "操作流程类，需理解AI协作基本流程",
                "typical_reader": "至少用AI辅助写过代码或文档"
            },
            "★★☆_advanced": {
                "meaning": "机制设计类，需实际项目经验支撑理解",
                "typical_reader": "至少完整跑过1个AI协作项目"
            },
            "★★★_expert": {
                "meaning": "方法论/元层次类，需方法论背景",
                "typical_reader": "理解框架自身的证据分类体系(§9.6)或等效训练"
            }
        },
        "chapter_difficulty_map": [
            {"chapter": "§1 框架总览", "difficulty": "☆☆☆", "type": "概念定义", "timing": "所有人最先读"},
            {"chapter": "§2 L0 Spec", "difficulty": "☆☆☆", "type": "清单/模板", "timing": "紧随§1，可直接套用"},
            {"chapter": "§3 L-H Human Gate", "difficulty": "★☆☆", "type": "操作流程", "timing": "开始第一个项目前"},
            {"chapter": "§4 L1 Prompt", "difficulty": "★☆☆", "type": "操作流程", "timing": "开始第一个项目前"},
            {"chapter": "§10 Dev Log", "difficulty": "★☆☆", "type": "操作流程", "timing": "可独立使用，随时查阅"},
            {"chapter": "§5 L2 Loop", "difficulty": "★★☆", "type": "机制设计", "timing": "跑完首个项目后精读"},
            {"chapter": "§6 L3 Workflow", "difficulty": "★★☆", "type": "机制设计", "timing": "需要多Agent编排时"},
            {"chapter": "§7 L4 Retrospect", "difficulty": "★★☆", "type": "机制设计", "timing": "项目至少完成一个里程碑后"},
            {"chapter": "§8 L5 Closure", "difficulty": "★★☆", "type": "机制设计", "timing": "项目收尾阶段"},
            {"chapter": "§9.1-9.5 操作性跨层关切", "difficulty": "★★☆", "type": "操作规范", "timing": "跑完首个项目后精读"},
            {"chapter": "§9.6-9.8 方法论跨层关切", "difficulty": "★★★", "type": "方法论/元层次", "timing": "理解基础工作流后精读"},
            {"chapter": "§9.9 阅读导航", "difficulty": "☆☆☆", "type": "导航工具", "timing": "任何人首次阅读框架前"},
            {"chapter": "§11 与现有系统集成", "difficulty": "★☆☆", "type": "概念对照", "timing": "按需查阅"},
            {"chapter": "§12 附录A-G(模板/清单)", "difficulty": "☆☆☆", "type": "模板/清单", "timing": "首次使用框架时直接套用"},
            {"chapter": "§12 附录H(反模式)+§13-14", "difficulty": "★★☆", "type": "反模式/对标/变更", "timing": "按需查阅"}
        ],
        "reading_paths": {
            "A_minimal_start": {
                "audience": "首次接触框架、想立刻开跑",
                "order": "§1 → §2 → 按需跳至目标章节",
                "estimated_time": "15-20 min"
            },
            "B_standard_practice": {
                "audience": "已有AI协作经验、想系统化",
                "order": "§1 → §2 → §3 → §4 → §10 → §5(轻量版) → §8.8(闭合分档)",
                "estimated_time": "45-60 min"
            },
            "C_full_methodology": {
                "audience": "方法论研究者、框架贡献者",
                "order": "逐章通读§1-§14，重点覆盖§9全系列(9.1-9.9)",
                "estimated_time": "2-3 h"
            }
        },
        "usage_notes": [
            "☆章节可速览：入门级章节以概念和清单为主——已熟悉AI协作概念的读者可速览§1后直接套用§2模板",
            "★☆章节建议实操后回读：基础操作流程的'真值'在跑过一个项目后才显现——首次阅读理解架构即可，完成后回读精进",
            "★★章节按需激活：进阶章节不必一口气读完——遇到对应场景时精读",
            "★★★章节是框架的'为什么'：跨层关切回答的不是'怎么做'而是'为什么这样设计'——不影响操作，但影响判断质量",
            "标注本身是[Sp]：难度分级基于框架设计者的单一视角——不同背景读者的感知可能差异显著。升级到[J]需收集≥3位不同背景读者的难度感知反馈"
        ],
        "upgrade_path": "[Sp]→[J]需: (a)收集≥3位不同背景读者的反馈; (b)将感知难度与标注对照; (c)若≥2位读者对同一章节的感知偏差≥2级，启动重标",
        "relationship": {
            "§1.4_usage_tiers": "§1.4 A/B/C三档定义框架本身用多少(使用强度)，本节三条路径定义从哪开始读(阅读顺序)。两者正交——C档用户可从路径A开始阅读",
            "§1.7_core_vs_plugin": "§1.7说明框架材料分布在主文档(核心)和4个配套目录(外挂)，本节在此结构上叠加难度分层导航——§1.7管'在哪找'，§9.9管'从哪开始读'"
        }
    }

    # Appendix H: Anti-patterns list
    data['anti_patterns_catalog'] = {
        "_section": "附录H",
        "_added": "v1.5.3",
        "_evidence_level": "[Sp]",
        "_source": "PocketFlow C1-C3反模式资产组 + Small_Scale H.1(原§6.5.1迁移) [PocketFlow方法论转化，2026-06-18]",
        "_comment": "反模式是经独立审查确认可迁移性的'不要这样做'的教训——案例事实和可迁移性经≥2个独立后端审查确认，但在本框架中的触发频率和治理收益仍为[Sp]待试跑验证。收录标准：(1)有具体项目案例(非假设); (2)经≥2个独立后端审查确认可迁移性; (3)有可操作的正向替代规则。",
        "usage": "在Spec设计(L0)、实现(L2)、编排(L3)等阶段，对照本清单做一次快速自检——'我是否正在重蹈其中某条反模式？'如匹配，按对应规则修正。",
        "entries": [
            {
                "id": "H.1",
                "name": "文件系统作IPC",
                "case": "Small_Scale仓库使用gen_id.txt文件作为推理脚本→评估脚本的进程间通信通道",
                "consequences": [
                    "竞态: 两个推理运行同时写→只有一个路径被保留，另一个静默丢失",
                    "原子性: 部分写入=损坏路径，读取方拿到残缺数据",
                    "一致性: 5个推理脚本中仅3个实际写入此协议，其余2个不参与"
                ],
                "rule": "即使是'只传递一个路径'，也应该用CLI参数、stdout或pipe，而非文件系统。如果必须用文件，至少需要：原子写入(write-then-rename)+唯一文件名(含timestamp/pid)+读取方校验文件完整性",
                "source": "Small_Scale分析，2026-06-13",
                "applicable_layers": ["L2 (Loop)", "L3 (Workflow)"],
                "severity": "中——单线程场景可能不暴露，并发时静默出错，调试困难",
                "evidence": "[S] 源码直接验证"
            },
            {
                "id": "H.2",
                "name": "极简主义的隐性成本",
                "case": "PocketFlow以'零依赖'为设计目标，拒绝提供LLM wrapper/embedding工具/search接口等参考实现。结果每个用户在各自项目中重复实现这些基础组件",
                "consequences": [
                    "重复劳动: N个用户=N套LLM wrapper，每套独立调试相同的连接/重试/超时问题",
                    "标准化缺失: 无统一接口契约→组件互换困难→生态碎片化，用户无法共享改进",
                    "安全不统一: API key管理/错误重试/超时处理等最佳实践靠个体自觉，缺乏基线保障",
                    "隐性成本转移: '零依赖'把集成成本从库作者转移给了每个用户——总成本(N×个人成本)远高于作者提供一次参考实现的成本"
                ],
                "rule": "提供参考实现的同时允许替换，比完全不留实现更好。不为'极简'牺牲正确性和可用性。参考实现应满足三条：(a)标注为'可替换'而非'必须使用'，降低锁定感；(b)暴露清晰接口契约，使替换有据可依；(c)至少覆盖80%用户的常见路径",
                "source": "PocketFlow方法论转化，2026-06-18",
                "applicable_layers": ["L0 (Spec/设计哲学)", "L1 (Prompt/设计约束)"],
                "severity": "中——不阻断功能，但系统性推高生态总成本，长期抑制社区贡献",
                "evidence": "[Sp] 案例事实成立但外推到其他项目的频率未验证"
            },
            {
                "id": "H.3",
                "name": "继承层次膨胀",
                "case": "PocketFlow用12个类实现sync/async×batch/parallel×node/flow的笛卡尔积。每新增一个正交维度(如streaming/distributed)，类数量将翻倍——3个维度=24个类，4个维度=48个类",
                "consequences": [
                    "类爆炸: N个正交维度→2^N个类，维护成本指数增长",
                    "代码重复: 每个组合类重复实现相似的协调逻辑",
                    "扩展阻力: 新增一个维度需触碰所有已有组合——修改面大，容易遗漏",
                    "测试负担: 每个组合类需要独立测试，但测试场景高度重叠"
                ],
                "rule": "正交维度优先用组合(composition)而非继承(inheritance)。判断标准：如果一个类的命名包含≥2个独立维度的形容词(如Async+Parallel+Batch)，应拆分为可组合的独立组件——async/sync是一个mixin或wrapper，batch/parallel是另一个独立的执行策略对象，两者通过组合而非继承协作",
                "source": "PocketFlow方法论转化，2026-06-18",
                "applicable_layers": ["L0 (Spec/架构约定)", "L2 (Loop/实现)"],
                "severity": "高——随维度增长持续恶化，修复成本随已有代码量累积，且新增维度的边际成本递增",
                "evidence": "[S] PocketFlow源码直接验证 + [J] 迁移性经2后端独立确认"
            },
            {
                "id": "H.4",
                "name": "重试逻辑与并发状态耦合",
                "case": "PocketFlow的AsyncParallelBatchNode将重试计数器self.cur_retry存为实例字段，被多个并发协程(通过asyncio.gather)共享读写",
                "consequences": [
                    "竞态条件: 并发访问共享可变状态→重试计数错乱",
                    "正确性失效: '最多重试N次'的保证在并发下不可证——单线程测试全部通过，生产并发才暴露",
                    "调试困难: 竞态非确定性→问题难以复现(可能100次才出现1次)",
                    "隐蔽性: 不正确的行为(重试被跳过或超额重试)不产生error/log，静默破坏语义"
                ],
                "rule": "执行状态(重试计数、中间结果、进度标记、临时缓存)应为局部变量或栈变量，不存实例字段。实例字段仅存配置(初始化参数、阈值、开关、连接池)。判断标准：如果一个字段的值在单次执行过程中会变化，且多个执行单元可能并发访问同一实例——它就是执行状态，必须局部化",
                "source": "PocketFlow方法论转化，2026-06-18",
                "applicable_layers": ["L2 (Loop/并发实现)"],
                "severity": "高——并发下静默破坏正确性保证，单线程测试不可检测，属最难排查的缺陷类别",
                "evidence": "[S] PocketFlow源码直接验证 + [J] 迁移性经2后端独立确认"
            }
        ],
        "expansion_reserved": "当前收录4条反模式。已知候选(待≥2个项目验证共性后入库)：§3.7.4.1自适应权重淘汰中的'静态规则腐化'反模式思想(来自Evolver项目，[Sp]待试跑验证)。未来项目分析产出的新反模式按上方收录标准评审后追加。"
    }

    # === 7. Add changelog entries for v1.5.2 and v1.5.3 ===
    changelog = data.get('changelog', {})

    changelog['v1_5_2'] = {
        "date": "2026-06-16",
        "title": "Protocol 3试跑1回写",
        "trigger": "首次真实试跑'方法论提取方法论'项目闭合(M-tier, 闭合时14/20 loops, Phase 8 Kimi核查后修正为闭合后15/20, 累计58项发现, 0 CRITICAL/MAJOR遗留). 试跑Retrospect与Phase 7系列审查提出6项Protocol 3改进",
        "changes": [
            {
                "id": "P3-0",
                "change": "版本头与文档状态更新为v1.5.2 'Protocol 3试跑1回写'",
                "source": "Protocol 3试跑1反馈(2026-06-16)",
                "type": "状态更新"
            },
            {
                "id": "P3-1",
                "change": "C1/C5增加可操作测量方法：C1以DEV_LOG HH:MM时间戳计loop耗时；C5维护'框架操作耗时'计数器；首次试跑未完整计时标注为预期内基线问题",
                "source": "同上",
                "type": "修正"
            },
            {
                "id": "P3-2",
                "change": "HG-0双检查点——Plan阶段(审查项目计划)+Spec阶段(审查Spec)，不是只审写完的Spec",
                "source": "同上",
                "type": "新增"
            },
            {
                "id": "P3-3",
                "change": "独立审查频率适应性上调——若项目含≥3概念判断Phase或方法论/概念归类或前期MAJOR密度>3/Phase，可从闭合前一次上调为每Phase后一次",
                "source": "同上",
                "type": "新增"
            },
            {
                "id": "P3-4",
                "change": "HG交互留存要求——每次HG触发时DEV_LOG须记录三项证据(人工响应时间戳/响应内容摘要/AI是否如实传达选项)",
                "source": "同上",
                "type": "新增"
            },
            {
                "id": "P3-5",
                "change": "C8≥2轮异后端审查建议写入审查编排规则",
                "source": "同上",
                "type": "新增"
            },
            {
                "id": "P3-6",
                "change": "S档Protocol 3适配备注——C6降为'≥1失效或≥1意外'，C8降为'1轮异后端审查≥6.0/10'，标注为待S档试跑验证",
                "source": "同上",
                "type": "备注"
            },
            {
                "id": "P3-7",
                "change": "深度版Retrospect模板新增'Protocol 3/框架层反馈'项，显式记录C1-C8裁决、证据缺口、HG/审查频率教训",
                "source": "同上",
                "type": "强化"
            }
        ],
        "sync_note": "本次仅修改主文档.md。.json与.docx尚未同步。",
        "methodology_source": "方法论提取方法论项目(Protocol 3首次试跑)"
    }

    changelog['v1_5_3'] = {
        "date": "2026-06-18",
        "title": "PocketFlow方法论转化A类资产写回",
        "trigger": "PocketFlow三轮独立分析(DeepSeek-V4-Pro R1 + ChatGPT-5.5 R2 + GLM-5.2 R3, 2026-06-16~18)产出的A类资产——可直接写回框架的方法论改进，无需额外验证实验. 共3项A类资产(B2/B1/C1-C3)，经三个并行agent独立规划后统一执行写回",
        "source_document": "<POCKETFLOW_PROJECT>/Methodology_Asset_Conversion.md §8.5汇总表",
        "changes": [
            {
                "id": "PF-1",
                "change": "新增§1.7「框架自身的架构原则：最小核心+示例外挂」——定义核心vs外挂的区分标准(普遍性/强制性/稳定性三条判定规则)+4种反模式警示+边界案例默认进外挂原则",
                "source": "PocketFlow B1资产——'最小核心+示例外挂架构'",
                "type": "新增",
                "evidence": "[Sp]"
            },
            {
                "id": "PF-2",
                "change": "新增§9.9「阅读导航与难度分层」——按☆☆☆/★☆☆/★★☆/★★★标注11个章节难度+3条推荐阅读路径(A最小启动/B标准实践/C完整方法论)+使用说明5条",
                "source": "PocketFlow B2资产——cookbook难度分层体系",
                "type": "新增",
                "evidence": "[Sp]"
            },
            {
                "id": "PF-3",
                "change": "新增「附录H:反模式清单」——集中收纳4条反模式(H.1文件系统作IPC已从§6.5.1迁移+H.2极简主义的隐性成本+H.3继承层次膨胀+H.4重试逻辑与并发状态耦合). 原§6.5.1改为交叉引用",
                "source": "PocketFlow C1-C3反模式资产组 + Small_Scale H.1(原§6.5.1迁移)",
                "type": "新增+重组",
                "evidence": "[S]+[J]"
            },
            {
                "id": "PF-4",
                "change": "§1.4末尾新增对§9.9和§1.7的交叉引用；§1.6末尾新增对§1.7的交叉引用",
                "source": "ALL",
                "type": "维护"
            },
            {
                "id": "PF-5",
                "change": "版本头更新：v1.5.2→v1.5.3；日期→2026-06-18；新增「PocketFlow方法论转化A类资产写回」标注段落",
                "source": "ALL",
                "type": "版本"
            }
        ],
        "evidence_note": "所有新增节均为[Sp]推测级——方法论来源可追溯(PocketFlow三轮独立分析)，但应用于本框架的有效性待试跑验证. B1 §1.7的N=2证据仅为方向性指示; B2 §9.9的难度分级基于框架设计者单一视角; C1-C3附录H的4条反模式满足收录标准(≥2独立后端审查确认可迁移性)，但在本框架场景中的实际触发频率待观察",
        "sync_note": "本次仅修改主文档.md。.json与.docx于2026-06-18同步(本脚本执行全量三件套同步)。",
        "methodology_source": "PocketFlow三轮独立分析(DeepSeek/ChatGPT-5.5/GLM-5.2)"
    }

    data['changelog'] = changelog

    # === 8. Update provenance_notes ===
    data['provenance_notes']['pocketflow_v1_5_3'] = (
        "[Sp] v1.5.3新增三节(§1.7/§9.9/附录H)的思想源于PocketFlow项目"
        "(<POCKETFLOW_PROJECT>/)的三轮独立分析. "
        "B1(最小核心+示例外挂)和B2(难度分层)的可迁移性经DeepSeek/ChatGPT-5.5/GLM-5.2三方确认; "
        "反模式H.2-H.4的案例事实经源码直接验证[S]，可迁移性经≥2后端确认[J]. "
        "但在本框架场景中的行为有效性/读者反馈/反模式触发频率均待试跑验证. "
        "PocketFlow分析报告和Methodology_Asset_Conversion.md存在于PocketFlow-analysis目录下."
    )

    # === 9. Update status in various places ===
    # Update evidence_classification self_application_status
    if 'evidence_classification' in data:
        data['evidence_classification']['self_application_status'] = (
            "[J] v1.5+v1.5.1+v1.5.3新增章节的证据类型标注基于作者判断, "
            "未经独立审查者逐条校准. v1.5.1四节经Codex ChatGPT-5.5 R4审查(7.2/10)验证了结构合理性"
            "但行为有效性仍为[Sp]. v1.5.3三节(§1.7/§9.9/附录H)均标注[Sp]待试跑验证."
        )

    # Update the framework_self_governance to remove stale freeze references
    if 'framework_self_governance' in data:
        data['framework_self_governance']['open_items_update_v1_5_2'] = (
            "v1.5.2: OPEN-2状态更新为'部分验证'——预登记载体已建立(框架级成熟度评估表), "
            "Protocol 3首次试跑已回写为第一条真实基线, 但死亡判据仍需连续项目数据才可触发"
        )

    # === 10. Write updated JSON and VERSION ===
    save_json(data)
    print(f"JSON updated successfully. Output: {JSON_PATH}")

    # Write VERSION file
    version = md['version']
    with open(VERSION_PATH, 'w', encoding='utf-8') as f:
        f.write(version + '\n')
    print(f"VERSION updated: {version}")

    # Verify
    data2 = load_json()
    print(f"\nVerification:")
    print(f"  version: {data2['metadata']['version']}")
    print(f"  date: {data2['metadata']['date']}")
    print(f"  edit_history entries: {len(data2['metadata'].get('edit_history', []))}")
    print(f"  independent_reviews entries: {len(data2['metadata'].get('independent_reviews', []))}")
    print(f"  changelog keys: {list(data2.get('changelog', {}).keys())}")
    print(f"  framework_architecture_principle: {'present' if 'framework_architecture_principle' in data2 else 'MISSING'}")
    print(f"  reading_navigation: {'present' if 'reading_navigation' in data2 else 'MISSING'}")
    print(f"  anti_patterns_catalog: {'present' if 'anti_patterns_catalog' in data2 else 'MISSING'}")
    print(f"  frozen: {data2['metadata'].get('freeze_status', {}).get('frozen')}")

if __name__ == '__main__':
    main()

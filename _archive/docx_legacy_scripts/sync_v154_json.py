#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync AI协作项目全生命周期框架.json to v1.5.4 — prompt-tdd A2 experiment writeback.

Minimal targeted update: bump metadata fields + add §4.1.1 structural node.
Run: PYTHONIOENCODING=utf-8 python _workflows/sync_v154_json.py
"""

import json
import os
import sys

JSON_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.json"
BACKUP_PATH = "<PROJECT_ROOT>/AI协作项目全生命周期框架.json.v153.backup"

def load_json():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, path=None):
    target = path or JSON_PATH
    with open(target, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    # Backup first
    data = load_json()
    save_json(data, BACKUP_PATH)
    print(f"Backup saved to: {BACKUP_PATH}")

    md = data['metadata']

    # === 1. Core metadata ===
    md['version'] = "1.5.4"
    md['date'] = "2026-06-19"
    md['revision'] = "v1.5.4 (2026-06-19)"
    md['revision_source'] = (
        "prompt-tdd A2实验写回(PF-8: prep/exec/post [E-]) + "
        "PocketFlow三轮独立分析(A类资产写回) + "
        "Evolver项目分析(Protocol 3试跑1回写) + "
        "GitNexus分析项目 + Small_Scale项目分析 + ChatGPT-5.5独立审查"
    )

    # === 2. Status ===
    md['status'] = (
        "草案, v1.5.4 (prompt-tdd A2实验写回§4.1.1[E-] + PocketFlow A类资产). "
        "v1.5.4新增: §4.1.1执行合约——prep/exec/post vs 一体式编号列表对照实验证据[E-]. "
        "v1.5.3新增: §1.7(最小核心+示例外挂)+§9.9(阅读导航与难度分层)+附录H(反模式清单). "
        "v1.5.2写回: Protocol 3试跑1的6项改进(C1/C5测量方法/HG-0双检查点/审查频率适应性上调/"
        "HG交互留存/C8≥2轮异后端建议/S-tier降级阈值备注). "
        "v1.5.1新增: §3.7.0(事件流健康度监测[Sp])+§3.7.4.1(自适应权重淘汰[Sp])"
        "+§9.7(经验注入上下文预算规则[Sp])+§9.8(研究经验对象REO[Sp]). "
        "方法论来源=Evolver项目分析(arXiv:2604.15097,综合评分4.1-4.2/10,四轮独立审查跨三个后端)"
        "+PocketFlow三轮独立分析(DeepSeek-V4-Pro/ChatGPT-5.5/GLM-5.2)"
        "+prompt-tdd A2 Tier 1对照实验(GPT-5.5,temp=0,n=24/臂,6轮独立审查). "
        "v1.5.1草案经Codex ChatGPT-5.5 R3→R4审查(R3驳回4.3→R4修改后通过7.2/10, Δ+2.9). "
        "v1.5新增: §6.2模式8/9+§9.2+§9.6, 经ChatGPT-5.5审查C+(5.43/10). "
        "v1.4新增: §3.7.2.6/§5.3.1/§6.5.1/§9.1/§1.5/§9.4/附录H(已取消), "
        "经三轮审查(ChatGPT-5.5 5.50+5.37+Kimi-K2.7-Code 5.00). "
        "审查独立性: [SEMI]——后端不同但提示词由作者撰写. "
        "仍待验证: 四个[Sp]节的行为有效性; §9.7 A/B测试; REO Phase 0-3实施; "
        "S-tier Protocol 3降级阈值; §1.7/§9.9/附录H的读者验证; §4.1.1多域/多模型复现."
    )

    md['status_note'] = (
        "草案冻结已解除(Protocol 3试跑1 Retrospect完成, 条件满足). "
        "v1.5.4写回prompt-tdd A2实验(PF-8: prep/exec/post [E-]→§4.1.1). "
        "v1.5.3写回PocketFlow A类资产(3项: §1.7+§9.9+附录H). "
        "v1.5.2写回Protocol 3试跑1反馈(6项改进). "
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
        "v1.5.4新增§4.1.1执行合约——prompt-tdd A2对照实验证据[E-]: "
        "prep/exec/post分段未证实优于一体式编号列表(代码审查域,GPT-5.5,n=24/臂). "
        "方法论来源=Evolver项目分析(GitNexus→Small_Scale→PilotDeck→Evolver四项目链)"
        "+PocketFlow三轮独立分析+prompt-tdd A2 Tier 1对照实验. "
        "基于ETF项目V3.6代码头部注释实践提炼."
    )

    # === 3. derived_from ===
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
        "PocketFlow三轮独立分析(2026-06-16~18: DeepSeek-V4-Pro/ChatGPT-5.5/GLM-5.2, 方法论提取A类资产3项→框架v1.5.3三节)",
        "prompt-tdd A2 Tier 1对照实验(2026-06-19: prep/exec/post vs 一体式编号列表, GPT-5.5 temp=0, n=24/臂, 6轮独立审查, PF-8→框架v1.5.4 §4.1.1 [E-])"
    ]

    # === 4. freeze_status note ===
    if 'freeze_status' in md:
        md['freeze_status']['unfreeze_reason'] = (
            "Protocol 3试跑1 Retrospect完成, 满足解除条件. "
            "v1.5.2为试跑回写版, v1.5.3为PocketFlow A类资产写回版, "
            "v1.5.4为prompt-tdd A2实验写回版."
        )
        if 'note_json_sync' in md.get('freeze_status', {}):
            md['freeze_status']['note_json_sync'] = (
                "R4审查指出的'json停v1.4'问题在v1.5.1时已同步修复. "
                "v1.5.3全域同步: 包括v1.5.2(Protocol 3试跑1回写)和v1.5.3(PocketFlow A类资产写回). "
                "v1.5.4同步: prompt-tdd A2实验写回(§4.1.1 [E-]). "
                "2026-06-16: 6处ASCII图→Mermaid(F12), json同步补edit_history+rendering元数据. "
                "2026-06-18: 三件套全量同步至v1.5.3. "
                "2026-06-19: json同步至v1.5.4."
            )

    # === 5. Edit history ===
    edit_history = md.get('edit_history', [])
    edit_history.append({
        "date": "2026-06-19",
        "editor_model": "DeepSeek-v4-pro",
        "editor_cli": "Claude Code CLI shell",
        "editor_house": "Claude house",
        "editor_role": "编辑者（框架作者，自编辑）",
        "independence_level": "[SELF]",
        "independence_note": (
            "作者自编辑，基于prompt-tdd A2 Tier 1对照实验完成（prep/exec/post vs 一体式编号列表，"
            "GPT-5.5 temp=0, n=24/臂，6轮异后端独立审查通过）。"
            "实验结果为阴性——H1不被支持，科学门全部FAIL。"
            "PF-8资产状态从留白[Sp]更新为[E-]（单域实验不支持），写入§4.1.1执行合约。"
            "待A3/A1实验积累多域证据后重新评估。"
        ),
        "scope": (
            "prompt-tdd A2实验写回——非新增机制，而是对§4.1的实证补充："
            "记录prep/exec/post分段prompt在特定条件下未证实优于一体式编号列表的具体证据"
        ),
        "changes": [
            {
                "id": "PF-8",
                "type": "实证记录",
                "desc": (
                    "A2资产状态更新——prep/exec/post三阶段分段prompt，在代码审查域、"
                    "GPT-5.5条件下未被证实优于一体式编号列表。在框架中诚实记录为[E-]"
                    "（单域实验不支持），替代此前留白的[Sp]"
                ),
                "location": "§4.1.1"
            }
        ]
    })

    # === 6. Add §4.1.1 node to chapter 4 structure ===
    # Find chapter 4 in the structure
    sections = data.get('sections', data.get('chapters', data.get('structure', [])))

    def find_and_update_ch4(nodes, path=""):
        """Recursively find chapter 4 and add §4.1.1."""
        if not isinstance(nodes, list):
            return False
        for i, node in enumerate(nodes):
            if isinstance(node, dict):
                title = node.get('title', '')
                num = node.get('number', '')
                # Match chapter 4
                if '4.' in str(num) or '# 4.' in title or 'L1: Prompt' in title or '4. L1' in title:
                    children = node.get('children', node.get('sections', []))
                    # Find §4.1 within chapter 4
                    for j, child in enumerate(children):
                        if isinstance(child, dict):
                            c_title = child.get('title', '')
                            c_num = child.get('number', '')
                            if '4.1' in str(c_num) or '4.1' in c_title or '定义' in c_title:
                                # Add §4.1.1 after §4.1
                                sub_children = child.get('children', child.get('subsections', []))
                                node_411 = {
                                    "number": "4.1.1",
                                    "title": "4.1.1 执行合约：结构化prompt的对照证据",
                                    "evidence_level": "[E-]",
                                    "evidence_note": "单域实验不支持",
                                    "source": "prompt-tdd A2 Tier 1对照实验（PocketFlow §8.1 A2转化）",
                                    "date": "2026-06-19",
                                    "content_summary": (
                                        "prep/exec/post三阶段分段prompt vs 一体式编号列表prompt的对照实验证据。"
                                        "H1不被支持（A_flat 0.954 ≥ B_structured 0.935）。"
                                        "4道科学门全部FAIL。框架含义：更多结构≠更好效果；"
                                        "天花板效应警示；反例价值——防止将三阶段分段作为通用最佳实践。"
                                    ),
                                    "limitations": [
                                        "单域（代码审查）",
                                        "单模型（GPT-5.5 temp=0）",
                                        "双LLM评分者无人类ground truth",
                                        "n=24仅满足sign test最小功效",
                                        "残余混淆（A组编号列表本身已是轻量结构化）",
                                        "κ因天花板效应退化至不可解释"
                                    ],
                                    "experiment_report": (
                                        "<PROMPT_TDD_PROJECT>/tests/pocketflow_assets/"
                                        "a2_prep_exec_post/experiment_report_tier1.md + .json"
                                    ),
                                    "cross_references": [
                                        "§6.3 模式选择决策树（不做过度工程化）",
                                        "PT-M1 天花板效应检测",
                                        "PT-M8 工程门/科学门分离"
                                    ]
                                }
                                sub_children.append(node_411)
                                child['subsections'] = sub_children
                                child['children'] = sub_children  # keep both keys
                                return True
                    return False
                # Recurse into children
                if find_and_update_ch4(node.get('children', node.get('sections', [])), path + '/' + str(i)):
                    return True
        return False

    found = find_and_update_ch4(sections)
    if not found:
        print("WARNING: Could not locate §4.1 in JSON structure. §4.1.1 node was NOT added to structure.")
        print("This is OK — the section exists in the .md source of truth. "
              "Next full sync_trio run will add it.")
    else:
        print("§4.1.1 node added to JSON structure under Chapter 4.")

    # === 7. Update changelog ===
    changelog = md.get('changelog', [])
    changelog.append({
        "version": "v1.5.4",
        "date": "2026-06-19",
        "trigger": "prompt-tdd A2 Tier 1对照实验完成（DeepSeek-V4-Pro via Claude Code CLI）",
        "summary": (
            "PF-8资产写回——prep/exec/post三阶段分段prompt在代码审查域、GPT-5.5(temp=0)、"
            "n=24/臂条件下，未证实优于内容等价的一体式编号列表prompt。"
            "H1不被支持（A_flat 0.954 ≥ B_structured 0.935）。"
            "4道科学门全部FAIL。6轮异后端独立审查通过，0未闭合发现。"
        ),
        "changes": [
            {
                "id": "PF-8",
                "type": "实证记录",
                "desc": "A2资产状态更新——prep/exec/post [Sp]→[E-]（单域实验不支持）",
                "location": "§4.1.1"
            }
        ],
        "evidence_level": "[E-]（单域实验不支持）",
        "three_piece_sync": "2026-06-19: .md已更新, .json已同步, .docx待重新生成",
        "limitations": [
            "单域（代码审查）",
            "单模型（GPT-5.5 temp=0）",
            "双LLM评分者无人类ground truth",
            "n=24仅满足sign test最小功效",
            "残余混淆（A组编号列表本身已是轻量结构化）"
        ]
    })
    md['changelog'] = changelog

    # === 8. Update companion_reviews ===
    md['companion_reviews'].append({
        "file": "<PROMPT_TDD_PROJECT>/reviews/",
        "status": "external",
        "relevant_version": "v1.5.4",
        "note": "prompt-tdd A2实验的6轮独立审查（R1 Codex+ZCode / R2 Codex / R3 Qwen / R4 Codex / R5 Codex / R6 Qwen），非框架自身的审查"
    })

    # Save
    save_json(data)
    print(f"JSON updated to v1.5.4: {JSON_PATH}")
    print("Done. Changes: version, date, revision, status, status_note, description,")
    print("  derived_from, freeze_status, edit_history, changelog, companion_reviews, §4.1.1 node")

if __name__ == '__main__':
    main()

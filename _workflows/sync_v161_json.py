#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync AI协作项目全生命周期框架.json v1.6 → v1.6.1 — A2 Qwen cross-model replication writeback.

Targeted update: metadata + status + changelog + version_timeline + reviews + known_limitations.
Run: PYTHONIOENCODING=utf-8 python _workflows/sync_v161_json.py
"""

import json
import os
import sys

JSON_PATH = "./AI协作项目全生命周期框架.json"
BACKUP_PATH = "./AI协作项目全生命周期框架.json.v16.backup"

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
    md['version'] = "1.6.1"
    md['date'] = "2026-06-20"
    md['model'] = "DeepSeek-V4-Pro (via Claude Code CLI shell)"
    md['revision'] = "v1.6.1 (2026-06-20)"
    md['revision_source'] = (
        "v1.6 Minor升级(A2+A3深度复盘 + Codex v1.5.5交叉验证 + "
        "prompt-tdd A2+A3实验写回 + 跨版本维护实践规范化 + "
        "PocketFlow三轮独立分析 + Evolver/GitNexus/Small_Scale项目分析) + "
        "v1.6.1 Patch升级(A2 Qwen qwen3.7-max跨模型复现写回——首次跨模型方向一致复现, "
        "证据二维M0→M2, Codex GPT-5.5单评分者盲评Δ=−0.014)"
    )

    # === 2. Status ===
    md['status'] = (
        "草案, v1.6.1 (v1.6证据体系升级+维护性增强 + v1.6.1 A2 Qwen跨模型复现写回). "
        "v1.6.1新增: §4.1.1 Qwen复现段落(A_flat=0.806/B_structured=0.792/Δ=−0.014, "
        "方向一致, GPT-5.5+Qwen双模型点证据, 证据二维M0→M2) + "
        "§1.8局限声明更新(跨模型复现反映) + §6.3.1交叉引用更新 + §9.6.1 A2行M0→M2. "
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
        "v1.6.1经Codex GPT-5.5交叉验证(FAIL_WITH_CAVEATS, 0 MAJOR + 5 MEDIUM/MINOR)→修正. "
        "审查独立性: [SEMI]——后端不同但提示词由作者撰写."
    )

    md['status_note'] = (
        "草案冻结已解除(Protocol 3试跑1 Retrospect完成, 条件满足). "
        "v1.6.1写回prompt-tdd A2 Qwen跨模型复现(PF-8扩展: Qwen复现[E-]→§4.1.1, 证据二维M0→M2). "
        "v1.6写回A2+A3深度复盘(P0证据体系升级+P1维护性增强). "
        "v1.5.5写回prompt-tdd A3实验(PF-9: Action Routing [E-]→§6.3.1). "
        "v1.5.4写回prompt-tdd A2实验(PF-8: prep/exec/post [E-]→§4.1.1). "
        "v1.5.3写回PocketFlow A类资产(3项: §1.7+§9.9+附录H). "
        "v1.5.2写回Protocol 3试跑1反馈(6项改进). "
        "仍待多项目验证. "
        "v1.5.1新增: §3.7.0事件流健康度监测[Sp]+§3.7.4.1自适应权重淘汰[Sp]+"
        "§9.7经验注入上下文预算规则[Sp]+§9.8研究经验对象(REO)[Sp]. "
        "方法论来源=Evolver项目分析(arXiv:2604.15097,综合评分4.1-4.2/10,四轮独立审查跨三个后端). "
        "完整规格见_research/框架v1.5.1_新增节草案.md. "
        "v1.5新增: §6.2模式8/9+§9.2+§9.6. "
        "v1.4新增: §3.7.2.6/§5.3.1/§6.2/§6.5.1/§9.1/§1.5/§9.4/附录H. "
        "v1.3遗留OPEN-1~4状态不变(OPEN-5已于v1.5.1冻结期关闭→§8.8). "
        "v1.3新增§3.7漂移检测层(五类信号+告警聚合+规则退役+宪法审计+闭环策展+监测模板)"
        "——将OPEN-1从候选草案升级为正式操作化方案. "
        "经ChatGPT-5.5独立审查全件(加权6.1/10,修改后通过), 10项修订已执行. "
        "21个决策点已拍板, 但Dev Log 7/10组件待实证、框架整体已经1次真实试跑(Protocol 3)."
    )

    # === 3. Changelog — prepend v1.6.1 entry ===
    v161_changelog = {
        "version": "v1.6.1",
        "date": "2026-06-20",
        "type": "Patch",
        "trigger": (
            "A2 Qwen qwen3.7-max跨模型复现完成——48/48收集成功, "
            "Codex GPT-5.5单评分者盲评: A_flat=0.806, B_structured=0.792, Δ=−0.014, "
            "方向与GPT-5.5原实验一致(A ≥ B, H1不被支持), "
            "首次跨模型方向一致复现, 证据二维M0→M2"
        ),
        "summary": (
            "v1.6.1 Patch升级——A2 Qwen跨模型复现写回. "
            "§4.1.1新增复现段落(含限制声明) + §1.8局限声明更新 + "
            "§6.3.1交叉引用更新 + §9.6.1 A2证据二维M0→M2. "
            "经Codex GPT-5.5交叉验证(FAIL_WITH_CAVEATS, 0 MAJOR + 5 MEDIUM/MINOR)→修正."
        ),
        "changes": [
            {"id": "v1.6.1-1", "type": "扩展", "desc": "§4.1.1新增Qwen跨模型复现段落——A_flat=0.806/B_structured=0.792/Δ=−0.014, 首次跨模型方向一致复现, 含完整限制声明", "location": "§4.1.1"},
            {"id": "v1.6.1-2", "type": "修订", "desc": "§1.8局限声明更新——A2跨模型复现反映, A2+A3跨任务一致性范围澄清", "location": "§1.8"},
            {"id": "v1.6.1-3", "type": "修订", "desc": "§6.3.1交叉引用更新——A2 Qwen复现状态反映", "location": "§6.3.1"},
            {"id": "v1.6.1-4", "type": "修订", "desc": "§9.6.1 A2行证据二维M0→M2(跨2模型家族验证)", "location": "§9.6.1"},
            {"id": "v1.6.1-5", "type": "修订", "desc": "§14标题与版本时间线更新至v1.6.1", "location": "§14"},
            {"id": "v1.6.1-6", "type": "修订", "desc": "版本头v1.6→v1.6.1 + 文末状态行更新", "location": "版本头/文末"},
        ],
        "evidence_level": "[B+/M2]——Qwen复现48/48收集+Codex盲评, GPT-5.5+Qwen双模型家族",
        "codex_reviews": [
            "Codex GPT-5.5交叉验证(FAIL_WITH_CAVEATS, 0 MAJOR + 3 Moderate + 2 Minor)→全量修正",
        ],
        "three_piece_sync": "2026-06-20: .md✅ v1.6.1 / .json🔄 本次同步 / .docx⏳ 待生成",
    }
    md['changelog'].insert(0, v161_changelog)

    # Update v1.6 changelog entry's three_piece_sync
    if md['changelog'][1]['version'] == 'v1.6':
        md['changelog'][1]['three_piece_sync'] = (
            "2026-06-20: .md已更新(v1.6→v1.6.1); .json已同步至v1.6后更新至v1.6.1; .docx已生成v1.6待更新至v1.6.1"
        )

    # === 4. Version timeline — append v1.6.1 row ===
    if 'version_timeline' not in md:
        md['version_timeline'] = []
    md['version_timeline'].append({
        "date": "2026-06-20",
        "version": "v1.6.1",
        "event": "Patch升级: A2 Qwen qwen3.7-max跨模型复现写回——§4.1.1新增复现段落+§1.8局限声明更新+§6.3.1交叉引用更新+§9.6.1 A2证据二维M0→M2",
        "evidence": "今日操作; Qwen复现全流程数据可复现(raw_outputs_qwen/+scores_qwen/+qwen_replication_report.md/.json); Codex GPT-5.5交叉验证(FAIL_WITH_CAVEATS, 0 MAJOR, 已修正)",
        "confidence": "🟡 较可信(本日操作, 复现数据完整, 报告经Codex审查修正)",
    })

    # === 5. Independent reviews — append Codex v1.6.1 review ===
    if 'independent_reviews' not in md:
        md['independent_reviews'] = []
    md['independent_reviews'].append({
        "version": "v1.6.1",
        "reviewer": "Codex GPT-5.5 (Codex CLI)",
        "date": "2026-06-20",
        "type": "异后端交叉验证(Patch升级审查)",
        "verdict": "FAIL_WITH_CAVEATS",
        "findings": "0 MAJOR + 3 Moderate + 2 Minor",
        "status": "全部修正",
        "report": "_codex_v161_review_output.txt",
        "prompt": "_codex_v161_review_prompt.txt",
    })

    # === 6. Update known_limitations item 1 ===
    if 'known_limitations' in data:
        data['known_limitations']['limitations'][0] = (
            "单模型证据主导——A2/A3最初均基于GPT-5.5 temp=0单模型。"
            "2026-06-20更新: A2经Qwen qwen3.7-max跨模型复现(48/48收集, Codex盲评, Δ=−0.014方向一致), "
            "首次跨模型方向一致复现, 证据二维M0→M2。"
            "A3尚未经跨模型复现。A2+A3的跨任务方向一致观察仍限GPT-5.5。"
            "以上结论严格限定于temp=0/CLI默认中文结构化判别任务内。"
        )
        data['known_limitations']['added_in'] = "v1.6, updated in v1.6.1"

    # === 7. Update framework_maintenance three_piece_sync note ===
    if 'framework_maintenance' in data:
        data['framework_maintenance']['current_sync_status'] = {
            "version": "v1.6.1",
            "date": "2026-06-20",
            "md": "v1.6.1 ✅",
            "json": "v1.6.1 ✅ (本次同步)",
            "docx": "v1.6.1 ⏳ (待生成)",
        }

    # === 8. Update description to include v1.6.1 ===
    md['description'] = (
        "AI协作项目的完整操作化框架——从Spec到Closure的七层+四跨层关切+开发手册产物. "
        "v1.6.1新增: A2 Qwen跨模型复现写回(首次跨模型方向一致复现, 证据二维M0→M2). "
        "v1.6新增: §9.6.1二维证据等级+§9.10 MF三层模板+§4.1.1.1对照实验设计强制检查清单+"
        "§2.6框架维护流程+§1.8诚实声明+§9.9路径D+附录H反向交叉引用. "
        "v1.5.5新增§6.3.1路由声明格式对照证据[E-](A3实验写回). "
        "v1.5.4新增§4.1.1执行合约[E-](A2实验写回). "
        "v1.5.3新增§1.7(最小核心+示例外挂)+§9.9(阅读导航)+附录H(反模式清单). "
        "v1.1新增Dev Log(开发手册). v1.2经三模型独立审查链校准. "
        "v1.3新增§3.7漂移检测层(五类信号+四级告警+规则退役+宪法审计+闭环策展+监测模板). "
        "v1.4新增§3.7.2.6难度分层监测+§5.3.1能力获取vs行为塑造+§6.5.1文件系统IPC反面模式+"
        "§9.1训练-评估对齐/Import完整性/配置验证/接口退化. "
        "v1.5新增§6.2模式8(Pipeline DAG)+模式9(Structured Multi-Role Review)+"
        "§9.2多轮多后端独立审查编排+§9.6证据分类(S/E/I/J/Sp). "
        "v1.5.1新增§3.7.0事件流健康度监测+§3.7.4.1自适应权重淘汰+"
        "§9.7经验注入上下文预算规则+§9.8研究经验对象(REO). "
        "v1.5.2写回Protocol 3试跑1的6项改进(C1/C5测量方法/HG-0双检查点/"
        "审查频率适应性上调/HG交互留存/C8≥2轮异后端建议/S-tier降级阈值). "
        "v1.5.3新增§1.7(最小核心+示例外挂)+§9.9(阅读导航与难度分层)+附录H(反模式清单). "
        "方法论来源=Evolver项目分析(GitNexus→Small_Scale→PilotDeck→Evolver四项目链)+"
        "PocketFlow三轮独立分析+prompt-tdd A2 Tier 1对照实验. "
        "基于ETF项目V3.6代码头部注释实践提炼."
    )

    save_json(data)
    print(f"JSON synced to v1.6.1: {JSON_PATH}")
    print("Done. Next: verify with diff, then sync .docx")

if __name__ == '__main__':
    main()

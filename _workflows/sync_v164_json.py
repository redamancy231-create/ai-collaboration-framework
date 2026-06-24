#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync AI协作项目全生命周期框架.json — 补齐 2026-06-23 发布前订正中尚未进入 .json 的 3 处差异。

背景：.json 是手工维护的结构化镜像（无 md→json 全量生成器）。v1.6.4 的结构化内容
（§6.3.2/§7.7/§9.11/§2.6/§1.8#9#10/M1*）此前已手工补入 .json body，但 2026-06-23 的
prose 订正只进了 .md 和 .docx（.docx 全量重生成时带入），.json 漏了以下 3 处：

1. §13.1.2 项目代号说明（9 代号表）—— .json external_references 缺此结构化内容
2. §13.2 Constraint Decoupling "已验证"→"已采纳"—— external_references.inspirations
3. version_timeline 中 3 处 "今日操作"→"当日操作"（v1.5.5/v1.6/v1.6.1）

不改版本号（挂 v1.6.4，与 .md/.docx 一致）。

作者模型: Claude Opus 4.8 (via Claude Code CLI) · 2026-06-24
经 Codex GPT-5.5 异后端独立 diff 验证（9/9 代号行一致 + 无意外副作用）。
Run: PYTHONIOENCODING=utf-8 python _workflows/sync_v164_json.py
"""

import json

JSON_PATH = "./AI协作项目全生命周期框架.json"


def load_json():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    data = load_json()
    report = []

    # === 1. 新增 §13.1.2 项目代号说明 ===
    er = data["external_references"]
    if "project_codenames" not in er:
        er["project_codenames"] = {
            "_comment": "v1.6.4 发布前订正（2026-06-23）新增。对应 md §13.1.2 项目代号说明。"
            "代号是框架方法论的证据来源，个人项目案例库不随框架公开发布，此处仅作可理解性锚点。",
            "note": "这些代号是框架方法论的证据来源，个人项目的案例库不随本框架公开发布，此处仅作可理解性锚点。",
            "codenames": [
                {"code": "prompt-tdd", "desc": "作者的 prompt 工程对照实验个人项目", "case_library_public": "否（仅写回结论）"},
                {"code": "形态匹配", "desc": "已封存的金融形态识别个人项目", "case_library_public": "否"},
                {"code": "BDC2026", "desc": "某数据竞赛项目", "case_library_public": "否"},
                {"code": "并购重组", "desc": "并购重组案例研究个人项目（8 阶段流水线）", "case_library_public": "否"},
                {"code": "ETF 项目 V3.6", "desc": "某 ETF 量化项目的结构化变更日志实践来源", "case_library_public": "否"},
                {"code": "PocketFlow", "desc": "外部开源项目（100 行核心 + 分难度 cookbook）", "case_library_public": "是（外部）"},
                {"code": "GitNexus", "desc": "外部开源项目（代码知识图谱工具）", "case_library_public": "是（外部）"},
                {"code": "Evolver", "desc": "外部论文项目（arXiv:2604.15097）", "case_library_public": "是（外部）"},
                {"code": "Small_Scale", "desc": "外部论文项目（ICLR 2026）", "case_library_public": "是（外部）"},
            ],
        }
        report.append("新增 external_references.project_codenames（§13.1.2，9 代号）")
    else:
        report.append("跳过：project_codenames 已存在")

    # === 2. §13.2 Constraint Decoupling "已验证"→"已采纳" ===
    cd = er["inspirations"]["Constraint_Decoupling"]
    old = cd["status"]
    if old.startswith("已验证"):
        cd["status"] = old.replace("已验证", "已采纳", 1)
        report.append(f"修正 Constraint_Decoupling.status: '{old}' → '{cd['status']}'")
    else:
        report.append(f"跳过：Constraint_Decoupling.status 已非'已验证'（当前：{old}）")

    # === 3. version_timeline 中 "今日操作"/"本日操作"→"当日操作" ===
    # 注意：.md 把"今日操作"和"本日操作"两个变体都统一为"当日操作"，
    # confidence 列用的是"本日操作"，evidence 列用的是"今日操作"——两个都要改。
    n_fixed = 0
    for vt in data["metadata"].get("version_timeline", []):
        for k in ("evidence", "event", "confidence"):
            if k in vt:
                new = vt[k].replace("今日操作", "当日操作").replace("本日操作", "当日操作")
                if new != vt[k]:
                    vt[k] = new
                    n_fixed += 1
    report.append(f"version_timeline '今日操作'/'本日操作'→'当日操作'：{n_fixed} 字段")

    # === 记录订正批次到 metadata ===
    data["metadata"]["release_prep_errata_20260623"] = (
        "2026-06-23 发布前订正（不升版本号，挂 v1.6.4）补入 .json："
        "新增 §13.1.2 项目代号说明（project_codenames）+ §13.2 Constraint Decoupling 已验证→已采纳 "
        "+ version_timeline 今日操作→当日操作。对应 .md 的 §14「v1.6.4 发布前订正批次」。"
        "同步执行：Claude Opus 4.8 (via Claude Code CLI)，2026-06-24。"
    )

    save_json(data)
    print("=== sync_v164_json 完成 ===")
    for r in report:
        print(" -", r)


if __name__ == "__main__":
    main()

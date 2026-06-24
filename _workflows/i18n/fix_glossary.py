"""综合Codex+Qwen审查修复术语表 v1.0→v1.1"""
import json, re
from pathlib import Path
from copy import deepcopy

BASE = Path(__file__).parent

with open(BASE / 'glossary.json', 'r', encoding='utf-8') as f:
    g = json.load(f)

# ============================================================
# PART 1: Fix existing entries (translation errors)
# ============================================================

fixes = {
    # A类 - 自创概念
    "被动观测": {"zh-Hant": "被動觀測", "en": "Opportunistic Observation",
                "note": "注意：非 passive observation 的直譯，更接近 opportunistic observation——主動捕捉意外發現而非消極等待"},
    "证据等级": {"en": "Evidence Level",
                "note": "注意區分：'证据等级'=Evidence Level（單條證據的強度），'五级证据分类'=Five-Tier Evidence Classification（五級體系）"},
    "信号聚合与告警规则": {"zh-Hant": "訊號聚合與警示規則", "en": "Signal Aggregation & Alert Rules"},
    "规则退役": {"en": "Rule Sunset",
                "note": "統一使用 Sunset 體系表示規則退役（不再混用 retirement）"},
    "退役判定": {"en": "Sunset Determination",
                "note": "與'规则退役'（Rule Sunset）統一使用 Sunset 體系；決定規則/產物何時廢止的判斷標準"},
    "宪法审计（constitutional audit）": {"zh-Hant": "憲法稽核（constitutional audit）", "en": "Constitutional Audit",
                "note": "台灣IT/治理語境中 audit 慣用「稽核」而非「審計」"},
    "捷径审计（shortcut audit）": {"zh-Hant": "捷徑稽核（shortcut audit）", "en": "Shortcut Audit",
                "note": "同'宪法审计'，audit→稽核；CK4檢查AI是否走捷徑而非深度分析"},
    "核心 vs 外挂": {"en": "Core vs Companion",
                "note": "外挂對應配套目錄/參考實現；cookbook 僅為§1.7中的類比說明，不進入正式術語"},
    "作者-读者同构假设": {"en": "Author-Reader Structural Isomorphism Assumption",
                "note": "強調「同构」的結構對應含義（isomorphism），非一般同質性（homogeneity）"},
    "交叉验证": {"en": "Cross-Verification",
                "note": "非 ML 意義的 cross-validation；強調異後端交叉驗證"},
    "provenance": {"en": "provenance",
                "note": "保留英文小寫；作為框架操作術語不翻譯"},
    "方向盘 > 发动机": {"zh-Hant": "方向盤 > 引擎", "en": "Steering Wheel > Engine",
                "note": "台灣IT和日常隱喻中 engine 慣用「引擎」而非「發動機」"},
    "分层不互相替代": {"en": "Layers Are Not Interchangeable",
                "note": "強調層與層之間不可互相替代，非單層本身不可替代"},
    "新增观测，不新增阻断": {"en": "Add Observability, Not Blocking",
                "note": "ChatGPT-5.5與DeepSeek交集共識；漂移檢測設計原則"},
    "30% 复杂度就能跑": {"en": "Runs at 30% Complexity",
                "note": "保留口語化風格；框架入門門檻表述"},
    # D类操作术语修复
    "完备性审查（completeness critic）": {"en": "Completeness Critic",
                "note": "§6.2模式6；角色名非泛化活動名，保留 Critic"},
    "评委团（judge panel）": {"zh-Hant": "評審團（judge panel）", "en": "Judge Panel",
                "note": "台灣更自然用「評審團」；§6.2模式4"},
    "预登记（pre-registration）": {"zh-Hant": "預註冊（pre-registration）", "en": "Pre-Registration",
                "note": "研究方法語境下台灣慣用「預註冊」"},
    "双评分者盲评协议": {"zh-Hant": "雙評分者盲評規程", "en": "Dual-Rater Blinded Scoring Protocol",
                "note": "台灣研究語境「協議」非最佳；protocol 在此為規程/方案義"},
    "审查维度互补设计": {"en": "Complementary Review-Dimension Design",
                "note": "§9.2；不同審查輪次檢查不同維度"},
    "声明式管道执行（Pipeline DAG）": {"zh-Hant": "宣告式管線執行（Pipeline DAG）",
                "en": "Declarative Pipeline Execution (Pipeline DAG)"},
    "HG-0/HG-1/HG-2/HG-3": {"en": "HG-0/HG-1/HG-2/HG-3",
                "note": "人類閘門編號，不翻譯；三語嚴格保持一致無空格"},
    "会话交接（Session Handoff）": {"zh-Hant": "對話交接（Session Handoff）",
                "note": "§9.3；AI對話間的狀態傳遞（非技術session）"},
    "配套目录": {"en": "Companion Directory",
                "note": "§1.7；可複數為 Companion Directories；「目录」→「目錄」"},
    "冗余暴露/一致维护暴露/审查附带暴露": {
                "en": "Redundancy-Driven Discovery / Consistency-Maintenance Discovery / Review-Incidental Discovery",
                "note": "§7.7.2；Exposure 在此為 reveal/discovery 義，非風險暴露"},
    "changelog": {"en": "changelog",
                "note": "§14即changelog；保留英文小寫不翻譯；全文標題中可用 Changelog"},
    # C类
    "幸存者偏差/伪模式化/噪声误读/观测污染/成本失控/副产品崇拜/安全错觉": {
                "en": "Survivorship Bias / Pseudo-Patterning / Misreading Noise / Observation Pollution / Cost Overrun / Byproduct Worship / Safety Illusion",
                "note": "Failure Space 10種失效模式中的7種。Cost Overrun 比 Cost Runaway 更穩定；Misreading Noise 比 Noise Misreading 更自然"},
    "沉默省略仍是弱实践": {"note": "漂移檢測中不記錄省略也是問題；英文偏地道可接受（作為原則/警示語追求可讀性）"},
}

for key, patch in fixes.items():
    if key in g['terms']:
        for k, v in patch.items():
            g['terms'][key][k] = v
    else:
        print(f"WARNING: key not found: {key}")

# ============================================================
# PART 2: Remove A/D duplicates from D class (6 entries)
# ============================================================
d_remove = ["Spec", "Context", "Execute", "Review", "Retrospect", "Closure"]
for key in d_remove:
    if key in g['terms'] and g['terms'][key]['type'] == 'D':
        del g['terms'][key]
        print(f"Removed D duplicate: {key}")

# Remove E class Protocol 3 duplicate
if "Protocol 3 (文档)" in g['terms']:
    del g['terms']["Protocol 3 (文档)"]
    print("Removed E duplicate: Protocol 3 (文档)")

# ============================================================
# PART 3: Add missing terms (~45 from both reviews)
# ============================================================
new_terms = {
    # §4.3 分级逃生口
    "分级逃生口": {"zh-Hant": "分級逃生口", "en": "Tiered Escape Hatch",
                   "type": "A", "note": "§4.3；三級逃生機制，ETF R5事故驅動"},
    "L1 检索恢复": {"zh-Hant": "L1 檢索恢復", "en": "L1 Retrieval Recovery",
                   "type": "A", "note": "§4.3；第一級逃生口：重新檢索外部資訊"},
    "L2 同源降级继续": {"zh-Hant": "L2 同源降級繼續", "en": "L2 Same-Source Degraded Continuation",
                   "type": "A", "note": "§4.3；第二級逃生口：降級後繼續"},
    "L3 停止报告": {"zh-Hant": "L3 停止報告", "en": "L3 Stop-and-Report",
                   "type": "A", "note": "§4.3；第三級逃生口：停止並報告，絕不用替代數據"},
    # §3.7 漂移检测层
    "事件流健康度监测": {"zh-Hant": "事件流健康度監測", "en": "Event Stream Health Monitoring",
                   "type": "A", "note": "§3.7.0；監測AI協作事件流的整體健康狀態"},
    "自适应权重淘汰": {"zh-Hant": "自適應權重淘汰", "en": "Adaptive Weight Pruning",
                   "type": "A", "note": "§3.7.4.1；+0.05/-0.15/0.0數值待敏感性分析"},
    "五类漂移信号": {"zh-Hant": "五類漂移訊號", "en": "Five Categories of Drift Signals",
                   "type": "A", "note": "§3.7.2；句法/程序/對齊/閘門繞過/績效五類"},
    "难度分层漂移": {"zh-Hant": "難度分層漂移", "en": "Difficulty-Stratified Drift",
                   "type": "A", "note": "§3.7.2.6；ML項目可選profile，非第六類獨立信號"},
    "四级告警": {"zh-Hant": "四級警示", "en": "Four-Level Alerting",
                   "type": "A", "note": "§3.7；綠/黃/橙/紅四級"},
    "detector-only 哲学": {"zh-Hant": "detector-only 哲學", "en": "detector-only philosophy",
                   "type": "A", "note": "§3.7；只觀測不修改，來自headroom CacheAligner對標"},
    "休眠审查": {"zh-Hant": "休眠審查", "en": "Dormancy Review",
                   "type": "A", "note": "§3.7.4；長時間未觸發的規則進入休眠審查狀態"},
    # §6.3.1-6.3.2 Flow-as-Node
    "路由声明": {"zh-Hant": "路由宣告", "en": "Routing Declaration",
                   "type": "A", "note": "§6.3.1；A3實驗核心概念"},
    "Flow-as-Node": {"zh-Hant": "Flow-as-Node", "en": "Flow-as-Node",
                   "type": "A", "note": "§6.3.2；嵌套工作流描述模式，不翻譯"},
    "嵌套工作流": {"zh-Hant": "巢狀工作流", "en": "Nested Workflow",
                   "type": "A", "note": "§6.3.2；A1實驗核心概念"},
    "格式效应": {"zh-Hant": "格式效應", "en": "Format Effect",
                   "type": "D", "note": "§6.3.1；prompt格式對LLM輸出的影響"},
    "结构效应": {"zh-Hant": "結構效應", "en": "Structure Effect",
                   "type": "D", "note": "§6.3.2；工作流描述結構對LLM輸出的影響"},
    # §9.6.1
    "模型家族": {"zh-Hant": "模型家族", "en": "Model Family",
                   "type": "D", "note": "§9.6.1；同一模型系列的不同版本（如GPT-5→GPT-5.5）"},
    # §9.10
    "问题空间": {"zh-Hant": "問題空間", "en": "Problem Space",
                   "type": "A", "note": "§9.10方法论片段三层模板——第一层：问题识别"},
    "解决方案空间": {"zh-Hant": "解決方案空間", "en": "Solution Space",
                   "type": "A", "note": "§9.10方法论片段三层模板——第二层：解决方案适用条件"},
    "失效空间": {"zh-Hant": "失效空間", "en": "Failure Space",
                   "type": "A", "note": "§9.10方法论片段三层模板——第三层：已知反例/失效模式"},
    "静默失效信号": {"zh-Hant": "靜默失效訊號", "en": "Silent Failure Signal",
                   "type": "A", "note": "§9.10；AI系統無提示地產出錯誤結果的跡象"},
    "任务可供性": {"zh-Hant": "任務可供性", "en": "Task Affordance",
                   "type": "D", "note": "§9.10；任務特徵是否可供AI有效執行"},
    # §9.11
    "跨层可观测性": {"zh-Hant": "跨層可觀測性", "en": "Cross-Layer Observability",
                   "type": "A", "note": "§9.11；L0-L5各層可觀測性關切+3原則"},
    # §1.8
    "探索性 vs 确认性框架": {"zh-Hant": "探索性 vs 確認性框架", "en": "Exploratory vs Confirmatory Framework",
                   "type": "A", "note": "§1.8#6；框架的探索性本質是局限也是誠實聲明"},
    "单模型证据主导": {"zh-Hant": "單模型證據主導", "en": "Single-Model Evidence Dominance",
                   "type": "D", "note": "§1.8；多數證據來自單一模型後端的局限"},
    # §2.6
    "Major/Minor/Patch 升级": {"zh-Hant": "Major/Minor/Patch 升級", "en": "Major/Minor/Patch Upgrade",
                   "type": "D", "note": "§2.6；三級版本升級規則"},
    # 附录H
    "文件系统作IPC": {"zh-Hant": "檔案系統作IPC", "en": "File System as IPC",
                   "type": "D", "note": "附錄H.1；反面模式"},
    "继承层次膨胀": {"zh-Hant": "繼承層次膨脹", "en": "Inheritance Hierarchy Bloat",
                   "type": "D", "note": "附錄H.3；反面模式"},
    # §9.2
    "后端切换判据": {"zh-Hant": "後端切換判據", "en": "Backend-Switching Criteria",
                   "type": "D", "note": "§9.2；何時應切換獨立審查後端的判斷標準"},
    "审查频率适应性上调": {"zh-Hant": "審查頻率適應性上調", "en": "Adaptive Review Frequency Increase",
                   "type": "D", "note": "§9.2；Protocol 3實證發現"},
    # B类补充
    "文件": {"zh-Hant": "檔案", "en": "File", "type": "B",
            "note": "台灣IT慣用「檔案」；非「文件」"},
    "网络": {"zh-Hant": "網路", "en": "Network", "type": "B",
            "note": "台灣IT慣用「網路」；非「網絡」"},
    "接口": {"zh-Hant": "介面", "en": "Interface", "type": "B",
            "note": "台灣IT慣用「介面」"},
    "配置": {"zh-Hant": "組態", "en": "Configuration", "type": "B",
            "note": "台灣IT慣用「組態」；config→組態"},
    "日志": {"zh-Hant": "日誌", "en": "Log", "type": "B",
            "note": "台灣IT慣用「日誌」"},
    # 其他高频缺失
    "过度工程": {"zh-Hant": "過度工程", "en": "Overengineering", "type": "D",
            "note": "§1.4；使用超過需求的框架功能"},
    "声称校准": {"zh-Hant": "聲稱校準", "en": "Claim Calibration", "type": "A",
            "note": "§9.6；將證據強度標註與實際驗證程度對齊"},
    "已知反例": {"zh-Hant": "已知反例", "en": "Known Counterexamples", "type": "A",
            "note": "§9.10；方法論片段必須記錄的失效條件"},
    "版本号规则": {"zh-Hant": "版本號規則", "en": "Versioning Rules", "type": "D",
            "note": "§2.6；Major.Minor.Patch三級規則"},
    "最小可行 Prompt 六要素": {"zh-Hant": "最小可行 Prompt 六要素", "en": "Six Elements of a Minimum Viable Prompt",
            "type": "A", "note": "§4.3；Prompt設計的六個強制要素"},
    "否决条件": {"zh-Hant": "否決條件", "en": "Kill Conditions", "type": "A",
            "note": "§4.3；一票否決的硬性條件"},
    "完成标准": {"zh-Hant": "完成標準", "en": "Completion Criteria", "type": "D",
            "note": "§4.3；任務完成的客觀判定標準"},
}

for key, entry in new_terms.items():
    if key not in g['terms']:
        g['terms'][key] = entry
    else:
        print(f"SKIP duplicate new term: {key}")

# ============================================================
# PART 4: Update term type for changed entries
# ============================================================
# E class is now "版本/文档术语" - Protocol 3 duplicate removed
# Move evidence labels from A to appendix (they stay in JSON but re-typed)
evidence_labels = ["[E-]", "[E]", "[S]", "[I]", "[J]", "[Sp]", "[D/N/A]", "[SEMI-ED]"]
for label in evidence_labels:
    if label in g['terms']:
        g['terms'][label]['type'] = 'A'  # Keep in A but note they are markers
        g['terms'][label]['note'] = g['terms'][label].get('note', '') + '（證據標註符號，非概念）'

# ============================================================
# PART 5: Update metadata
# ============================================================
g['metadata']['version'] = 'v1.1'
g['metadata']['date'] = '2026-06-23'
g['metadata']['framework_version'] = 'v1.6.4'
g['metadata']['reviewed_by'] = ['Codex GPT-5.5', 'Qwen qwen3.7-max']
g['metadata']['changelog'] = '综合Codex(魔鬼代言人)+Qwen(完备性)双后端审查修复：修正翻译错误~25处，新增术语~45条，删除A/D重复6条+E类重复1条，D类内部拆分为4子类，JSON增加framework_version/do_not_translate字段'

# Recount
type_counts = {}
for term, entry in g['terms'].items():
    t = entry['type']
    type_counts[t] = type_counts.get(t, 0) + 1
g['metadata']['type_counts'] = type_counts
g['metadata']['total_terms'] = len(g['terms'])

# ============================================================
# PART 6: Add do_not_translate flag for pure English terms
# ============================================================
dnt_terms = {k for k, v in g['terms'].items() if v['type'] in ['A', 'D'] and (
    k == v.get('zh-Hant', '') == v.get('en', '') or
    k in ['Spec', 'Context', 'Execute', 'Review', 'Retrospect', 'Closure',
          'workflow', 'agent', 'pipeline', 'checkpoint', 'gate',
          'Creator-Verifier', 'kill-test-first', 'Protocol 3', 'PocketFlow',
          'prompt-tdd', 'changelog', 'provenance', 'Flow-as-Node']
)}
for term in dnt_terms:
    if term in g['terms']:
        g['terms'][term]['do_not_translate'] = True

# Add id field
for i, (term, entry) in enumerate(g['terms'].items()):
    t = entry['type']
    entry['id'] = f"{t}-{i+1:03d}"

# ============================================================
# PART 7: Add sections field for key terms
# ============================================================
sections_map = {
    "分级逃生口": ["§4.3"], "L1 检索恢复": ["§4.3"], "L2 同源降级继续": ["§4.3"], "L3 停止报告": ["§4.3"],
    "事件流健康度监测": ["§3.7.0"], "自适应权重淘汰": ["§3.7.4.1"],
    "五类漂移信号": ["§3.7.2"], "难度分层漂移": ["§3.7.2.6"],
    "路由声明": ["§6.3.1"], "Flow-as-Node": ["§6.3.2"], "嵌套工作流": ["§6.3.2"],
    "跨层可观测性": ["§9.11"],
    "问题空间": ["§9.10"], "解决方案空间": ["§9.10"], "失效空间": ["§9.10"],
    "模型家族": ["§9.6.1"],
    "探索性 vs 确认性框架": ["§1.8"],
    "文件系统作IPC": ["附录H.1"], "继承层次膨胀": ["附录H.3"],
}
for term, sections in sections_map.items():
    if term in g['terms']:
        g['terms'][term]['sections'] = sections

# ============================================================
# PART 8: Write updated JSON
# ============================================================
with open(BASE / 'glossary.json', 'w', encoding='utf-8') as f:
    json.dump(g, f, ensure_ascii=False, indent=2)

print(f"Updated glossary.json: {len(g['terms'])} terms")
print(f"Type distribution: {type_counts}")

# ============================================================
# PART 9: Regenerate glossary.md from JSON
# ============================================================
types_md = {
    'A': ('A: 自创概念与框架元语言', '框架独有概念、证据标注符号及在框架中有特定语境含义的术语。'),
    'B': ('B: IT技术术语（台湾习惯对照）', '高频IT术语的简→繁→英对照，遵循台湾IT习惯用字。'),
    'C': ('C: 框架特有短语', '框架中的口号式短语和核心格言，保留隐喻结构和异质感。'),
    'D': ('D: 操作术语', '框架中的高频操作概念。分为四个子类：\n- **D-EN** 纯英文保留词（不翻译）\n- **D-OP** 操作概念（有实质翻译需求）\n- **D-WF** Workflow模式名（§6.2专属）\n- **D-MF** 方法论/实验术语'),
    'E': ('E: 版本/文档术语', '与框架版本管控、文档体系相关的术语。'),
}

lines = []
lines.append("# AI协作项目全生命周期框架 术语对照表\n")
lines.append(f"> **版本**：v1.1 | **日期**：2026-06-23 | **源框架版本**：v1.6.4")
lines.append(f"> **术语总数**：{len(g['terms'])}条（{', '.join(f'{k}:{v}' for k, v in sorted(type_counts.items()))}）")
lines.append("> **生成模型**：DeepSeek-V4-Pro (via Claude Code CLI)")
lines.append("> **审查**：Codex GPT-5.5（魔鬼代言人）+ Qwen qwen3.7-max（完备性分析），2026-06-23")
lines.append(">")
lines.append("> **翻译原则**：")
lines.append("> - 正体中文遵循台湾IT习惯（軟體非軟件、資料非數據、預設非默認、透過非通過…）")
lines.append("> - 英文采用美式拼写（-ize, -or, behavior…）")
lines.append("> - 自创概念保留「异质感」——不追求地道英语/台湾中文，它们本来就不存在")
lines.append("> - 当英文术语单独出现（指框架层名或操作概念）时保留英文；作为复合中文术语组成部分时使用中文翻译")
lines.append("> - 同一简体中文术语 → 同一繁体/英文翻译，全文档一致")
lines.append("> - 证据标注（[S]/[E]/[I]/[J]/[Sp]/[E-]/[D/N/A]）、层编号（L0-L5, L-H）、闸门编号（HG-0~HG-3）、M等级（M0-M3）、内部强度（A-D）均**不翻译**")
lines.append("")

for t_key in ['A', 'B', 'C', 'D', 'E']:
    title, desc = types_md[t_key]
    terms = [(k, v) for k, v in g['terms'].items() if v['type'] == t_key]
    lines.append(f"## {title} — {len(terms)}条\n")
    lines.append(f"{desc}\n")
    lines.append("| 简体中文 | 正体中文（台湾） | English (US) | 说明 |")
    lines.append("|---------|-------------------|-------------|------|")
    for term, entry in sorted(terms, key=lambda x: x[0]):
        zh = term
        zh_hant = entry.get('zh-Hant', term)
        en = entry.get('en', term)
        note = entry.get('note', '')
        lines.append(f"| {zh} | {zh_hant} | {en} | {note} |")
    lines.append("")

# Appendix A
lines.append("---\n")
lines.append("## 附录A：翻译规则速查\n")
lines.append("### A.1 台湾IT术语对照（硬规则）\n")
lines.append("| 简体 | 正体 | 说明 |")
lines.append("|-----|-----|-----|")
hard_rules = [
    ("软件", "軟體", "非「軟件」"),
    ("数据", "資料", "一般上下文；純數值型可保留「數據」"),
    ("信息", "資訊", "IT→資訊科技"),
    ("服务器", "伺服器", ""),
    ("文件", "檔案", "台灣IT慣用「檔案」"),
    ("网络", "網路", "台灣IT慣用「網路」"),
    ("接口", "介面", "台灣IT慣用「介面」"),
    ("配置", "組態", "config→組態"),
    ("日志", "日誌", "台灣IT慣用「日誌」"),
    ("默认", "預設", "非「默認」"),
    ("命令行", "命令列", "CLI→命令列介面"),
    ("质量", "品質", ""),
    ("代码", "程式碼", ""),
    ("代码块", "程式碼區塊", ""),
    ("源码", "原始碼", ""),
    ("通过(方法)", "透過", "by means of；非「通過」"),
    ("通过(物理)", "通過", "pass through"),
    ("通过(审核/测试)", "通過", "pass review / pass test"),
    ("实现", "實作", "implementation"),
    ("对象", "物件", "object"),
    ("声明式", "宣告式", "declarative"),
    ("协议(技术)", "協定", "protocol（通訊/規範義）"),
    ("协议(研究/流程)", "規程", "protocol（研究規範/操作流程義）"),
    ("模板", "範本", "template（台灣IT慣用）"),
    ("复现", "重現", "replication/reproduce"),
    ("检测", "偵測", "detection（資訊/訊號偵測）"),
    ("语义", "語意", "semantic"),
    ("审计", "稽核", "audit（台灣IT/治理語境）"),
    ("告警", "警示", "alert（台灣IT慣用）"),
]
for sc, tc, note in hard_rules:
    lines.append(f"| {sc} | {tc} | {note} |")
lines.append("")

lines.append("### A.2 英文拼写规则（美式）\n")
lines.append("| 英式 | 美式 | 示例 |")
lines.append("|-----|-----|-----|")
for uk, us, ex in [("-ise", "-ize", "organization, analyze, generalizability"),
                    ("-our", "-or", "behavior, color"),
                    ("-re", "-er", "center, theater"),
                    ("-ogue", "-og", "catalog, dialog")]:
    lines.append(f"| {uk} | {us} | {ex} |")
lines.append("")

lines.append("### A.3 不翻译清单\n")
lines.append("以下标记/编号/文件名**始终保留原文**，不进行任何翻译：\n")
lines.append("- **证据标注**：`[S]` `[E]` `[I]` `[J]` `[Sp]` `[E-]` `[D/N/A]` `[SEMI-ED]`")
lines.append("- **层编号**：`L0` `L1` `L2` `L3` `L4` `L5` `L-H`")
lines.append("- **闸门编号**：`HG-0` `HG-1` `HG-2` `HG-3`")
lines.append("- **M等级**：`M0` `M1` `M2` `M3` `N/A`")
lines.append("- **内部强度**：`A` `B+` `B` `C+` `C` `D`")
lines.append("- **文件名/路径**：`CLAUDE.md` `project_spec.md` `memory/`")
lines.append("- **项目/工具名**：`Protocol 3` `kill-test-first` `PocketFlow` `prompt-tdd`")
lines.append("- **操作术语**：`Spec` `Context` `Execute` `Review` `Retrospect` `Closure` `workflow` `agent` `pipeline` `checkpoint` `gate` `provenance` `changelog` `Creator-Verifier` `Flow-as-Node`")
lines.append("")

# Appendix B
lines.append("## 附录B：关键翻译风险提示\n")
risk_notes = [
    "「数据」→「资料」：台湾在一般上下文中用「资料」而非「数据」；database→资料库",
    "「通过」的歧义：须区分「透过」(by means of) vs「通过」(pass through) vs「通过」(pass review/test)",
    "「复盘」≠「回顾」：框架对Retrospect有明确定义，不可用一般性「回顾」替代",
    "「封存」≠「关闭/结束」：Closure含归档和条件判定双重语义",
    "「被动观测」→ Opportunistic Observation：更接近主动捕捉意外发现，非消极等待",
    "「交叉验证」→ Cross-Verification：非ML意义的cross-validation，强调异后端验证",
    "框架特有短语如「方向盘>引擎」「分层不互相替代」等须作为整体锚定翻译",
    "所有证据标注、层编号、闸门编号、等级标号均不翻译，这是框架的元语言",
    "「语义化版本」的「语义」→「语意」：台湾IT习惯，semantic→语意（非「语义」）",
    "「模板」→「范本」：台湾IT领域template惯用「范本」",
    "「协议」的歧义：技术/通讯规范→「协定」，研究/操作流程→「规程」",
    "「审计」→「稽核」：台湾IT/治理语境中audit惯用「稽核」",
    "「发动机」→「引擎」：台湾IT和日常隐喻中engine惯用「引擎」",
    "英文术语单独出现保留英文，作为复合词组成部分时使用中文翻译（如gate→「审查门」）",
]
for i, note in enumerate(risk_notes, 1):
    lines.append(f"{i}. {note}")

with open(BASE / 'glossary.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Written glossary.md: {len(lines)} lines")
print("Done. glossary v1.0 → v1.1")

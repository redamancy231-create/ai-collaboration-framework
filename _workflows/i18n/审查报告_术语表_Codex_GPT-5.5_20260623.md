# 审查报告：术语表 Codex GPT-5.5 魔鬼代言人审查

> 审查对象：`_workflows/i18n/glossary.md`、`_workflows/i18n/glossary.json`  
> 审查日期：2026-06-23  
> 审查方式：只读审查，未修改术语表与配套 JSON

## 1. 总体评估

术语表的基本结构可用：Markdown 正文 153 条与 JSON 153 条一致，A/B/C/D/E 计数与文件头一致，未发现 Markdown 与 JSON 的值级漂移。但作为三语锚定表，它仍存在若干会影响后续翻译质量的问题：一是核心概念覆盖不完整，尤其 §4.3 分级逃生口、§3.7 事件流健康度/只观测不阻断、§9.6 声称校准、§9.10 三层模板字段等高频概念缺锚；二是部分核心英文翻译与说明互相打架或过度中式化；三是台湾 IT 习惯执行不稳定，例如「審計/告警/評委/發動機/預登記」等用词未完全台湾化；四是 E 类标题与任务描述的类别预期不一致，且 `Protocol 3` 在 D/E 两类形成重复锚定。结论：不建议直接作为全框架翻译的冻结版，应先修正 CRITICAL/MAJOR 项后再下发给译者。

## 2. 逐类发现

### A 类：自创概念

1. `glossary.md:44`，`被动观测`：英文列为 `Passive Observation`，说明却写「≠ passive observation 的直接翻譯，更接近 opportunistic observation」。这是列值与说明直接矛盾。若要保留异质感，说明不应否认当前英文；若要表达真实语义，建议改为 `Opportunistic Observation` 或 `Passive Observation (Opportunistic Observation)`。

2. `glossary.md:50`，`证据等级`：英文为 `Evidence Classification`，但 D 类 `五级证据分类` 已译为 `Five-Tier Evidence Classification`（`glossary.md:173`）。「等级」与「分类」被合并成同一英文概念，后续 §9.6/§9.6.1 会混淆。建议 `证据等级` 改为 `Evidence Level` 或 `Evidence Grade`，`五级证据分类` 保留 `Five-Tier Evidence Classification`。

3. `glossary.md:54`，`信号聚合与告警规则`：`告警` 在台湾一般更常见为「警示」或「警報」，尤其此处是 alert rules 而非大陆运维语境。建议正体改为 `訊號聚合與警示規則`，英文可保留 `Signal Aggregation & Alert Rules`。

4. `glossary.md:55` 与 `glossary.md:195`，`规则退役`/`退役判定`：英文分别使用 `Rule Sunset / Rule Retirement` 与 `Sunset Determination`。同一「退役」概念在英文中同时给出 sunset/retirement 两套锚，容易造成后续文本摇摆。建议统一：若强调治理生命周期，用 `Sunset`；若强调移出活跃规则，用 `Retirement`，不要在正式术语列写斜杠双译。

5. `glossary.md:56`，`宪法审计`：正体使用 `憲法審計`，但台湾 IT/治理语境中 audit 更常译为「稽核」。建议改为 `憲法稽核`；若保留「審計」，说明应解释为何不用台湾常用的「稽核」。同类问题也影响 `捷径审计`（`glossary.md:163`）。

6. `glossary.md:63`，`核心 vs 外挂`：英文为 `Core vs Cookbook / Companion`，同时给出 `Cookbook` 和 `Companion` 两个锚。主文档 §1.7 中 cookbook 只是类比，`外挂` 实际对应配套目录/参考实现；D 类 `配套目录` 又译为 `Companion Directory`（`glossary.md:180`）。建议统一为 `Core vs Companion` 或 `Core vs Add-on`，把 cookbook 放入说明而非术语列。

7. `glossary.md:68`，`作者-读者同构假设`：英文 `Author-Reader Homogeneity Assumption` 弱化了「同构」的结构对应含义，变成一般同质性。建议改为 `Author-Reader Isomorphism Assumption` 或 `Author-Reader Structural Isomorphism Assumption`。

8. `glossary.md:80`，`交叉验证`：英文 `Cross-Validation` 虽常见，但说明又强调「非 ML 意义」。在英文读者处反而会优先触发 ML 术语联想。建议改为 `Cross-Verification` 或 `Cross-Checking`，除非全文确实要借用 ML 的 cross-validation 隐喻。

9. `glossary.md:72`、`159`，`协议` 一律转为 `協定`：`三件套同步协议`、`双评分者盲评协议`都不是网络通信 protocol，而是流程/研究规范。台湾语境下「協定」偏通信或正式约定；研究/流程语境可考虑「規程」「協議」「方案」。建议按语境拆分规则，避免 `protocol → 協定` 一刀切。

10. `glossary.md:82`，`provenance`：正体列为小写 `provenance`，英文列为大写 `Provenance`。若该词在全文作为不翻译操作术语，应统一大小写；建议英文列也用 `provenance`，或说明何时标题化。

### B 类：IT 技术术语

1. `glossary.md:94-108`：B 类覆盖了数据、软件、信息、服务器、默认、命令行、质量、代码等硬规则，但缺少文件/文档/目录/接口/配置/日志等主文档高频 IT 词。尤其提示词明确举例「文件→檔案」，而 B 类没有 `文件` 条目，导致后续 `配套文件`、`关键文件路径`、`文件命名约定` 等高频表达无锚。

2. `glossary.md:105-106`：`通过` 拆成方法/物理两条是正确方向，但说明仅覆盖「物理空间穿越」。主文档中大量「通过」表示流程达标、审查通过、验证通过，这些并非物理穿越，也不等于 `透過`。建议新增第三类：`通过（审核/测试/门槛） → 通過 → pass / pass review`。

3. `glossary.md:107`，`审查`：说明写「大陆『查』从木旦，台灣『查』从木旦（同字）」没有实质价值，还可能显得像机械注释。建议改为说明 `审→審；查不变`，并补充 review/assessment/audit 的边界。

### C 类：框架特有短语

1. `glossary.md:116`，`方向盘 > 发动机`：正体为 `方向盤 > 發動機`。台湾日常和 IT 隐喻中 engine 更常译为「引擎」，`發動機`偏机械/大陆书面。建议改为 `方向盤 > 引擎`。

2. `glossary.md:117`，`分层不互相替代`：英文 `Layers Are Not Substitutable` 生硬，且 `substitutable` 容易理解为单个 layer 本身不可替代，而不是「层与层之间不能互相替代」。建议 `Layers Do Not Substitute for One Another` 或 `Layers Are Not Interchangeable`。

3. `glossary.md:120`，`新增观测，不新增阻断`：英文 `Add Observation, Not Blockage` 不自然，`blockage` 更像堵塞物。该短语是 OPEN-1 核心原则，建议改为 `Add Observability, Not Blocking` 或 `Add Observation, Not New Gates`。

4. `glossary.md:122`，`30% 复杂度就能跑`：英文 `30% Complexity Is Enough to Run` 是中式英语，且缺少「启动/跑起来」的语气。建议 `Runs at 30% Complexity`、`30% Complexity Is Enough to Start` 或 `You Can Start with 30% Complexity`。

5. `glossary.md:126`，复合失效模式短语：`Noise Misreading`、`Cost Runaway`、`Byproduct Worship` 有保留异质感的理由，但其中 `Cost Runaway` 比常用的 `Cost Overrun` 更不稳定，`Noise Misreading` 也不如 `Misreading Noise` 自然。建议至少在说明中标注哪些是刻意异质化，哪些是常规译法。

### D 类：操作术语

1. `glossary.md:148`，`完备性审查（completeness critic）`：主文档 §6.2 模式 6 的模式名是 `Completeness Critic`，但术语表英文给 `Completeness Review`，角色名被改成泛化活动名。建议英文改为 `Completeness Critic`；正体可为 `完備性批評者（completeness critic）` 或 `完備性審查（Completeness Critic）`。

2. `glossary.md:150`，`评委团（judge panel）`：正体 `評委團`偏大陆用法，台湾更自然是 `評審團`。建议改为 `評審團（judge panel）`。

3. `glossary.md:157`，`预登记（pre-registration）`：研究方法语境下 preregistration 在台湾更常见为 `預註冊`，`預登記`较泛。建议改为 `預註冊（pre-registration）`，英文保留 `Preregistration` 或 `Pre-Registration` 均可，但需全表统一。

4. `glossary.md:159`，`双评分者盲评协议`：英文 `Dual-Rater Blind Review Protocol` 容易被理解为同行评审 blind review；此处是两个评分者对实验输出盲评。建议 `Dual-Rater Blinded Scoring Protocol`，正体建议 `雙評分者盲評規程` 或 `雙評分者盲評方案`。

5. `glossary.md:161`，`审查维度互补设计`：英文 `Complementary Review Dimension Design` 语序生硬。建议 `Complementary Design of Review Dimensions` 或 `Complementary Review-Dimension Design`。

6. `glossary.md:163`，`捷径审计（shortcut audit）`：同 A 类 `宪法审计`，台湾语境建议 `捷徑稽核`；英文 `Shortcut Audit` 可保留。

7. `glossary.md:174`，`HG-0/HG-1/HG-2/HG-3`：提示原则说闸门编号不翻译，但英文列加了空格 `HG-0 / HG-1 / HG-2 / HG-3`。严格锚定时应保持完全一致，建议三列均为 `HG-0/HG-1/HG-2/HG-3`。

8. `glossary.md:175`，`会话交接（Session Handoff）`：`會話`在台湾 IT 中可用，但若对应 session state/handoff，`工作階段交接`更精确。建议根据全文「AI 对话」还是「runtime session」二选一：AI 对话用 `對話交接`，技术 session 用 `工作階段交接`。

9. `glossary.md:180`，`配套目录`：英文 `Companion Directory` 为单数，但主文档 §1.7 明确是四个配套目录。建议术语可用单数，但说明中补「可复数为 Companion Directories」，避免整段翻译时误写为一个目录。

10. `glossary.md:184`，`冗余暴露/一致维护暴露/审查附带暴露`：英文三项都用 `Exposure`，容易被理解为风险暴露而不是「被动观测中暴露出线索」。建议考虑 `Redundancy-Driven Discovery / Consistency-Maintenance Discovery / Review-Incidental Discovery`，或至少说明 `Exposure` 是 reveal/discovery 意义。

### E 类：版本/文档术语

1. `glossary.md:187`：E 类标题为「版本/文档术语」，但任务提示描述 E 为「方法论」。如果这是术语表设计本身，应改提示或改分类；如果按提示审查，E 类整体分类错误。当前 E 类 10 条多数是版本/文档项，并非方法论项。

2. `glossary.md:193`，`changelog`：作为章节/文档类型时通常写 `Changelog`；作为保留小写操作术语则可用 `changelog`。当前 D 类操作术语附录也列 `changelog` 不翻译，建议说明大小写规则，否则标题翻译会不稳定。

3. `glossary.md:195`，`退役判定`：与 A 类 `规则退役` 的 sunset/retirement 双译冲突，见 A 类第 4 条。建议统一为 `Sunset Determination` 并将 `Rule Sunset` 固定下来，或统一 retirement 体系。

4. `glossary.md:200`，`模板（附录A-G）`：正体 `範本`正确，但 A 类 `三层模型（MF模板）` 仍保留 `MF模板`（`glossary.md:41`）。若括号中中文不是文件名或固定原文，也应统一为 `MF範本`。当前「模板→範本」规则执行不一致。

5. `glossary.md:202`，`Protocol 3 (文档)`：正体和英文都变成 `Protocol 3`，与 D 类 `Protocol 3`（`glossary.md:170`）完全同译，两个不同简体条目指向同一正体/英文。建议二选一：删除 E 类重复条目并在 D 类说明其文档用法；或改为 `Protocol 3（文件） / Protocol 3 (Document)` 以保留区分。

## 3. 遗漏清单

以下术语在指定章节中出现或承担核心锚定功能，但未进入术语表。建议优先补入，而不是等翻译时临场发挥。

| 来源 | 缺失术语 | 建议正体 | 建议英文 |
|---|---|---|---|
| §1.4 | 过度工程 | 過度工程 | Overengineering |
| §1.5 | 绕过率 | 繞過率 | Bypass Rate |
| §1.5 | HG 过载 | HG 過載 | HG Overload |
| §1.6 | 严重性夷平 | 嚴重性夷平 | Severity Flattening |
| §1.7 | canonical source of truth（规范来源） | canonical source of truth（規範來源） | canonical source of truth |
| §1.7 | 规范性参考 | 規範性參考 | Normative Reference |
| §1.7 | 边界案例处理原则 | 邊界案例處理原則 | Boundary-Case Handling Principle |
| §1.8 | 单模型证据主导 | 單模型證據主導 | Single-Model Evidence Dominance |
| §1.8 | 单团队实验者效应 | 單團隊實驗者效應 | Single-Team Experimenter Effect |
| §1.8 | 无独立人类专家校准 | 無獨立人類專家校準 | No Independent Human-Expert Calibration |
| §1.8 | 二维证据体系未试跑 | 二維證據體系未試跑 | Untested Two-Dimensional Evidence System |
| §1.8 | 探索性 vs 确认性框架 | 探索性 vs 確認性框架 | Exploratory vs Confirmatory Frameworks |
| §1.8 | 测试集区分度 | 測試集區分度 | Test-Set Discrimination |
| §1.8 | 有效样本量 | 有效樣本量 | Effective Sample Size |
| §2.6 | 版本号规则 | 版本號規則 | Versioning Rules |
| §2.6 | Major/Minor/Patch 升级 | Major/Minor/Patch 升級 | Major/Minor/Patch Upgrade |
| §2.6 | 0 MAJOR 未闭合 | 0 MAJOR 未閉合 | Zero Unclosed MAJOR Findings |
| §3.7 | 事件流健康度监测 | 事件流健康度監測 | Event-Stream Health Monitoring |
| §3.7 | 只观测，不阻断 | 只觀測，不阻斷 | Observe Only, Do Not Block / Add Observability, Not Blocking |
| §3.7 | detector-only 哲学 | detector-only 哲學 | detector-only philosophy |
| §3.7 | 事实优先，解释在后 | 事實優先，解釋在後 | Facts First, Interpretation Later |
| §3.7 | 覆盖留下痕迹的漂移 | 覆蓋留下痕跡的漂移 | Cover Drift That Leaves Traces |
| §3.7 | 退化路径内置 | 退化路徑內建 | Built-In Degradation Path |
| §3.7 | 传感面 | 感測面 | Sensing Surface |
| §3.7 | 低信任 | 低信任 | Low Trust |
| §3.7 | 四级告警 | 四級警示 | Four-Level Alerting |
| §3.7 | 连续红级升级机制 | 連續紅級升級機制 | Consecutive-Red Escalation Mechanism |
| §3.7 | 自适应权重淘汰 | 自適應權重淘汰 | Adaptive Weight-Based Pruning |
| §4.3 | 最小可行 Prompt 六要素 | 最小可行 Prompt 六要素 | Six Elements of a Minimum Viable Prompt |
| §4.3 | 完成标准 | 完成標準 | Completion Criteria |
| §4.3 | 否决条件 | 否決條件 | Kill Conditions / Rejection Criteria |
| §4.3 | 分级逃生口 | 分級逃生口 | Tiered Escape Hatch |
| §4.3 | 检索/验证恢复 | 檢索/驗證恢復 | Retrieval/Verification Recovery |
| §4.3 | 同源降级继续 | 同源降級繼續 | Same-Source Degraded Continuation |
| §4.3 | 停止报告 | 停止報告 | Stop-and-Report |
| §4.3 | 异源替换 | 異源替換 | Cross-Source Substitution |
| §6.2 | Swarm/Solo 双模式 | Swarm/Solo 雙模式 | Swarm/Solo Dual Mode |
| §6.2 | 输出合同 | 輸出合約 | Output Contract |
| §6.2 | 隐藏耦合 | 隱藏耦合 | Hidden Coupling |
| §6.2 | 声明依赖 | 宣告依賴 | Declared Dependencies |
| §6.2 | 综合批评者 | 綜合批評者 | Synthesis Critic / Integrating Critic |
| §6.2 | 硬关卡纪律 | 硬關卡紀律 | Hard-Gate Discipline |
| §9.2 | AI 自评 | AI 自評 | AI Self-Assessment |
| §9.2 | 人类审查 | 人類審查 | Human Review |
| §9.2 | 后端切换判据 | 後端切換判據 | Backend-Switching Criteria |
| §9.2 | 审查频率适应性上调 | 審查頻率適應性上調 | Adaptive Increase in Review Frequency |
| §9.2 | 维度轮换策略 | 維度輪換策略 | Dimension-Rotation Strategy |
| §9.6 | 声称校准 | 聲稱校準 | Claim Calibration |
| §9.6 | 关键声称 | 關鍵聲稱 | Key Claims |
| §9.6 | 推断链 | 推斷鏈 | Inference Chain |
| §9.6 | 未验证清单 | 未驗證清單 | Unverified Claims List |
| §9.6.1 | 模型家族 | 模型家族 | Model Family |
| §9.6.1 | 异模型复现 | 異模型重現 | Cross-Model-Family Replication |
| §9.6.1 | 内部效度/外部效度 | 內部效度/外部效度 | Internal Validity / External Validity |
| §9.10 | 问题识别 | 問題識別 | Problem Identification |
| §9.10 | 解决方案适用条件 | 解決方案適用條件 | Solution Applicability Conditions |
| §9.10 | 已知反例 | 已知反例 | Known Counterexamples |
| §9.10 | 失效模式 | 失效模式 | Failure Modes |
| §9.10 | 静默失效信号 | 靜默失效訊號 | Silent-Failure Signals |
| §9.10 | 三层独立维护规则 | 三層獨立維護規則 | Three-Layer Independent Maintenance Rules |
| §9.10 | 任务可供性 | 任務可供性 | Task Affordance |
| §9.10 | 替代因变量（DV） | 替代依變量（DV） | Alternative Dependent Variable (DV) |

## 4. 严重度排序

### CRITICAL

1. 核心术语遗漏：§4.3 分级逃生口、§3.7 事件流健康度/只观测不阻断、§9.6 声称校准、§9.10 三层字段等缺失，会导致最关键机制无法稳定翻译。
2. `glossary.md:44` `被动观测` 英文列与说明互相矛盾，核心概念语义不可靠。
3. `glossary.md:202` 与 `glossary.md:170` 的 `Protocol 3` 重复锚定，两个不同条目映射为同一正体/英文，应合并或显式区分。

### MAJOR

1. `glossary.md:148` `Completeness Critic` 被译成 `Completeness Review`，模式名丢失。
2. `glossary.md:50` `证据等级` 与 `五级证据分类` 的英文边界混乱。
3. `glossary.md:63` `核心 vs 外挂` 英文双锚 `Cookbook / Companion` 不稳定。
4. `glossary.md:68` `作者-读者同构假设` 被译成 homogeneity，丢失「同构」含义。
5. `glossary.md:80` `交叉验证` 使用 `Cross-Validation`，与说明中的「非 ML 意义」冲突。
6. `glossary.md:116` `發動機`、`glossary.md:150` `評委團`、`glossary.md:157` `預登記`、`glossary.md:159` `協定` 等不够符合台湾 IT/研究语境。
7. `glossary.md:187` E 类标题与任务描述的「方法论」分类不一致，应确认分类体系。

### MINOR

1. `glossary.md:54` `告警` 建议台湾化为 `警示/警報`。
2. `glossary.md:56`、`163` 的 audit 建议统一为 `稽核` 或说明为何用 `審計`。
3. `glossary.md:117`、`120`、`122` 多个口号英文存在中式或不自然表达，建议重写为更稳定的英文锚。
4. `glossary.md:174` 闸门编号英文列增加空格，严格不翻译时应保持原样。
5. `glossary.md:193` `changelog` 大小写规则未说明。
6. `glossary.md:41` `MF模板` 与 `glossary.md:200` `模板→範本` 规则执行不一致。

## 5. 机械一致性结果

- `glossary.md` 正式条目数：153。
- `glossary.json` 条目数：153。
- A/B/C/D/E 计数：A=65，B=15，C=11，D=52，E=10。
- Markdown 与 JSON 条目、正体、英文、类别、说明字段一致，未发现配套 JSON 漂移。
- 唯一机械重复锚定：`Protocol 3`（D 类）与 `Protocol 3 (文档)`（E 类）正体/英文完全相同。
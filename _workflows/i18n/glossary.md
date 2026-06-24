# AI协作项目全生命周期框架 术语对照表

> **版本**：v1.1 | **日期**：2026-06-23 | **源框架版本**：v1.6.4
> **术语总数**：188条（A:89, B:20, C:11, D:59, E:9）
> **生成模型**：DeepSeek-V4-Pro (via Claude Code CLI)
> **审查**：Codex GPT-5.5（魔鬼代言人）+ Qwen qwen3.7-max（完备性分析），2026-06-23
>
> **翻译原则**：
> - 正体中文遵循台湾IT习惯（軟體非軟件、資料非數據、預設非默認、透過非通過…）
> - 英文采用美式拼写（-ize, -or, behavior…）
> - 自创概念保留「异质感」——不追求地道英语/台湾中文，它们本来就不存在
> - 当英文术语单独出现（指框架层名或操作概念）时保留英文；作为复合中文术语组成部分时使用中文翻译
> - 同一简体中文术语 → 同一繁体/英文翻译，全文档一致
> - 证据标注（[S]/[E]/[I]/[J]/[Sp]/[E-]/[D/N/A]）、层编号（L0-L5, L-H）、闸门编号（HG-0~HG-3）、M等级（M0-M3）、内部强度（A-D）均**不翻译**

## A: 自创概念与框架元语言 — 89条

框架独有概念、证据标注符号及在框架中有特定语境含义的术语。

| 简体中文 | 正体中文（台湾） | English (US) | 说明 |
|---------|-------------------|-------------|------|
| Dev Log（开发手册） | Dev Log（開發手冊） | Dev Log (Development Log) | 貫穿全文的跨層產物；保留英文+中文括注 |
| Flow-as-Node | Flow-as-Node | Flow-as-Node | §6.3.2；嵌套工作流描述模式，不翻譯 |
| L-H Human Gate（人类闸门） | L-H Human Gate（人類閘門） | L-H Human Gate | 保留英文+中文括注；「闸门」→「閘門」為兩岸一致轉換 |
| L0 Spec | L0 Spec | L0 Spec | 層編號體系，不翻譯 |
| L1 Context（上下文管理）/ Prompt（任务规格） | L1 Context（上下文管理）/ Prompt（任務規格） | L1 Context (Context Management) / Prompt (Task Specification) | 保留英文+中文括注；「任务」→「任務」、「规格」→「規格」為兩岸一致轉換 |
| L1 检索恢复 | L1 檢索恢復 | L1 Retrieval Recovery | §4.3；第一級逃生口：重新檢索外部資訊 |
| L2 Execute（执行）/ Loop（执行迭代） | L2 Execute（執行）/ Loop（執行迭代） | L2 Execute (Execution) / Loop (Execution Iteration) | 保留英文+中文括注；「执行」→「執行」為兩岸一致轉換 |
| L2 同源降级继续 | L2 同源降級繼續 | L2 Same-Source Degraded Continuation | §4.3；第二級逃生口：降級後繼續 |
| L3 Review（审查）/ Workflow（多任务编排） | L3 Review（審查）/ Workflow（多任務編排） | L3 Review (Review) / Workflow (Multi-Task Orchestration) | 保留英文+中文括注；「审查」→「審查」、「任务」→「任務」為台灣習慣 |
| L3 停止报告 | L3 停止報告 | L3 Stop-and-Report | §4.3；第三級逃生口：停止並報告，絕不用替代數據 |
| L4 Retrospect（复盘） | L4 Retrospect（復盤） | L4 Retrospect (Post-Mortem Analysis) | 注意：不是「回顧」，框架明確用「复盘/復盤」；英文Retrospect保留大寫 |
| L5 Closure（封存） | L5 Closure（封存） | L5 Closure (Archival & Sunset Determination) | 注意：不是「關閉」或「結束」；含歸檔與條件判定雙重語義 |
| Spec（项目宪法） | Spec（專案憲法） | Spec (Project Constitution) | 框架核心層名，保留英文Spec大寫；「宪法」→「憲法」為兩岸一致轉換 |
| [D/N/A] | [D/N/A] | [D/N/A] | 編輯者判斷/非LLM來源，證據標註，不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [E-] | [E-] | [E-] | 陰性證據標註，不翻譯；表示預期驗證但未通過（證據標註符號，非概念）（證據標註符號，非概念） |
| [E] | [E] | [E] | External-verified，證據標註，不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [I] | [I] | [I] | Inferred，證據標註，不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [J] | [J] | [J] | Expert judgment，證據標註，不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [SEMI-ED] | [SEMI-ED] | [SEMI-ED] | 編輯獨立性標註；Semi-Editorial；不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [S] | [S] | [S] | Source-verified，證據標註，不翻譯（證據標註符號，非概念）（證據標註符號，非概念） |
| [Sp] | [Sp] | [Sp] | Speculative，證據標註，不翻譯；貫穿全文（證據標註符號，非概念）（證據標註符號，非概念） |
| detector-only 哲学 | detector-only 哲學 | detector-only philosophy | §3.7；只觀測不修改，來自headroom CacheAligner對標 |
| provenance | provenance | provenance | 保留英文小寫；作為框架操作術語不翻譯 |
| 三件套 | 三件套 | Three-Piece Suite | .md / .json / .docx 配套檔案組；保留口語化異質感 |
| 三件套同步协议 | 三件套同步協定 | Three-Piece Suite Synchronization Protocol | 「协议」→「協定」為台灣IT習慣（protocol在台灣慣用「協定」） |
| 三层模型（MF模板） | 三層模型（MF模板） | Three-Layer Model (MF Template) | Problem Space / Solution Space / Failure Space；「层」→「層」為兩岸一致轉換 |
| 上下文隔离 | 上下文隔離 | Context Isolation | 審查獨立性的必要條件之一 |
| 事件流健康度监测 | 事件流健康度監測 | Event Stream Health Monitoring | §3.7.0；監測AI協作事件流的整體健康狀態 |
| 五类漂移信号 | 五類漂移訊號 | Five Categories of Drift Signals | §3.7.2；句法/程序/對齊/閘門繞過/績效五類 |
| 交叉验证 | 交叉驗證 | Cross-Verification | 非 ML 意義的 cross-validation；強調異後端交叉驗證 |
| 休眠审查 | 休眠審查 | Dormancy Review | §3.7.4；長時間未觸發的規則進入休眠審查狀態 |
| 作者-读者同构假设 | 作者-讀者同構假設 | Author-Reader Structural Isomorphism Assumption | 強調「同构」的結構對應含義（isomorphism），非一般同質性（homogeneity） |
| 使用强度分档 | 使用強度分檔 | Usage Intensity Tier | A（最低強制版）/ B（預設版）/ C（完整版）；「档」→「檔」為兩岸一致轉換 |
| 信号聚合与告警规则 | 訊號聚合與警示規則 | Signal Aggregation & Alert Rules | 四級：綠/黃/橙/紅；「信号」→「訊號」、「与」→「與」為台灣習慣 |
| 内部强度 A/B+/B/C+/C/D | 內部強度 A/B+/B/C+/C/D | Internal Strength A/B+/B/C+/C/D | A-D六級，保留英文等級標記；「强度」→「強度」為兩岸一致轉換 |
| 写回 | 寫回 | Write-Back | Retrospect→Spec 操作；「写」→「寫」為兩岸一致轉換 |
| 写回审查门 | 寫回審查門 | Write-Back Review Gate | Retrospect→Spec寫回前的強制審查關卡 |
| 冷读（blind-first assessment） | 冷讀（blind-first assessment） | Cold Read (Blind-First Assessment) | 審查方法論；先不看原文資訊進行獨立判斷 |
| 冻结期 | 凍結期 | Freeze Period | 「冻」→「凍」為兩岸一致轉換 |
| 分级逃生口 | 分級逃生口 | Tiered Escape Hatch | §4.3；三級逃生機制，ETF R5事故驅動 |
| 双轴独立性 | 雙軸獨立性 | Dual-Axis Independence | 後端模型不同 + 上下文隔離；「轴」→「軸」為兩岸一致轉換 |
| 反向沉淀 | 反向沉澱 | Reverse Precipitation | 從失敗和驚喜中反向提煉；保留異質感，非地道英語成語 |
| 合规牙齿 | 合規牙齒 | Compliance Teeth | 比喻性術語，保留原文異質感；指規則的實際約束力 |
| 否决条件 | 否決條件 | Kill Conditions | §4.3；一票否決的硬性條件 |
| 四级告警 | 四級警示 | Four-Level Alerting | §3.7；綠/黃/橙/紅四級 |
| 声称校准 | 聲稱校準 | Claim Calibration | §9.6；將證據強度標註與實際驗證程度對齊 |
| 外部依赖漂移风险 | 外部依賴漂移風險 | External Dependency Drift Risk | 「依赖」→「依賴」、「风险」→「風險」為兩岸一致轉換 |
| 天花板效应 | 天花板效應 | Ceiling Effect | 注意與統計學「天花板效應」區分；此處指AI審查能力上限 |
| 失效空间 | 失效空間 | Failure Space | §9.10方法论片段三层模板——第三层：已知反例/失效模式 |
| 审查链 | 審查鏈 | Review Chain | 「审查」→「審查」、「链」→「鏈」為台灣習慣 |
| 审查链谱系 | 審查鏈譜系 | Review Provenance | 記錄每次審查的後端模型與上下文；provenance在此處作為概念名詞 |
| 审查门 | 審查門 | Review Gate | 「门」→「門」為兩岸一致轉換 |
| 宪法审计（constitutional audit） | 宪法稽核（constitutional audit） | Constitutional Audit | Spec合規檢查；保留英文括注；台灣IT/治理語境 audit→稽核 |
| 嵌套工作流 | 巢狀工作流 | Nested Workflow | §6.3.2；A1實驗核心概念 |
| 已知反例 | 已知反例 | Known Counterexamples | §9.10；方法論片段必須記錄的失效條件 |
| 已知待决项登记（OPEN items） | 已知待決項登記（OPEN items） | OPEN Items Registry | OPEN-1至OPEN-5；保留英文標記 |
| 异后端审查 | 異後端審查 | Cross-Backend Review | 使用不同AI模型後端進行審查；「异」→「異」、「后」→「後」為兩岸一致轉換 |
| 强制启用清单 | 強制啟用清單 | Mandatory Activation Checklist | 「启」→「啟」為兩岸一致轉換 |
| 循环漂移账本（Loop Drift Ledger） | 迴圈漂移帳本（Loop Drift Ledger） | Loop Drift Ledger | 保留英文括注；「循环」→「迴圈」、「账」→「帳」為台灣習慣 |
| 探索性 vs 确认性框架 | 探索性 vs 確認性框架 | Exploratory vs Confirmatory Framework | §1.8#6；框架的探索性本質是局限也是誠實聲明 |
| 方法论片段（MF） | 方法論片段（MF） | Methodology Fragment (MF) | 全文高頻；MF縮寫保留；「论」→「論」為兩岸一致轉換 |
| 最低强制版/默认版/完整版 | 最低強制版/預設版/完整版 | Minimum Mandatory / Default / Full Edition | A/B/C三檔；「默认」→「預設」為台灣IT習慣 |
| 最小可行 Prompt 六要素 | 最小可行 Prompt 六要素 | Six Elements of a Minimum Viable Prompt | §4.3；Prompt設計的六個強制要素 |
| 核心 vs 外挂 | 核心 vs 外掛 | Core vs Companion | 外挂對應配套目錄/參考實現；cookbook 僅為§1.7中的類比說明，不進入正式術語 |
| 框架级成熟度评估表 | 框架級成熟度評估表 | Framework-Level Maturity Assessment Table | 「级」→「級」為兩岸一致轉換 |
| 死亡判据 | 死亡判據 | Kill Criteria | 框架自身的終止條件；「据」→「據」為兩岸一致轉換 |
| 漂移信号（句法/语义/程序/对齐/绩效） | 漂移訊號（句法/語意/程序/對齊/績效） | Drift Signals (Syntactic / Semantic / Procedural / Alignment / Performance) | 「信号」→「訊號」、「语义」→「語意」、「对齐」→「對齊」為台灣習慣 |
| 漂移检测层 | 漂移偵測層 | Drift Detection Layer | 「检测」→「偵測」為台灣IT習慣（detection選用「偵測」而非「檢測」） |
| 独立审查 | 獨立審查 | Independent Review | 「审查」→「審查」為台灣習慣 |
| 研究经验对象（REO） | 研究經驗物件（REO） | Research Experience Object (REO) | 保留英文縮寫+中文；「对象」→「物件」為台灣IT習慣（object→物件） |
| 经验注入 | 經驗注入 | Experience Injection | 將被動觀測所得回饋至框架；注入保留原文異質感 |
| 自适应权重淘汰 | 自適應權重淘汰 | Adaptive Weight Pruning | §3.7.4.1；+0.05/-0.15/0.0數值待敏感性分析 |
| 被动观测 | 被動觀測 | Opportunistic Observation | 注意：非 passive observation 的直譯，更接近 opportunistic observation——主動捕捉意外發現而非消極等待 |
| 裸环境 checklist | 裸環境 checklist | Bare Environment Checklist | 獨立審查的前置檢查清單；「环」→「環」為兩岸一致轉換 |
| 规则退役 | 規則退役 | Rule Sunset | 統一使用 Sunset 體系表示規則退役（不再混用 retirement） |
| 解决方案空间 | 解決方案空間 | Solution Space | §9.10方法论片段三层模板——第二层：解决方案适用条件 |
| 证据二维矩阵 | 證據二維矩陣 | Two-Dimensional Evidence Matrix | 內部強度 × 跨模型推廣性；「矩阵」→「矩陣」為兩岸一致轉換 |
| 证据等级 | 證據等級 | Evidence Level | 注意區分：'证据等级'=Evidence Level（單條證據的強度），'五级证据分类'=Five-Tier Evidence Classification（五級體系） |
| 诚实声明 | 誠實聲明 | Honesty Statement | 框架的自我限制宣告 |
| 跨层可观测性 | 跨層可觀測性 | Cross-Layer Observability | §9.11；L0-L5各層可觀測性關切+3原則 |
| 跨模型推广性 M0/M1/M2/M3/N/A | 跨模型推廣性 M0/M1/M2/M3/N/A | Cross-Model Generalizability M0/M1/M2/M3/N/A | M等級體系，保留英文等級標記；「推广」→「推廣」為兩岸一致轉換 |
| 路由声明 | 路由宣告 | Routing Declaration | §6.3.1；A3實驗核心概念 |
| 逃生口 | 逃生口 | Escape Hatch | 偏離框架的合法出口；保留口語化隱喻 |
| 闭环策展 | 閉環策展 | Closed-Loop Curation | 「环」→「環」為兩岸一致轉換；策展取其「篩選+維護」義 |
| 问题空间 | 問題空間 | Problem Space | §9.10方法论片段三层模板——第一层：问题识别 |
| 难度分层漂移 | 難度分層漂移 | Difficulty-Stratified Drift | §3.7.2.6；ML項目可選profile，非第六類獨立信號 |
| 静默失效信号 | 靜默失效訊號 | Silent Failure Signal | §9.10；AI系統無提示地產出錯誤結果的跡象 |
| 项目规模分档 | 專案規模分檔 | Project Scale Tier | S（探索）/ M（標準）/ L（正式）；「项目」→「專案」為台灣IT習慣 |
| 魔鬼代言人审查 | 魔鬼代言人審查 | Adversarial Review | 注意非字面「devil's advocate」；英文用adversarial review更準確表達對抗式檢驗 |

## B: IT技术术语（台湾习惯对照） — 20条

高频IT术语的简→繁→英对照，遵循台湾IT习惯用字。

| 简体中文 | 正体中文（台湾） | English (US) | 说明 |
|---------|-------------------|-------------|------|
| 代码 | 程式碼 | code | 台灣IT習慣用「程式碼」 |
| 代码块 | 程式碼區塊 | code block | 「代码」→「程式碼」、「块」→「區塊」為台灣IT習慣 |
| 信息 | 資訊 | information | 台灣用「資訊」；information technology→資訊科技 |
| 后端 | 後端 | backend | 指AI模型後端；台灣IT用「後端」 |
| 命令行 | 命令列 | command line | 台灣IT習慣用「命令列」；CLI→命令列介面 |
| 审查 | 審查 | review | 兩岸字形差異：大陆「查」从木旦，台灣「查」从木旦（同字）；但「审」→「審」 |
| 接口 | 介面 | Interface | 台灣IT慣用「介面」 |
| 数据 | 資料 | data | 一般上下文用「資料」；數值型數據可用「數據」；台灣IT：database→資料庫 |
| 文件 | 檔案 | File | 台灣IT慣用「檔案」；非「文件」 |
| 日志 | 日誌 | Log | 台灣IT慣用「日誌」 |
| 服务器 | 伺服器 | server | 台灣IT標準譯法；§9.5 |
| 框架 | 框架 | framework | 兩岸一致 |
| 源码 | 原始碼 | source code | 台灣IT習慣用「原始碼」 |
| 网络 | 網路 | Network | 台灣IT慣用「網路」；非「網絡」 |
| 质量 | 品質 | quality | 台灣IT習慣用「品質」 |
| 软件 | 軟體 | software | 台灣用「軟體」而非「軟件」 |
| 通过（方法/手段） | 透過 | by means of / via | 台灣用「透過」表示by means of；「通過」僅用於物理空間穿越 |
| 通过（物理穿越） | 通過 | pass through | 僅用於物理空間穿越；by means of應作「透過」 |
| 配置 | 組態 | Configuration | 台灣IT慣用「組態」；config→組態 |
| 默认 | 預設 | default | 台灣IT習慣用「預設」而非「默認」 |

## C: 框架特有短语 — 11条

框架中的口号式短语和核心格言，保留隐喻结构和异质感。

| 简体中文 | 正体中文（台湾） | English (US) | 说明 |
|---------|-------------------|-------------|------|
| 30% 复杂度就能跑 | 30% 複雜度就能跑 | Runs at 30% Complexity | 保留口語化風格；框架入門門檻表述 |
| AI 内部闭环 ≠ 人类审查 | AI 內部閉環 ≠ 人類審查 | AI Internal Closed Loop ≠ Human Review | 核心警示；「环」→「環」為兩岸一致轉換 |
| 从失败中反向沉淀 | 從失敗中反向沉澱 | Reverse Precipitation from Failures | 保留異質感，不追求地道英語 |
| 分层不互相替代 | 分層不互相替代 | Layers Are Not Interchangeable | 強調層與層之間不可互相替代，非單層本身不可替代 |
| 加复杂度比减复杂度容易 | 加複雜度比減複雜度容易 | Adding Complexity Is Easier Than Removing It | 框架設計原則；提醒克制添加規則 |
| 幸存者偏差/伪模式化/噪声误读/观测污染/成本失控/副产品崇拜/安全错觉 | 倖存者偏差/偽模式化/雜訊誤讀/觀測污染/成本失控/副產品崇拜/安全錯覺 | Survivorship Bias / Pseudo-Patterning / Misreading Noise / Observation Pollution / Cost Overrun / Byproduct Worship / Safety Illusion | Failure Space 10種失效模式中的7種。Cost Overrun 比 Cost Runaway 更穩定；Misreading Noise 比 Noise Misreading 更自然 |
| 新增观测，不新增阻断 | 新增觀測，不新增阻斷 | Add Observability, Not Blocking | ChatGPT-5.5與DeepSeek交集共識；漂移檢測設計原則 |
| 方向盘 > 发动机 | 方向盤 > 引擎 | Steering Wheel > Engine | 台灣IT和日常隱喻中 engine 慣用「引擎」而非「發動機」 |
| 沉默省略仍是弱实践 | 沉默省略仍是弱實踐 | Silent Omission Is Still Weak Practice | 漂移檢測中不記錄省略也是問題；英文偏地道可接受（作為原則/警示語追求可讀性） |
| 离散审查测不出连续漂移 | 離散審查測不出連續漂移 | Discrete Reviews Cannot Detect Continuous Drift | OPEN-1核心表述；「测」→「測」為兩岸一致轉換 |
| 规则只增不减 | 規則只增不減 | Rules Only Increase, Never Decrease | 防止「狼來了」效應；「减」→「減」為兩岸一致轉換 |

## D: 操作术语 — 59条

框架中的高频操作概念。分为四个子类：
- **D-EN** 纯英文保留词（不翻译）
- **D-OP** 操作概念（有实质翻译需求）
- **D-WF** Workflow模式名（§6.2专属）
- **D-MF** 方法论/实验术语

| 简体中文 | 正体中文（台湾） | English (US) | 说明 |
|---------|-------------------|-------------|------|
| Creator-Verifier | Creator-Verifier | Creator-Verifier | §6.2模式7；獨立驗證模式；不翻譯 |
| HG-0/HG-1/HG-2/HG-3 | HG-0/HG-1/HG-2/HG-3 | HG-0/HG-1/HG-2/HG-3 | 人類閘門編號，不翻譯；三語嚴格保持一致無空格 |
| Major/Minor/Patch 升级 | Major/Minor/Patch 升級 | Major/Minor/Patch Upgrade | §2.6；三級版本升級規則 |
| PocketFlow | PocketFlow | PocketFlow | 外部參考專案，不翻譯 |
| Protocol 3 | Protocol 3 | Protocol 3 | 框架內部審查協議編號，不翻譯 |
| agent | agent | agent | 保留英文小寫 |
| checkpoint | checkpoint | checkpoint | 保留英文小寫 |
| gate | gate | gate | 閘門；保留英文小寫 |
| kill-test-first | kill-test-first | kill-test-first | skill名稱，不翻譯 |
| pipeline | pipeline | pipeline | 保留英文小寫 |
| prompt-tdd | prompt-tdd | prompt-tdd | 外部參考專案，不翻譯 |
| workflow | workflow | workflow | 保留英文小寫 |
| 五级证据分类 | 五級證據分類 | Five-Tier Evidence Classification | [S]/[E]/[I]/[J]/[Sp]五級體系 |
| 任务可供性 | 任務可供性 | Task Affordance | §9.10；任務特徵是否可供AI有效執行 |
| 会话交接（Session Handoff） | 對話交接（Session Handoff） | Session Handoff | §9.3；AI對話間的狀態傳遞（非技術session） |
| 假多样性 | 假多樣性 | Pseudo-Diversity | §6.2模式3；看似多模型審查實則同源偏差 |
| 冗余暴露/一致维护暴露/审查附带暴露 | 冗餘暴露/一致維護暴露/審查附帶暴露 | Redundancy-Driven Discovery / Consistency-Maintenance Discovery / Review-Incidental Discovery | §7.7.2；Exposure 在此為 reveal/discovery 義，非風險暴露 |
| 半开放方法论 | 半開放方法論 | Semi-Open Methodology | §1.8；部分公開、部分封存的研究方法 |
| 单模型证据主导 | 單模型證據主導 | Single-Model Evidence Dominance | §1.8；多數證據來自單一模型後端的局限 |
| 参考实现 | 參考實作 | Reference Implementation | §1.7；台灣IT習慣用「實作」而非「实现」 |
| 双评分者盲评协议 | 雙評分者盲評規程 | Dual-Rater Blinded Scoring Protocol | 台灣研究語境「協議」非最佳；protocol 在此為規程/方案義 |
| 可复现性声明 | 可重現性聲明 | Reproducibility Statement | §2.2, §9.1；台灣習慣用「重現」而非「复现」 |
| 后端切换判据 | 後端切換判據 | Backend-Switching Criteria | §9.2；何時應切換獨立審查後端的判斷標準 |
| 声明式管道执行（Pipeline DAG） | 宣告式管線執行（Pipeline DAG） | Declarative Pipeline Execution (Pipeline DAG) | §6.2模式8；「声明」→「宣告」為台灣IT習慣（declarative→宣告式） |
| 多后端审查链 | 多後端審查鏈 | Multi-Backend Review Chain | §14；使用多個AI模型後端串聯審查 |
| 完备性审查（completeness critic） | 完備性審查（completeness critic） | Completeness Critic | §6.2模式6；角色名非泛化活動名，保留 Critic |
| 完成标准 | 完成標準 | Completion Criteria | §4.3；任務完成的客觀判定標準 |
| 审查维度互补设计 | 審查維度互補設計 | Complementary Review-Dimension Design | §9.2；不同審查輪次檢查不同維度 |
| 审查频率适应性上调 | 審查頻率適應性上調 | Adaptive Review Frequency Increase | §9.2；Protocol 3實證發現 |
| 对抗验证（adversarial verify） | 對抗驗證（adversarial verify） | Adversarial Verification | §6.2模式3；保留英文括注 |
| 对照实验 | 對照實驗 | Controlled Experiment | 「实验」→「實驗」為兩岸一致轉換 |
| 屏障并行（barrier parallel） | 屏障並行（barrier parallel） | Barrier Parallel | §6.2模式2；「并」→「並」為兩岸一致轉換 |
| 捷径审计（shortcut audit） | 捷径稽核（shortcut audit） | Shortcut Audit | CK4；檢查AI是否走捷徑而非深度分析；台灣IT/治理語境 audit→稽核 |
| 文件系统作IPC | 檔案系統作IPC | File System as IPC | 附錄H.1；反面模式 |
| 最低强制核心 | 最低強制核心 | Minimum Mandatory Core | §1.7；框架不可削減的最小集合 |
| 格式效应 | 格式效應 | Format Effect | §6.3.1；prompt格式對LLM輸出的影響 |
| 模型家族 | 模型家族 | Model Family | §9.6.1；同一模型系列的不同版本（如GPT-5→GPT-5.5） |
| 比较型/维护型/审查型/执行型/失败型/使用型/时漂型/缺失型 | 比較型/維護型/審查型/執行型/失敗型/使用型/時漂型/缺失型 | Comparative / Maintenance / Review / Execution / Failure / Usage / Temporal-Drift / Absence Types | §7.7.3；八種被動觀測渠道 |
| 流水线（pipeline） | 管線（pipeline） | Pipeline | §6.2模式1；台灣IT習慣「管線」而非「流水線」；保留英文括注 |
| 版本号规则 | 版本號規則 | Versioning Rules | §2.6；Major.Minor.Patch三級規則 |
| 硬关卡（hard gate） | 硬關卡（hard gate） | Hard Gate | §6.2模式9；必須通過才能繼續的強制檢查點 |
| 确认偏误（二次确认偏误） | 確認偏誤（二次確認偏誤） | Confirmation Bias (Second-Order Confirmation Bias) | §14；「偏误」→「偏誤」為台灣習慣 |
| 科学门（science gates） | 科學門（science gates） | Science Gates | §4.1.1；實驗設計的品質關卡 |
| 结构化多角色审查（Structured Multi-Role Review） | 結構化多角色審查（Structured Multi-Role Review） | Structured Multi-Role Review | §6.2模式9；「审查」→「審查」為台灣習慣 |
| 结构效应 | 結構效應 | Structure Effect | §6.3.2；工作流描述結構對LLM輸出的影響 |
| 继承层次膨胀 | 繼承層次膨脹 | Inheritance Hierarchy Bloat | 附錄H.3；反面模式 |
| 自指涉节 | 自指涉節 | Self-Referential Section | §1.7；框架中描述框架自身的章節 |
| 规则疲劳 | 規則疲勞 | Rule Fatigue | §2.6；過多規則導致遵守意願下降 |
| 评委团（judge panel） | 評審團（judge panel） | Judge Panel | 台灣更自然用「評審團」；§6.2模式4 |
| 跨模型复现 | 跨模型重現 | Cross-Model Replication | §1.8, §9.6.1；台灣習慣用「重現」而非「复现」 |
| 路径隔离原则 | 路徑隔離原則 | Path Isolation Principle | §6.2模式3；確保審查者不接觸被審查者的上下文 |
| 过度工程 | 過度工程 | Overengineering | §1.4；使用超過需求的框架功能 |
| 迭代至枯竭（loop-until-dry） | 迭代至枯竭（loop-until-dry） | Loop-Until-Dry | §6.2模式5；迭代到無新發現為止 |
| 配套目录 | 配套目錄 | Companion Directory | §1.7；可複數為 Companion Directories；「目录」→「目錄」 |
| 锚定风险/锚定 | 錨定風險/錨定 | Anchoring Risk / Anchoring | §6.2模式9, §9.2；先入為主資訊影響後續判斷 |
| 阴性结果 | 陰性結果 | Negative Result | 假設未獲支持的實驗結果 |
| 阴性结论 | 陰性結論 | Negative Conclusion | §6.3.1；不支持假設的研究結論 |
| 静默失效 | 靜默失效 | Silent Failure | §9.10；AI系統無提示地產出錯誤結果 |
| 预登记（pre-registration） | 預註冊（pre-registration） | Pre-Registration | 研究方法語境下台灣慣用「預註冊」 |

## E: 版本/文档术语 — 9条

与框架版本管控、文档体系相关的术语。

| 简体中文 | 正体中文（台湾） | English (US) | 说明 |
|---------|-------------------|-------------|------|
| CLAUDE.md | CLAUDE.md | CLAUDE.md | 檔案名稱，不翻譯 |
| changelog | changelog | changelog | §14即changelog；保留英文小寫不翻譯；全文標題中可用 Changelog |
| memory/ | memory/ | memory/ | 目錄名稱，不翻譯 |
| project_spec.md | project_spec.md | project_spec.md | §2.2, §8.5；檔案名稱，不翻譯 |
| 反模式清单（附录H） | 反模式清單（附錄H） | Anti-Pattern Catalog (Appendix H) | §1.7, 附錄H；「模式」兩岸一致，「清单」→「清單」 |
| 模板（附录A-G） | 範本（附錄A-G） | Templates (Appendices A-G) | §12；台灣IT習慣用「範本」而非「模板」；「附录」→「附錄」 |
| 版本时间线 | 版本時間線 | Version Timeline | §14；「线」→「線」為兩岸一致轉換 |
| 语义化版本 | 語意化版本 | Semantic Versioning | Major.Minor.Patch；「语义」→「語意」為台灣IT習慣（semantic→語意） |
| 退役判定 | 退役判定 | Sunset Determination | 與'规则退役'（Rule Sunset）統一使用 Sunset 體系；決定規則/產物何時廢止的判斷標準 |

---

## 附录A：翻译规则速查

### A.1 台湾IT术语对照（硬规则）

| 简体 | 正体 | 说明 |
|-----|-----|-----|
| 软件 | 軟體 | 非「軟件」 |
| 数据 | 資料 | 一般上下文；純數值型可保留「數據」 |
| 信息 | 資訊 | IT→資訊科技 |
| 服务器 | 伺服器 |  |
| 文件 | 檔案 | 台灣IT慣用「檔案」 |
| 网络 | 網路 | 台灣IT慣用「網路」 |
| 接口 | 介面 | 台灣IT慣用「介面」 |
| 配置 | 組態 | config→組態 |
| 日志 | 日誌 | 台灣IT慣用「日誌」 |
| 默认 | 預設 | 非「默認」 |
| 命令行 | 命令列 | CLI→命令列介面 |
| 质量 | 品質 |  |
| 代码 | 程式碼 |  |
| 代码块 | 程式碼區塊 |  |
| 源码 | 原始碼 |  |
| 通过(方法) | 透過 | by means of；非「通過」 |
| 通过(物理) | 通過 | pass through |
| 通过(审核/测试) | 通過 | pass review / pass test |
| 实现 | 實作 | implementation |
| 对象 | 物件 | object |
| 声明式 | 宣告式 | declarative |
| 协议(技术) | 協定 | protocol（通訊/規範義） |
| 协议(研究/流程) | 規程 | protocol（研究規範/操作流程義） |
| 模板 | 範本 | template（台灣IT慣用） |
| 复现 | 重現 | replication/reproduce |
| 检测 | 偵測 | detection（資訊/訊號偵測） |
| 语义 | 語意 | semantic |
| 审计 | 稽核 | audit（台灣IT/治理語境） |
| 告警 | 警示 | alert（台灣IT慣用） |

### A.2 英文拼写规则（美式）

| 英式 | 美式 | 示例 |
|-----|-----|-----|
| -ise | -ize | organization, analyze, generalizability |
| -our | -or | behavior, color |
| -re | -er | center, theater |
| -ogue | -og | catalog, dialog |

### A.3 不翻译清单

以下标记/编号/文件名**始终保留原文**，不进行任何翻译：

- **证据标注**：`[S]` `[E]` `[I]` `[J]` `[Sp]` `[E-]` `[D/N/A]` `[SEMI-ED]`
- **层编号**：`L0` `L1` `L2` `L3` `L4` `L5` `L-H`
- **闸门编号**：`HG-0` `HG-1` `HG-2` `HG-3`
- **M等级**：`M0` `M1` `M2` `M3` `N/A`
- **内部强度**：`A` `B+` `B` `C+` `C` `D`
- **文件名/路径**：`CLAUDE.md` `project_spec.md` `memory/`
- **项目/工具名**：`Protocol 3` `kill-test-first` `PocketFlow` `prompt-tdd`
- **操作术语**：`Spec` `Context` `Execute` `Review` `Retrospect` `Closure` `workflow` `agent` `pipeline` `checkpoint` `gate` `provenance` `changelog` `Creator-Verifier` `Flow-as-Node`

## 附录B：关键翻译风险提示

1. 「数据」→「资料」：台湾在一般上下文中用「资料」而非「数据」；database→资料库
2. 「通过」的歧义：须区分「透过」(by means of) vs「通过」(pass through) vs「通过」(pass review/test)
3. 「复盘」≠「回顾」：框架对Retrospect有明确定义，不可用一般性「回顾」替代
4. 「封存」≠「关闭/结束」：Closure含归档和条件判定双重语义
5. 「被动观测」→ Opportunistic Observation：更接近主动捕捉意外发现，非消极等待
6. 「交叉验证」→ Cross-Verification：非ML意义的cross-validation，强调异后端验证
7. 框架特有短语如「方向盘>引擎」「分层不互相替代」等须作为整体锚定翻译
8. 所有证据标注、层编号、闸门编号、等级标号均不翻译，这是框架的元语言
9. 「语义化版本」的「语义」→「语意」：台湾IT习惯，semantic→语意（非「语义」）
10. 「模板」→「范本」：台湾IT领域template惯用「范本」
11. 「协议」的歧义：技术/通讯规范→「协定」，研究/操作流程→「规程」
12. 「审计」→「稽核」：台湾IT/治理语境中audit惯用「稽核」
13. 「发动机」→「引擎」：台湾IT和日常隐喻中engine惯用「引擎」
14. 英文术语单独出现保留英文，作为复合词组成部分时使用中文翻译（如gate→「审查门」）
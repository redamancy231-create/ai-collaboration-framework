你是独立审查者 GPT-5.5 (via Codex CLI)。对 AI 协作框架 v1.6 的 JSON 配套文件进行忠实度审查。

## 审查任务

读取以下两个文件并对照：
1. **主文档（源码）**：`./AI协作项目全生命周期框架.md`
2. **JSON 配套（审查对象）**：`./AI协作项目全生命周期框架.json`

## 审查维度

### 1. 元数据忠实度（P0）

逐项核对 JSON `metadata` 字段与 .md 版本头的一致性：
- `version`: 应为 "1.6"
- `date`: 应为 "2026-06-20"
- `model`: 应与 .md 第 5 行一致
- `revision`: 版本号和日期
- `revision_source`: 应覆盖 v1.6 的 7 项新增来源（A2+A3深度复盘 + Codex v1.5.5 + 跨版本实践规范化）
- `status`: 应包含 v1.6 新增节摘要（§9.6.1/§9.10/§4.1.1.1 + §2.6/§1.8/§9.9路径D/附录H）
- `changelog[0]`: 应为 v1.6 条目，包含 7 项 changes、evidence_level、codex_reviews、three_piece_sync、unadopted_downgraded

### 2. 版本时间线

- `version_timeline[-1]` 应为 v1.6 行，日期/版本/事件/证据/置信度与实际一致

### 3. 独立审查记录

- `independent_reviews[-1]` 应记录 Codex v1.6 初审+重审（verdict_initial: FAIL_WITH_MAJOR_ISSUES, verdict_rereview: FAIL_WITH_CAVEATS），报告路径正确

### 4. 新增结构节点（P0）

检查 5 个新增节点是否忠实反映 .md 对应节的内容：

**4.1 `known_limitations`** → 对应 .md §1.8
- limitations 数组应有 8 条局限（不是 6 条）
- 核对第 6 条（探索vs确认张力）和第 7 条（测试集区分度）是否存在
- evidence_level 和 source 与 .md 一致

**4.2 `framework_maintenance`** → 对应 .md §2.6
- key_rules 应包含 versioning/changelog/writeback_review_gate/three_piece_sync/freeze_rules
- transition_clause 应提及"审查门自 v1.6 审查通过后的下一版起生效"

**4.3 `experiment_design_checklist`** → 对应 .md §4.1.1.1
- tier1_hard_gates 应包含 CK1/CK2/CK3
- conditional_items 应包含 CK4/CK5/CK6
- usage 应区分硬门和条件触发

**4.4 `two_dimensional_evidence`** → 对应 .md §9.6.1
- dimension_1_internal 应有 A/B+/B/C+/C/D 六级
- dimension_2_cross_model 应有 M3/M2/M1/M0/N/A 五级
- M1 定义应为"两实验单模型家族"（不是"单模型家族"）

**4.5 `methodological_fragment_three_layer_template`** → 对应 .md §9.10
- layers 应包含 layer_1（问题识别）/layer_2（解决方案）/layer_3（已知反例与失效模式）
- layer_3 应包含静默失效信号相关内容
- pt_m1_example 应提及 Hard Mode 和任务可供性

### 5. 机械一致性

- JSON 中是否所有 "v1.5.5" 引用仅在历史 changelog 和 status 继承段中出现（不应出现在新增节点中）
- `changelog[0].changes` 应为 7 项（v1.6-1 至 v1.6-7）
- `changelog[0].unadopted_downgraded` 应列出复盘 §7.3-§7.7 的降级项并附理由

### 6. 遗漏检查

- .md 中 v1.6 新增的关键限定（如 §4.1.1.1 的 CK6 "37.5% 来自单一未执行设计的审查预期——不作为参数估计推广"）在 JSON 中是否保留
- .md §14 的"未采纳/降级清单"表格是否在 JSON changelog 中有对应

## 判词

PASS / FAIL_WITH_CAVEATS / FAIL_WITH_MAJOR_ISSUES

## 发现格式

[MAJOR/MEDIUM/MINOR] 具体发现（JSON 字段路径 + .md 行号对照 + 修正建议）

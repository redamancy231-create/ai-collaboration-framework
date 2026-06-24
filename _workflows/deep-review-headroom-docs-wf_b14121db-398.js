export const meta = {
  name: 'deep-review-headroom-docs',
  description: '六维度深度审阅三份headroom对标文档：事实准确性/逻辑连贯性/交叉一致性/论证强度/完整性/对抗式验证',
  phases: [
    { title: 'Multi-dimension review', detail: '六维度并行审阅 + 对抗式验证' },
    { title: 'Synthesize', detail: '冲突裁决 + 严重性排序 + 综合报告' }
  ]
}

// ============================================================
// Phase 1: Six-dimension parallel review + adversarial
// ============================================================
phase('Multi-dimension review')

const REVIEW_DIMS = [
  {
    key: 'factual_accuracy',
    prompt: `你是事实准确性审阅者。验证以下三份文档中所有声称的事实是否准确。

文档摘要：
文档A(CacheAligner对标): CacheAligner是headroom中detector-only组件,检测UUID/ISO8601/JWT/HexHash四类易变内容,PR-A2修复移除rewrite路径。与AI框架OPEN-1(§3.6缓慢漂移)对标,提出双层检测架构修正建议。
文档B(SmartCrusher方法论): 五维保留评分(错误项/首尾项/离群/相关性/变点),三阶段决策流(ContentRouter→Lossless-first→CCR兜底),统计工具箱(帕累托稀有状态/Bug#3修复/香农熵/Bug#2修复/变点检测),四个可迁移原理,TOIN学习闭环。
文档C(CCR逃生口案例): CCR四阶段架构(CompressionStore→ToolInjection→ResponseHandler→ContextTracker),分级逃生口模式(L1检索恢复→L2降级继续→L3停止报告),五个安全决策,给框架§4.3的具体措辞建议。

请逐条验证以下类型的事实：
1. 代码引用是否正确？例如"outliers.rs:237-283"、"crusher.rs:690-706"、"statistics.rs:51-83"这些文件和行号范围是否合理？(不需要精确行号,但函数/模块名应对应)
2. headroom项目事实：CacheAligner是否真的是detector-only？PR-A2/P2-23是否真的存在？SmartCrusher的五个维度是否准确描述？CCR的四阶段是否正确？
3. AI框架事实：OPEN-1是否真的是§3.6？§4.3逃生口的三条规则是否准确引用？框架的四个核心信念是否正确？
4. 数字事实：30%阈值(lossless_min_savings_ratio)、96位hash、300秒TTL、50基数上限、2σ阈值等是否正确？
5. 任何你怀疑可能不准确的事实

对于每个发现,标注: [文档名] [章节] 问题描述 + 严重性(致命/重要/次要)`,
    schema: {
      type: 'object',
      properties: {
        findings: { type: 'array', items: { type: 'object', properties: { doc: {type:'string'}, section: {type:'string'}, issue: {type:'string'}, severity: {type:'string', enum:['致命','重要','次要']}, correction: {type:'string'} }, required: ['doc','section','issue','severity'] } },
        overall_accuracy: { type: 'string' }
      }
    }
  },
  {
    key: 'logical_coherence',
    prompt: `你是逻辑连贯性审阅者。检查每份文档内部和跨文档的论证逻辑。

三份文档摘要同上。

请检查：
1. 每份文档的核心论点是否被其子论点有效支持？
2. 是否有循环论证？(例如用"因为detector-only好"证明"OPEN-1应改",但没有独立证明detector-only为什么好)
3. 是否有偷换概念？(例如将"缓存前缀漂移"等同于"项目方向漂移"而不加论证)
4. 类比推理是否恰当？(例如将CacheAligner的rewrite路径类比OPEN-1的AI自我报告——这个类比在哪些方面成立,哪些方面可能不成立?)
5. 三段论是否完整？找出任何隐含前提未被阐明的地方
6. 结论是否从论证中自然导出,还是跳跃过度？

对每个发现标注严重性。`,
    schema: {
      type: 'object',
      properties: {
        findings: { type: 'array', items: { type: 'object', properties: { doc: {type:'string'}, location: {type:'string'}, fallacy_type: {type:'string'}, description: {type:'string'}, severity: {type:'string', enum:['致命','重要','次要']} }, required: ['doc','location','fallacy_type','description','severity'] } },
        overall_coherence: { type: 'string' }
      }
    }
  },
  {
    key: 'cross_consistency',
    prompt: `你是交叉一致性审阅者。检查三份文档之间在共享事实上是否一致。

三份文档摘要同上。

请检查：
1. 三份文档中对同一headroom组件的描述是否一致？(例如CacheAligner在文档A和文档C中的描述、SmartCrusher在文档B和文档C中的描述、CCR在文档B和文档C中的描述)
2. 对AI框架同一章节的引用是否一致？(例如§4.3在文档A、B、C中的引用)
3. 交叉引用节是否准确指向了实际存在的节号？(文档A§7指向文档B§5和文档C§4——这些节号是否存在且内容匹配?)
4. 术语使用是否一致？(例如"detector-only"、"缓慢漂移"、"逃生口"、"有损/无损")
5. 数字事实在三份文档中是否一致？(30%阈值、96位hash、300秒TTL等)

对每个不一致标注严重性和哪份文档需要修正。`,
    schema: {
      type: 'object',
      properties: {
        inconsistencies: { type: 'array', items: { type: 'object', properties: { topic: {type:'string'}, docs_in_conflict: {type:'string'}, description: {type:'string'}, severity: {type:'string', enum:['致命','重要','次要']}, recommended_fix: {type:'string'} }, required: ['topic','docs_in_conflict','description','severity'] } },
        overall_consistency: { type: 'string' }
      }
    }
  },
  {
    key: 'argument_strength',
    prompt: `你是论证强度审阅者。评估每份文档中关键主张的论证支撑力度。

三份文档摘要同上。

请对每份文档的3-5个最关键主张进行评估：
1. 主张是什么？
2. 支撑证据是什么？(代码引用/逻辑推理/类比/权威引用)
3. 证据强度评级：强(直接证据)/中(间接证据或合理推理)/弱(推测或弱类比)
4. 反方观点是否被充分考虑？
5. 如果主张被推翻,会是因为什么？

重点关注：
- 文档A的核心主张："OPEN-1应从AI自我报告改为双层检测架构"——这个主张的证据链有多强？
- 文档B的核心主张："五维保留评分是可迁移的通用模式"——这个主张是否有足够的跨领域证据？
- 文档C的核心主张："框架§4.3应增加L1和L2分级逃生口"——这个主张是否充分考虑了反对意见(ChatGPT-5.5说闸门太多)?

对每个主张给出1-5分的论证强度评分。`,
    schema: {
      type: 'object',
      properties: {
        claims_evaluated: { type: 'array', items: { type: 'object', properties: { doc: {type:'string'}, claim: {type:'string'}, evidence_summary: {type:'string'}, strength_score: {type:'integer', minimum:1, maximum:5}, weakness: {type:'string'} }, required: ['doc','claim','evidence_summary','strength_score'] } },
        overall_strength: { type: 'string' }
      }
    }
  },
  {
    key: 'completeness',
    prompt: `你是完整性审阅者。检查三份文档覆盖了应该覆盖的内容,识别遗漏。

三份文档摘要同上。

请检查：
1. 每份文档在其声明的范围内是否完整？(文档A声称对标CacheAligner和OPEN-1——是否遗漏了重要的对标维度？文档B声称提取方法论——是否遗漏了SmartCrusher的重要设计元素？文档C声称CCR是逃生口案例——是否遗漏了CCR的重要安全属性？)
2. headroom项目中是否有被三份文档集体遗漏的重要组件或概念？(例如:TOIN的隐私影响?压缩的延迟成本?headroom learn功能?)
3. AI框架中是否有被三份文档集体遗漏的相关章节？(例如§9.2独立审查定义?§1.5死亡判据?§10.8 Dev Log成熟度?)
4. "负面空间"——哪些反例或失败案例没有被讨论？(例如:CCR有没有已知的失败案例?CacheAligner有没有漏检的易变模式?)
5. 实践建议是否足够具体？(如果读者想实施文档中的建议,是否知道从哪开始?)

对每个遗漏标注严重性和建议补充的内容。`,
    schema: {
      type: 'object',
      properties: {
        gaps: { type: 'array', items: { type: 'object', properties: { doc: {type:'string'}, gap_description: {type:'string'}, severity: {type:'string', enum:['致命','重要','次要']}, suggested_addition: {type:'string'} }, required: ['doc','gap_description','severity'] } },
        overall_completeness: { type: 'string' }
      }
    }
  },
  {
    key: 'adversarial',
    prompt: `你是对抗式验证者(魔鬼代言人)。你的任务是尝试推翻每份文档中最强的3个主张。

三份文档摘要同上。

对每个主张：
1. 陈述主张
2. 构建最强反驳——站在反对者立场,用最有力的论据试图推翻它
3. 评估反驳的说服力：强(主张可能被推翻)/中(主张需要限定条件)/弱(主张经受住了攻击)
4. 如果反驳成功,主张应该如何修正？

重点攻击目标：
- 文档A："CacheAligner的detector-only哲学适用于OPEN-1"——也许缓存前缀检测和语义漂移检测的差异大到方法论不可迁移？
- 文档B："错误项绝对优先是可迁移的通用原则"——也许在某些领域(如创意写作、头脑风暴)"错误"不是明确定义的？
- 文档C："三级逃生口模式应纳入框架"——也许增加层级会让框架更复杂、更难执行,正好印证ChatGPT-5.5"闸门太多"的批评？
- 文档A+B+C的共同隐含假设："headroom的设计决策对AI协作框架有方法论价值"——也许headroom解决的是工程问题(缓存/压缩),框架解决的是治理问题,两者层次不同,对标本身就是范畴错误？

对每个主张给出反驳强度评分(1-5,5=主张可能被推翻)。`,
    schema: {
      type: 'object',
      properties: {
        refutations: { type: 'array', items: { type: 'object', properties: { doc: {type:'string'}, claim_attacked: {type:'string'}, counter_argument: {type:'string'}, refutation_strength: {type:'integer', minimum:1, maximum:5}, recommended_modification: {type:'string'} }, required: ['doc','claim_attacked','counter_argument','refutation_strength'] } },
        most_vulnerable_claim: { type: 'string' },
        overall_adversarial_assessment: { type: 'string' }
      }
    }
  }
]

const results = await pipeline(
  REVIEW_DIMS,
  dim => agent(dim.prompt, { label: `review:${dim.key}`, phase: 'Multi-dimension review', schema: dim.schema })
)

// ============================================================
// Phase 2: Synthesize
// ============================================================
phase('Synthesize')

const allFindings = results.filter(Boolean).flatMap(r => {
  const key = Object.keys(r)[0]
  return (r.findings || r.inconsistencies || r.gaps || r.claims_evaluated || r.refutations || []).map(f => ({...f, _dimension: key}))
})

const criticalFindings = allFindings.filter(f => f.severity === '致命' || f.strength_score <= 2 || f.refutation_strength >= 4)

const synthesis = await agent(`
你是综合审阅者。以下是六个独立审阅维度的结果。请整合为一份深度审阅报告。

## 输入

### 事实准确性审阅
${JSON.stringify(results[0])}

### 逻辑连贯性审阅
${JSON.stringify(results[1])}

### 交叉一致性审阅
${JSON.stringify(results[2])}

### 论证强度审阅
${JSON.stringify(results[3])}

### 完整性审阅
${JSON.stringify(results[4])}

### 对抗式验证
${JSON.stringify(results[5])}

## 输出要求

生成一份综合审阅报告(中文),结构如下：

# 三份Headroom对标文档深度审阅报告

## 1. 总体评估
- 三份文档的整体质量判断
- 最突出的优点(2-3个)
- 最严重的问题(2-3个)

## 2. 按严重性排序的发现
### 致命问题
### 重要问题
### 次要问题

## 3. 各文档独立评估
每份文档一个简短段落：核心贡献 + 主要问题

## 4. 对抗式验证关键发现
哪些主张经受住了攻击？哪些被削弱了？

## 5. 修正建议优先级
如有需要修正的问题,按优先级排列

## 6. 质量评分
每份文档按以下维度打分(1-10):
- 事实准确性
- 逻辑连贯性
- 论证强度
- 完整性
- 可操作性(建议是否具体可落地)
`, { phase: 'Synthesize' })

return synthesis

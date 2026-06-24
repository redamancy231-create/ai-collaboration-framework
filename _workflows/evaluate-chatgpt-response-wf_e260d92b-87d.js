export const meta = {
  name: 'evaluate-chatgpt-response',
  description: '多视角独立评估 ChatGPT-5.5 对再审查意见的回应，并对抗式核验"是否回避了最关键发现"',
  phases: [
    { title: '独立评估' },
    { title: '对抗验证' },
  ],
}

const DIR = '../AI协作项目全生命周期框架'
const F = {
  response: `${DIR}/AI协作项目全生命周期框架_ChatGPT-5.5对再审查意见的回应.md`,
  rereview: `${DIR}/AI协作项目全生命周期框架_审查报告再审查.md`,
  original: `${DIR}/AI协作项目全生命周期框架_ChatGPT-5.5审查报告.md`,
  framework: `${DIR}/AI协作项目全生命周期框架.md`,
}

const COMMON = `这是一条 AI 互审链路：(1) 框架 v1.1（设计者本人参与）；(2) ChatGPT-5.5 写了独立审查报告；(3) Claude 作为框架设计参与者写了"对抗式再审查"，给原审查打 8/10，提出 4 条异议、4 个盲点、2 个应问未问的问题，核心新发现是"缓慢漂移"——人的审查是离散的（按里程碑/HG），AI 执行是连续的（每轮 Loop），离散审查无法检测连续方向漂移，且 Human Gate 频率天然低于 AI 犯错频率（"AI 登记了但人不看"=阿喀琉斯之踵）；(4) 现在 ChatGPT-5.5 写了"对再审查意见的回应"。

请先用 Read 工具读这四个文件：
- ChatGPT-5.5 的回应（评估对象）：${F.response}
- Claude 的再审查（被回应对象）：${F.rereview}
- ChatGPT-5.5 的原始审查：${F.original}
- 框架主文档（核实事实用）：${F.framework}

全程用中文。你的返回值是结构化数据，不是给人读的寒暄。要给出具体的文件证据（引用原句/小节），不要泛泛而谈。`

const LENS_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['lens', 'items', 'verdict', 'confidence'],
  properties: {
    lens: { type: 'string' },
    items: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['point', 'assessment', 'evidence'],
        properties: {
          point: { type: 'string', description: '评估的具体点' },
          assessment: { type: 'string', description: '判断' },
          evidence: { type: 'string', description: '来自文件的具体证据/引用' },
        },
      },
    },
    verdict: { type: 'string', description: '该视角下对回应的总体裁决（含最尖锐的一句）' },
    confidence: { type: 'string', enum: ['高', '中', '低'] },
  },
}

const VERIFY_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['claim', 'tried_to_refute', 'found_engagement', 'engagement_evidence', 'verdict', 'confidence'],
  properties: {
    claim: { type: 'string' },
    tried_to_refute: { type: 'string', description: '你为反驳该断言做了哪些检索/比对' },
    found_engagement: { type: 'boolean', description: 'ChatGPT-5.5 回应是否真的触及了该发现' },
    engagement_evidence: { type: 'string', description: '若触及，引用原句；若未触及，说明你查遍了哪些小节都没有' },
    verdict: { type: 'string', description: '断言成立 / 部分成立 / 被推翻，及理由' },
    confidence: { type: 'string', enum: ['高', '中', '低'] },
  },
}

phase('独立评估')

const lenses = [
  {
    label: 'lens:回避检测',
    prompt: `${COMMON}

【你的视角：逐项映射，检测回避】把 Claude 再审查中提出的每一条发现，逐一映射到 ChatGPT-5.5 回应的处理状态。再审查的发现包括：
- 第三节 4 条异议：异议1 外部对标类别错配(组织级vs个人级)；异议2 "过度工程"含稻草人倾向(模式库≠必做清单)；异议3 反向偏差确有体现(肯定/批评比例失衡等4个子项a-d)；异议4 验证实验可行性被高估(A/B不可行)。
- 第四节 4 个盲点：盲点1 没检验设计哲学(四核心信念)内部自洽性；盲点2 没评估框架对已有实践的"提炼准确度"(可能把80分实践提炼成60分模板)；盲点3 没识别Human Gate"频率-覆盖"缺口(累积偏差/连续漂移)；盲点4 没给复扩条件。
- 第五节 2 个问题：问题1 最可能失败模式=缓慢漂移(Human Gate阿喀琉斯之踵)；问题2 框架最低上手时间(让非设计者试读计时)。

对每一条，判定 ChatGPT-5.5 的回应是【充分处理/部分处理/实质回避/完全未提】，并给出回应文件中的具体证据(引用小节或原句)。特别注意哪些是被明确接受/部分接受/保留异议，哪些根本没出现在回应里。每个 item 的 point 用"异议N/盲点N/问题N: 简述"。`,
  },
  {
    label: 'lens:保留异议有效性',
    prompt: `${COMMON}

【你的视角：核验保留异议是否站得住】ChatGPT-5.5 在回应第三节保留了 4 条异议(RD1 稻草人指控不完全成立；RD2 Dev Log双视图仍是实质风险；RD3 Closure分档仍不够明确；RD4 反向偏差不削弱核心问题)。逐条判断：这些保留是否在技术与逻辑上站得住？是合理坚持还是死守？特别核验：(a) RD1说"批评重点不是六模式全用而是默认/强制/升级路径不清"——这是否与原审查第五节"Workflow六模式并列…过度工程"的原文一致，还是事后改述(retcon)？请对照原审查原文。(b) RD2"同一Markdown文件的两个section在维护语义上仍是两套索引"——技术上是否成立？(c) RD3 framework里 Closure 是否真的缺项目规模分档？查框架文档。给出每条的裁决。`,
  },
  {
    label: 'lens:框架与定位',
    prompt: `${COMMON}

【你的视角：合并方案与定性框架是否公允】ChatGPT-5.5 把整件事定性为"原审查=问题发现/主要问题输入，再审查=采纳策略输入/把采纳方式调准"。请评估：(1) 这个定性是否公允地对待了再审查的"独立发现"性质？再审查的盲点(尤其盲点2、盲点3)和问题1，本质是关于"框架本身"的新发现(原审查漏掉的)，还是仅仅是"如何采纳原审查"的策略？把它们归入"采纳策略输入"是否变相降格(demote)了再审查的实质贡献、从而让回应得以不正面接战那些盲点？(2) 合并后的行动序列(立即/下个项目/试跑后)+复扩条件表，本身作为给 v1.2 的输入是否完整、可执行、有无自己的缺口？(3) 回应反复强调"原审查核心结论仍成立"——这是稳健，还是一种防守性的立场锚定？`,
  },
  {
    label: 'lens:红队反讽',
    prompt: `${COMMON}

【你的视角：先 steelman 再致命一击 + 元层反讽】(1) 先尽力为 ChatGPT-5.5 的回应辩护：它做对了什么？(承认矛盾、给复扩条件表、合并成可执行方案、不全盘投降也不死守——列出真实优点)。(2) 然后给出对这份回应最致命的一条批评。(3) 元层反讽视角：这份回应本身——结构工整、礼貌收敛、迅速达成"合并共识"、绕开最难啃的对抗内核(缓慢漂移那条)——是否恰好就是再审查所诊断的"缓慢漂移/AI闭环≠人类审查/收敛性附和"的一个活体样本？即：两个 AI 互审最后平滑收口成一份漂亮的合并清单，而那条最有杀伤力的结构性发现在交接中被悄悄稀释掉了。请把这个元层观察讲透，这正是用户(把项目当方法论材料)最想要的角度。`,
  },
]

const evals = await parallel(lenses.map(l => () =>
  agent(l.prompt, { label: l.label, phase: '独立评估', schema: LENS_SCHEMA })))

phase('对抗验证')

const verifies = await parallel([
  () => agent(`${COMMON}

【你的任务：对抗式核验，目标是推翻下面这个断言】
断言：ChatGPT-5.5 的回应【完全没有正面处理】再审查中最重要的发现——"缓慢漂移/累积偏差检测缺口/Human Gate频率-覆盖缺口"(再审查盲点3 + 问题1)。具体即：离散审查无法检测连续漂移、需要在Loop中插入"方向一致性自我报告"、"AI登记了但人不看"是Human Gate的阿喀琉斯之踵。

请尽最大努力反驳这个断言：把 ChatGPT-5.5 回应整篇逐节检查(总体立场/接受意见表/保留异议/修正结论/行动序列/复扩条件/最终裁定)，找出任何一处哪怕间接触及了"累积漂移/连续vs离散审查/方向一致性自我报告/HG频率低于犯错频率"的文字。注意区分：回应里提到的"HG-2粒度过粗/分级"是原审查就有的旧点，不等于触及"频率-覆盖缺口/连续漂移"这个再审查的新点——不要把这两者混为一谈。若确实找不到任何正面处理，则断言成立。`,
    { label: 'verify:缓慢漂移是否被回避', phase: '对抗验证', schema: VERIFY_SCHEMA }),
  () => agent(`${COMMON}

【你的任务：对抗式核验，目标是推翻下面这个断言】
断言：ChatGPT-5.5 的回应【完全没有处理】再审查盲点2——"没有评估框架对已有实践的提炼准确度"(即框架是否把用户已有的80分实践提炼成了60分的形式化模板；这与'有没有外部对标'是两个不同问题)。

请尽力反驳：逐节检查回应全文，找任何触及"提炼准确度/对已有实践形式化是否失真/是否把好实践做差了"的文字。同时核验：盲点1(设计哲学内部自洽性检验)被 ChatGPT 以"原审查低估框架核心信念自洽性→部分接受"处理了，但它是否接战了再审查更尖锐的那层意思——"在信念层找矛盾比在实施层找6条过度工程杀伤力大得多，原审查跳过信念层是深度局限"？给出裁决。`,
    { label: 'verify:提炼准确度与信念层', phase: '对抗验证', schema: VERIFY_SCHEMA }),
])

return {
  evaluations: evals.filter(Boolean),
  verifications: verifies.filter(Boolean),
}

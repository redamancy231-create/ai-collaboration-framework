export const meta = {
  name: 'analyze-claude-code-guide',
  description: '多维度分析 Claude Code Ultimate Guide 项目：结构、内容质量、技术架构、作者方法论文档实践、可用性',
  phases: [
    { title: 'Scout', detail: '并行侦察各子系统：guide/examples/tools/whitepapers/quiz/mcp-server/scripts' },
    { title: 'Deep Read', detail: '深度阅读关键文件：主指南、模板、MCP服务器源码、工作流定义' },
    { title: 'Synthesize', detail: '综合分析与报告撰写' },
    { title: 'Red Team', detail: '红队质疑：盲点、过时、方法论缺陷、组织问题' },
  ]
}

// ===== PHASE 1: Scout =====
phase('Scout')

log('启动7路并行侦察...')

const scoutResults = await parallel([
  // 1. Guide structure
  () => agent(`Explore the guide/ directory structure thoroughly. Read the table of contents from guide/ultimate-guide.md (first 200 lines at least), and key sections. Tell me:
1. What are the main chapters/sections?
2. How deep does the coverage go?
3. What's the overall organization quality?
4. Any obvious gaps or outdated content?
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/`, {label: 'scout:guide'}),

  // 2. Examples/templates
  () => agent(`Explore the examples/ directory comprehensively. List all subdirectories, count templates, and read a sample from each major category (agents, commands, hooks, skills, scripts, workflows, MCP configs, etc.). Tell me:
1. What categories of templates exist and how many in each?
2. What's the quality of these templates?
3. Are they production-ready as claimed?
4. What's missing?
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/examples/`, {label: 'scout:examples'}),

  // 3. Tools and scripts
  () => agent(`Explore the tools/, scripts/, and quiz/ directories. Read key scripts to understand their function. For quiz/: read quiz/src/ to understand the quiz engine. Tell me:
1. What utilities exist?
2. What scripts are provided and what do they do?
3. How does the quiz system work? (read quiz/src/ files)
4. Are there tests?
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/`, {label: 'scout:tools'}),

  // 4. MCP server
  () => agent(`Explore the mcp-server/ directory thoroughly. Read the source code in mcp-server/src/ and the content in mcp-server/content/. Tell me:
1. What does this MCP server do?
2. What's the architecture?
3. What content does it serve?
4. Quality assessment of the code
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/mcp-server/`, {label: 'scout:mcp-server'}),

  // 5. Whitepapers
  () => agent(`Explore the whitepapers/ directory. Read a few .qmd files from both en/ and fr/ to understand the format and content. Tell me:
1. What topics do the whitepapers cover?
2. What's the quality of the EN translations?
3. How are they built? (check for build scripts)
4. Are they substantive or superficial?
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/whitepapers/`, {label: 'scout:whitepapers'}),

  // 6. CI/CD and project infra
  () => agent(`Explore .github/, .claude/, .agents/, .codex/, pre-commit config, and any CI files. Tell me:
1. What CI/CD pipelines exist?
2. What Claude Code custom configs does this project use (commands, hooks, agents, skills)?
3. How does the project dogfood Claude Code?
4. What pre-commit hooks are configured?
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/`, {label: 'scout:infra'}),

  // 7. Machine-readable and docs
  () => agent(`Explore machine-readable/, docs/, claudedocs/, and the cheatsheet. Read machine-readable/reference.yaml to understand the index structure. Check docs/resource-evaluations/ for a few samples. Tell me:
1. How is the machine-readable reference structured?
2. What's in docs/ vs claudedocs/?
3. What are the resource evaluations?
4. Quality of the cheatsheet
Base path: https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/`, {label: 'scout:docs'}),
])

// Compress scout results
const scoutSummary = {}
for (const r of scoutResults.filter(Boolean)) {
  scoutSummary[r._label || 'unknown'] = r
}

log(`侦察完成: ${scoutResults.filter(Boolean).length}/7 路返回数据`)

// ===== PHASE 2: Deep Read =====
phase('Deep Read')

log('深度阅读关键文件...')

const deepReads = await parallel([
  // Read the main guide deeply
  () => agent(`Read https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/ultimate-guide.md comprehensively. This is a ~20K line file. Read it in chunks if needed (offset/limit). Focus on:
1. The overall structure and flow
2. How well it teaches Claude Code concepts
3. Accuracy of technical claims (compare against what you know about Claude Code)
4. Gaps or outdated sections
5. Writing quality and clarity
6. Use of examples and practical guidance
Start from the beginning and read progressively.`, {label: 'deep:main-guide'}),

  // Read key templates deeply
  () => agent(`Deep-read these specific files from https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/examples/:
- A few agent templates (pick the most interesting ones)
- Several hook examples (both bash and PowerShell)
- A few skill definitions
- The workflows examples
- MCP config examples

Evaluate each for:
1. Production readiness
2. Best practice adherence
3. Completeness of error handling
4. Documentation quality within templates
Report specific findings with file paths.`, {label: 'deep:templates'}),

  // Analyze CHANGELOG for project evolution
  () => agent(`Read https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/CHANGELOG.md (it's 601KB - read portions from the beginning, middle, and end to understand the evolution). Tell me:
1. How frequently is the project updated?
2. What's the version history pattern?
3. Major milestones or pivots?
4. How well are changes documented?
5. Is the changelog useful or bloated?`, {label: 'deep:changelog'}),

  // Read IDEAS.md and assess roadmap
  () => agent(`Read https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/IDEAS.md fully. Also check CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md. Tell me:
1. What's planned for the future?
2. How mature is the contribution process?
3. What community norms are established?
4. Is there a clear project governance model?`, {label: 'deep:governance'}),
])

log(`深度阅读完成: ${deepReads.filter(Boolean).length}/4`)

// ===== PHASE 3: Synthesize =====
phase('Synthesize')

log('开始综合分析与报告撰写...')

const synthesis = await agent(`You are synthesizing a comprehensive analysis of the "Claude Code Ultimate Guide" project.

## Project Context
- GitHub: https://github.com/FlorianBruniaux/claude-code-ultimate-guide
- Version: 3.41.1
- 4984 stars, 662 forks
- ~26K lines of documentation, 314 templates, 334 quiz questions
- License: CC BY-SA 4.0
- Primary language: Markdown/Python
- Author: [项目作者], Founding Engineer @ Méthode Aristote

## Scout Findings Summary:
${JSON.stringify(scoutSummary, null, 2)}

## Your Task
Write a comprehensive analysis report in Chinese covering these dimensions:

### 1. 项目概况与定位
- What is this project, who is it for?
- Market positioning and audience

### 2. 内容质量评估
- Accuracy of technical claims
- Completeness of coverage
- Writing quality
- Currency (is it up to date?)

### 3. 组织结构与架构
- Repository structure quality
- Cross-referencing effectiveness
- Build/deploy pipeline maturity

### 4. 模板与实战价值
- Are the 314 templates actually useful?
- Production readiness
- Best practice alignment

### 5. 技术实现
- MCP server quality
- Quiz system
- Scripts and automation
- Machine-readable formats

### 6. 作者的方法论
- What does the project reveal about the author's approach to documentation?
- Dogfooding patterns
- Community building strategy

### 7. 与官方文档的关系
- How does it differ from/improve on official Anthropic docs?
- What unique value does it add?

### 8. 评分卡 (Scorecard)
- Overall quality: /10
- Accuracy: /10
- Completeness: /10
- Usability: /10
- Production value: /10
- Innovation: /10
- Maintenance health: /10

Format as a detailed markdown report. Be specific, cite file paths and examples. Don't pull punches - be critical where warranted.`, {label: 'synthesis', model: 'opus'})

log('综合分析完成，进入红队阶段...')

// ===== PHASE 4: Red Team =====
phase('Red Team')

const redTeam = await agent(`You are a red team auditor. Your job is to find flaws, blind spots, risks, and issues in the "Claude Code Ultimate Guide" project that the synthesis might have missed or softened.

## Project Context
- Version 3.41.1, 4984 stars, 662 forks
- ~26K lines of documentation
- Author: [项目作者], solo maintainer
- License: CC BY-SA 4.0

## Red Team Questions to Answer:

1. **单一维护者风险**: This seems to be a solo project. What happens if the author steps away? Is there a succession plan?

2. **版本追踪负担**: The project tracks Claude Code releases. With ~26K lines of docs referencing specific version numbers, how sustainable is this? Look for version drift.

3. **Claims vs Reality**: The project claims "314 production templates" and "334 quiz questions." Are these inflated? Are templates truly "production-ready" or just examples?

4. **准确性问题**: Given that Claude Code updates frequently (weekly releases), how much of the guide is likely already outdated? Check for stale references.

5. **深度 vs 广度**: Is the guide comprehensive but shallow, or does it go deep where needed?

6. **原创性**: How much is original work vs. reorganized official documentation?

7. **安全建议准确性**: The project tracks CVEs and provides security hardening. Are the security recommendations sound, or could they mislead?

8. **LLM生成痕迹**: With 556 .md files, is there evidence of AI-generated filler content? Quality over quantity?

9. **多语言维持**: FR and EN whitepapers - is translation quality maintained?

10. **依赖与构建复杂度**: How many tools/formats are required to contribute? Is the build system over-engineered?

Be harsh but fair. Point to specific evidence. If you can't verify a claim, flag it as unverified.`, {label: 'red-team', model: 'opus'})

// ===== FINAL: Merge and Write Report =====
phase('Finalize')

log('撰写终期报告...')

const finalReport = await agent(`Combine the synthesis and red team findings into a final comprehensive report.

## Synthesis
${synthesis}

## Red Team Findings
${redTeam}

## Instructions
Write a FINAL comprehensive analysis report in Chinese to:
./claude-code-ultimate-guide-analysis.md

Also write a machine-readable JSON summary to:
./claude-code-ultimate-guide-analysis.json

The report should:
1. Include metadata header with model provenance (model: DeepSeek-v4-pro via Claude Code workflow)
2. Structure: Executive Summary → 8 Dimensions → Red Team → Scorecard → Recommendations → Appendix
3. The JSON should mirror the same structure for machine consumption
4. Be honest, specific, and evidence-based
5. Include concrete file path references
6. Score the project on all dimensions

Write BOTH files.`, {model: 'opus'})

return {
  scout: `7 agents completed`,
  deepRead: `4 agents completed`,
  synthesis: synthesis?.substring(0, 200) + '...',
  redTeam: redTeam?.substring(0, 200) + '...',
  reportPath: './claude-code-ultimate-guide-analysis.md',
  jsonPath: './claude-code-ultimate-guide-analysis.json',
}

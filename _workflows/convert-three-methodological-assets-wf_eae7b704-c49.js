export const meta = {
  name: 'convert-three-methodological-assets',
  description: '将claude-code-guide分析的三个方法论模式转化为用户资产：①框架§3.7漂移检测层 ②独立审查SOP ③元审查合规清单',
  phases: [
    { title: 'Scout', detail: '读取框架v1.2现有结构和相关记忆文件' },
    { title: 'Design', detail: '三路并行设计三个产出' },
    { title: 'Write', detail: '三路并行写入最终文件' },
    { title: 'Cross-check', detail: '交叉验证三件产出的一致性和完整性' },
  ]
}

// ===== PHASE 1: Scout =====
phase('Scout')

log('读取框架v1.2和相关上下文...')

const frameworkMd = await agent(
  `Read the full AI协作项目全生命周期框架 v1.2 main document at:
./AI协作项目全生命周期框架.md

Focus on:
1. §1.4 使用强度分档, §1.5 框架自身死亡判据, §1.6 待决项登记 (especially OPEN-1 缓慢漂移)
2. §3 L-H Human Gate layer — all subsections §3.1 through §3.6, especially §3.6 缓慢漂移/频率-覆盖缺口
3. §9.2 独立审查定义
4. §14 变更记录 v1.1→v1.2

Return: the exact structure of §3 (subsection titles and line ranges), the current OPEN-1 description, the §9.2 definition, and where new content should be inserted.`,
  {label: 'scout:framework'}
)

const frameworkJson = await agent(
  `Read the JSON version at:
./AI协作项目全生命周期框架.json

Focus on:
1. The overall JSON schema/structure
2. How sections are organized in the JSON
3. The decisions_log or changelog structure
4. How OPEN-1 is represented

Return: key structural observations + relevant JSON paths for where new fields need to be added.`,
  {label: 'scout:json'}
)

const contextEngineeringSource = await agent(
  `Read the context engineering guide from the analyzed project:
https://github.com/FlorianBruniaux/claude-code-ultimate-guide/blob/main/guide/core/context-engineering.md

Extract the core concepts that are most relevant for integration into an AI collaboration framework:
1. The five friction signal types (syntactic/semantic/procedural/alignment/performance) — define each
2. The PR-based closed-loop curation mechanism
3. The rule retirement/dormancy detection mechanism
4. The constitutional audit pattern
5. The L0-L5 maturity scale

Return: a structured extraction of these 5 concepts with enough detail to design an integration.`,
  {label: 'scout:source-material'}
)

log(`侦察完成，进入设计阶段...`)

// ===== PHASE 2: Design (parallel) =====
phase('Design')

const [designDrift, designSOP, designMetaAudit] = await Promise.all([
  // Design 1: Framework §3.7 漂移检测层
  agent(
    `## Task: Design Framework §3.7 漂移检测层

### Context
The user's AI协作项目全生命周期框架 v1.2 has an unresolved issue OPEN-1: "缓慢漂移 — 离散审查测不出连续漂移". The framework's §3 (L-H Human Gate) currently goes §3.1-§3.6. We need to design §3.7 as a new drift detection layer.

### Source Material to Adapt
From the Claude Code Ultimate Guide's context engineering guide (~2300 lines), extract and adapt:
1. **Five friction signal types** to map to framework monitoring:
   - syntactic: format/lint violations, schema mismatches
   - semantic: inconsistent claims, provenance gaps, logic errors
   - procedural: skipped steps, missing gates, checklist drift
   - alignment: outputs not matching registered intent/rules
   - performance: quality scores trending down, review rejection rate increasing

2. **Rule retirement automation**: Every rule/constraint written into the framework gets:
   - A "last-triggered" timestamp
   - A "dormancy threshold" (e.g., not triggered in 3 cycles → review)
   - An "auto-sunset" condition (e.g., 5 cycles untouched → deprecate)

3. **Constitutional audit**: Periodic gate that doesn't ask "is this correct?" but "does actual behavior deviate from registered rules?"
   - Compare last N sessions against registered constraints
   - Flag rules that are consistently violated (too strict/unrealistic)
   - Flag rules that are never triggered (dead code in the framework)

4. **Closed-loop curation**: When drift is detected, don't just roll back — curate:
   - If rule violated → rule may be too strict → revise
   - If rule dormant → rule may be obsolete → sunset
   - If new pattern emerged → register as new rule

### Design Requirements
- §3.7 should be ~200-400 lines in the final md
- Must reference §3.6 (existing drift discussion) and OPEN-1
- Must include: detection mechanisms, response protocols, measurement metrics
- Must fit the framework's existing tone (Chinese, technical but accessible, methodical)
- Should include a concrete monitoring template/schema

### Current Framework Context
${frameworkMd}

Return the COMPLETE text of §3.7 as it should appear in the framework, with subsection numbering (§3.7.1, §3.7.2, etc.).`,
    {label: 'design:drift-layer'}
  ),

  // Design 2: 独立审查SOP
  agent(
    `## Task: Design 独立审查标准操作程序 (SOP)

### Context
The user has:
- A reminder mechanism for independent review (feedback_independent_review_reminder)
- A framework §9.2 that defines independent review
- A multi-model experiment project with "bare environment" checklists
- A core independence criterion: (后端模型是否不同) × (上下文是否隔离)

What's missing: a concrete, actionable SOP for executing independent reviews.

### Source Material to Adapt
From the Claude Code Ultimate Guide's adversarial QC pattern:
1. **Four-step process**: ① Fact extraction + source verification → ② Scoring (1-5) → ③ Agent challenges initial assessment → ④ Final judgment
2. **Public audit trail**: All reviews published with score adjustment records
3. **Confidence tiers**: Tier 1 (official doc verified) / Tier 2 (70-90% reverse-engineered) / Tier 3 (40-70% community-inferred)

### Adaptation for User's Context
The source uses same-backend agents for adversarial review — this does NOT meet the user's independence criterion. The adaptation must:
- Require DIFFERENT backends for the challenging reviewer (not just a different agent on the same model)
- Require ISOLATED context (no shared memory, no shared framework documents)
- Include a provenance verification step (confirm backend identity before accepting review)

### Design Requirements
- ~2 page SOP document (~300-500 lines md)
- Must cover: when to trigger, who does what, how to verify independence, output format
- Must include a pre-review checklist and post-review verification
- Must be actionable — someone reading it should be able to execute an independent review
- Chinese language
- Standalone document (not embedded in framework), but with forward/backward references to framework §9.2

Return the COMPLETE SOP document text.`,
    {label: 'design:sop'}
  ),

  // Design 3: 元审查合规清单
  agent(
    `## Task: Design 元审查合规清单 (Meta-Audit Checklist)

### Context
The user's framework v1.2 governs AI collaboration projects. But the framework itself is managed using AI collaboration — creating a self-referential loop. The "dogfooding" pattern from the Claude Code Ultimate Guide shows that the project's own .claude/ config should be the living proof of its own best practices.

### What to Design
A meta-audit gate: use the framework's own standards to audit the framework's own compliance.

### Four Check Dimensions

1. **Provenance完整性**: 
   - Does every framework output carry a model provenance header?
   - Are all review chain entries traceable to specific backends?
   - Are any "Claude" labels ambiguous about which backend?

2. **审查独立性**:
   - For each review in the chain, can we verify (后端×上下文隔离)?
   - Are any reviews self-reviews (same backend as author)?
   - Is the independence claim documented per-review or just per-chain?

3. **记忆系统健康**:
   - Are any memory files referencing outdated/obsolete facts?
   - Do memory files contradict each other?
   - Are "last updated" timestamps present and recent?
   - Are there orphaned memories (referenced but missing)?

4. **最佳实践实际使用**:
   - Is the framework's own CLAUDE.md consistent with what the framework recommends?
   - Are the framework's review processes following its own §9.2 independence rules?
   - Does the project use kill-test-first before new methodological claims?
   - Are pre-commit hooks, version sync scripts, etc. actually configured and running?

### Design Requirements
- A checklist document (~200-400 lines md)
- Each check item: condition to verify, pass/fail criteria, remediation action
- A trigger mechanism: when should this audit run? (suggest: per framework version release + monthly)
- An audit log template
- Chinese language

Return the COMPLETE meta-audit checklist document text.`,
    {label: 'design:meta-audit'}
  ),
])

log(`设计完成，进入写入阶段...`)

// ===== PHASE 3: Write (parallel) =====
phase('Write')

const writeResults = await parallel([
  // Write 1: Framework v1.3 update
  () => agent(
    `## Task: Produce Framework v1.3 Deliverables

### What to Write

**File 1**: ./AI协作项目全生命周期框架.md

Read the current v1.2 file, then apply these changes:
1. Insert §3.7 漂移检测层 after §3.6 (the new section text is provided below)
2. Update §1.6 待决项登记: mark OPEN-1 as "已覆盖 → §3.7" (don't delete it, show resolution trail)
3. Update §14 变更记录: add v1.2→v1.3 entry documenting these changes
4. Update the version number to v1.3
5. Update any cross-references that need adjusting due to the new §3.7

**NEW §3.7 TEXT TO INSERT:**
${designDrift}

**File 2**: ./AI协作项目全生命周期框架.json

Update the JSON to reflect:
1. Version → v1.3
2. New §3.7 fields in the schema
3. OPEN-1 resolution metadata
4. Changelog entry for v1.2→v1.3
5. metadata.model → "DeepSeek-v4-pro (via Claude Code CLI shell)"

IMPORTANT: Actually write both files using the Write tool. Read the current files first, then produce the updated versions.`,
    {label: 'write:framework-v1.3'}
  ),

  // Write 2: 独立审查SOP
  () => agent(
    `## Task: Write 独立审查SOP files

Write TWO files:

**File 1**: ../methodological-review-sop.md
**File 2**: ../methodological-review-sop.json

Use the designed content below as the core text. The md file should have:
- Metadata header with model provenance: "DeepSeek-v4-pro (via Claude Code CLI shell)"
- Date: 2026-06-13
- Clear section structure
- Forward reference to: AI协作项目全生命周期框架 §9.2
- Backward reference from framework to this SOP

The JSON should mirror the md structure with metadata.model field.

**SOP CONTENT:**
${designSOP}

IMPORTANT: Actually write both files to disk using the Write tool.`,
    {label: 'write:sop'}
  ),

  // Write 3: 元审查合规清单
  () => agent(
    `## Task: Write 元审查合规清单 files

Write TWO files:

**File 1**: ../meta-audit-checklist.md
**File 2**: ../meta-audit-checklist.json

Use the designed content below as the core text. The md file should have:
- Metadata header with model provenance: "DeepSeek-v4-pro (via Claude Code CLI shell)"
- Date: 2026-06-13
- Four dimensions clearly labeled
- Each check item with: ID, condition, pass/fail criteria, remediation
- Trigger mechanism section
- Audit log template

The JSON should mirror the md structure with metadata.model field.

**CHECKLIST CONTENT:**
${designMetaAudit}

IMPORTANT: Actually write both files to disk using the Write tool.`,
    {label: 'write:meta-audit'}
  ),
])

log(`写入完成，进入交叉验证...`)

// ===== PHASE 4: Cross-check =====
phase('Cross-check')

const crossCheck = await agent(
  `## Task: Cross-verify all three deliverables

Read the final written files:
1. ./AI协作项目全生命周期框架.md (check §3.7, §1.6 OPEN-1 update, §14 changelog)
2. ./AI协作项目全生命周期框架.json
3. ../methodological-review-sop.md + .json
4. ../meta-audit-checklist.md + .json

Verify:
1. **Internal consistency**: Do the three documents cross-reference each other correctly?
2. **Framework consistency**: Does §3.7 fit naturally into the existing framework structure?
3. **SOP completeness**: Is the SOP actually executable?
4. **Meta-audit completeness**: Are all four check dimensions adequately covered?
5. **Provenance compliance**: Do all 6 files (3 md + 3 json) carry model provenance metadata?
6. **OPEN-1 resolution**: Is the resolution trail clear (OPEN-1 → §3.7)?

If you find any issues, FIX them directly by editing the files.
If everything is good, confirm with a summary.

Report what you checked and what (if anything) you fixed.`,
  {label: 'cross-check'}
)

return {
  framework_v1_3: {
    md: './AI协作项目全生命周期框架.md',
    json: './AI协作项目全生命周期框架.json'
  },
  independent_review_sop: {
    md: '../methodological-review-sop.md',
    json: '../methodological-review-sop.json'
  },
  meta_audit_checklist: {
    md: '../meta-audit-checklist.md',
    json: '../meta-audit-checklist.json'
  },
  crossCheck: crossCheck?.substring(0, 300) + '...',
}

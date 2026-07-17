Reading prompt from stdin...
OpenAI Codex v0.144.1
--------
workdir: C:\Users\33455
model: gpt-5.6-sol
provider: packycode
approval: never
sandbox: danger-full-access
reasoning effort: xhigh
reasoning summaries: none
session id: 019f6fa9-4866-7f11-ae2b-595494fb40e2
--------
user
You are adding time-boxed reading paths to a methodology document. The project is at: E:/workspace/projects/ai-collaboration-framework

Read the main document: `AI协作项目全生命周期框架.md` — especially:
- The table of contents (§1-§14)
- The existing reading difficulty annotations in §9.9 (☆☆☆/★☆☆/★★☆/★★★)
- The README's existing "快速导航" table

## Task: Add a "## 时间限阅读路径 | Time-Boxed Reading Paths" section

### Where to add
Add this as a new section in the README, between the existing "快速导航" table and the "子目录命名约定" section.

### Content

Create 4 reading paths, each with a time budget and clear goal:

**🕐 5 分钟 | 5 minutes — 判断是否适合我**
- Read: README + §1.1 核心理念 + §1.8 已知局限
- Goal: Decide if this framework fits your needs

**🕐 30 分钟 | 30 minutes — 理解核心机制**
- Read: §1-§3 (L0 Spec + L-H Human Gate) + §9.9 阅读导航
- Goal: Understand the two most important layers and how to navigate the rest

**🕐 2 小时 | 2 hours — 跑通一个实验**
- Read: §4 L1 Prompt + §4.1.1.1 对照实验设计检查清单 + §6 L3 Workflow
- Goal: Design and execute your first controlled prompt experiment

**🕐 完整采纳 | Full Adoption — 端到端掌握**
- Read: §1-§14 sequentially, then `_protocols-and-tools/` supplementary materials
- Goal: Apply the full framework to a real project from start to closure

### Requirements

- Bilingual format (Chinese primary, English labels)
- Each path must list specific sections to read (with section numbers matching the TOC)
- Reference the existing difficulty annotations (§9.9) where relevant
- Keep it concise — this is a navigation aid, not a replacement for the TOC
- Provenance comment in markdown: "<!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->"

### What NOT to do

- Don't modify the main document
- Don't change other README sections
- Don't add new files

### Output

Show the exact markdown to insert and the exact insertion point in the README.

warning: Skill descriptions were shortened to fit the 2% skills context budget. Codex can still see every skill, but some descriptions are shorter. Disable unused skills or plugins to leave more room for the rest.
2026-07-17T10:40:04.306790Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Force; if (Test-Path -LiteralPath '"'AGENTS.md') { Write-Output \""'`n--- AGENTS.md ---"; Get-Content -Raw -Encoding UTF8 -LiteralPath '"'AGENTS.md' }; Write-Output \""'`n--- git status ---"; git status --short' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 258ms:


    目录: E:\workspace\projects\ai-collaboration-framework


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
d--h--          2026/7/5     12:46                .git                                                                 
d-----          2026/7/5     11:57                .githooks                                                            
d-----          2026/7/5     12:03                .github                                                              
d-----          2026/7/5     11:57                docs                                                                 
d-----          2026/7/5     11:57                en                                                                   
d-----          2026/7/5     11:57                zh-Hant                                                              
d-----          2026/7/5     11:57                _archive                                                             
d-----          2026/7/5     11:57                _mermaid_png                                                         
d-----          2026/7/5     11:57                _protocols-and-tools                                                 
d-----          2026/7/5     11:57                _research                                                            
d-----         2026/7/17     18:29                _review                                                              
d-----          2026/7/9      2:02                _reviews                                                             
d-----          2026/7/5     11:57                _workflows                                                           
-a----          2026/7/5     11:57            503 .gitattributes                                                       
-a----          2026/7/5     11:57            942 .gitignore                                                           
-a----          2026/7/5     11:57            176 .lsp.json                                                            
-a----          2026/7/5     11:57         204202 AI协作项目全生命周期框架.json                                                   
-a----          2026/7/5     11:57         329806 AI协作项目全生命周期框架.md                                                     
-a----          2026/7/5     11:57            379 check.sh                                                             
-a----          2026/7/5     11:57            914 CITATION.cff                                                         
-a----          2026/7/5     11:57          10031 CLAUDE.md                                                            
-a----          2026/7/5     11:57            864 CONTRIBUTING.md                                                      
-a----          2026/7/5     11:57          14781 inventory.csv                                                        
-a----          2026/7/5     11:57          19047 LICENSE                                                              
-a----          2026/7/5     11:57           8090 pre_push_check.py                                                    
-a----          2026/7/5     11:57           2329 project.yaml                                                         
-a----         2026/7/16      1:16          25045 project_status.md                                                    
-a----          2026/7/5     11:57           4233 PUBLISHING.md                                                        
-a----         2026/7/17     18:38          13244 README.md                                                            
-a----          2026/7/5     12:35           9297 reference_files.md                                                   
-a----          2026/7/5     11:57          14606 verify_version_consistency.py                                        
-a----          2026/7/5     11:57              7 VERSION                                                              

--- git status ---
 M README.md
 M project_status.md
?? _review/
?? _reviews/retrospect_2026-07-09.md



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $paths = @('"'E:\\workspace\\projects\\ai-collaboration-framework\\AGENTS.md','E:\\workspace\\projects\\AGENTS.md','E:\\workspace\\AGENTS.md','E:\\AGENTS.md'); foreach ("'$p in $paths) { if (Test-Path -LiteralPath $p) { Write-Output "--- $p ---"; Get-Content -Raw -Encoding UTF8 -LiteralPath $p } }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 146ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; @'"'
from pathlib import Path
for name in ['README.md', 'AI协作项目全生命周期框架.md']:
    p = Path(name)
    data = p.read_bytes()
    print(f'{name}: BOM={data.startswith(bytes([0xEF,0xBB,0xBF]))}, CRLF={data.count(bytes([13,10]))}, LF={data.count(bytes([10]))}')

readme = Path('README.md').read_text(encoding='utf-8')
lines = readme.splitlines()
for i, line in enumerate(lines, 1):
    if '快速导航' in line or '子目录命名约定' in line:
        start=max(1,i-3); end=min(len(lines),i+25)
        print(f'\\n--- README lines {start}-{end} ---')
        for n in range(start,end+1): print(f'{n:4}: {lines[n-1]}')

main = Path('AI协作项目全生命周期框架.md').read_text(encoding='utf-8')
mlines = main.splitlines()
print('\\n--- Main document likely TOC/headings §1-§14 ---')
for i,line in enumerate(mlines,1):
    if i <= 250 and (line.startswith('#') or ('目录' in line and i < 100)):
        print(f'{i:4}: {line}')
print('\\n--- §9.9 occurrences/context ---')
for i,line in enumerate(mlines,1):
    if '9.9' in line and (line.startswith('#') or '阅读导航' in line):
        start=max(1,i-5); end=min(len(mlines),i+120)
        for n in range(start,end+1): print(f'{n:5}: {mlines[n-1]}')
        break
'@ | python -" in E:\workspace\projects\ai-collaboration-framework
2026-07-17T10:40:57.465384Z ERROR codex_core::tools::router: error=Exit code: 1
Wall time: 0.2 seconds
Output:
  File "<stdin>", line 1
    \ufefffrom pathlib import Path
    ^
SyntaxError: invalid non-printable character U+FEFF

 exited 1 in 151ms:
  File "<stdin>", line 1
    \ufefffrom pathlib import Path
    ^
SyntaxError: invalid non-printable character U+FEFF

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $utf8 = [System.Text.Encoding]::UTF8; foreach ($name in @('"'README.md','AI协作项目全生命周期框架.md')) { "'$bytes=[System.IO.File]::ReadAllBytes((Join-Path (Get-Location) $name)); $bom=($bytes.Length -ge 3 -and $bytes[0]-eq 239 -and $bytes[1]-eq 187 -and $bytes[2]-eq 191); $text=$utf8.GetString($bytes); $crlf=([regex]::Matches($text,"`r`n")).Count; $lf=([regex]::Matches($text,"(?<!`r)`n")).Count; Write-Output "$name : BOM=$bom CRLF=$crlf LF-only=$lf" }; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'README.md'; "'$hits = Select-String -InputObject $lines -Pattern '"'快速导航|子目录命名约定' -AllMatches; for ("'$i=0; $i -lt $lines.Count; $i++) { if ($lines[$i] -match '"'快速导航|子目录命名约定') { "'$start=[Math]::Max(0,$i-3); $end=[Math]::Min($lines.Count-1,$i+25); Write-Output "`n--- README lines $($start+1)-$($end+1) ---"; for ($j=$start; $j -le $end; $j++) { '"'{0,4}: {1}' -f ("'$j+1),$lines[$j] } } }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 212ms:
README.md : BOM=False CRLF=195 LF-only=0
AI协作项目全生命周期框架.md : BOM=False CRLF=3786 LF-only=0

--- README lines 132-160 ---
 132: 
 133: ---
 134: 
 135: ## 快速导航
 136: 
 137: | 你想…… | 从这里开始 |
 138: |---------|-----------|
 139: | 了解框架内容 | [`AI协作项目全生命周期框架.md`](AI协作项目全生命周期框架.md) |
 140: | 机器处理/交叉分析 | [`AI协作项目全生命周期框架.json`](AI协作项目全生命周期框架.json) |
 141: | 了解项目当前状态和待办 | [`project_status.md`](project_status.md) |
 142: | 查找特定文件 | [`reference_files.md`](reference_files.md) |
 143: | 查看独立审查记录 | [`_reviews/`](_reviews/) |
 144: | 查看审查 SOP | [`_protocols-and-tools/methodological-review-sop.md`](_protocols-and-tools/methodological-review-sop.md) |
 145: | 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |
 146: 
 147: ---
 148: 
 149: ## 子目录命名约定
 150: 
 151: | 前缀 | 含义 |
 152: |------|------|
 153: | `_` | AI 工作中间产物（不被人类直接消费） |
 154: | 无前缀 | 人类直接消费的核心文件 |
 155: 
 156: `_archive` / `_mermaid_png` / `_reviews` / `_workflows` 均为 AI 工作目录。  
 157: `_protocols-and-tools` / `_research` 人类可读，但非主文档。
 158: 
 159: ---
 160: 

--- README lines 146-174 ---
 146: 
 147: ---
 148: 
 149: ## 子目录命名约定
 150: 
 151: | 前缀 | 含义 |
 152: |------|------|
 153: | `_` | AI 工作中间产物（不被人类直接消费） |
 154: | 无前缀 | 人类直接消费的核心文件 |
 155: 
 156: `_archive` / `_mermaid_png` / `_reviews` / `_workflows` 均为 AI 工作目录。  
 157: `_protocols-and-tools` / `_research` 人类可读，但非主文档。
 158: 
 159: ---
 160: 
 161: ## 三件套约定
 162: 
 163: 主文档同时维护三种格式：
 164: 
 165: | 格式 | 用途 | 消费者 |
 166: |------|------|--------|
 167: | `.md` | 权威版本 | 人类 + AI |
 168: | `.json` | 结构化配套 | 机器（脚本消费、交叉验证） |
 169: | `.docx` | 传统分发 | 人类（Word 阅读/打印） |
 170: 
 171: `.json` 和 `.docx` 均由 `.md` 派生，修改以 `.md` 为准。
 172: 
 173: ---
 174: 

2026-07-17T10:41:21.067469Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when Client(HttpRequest(HttpRequest("http/request failed: error sending request for url (https://developers.openai.com/mcp)")))
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'AI协作项目全生命周期框架.md'; Write-Output '--- Main document lines 1-260 (headings and TOC-like lines) ---'; for ("'$i=0; $i -lt [Math]::Min(260,$lines.Count); $i++) { if ($lines[$i] -match '"'"'^#{1,6} '"' -or "'$lines[$i] -match '"'"'^'"\\s*[-*]\\s+\\[?.*§?[0-9]') { '{0,5}: {1}' -f ("'$i+1),$lines[$i] } }; Write-Output "`n--- §9.9 heading/context ---"; $hit = Select-String -Path '"'AI协作项目全生命周期框架.md' -Pattern '"'^#{1,6}'"\\s+9\\.9|9\\.9.*阅读导航' -Encoding UTF8 | Select-Object -First 1; if ("'$hit) { $start=[Math]::Max(0,$hit.LineNumber-8); $end=[Math]::Min($lines.Count-1,$hit.LineNumber+130); for ($j=$start; $j -le $end; $j++) { '"'{0,5}: {1}' -f ("'$j+1),$lines[$j] } } else { Write-Output '"'No §9.9 heading found'; Select-String -Path 'AI协作项目全生命周期框架.md' -Pattern '阅读导航|☆☆☆|★☆☆|★★☆|★★★' -Encoding UTF8 | Select-Object -First 30 | ForEach-Object { '{0,5}: {1}' -f "'$_.LineNumber,$_.Line } }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 221ms:
--- Main document lines 1-260 (headings and TOC-like lines) ---
    1: # AI协作项目全生命周期框架
   29: ## 目录
   32:    - [1.7 框架自身的架构原则：最小核心 + 示例外挂](#17-框架自身的架构原则最小核心--示例外挂)
   33:    - [1.8 已知局限与诚实声明](#18-已知局限与诚实声明)
   35:    - [2.6 框架自身的维护流程](#26-框架自身的维护流程)
   37:    - [3.6 已知缺口（OPEN-1）](#36-已知缺口待决--open-1连续漂移与-human-gate-频率-覆盖)
   38:    - [3.7 漂移检测层（v1.3 新增）](#37-漂移检测层从离散闸门到连续观测v13-草案)
   40:    - [4.1.1.1 对照实验设计强制检查清单](#4111-对照实验设计强制检查清单)
   44:    - [7.7 被动观测：意外发现的发现机制](#77-被动观测意外发现的发现机制)
   47:    - [9.6.1 证据等级的二维表示](#961-证据等级的二维表示内部强度--跨模型推广性)
   48:    - [9.9 阅读导航与难度分层](#99-阅读导航与难度分层)
   49:    - [9.10 方法论片段模板：三层模型](#910-方法论片段模板三层模型)
   50:    - [9.11 跨层可观测性设计](#911-跨层可观测性设计)
   60: ## 1. 框架总览
   62: ### 1.1 核心理念
   73: ### 1.2 完整生命周期视图
  141: ### 1.3 七层 + 四跨层关切速览
  161: ### 1.4 使用强度分档（最低强制版 / 默认版 / 完整版）
  179: ### 1.5 框架自身的死亡判据
  194: ### 1.6 已知待决项登记（Open Items）
  210: ### 1.7 框架自身的架构原则：最小核心 + 示例外挂
  220: - **最低强制核心**（§1.4 明确列出 + 死亡判据 §1.5 + 闸门规则 §3.2-3.5 + 逃生口 §4.3 + 闭合条件 §8 + §6.3 模式选择决策树）：有合规牙齿，违反会被死亡判据或审查标准捕获
  221: - **规范性参考**（`[Sp]` 推测机制如 §3.7.0/§9.7/§9.8、模板附录 A-G、变更记录 §14、候选 profile 如 §3.7.2.6）：在主文档中以便查阅，但标注了证据等级和启用条件，不等同于强制项
  222: - **导航与元信息**（§9.9、§13、本文档元数据）：辅助读者高效使用框架，不产生合规义务

--- §9.9 heading/context ---
    5: > **生成模型**: DeepSeek-V4-Pro (via Claude Code CLI shell)  
    6: > **发布前订正（2026-06-23，Claude Opus 4.8 via Claude Code CLI）**: 不升版本号的措辞订正与可理解性补充（过期时效声明更新 + 新增 §13.1.2 项目代号说明 + 面向公开读者的口吻中性化）。无机制/证据等级变更。详见 §14「v1.6.4 发布前订正批次」。
    7: > **v1.6.4 新增（2026-06-22，DeepSeek-V4-Pro via Claude Code CLI）**: prompt-tdd A1 Flow-as-Node Tier 0 对照实验写回——新增 §6.3.2 Flow-as-Node 嵌套工作流对照证据 [E-] ceiling-limited（Tier 0 负证据；3/5 类别天花板，ΔF1=0.000）。经 7 轮双后端审查链（Codex GPT-5.5 ×4 + Qwen qwen3.7-max ×3），0 未闭合发现。同时更新 header 元数据新增 A1 写回声明。详见 §14。  
    8: > **v1.6.2 新增（2026-06-21，DeepSeek-V4-Pro via Claude Code CLI）**: 基于用户记忆系统三次被动观测事件（`method_llm_review_coverage_single_run` / `methodology_review_prompt_mechanical_checks` / `todo_verify_glm5_identity`）的跨案例分析，新增 §7.7「被动观测：意外发现的发现机制」。概念经 Codex GPT-5.5 魔鬼代言人独立审查（2026-06-21，总体判断：有条件支持）——审查意见已系统性纳入：定义收紧（不声称"只能被动发现"）、模式降级为"当前已识别"（非完备分类）、补扩展分类框架（待实证）、补 Failure Space（10 种失效模式+硬约束）、深度版 Retrospect 模板增强（发现方式/复核状态/适用边界）。伴随更新：目录、§14 变更记录、§9 跨层交叉引用、附录 C 深度版 Retrospect 模板。详见 §14。  
    9: > **v1.6 新增（2026-06-20，DeepSeek-V4-Pro via Claude Code CLI）**: 本次为 Minor 升级——7 项新增/增强。(P0) 来源为 A2+A3 深度复盘 + Codex v1.5.5 交叉验证：§9.6.1 证据等级二维表示 + §9.10 方法论片段三层模型 + §4.1.1.1 对照实验设计强制检查清单（6 项）。(P1) 来源为跨版本实践规范化 + 审查反馈推导：§2.6 框架维护流程 + §1.8 诚实声明 + §9.9 路径 D + 附录 H 反向交叉引用。详见 §14。**注意**：v1.6 初版由 DeepSeek-V4-Pro 单后端编辑，后经 Codex GPT-5.5 异后端交叉验证（初审→重审，2 MAJOR + 多项 MEDIUM 全部修正闭合，见 §14 及 `_reviews/codex_v16_crosscheck_*`）。
   10: > **Protocol 3 试跑1回写（2026-06-16，Codex CLI 编辑）**: 首次真实试跑"方法论提取方法论"项目已闭合（M-tier，闭合时 14/20 loops；Phase 8 Kimi 核查后修正为闭合后 15/20，58 项发现，0 CRITICAL/MAJOR 遗留）。本次按试跑 Retrospect + Phase 7 系列审查 + `框架级成熟度评估表.md` §9，将 6 项 Protocol 3 改进写回主文档：C1/C5 测量方法、HG-0 Plan/Spec 双审查、审查频率适应性上调、HG 交互留存、C8 ≥2 轮异后端建议、S-tier 降级阈值备注。来源统一标注为"[Protocol 3 试跑1反馈，2026-06-16]"。  
   11: > **Mermaid 可视化转换（2026-06-16，DeepSeek-v4-pro via Claude Code CLI）**: 将 6 处 ASCII/缩进文本图转为 ` ```mermaid ` 代码块（§1.2 生命周期总览 / §3.2 闸门流程图 / §3.7.4 规则退役状态图 / §3.7.6 策展决策树 / §5.2 Loop 循环图 / §6.3 模式选择决策树）。转换方案经 **ChatGPT-5.5 (Codex CLI, GPT-5.5)** 独立审阅确认——两后端在 4/5 优先图上共识、差异点（§3.2 vs §3.7.4 优先级）已通过"全做"调和。遵循选择性转换原则：流程/决策/状态迁移 → Mermaid；伪代码/表格/目录树 → 保留原样。属冻结期白名单内的"修确凿 bug"——ASCII 框线图在不同渲染环境易错位、难维护，Mermaid 不改任何机制内容，仅改展示格式。  
   12: > **PocketFlow 方法论转化 A 类资产写回（2026-06-18，DeepSeek-v4-pro via Claude Code CLI）**: 基于 PocketFlow 三轮独立分析（DeepSeek-V4-Pro / ChatGPT-5.5 / GLM-5.2，2026-06-16~18）产出的 A 类资产（可直接写回框架的方法论改进，无需额外验证实验），本版（v1.5.3）共写回 3 项：(1) **B2 资产 → 新增 §9.9「阅读导航与难度分层」**——按 ☆☆☆/★☆☆/★★☆/★★★ 标注 15 个章节/条目难度，提供 3 条推荐阅读路径；(2) **B1 资产 → 新增 §1.7「框架自身的架构原则：最小核心 + 示例外挂」**——定义核心（主文档强制规则）vs 外挂（配套目录参考实现）的区分标准及 4 种反模式警示；(3) **PF-反模式资产组 → 新增「附录 H: 反模式清单」**——集中收纳 4 条经独立审查确认可迁移性的反模式，原 §6.5.1 文件系统作 IPC 条目迁移至此并新增 PocketFlow 来源 3 条。伴随更新：§1.4 末尾新增对 §9.9 和 §1.7 的交叉引用；§1.6 末尾新增对 §1.7 的交叉引用。所有新增内容标注来源为 "[PocketFlow方法论转化，2026-06-18]"。详见 §14。
   13: > **prompt-tdd A2 实验写回（2026-06-19，DeepSeek-v4-pro via Claude Code CLI）**: prompt-tdd A2 Tier 1 对照实验完成——prep/exec/post 分段 vs 一体式编号列表 prompt，代码审查域、GPT-5.5 (temp=0)、n=24/臂。H1 不被支持（A_flat correctness_rate=0.954 ≥ B_structured=0.935，方向与假设相反）。PF-8 资产从留白 [Sp] 更新为 [E-]（单域实验不支持），诚实记录于 §4.1.1。详见 §14。
   14: > **prompt-tdd A3 实验写回（2026-06-20，DeepSeek-V4-Pro via Claude Code CLI）**: prompt-tdd A3 Action Routing 对照实验完成（v1 + Pilot）——声明式 vs NL 路由描述，GPT-5.5 (temp=0)、中文路由任务、6-15 actions。两个实验均未检测到格式效应（Δ=0, discordant率=0%），经 10 轮审查链确认（含 Codex GPT-5.5 ×4, Qwen qwen3.7-max ×3, 合并/咨询/对齐各×1；非全为同质独立审查轮）。PF-9 资产记录为 [E-]（阴性结论；格式效应在上述条件下不可检测），诚实记录于 §6.3。详见 §14。
   15: > **prompt-tdd A1 实验写回（2026-06-22，DeepSeek-V4-Pro via Claude Code CLI）**: prompt-tdd A1 Flow-as-Node Tier 0 对照实验完成——层级化工作流描述 vs 内容等价的扁平描述，编码 Agent 工作流理解域、GPT-5.5 (temp=0)、n=20/臂。H1 不被支持（Δ median F1 = 0.000, 3/5 类别天花板）。经 7 轮双后端审查链确认（Codex GPT-5.5 ×4 + Qwen qwen3.7-max ×3），0 未闭合发现。PF-A1-001 资产从留白 [Sp] 更新为 [E-] ceiling-limited（Tier 0 负证据；仅 C4/C5 有区分空间且每类 n=4），诚实记录于 §6.3.2。详见 §14。
   16: 
   17: > **冻结期编辑记录（2026-06-14/15，跨天编辑）**: 本文档 v1.5.1 冻结期内的结构性修订由 **GLM-5.2 (via ZCode CLI shell)** 执行（编辑始于 2026-06-14 23:14，免费额度刷新后于 2026-06-15 00:00 继续完成）。**重要 provenance 声明**：GLM-5.2 是框架审查链谱系之外的**第五个后端**（在 GLM-5.2 编辑者介入时，已有 DeepSeek-v4-pro / Opus 4.8 / ChatGPT-5.5 / Kimi-K2.7-Code / Qwen3.7-Max 五个后端，跨四个 CLI house：Claude / Codex / Kimi / Qwen）。GLM-5.2 在本次编辑中**仅承担编辑者角色，非独立审查者**——其修订基于框架自身已记录的证据（Codex 审查报告、§10.8 成熟度评估等）。**本次编辑引入了已标注的编辑者判断（F9 成熟度评估的逐行分级与分布估计、F10 协议 2 冷读 prompt 与判读规则），待独立复核**。所有修订项均为冻结期白名单内的"修确凿 bug / 补零试跑诚实性产物"，无新增 [Sp] 节。**逐条修订清单见 §14「v1.5.1 冻结期编辑记录（GLM-5.2）」**。按框架 §9.2 独立审查标准，本次编辑独立性级别为 **[SEMI-ED]**（编辑独立于内容创作，但 GLM-5.2 的修订指令由用户提供、修订对象由用户选定）。后续独立审查者复核本批次修订时，应：(a) 验证每条修订是否真属"修 bug"而非"加机制"；(b) 验证 GLM-5.2 是否引入了未声明的实质性判断。
   18: > **冻结声明（2026-06-14 起，2026-06-16 已满足解除条件）**: v1.5.1 曾进入冻结期。在完成 ≥1 次真实试跑 + Retrospect 回写（产出《框架级成熟度评估表》初版）之前，**不接受新增 [Sp] / 机制节**。冻结期内只允许：(a) 修确凿 bug（版本漂移/引用失效/编辑错乱）、(b) 执行已设计未跑的协议（OPEN-4 试读、OPEN-1 verify）、(c) 补零试跑即可做的诚实性产物（框架级成熟度表）。**理由**：框架自身已记录"加复杂度比减复杂度容易"的倾向（v1.3.2 修正路线图"二次确认偏误"教训 + v1.5.1 同日 4 个 [Sp] 节连加），但尚未变成执行约束。冻结把教训文字变成纪律。冻结解除条件 = 试跑 1 Retrospect 完成；该条件已由 Protocol 3 试跑1满足，本版为试跑回写。详见 §14。
   19: > **独立审查**: v1.4: ChatGPT-5.5 (5.37) + Kimi-K2.7-Code (5.00) / v1.5: ChatGPT-5.5 C+ (5.43/10) / v1.5.1草案: Codex ChatGPT-5.5 R3(4.3,驳回)→R4(7.2,修改后通过)  
   20: > **状态**: **草案，两次真实试跑已回写（分析型+实验型），仍待多项目验证**（v1.6.4: prompt-tdd A1 实验写回 §6.3.2 [E-] ceiling-limited / v1.6.3: 维护流程补全+诚实声明扩展 / v1.6.2: 被动观测机制 / v1.6: 证据体系升级+维护性增强 / v1.5.5: prompt-tdd A3 实验写回 §6.3.1 [E-] / v1.5.4: prompt-tdd A2 实验写回 §4.1.1 [E-] / v1.5.2 写回 Protocol 3 试跑1反馈；v1.5.1 新增: §3.7.0 事件流健康度监测 [Sp] + §3.7.4.1 自适应权重淘汰 [Sp] + §9.7 经验注入上下文预算规则 [Sp] + §9.8 研究经验对象(REO) [Sp]。方法论来源=Evolver项目分析(arXiv:2604.15097, 综合评分4.1-4.2/10, 四轮独立审查跨三个后端)。完整规格见 `_research/框架v1.5.1_新增节草案.md`。v1.5 新增: §6.2 模式8/9 + §9.2 + §9.6。v1.4 新增: §3.7.2.6/§5.3.1/§6.2/§6.5.1/§9.1/§1.5/§9.4/附录H。v1.3 遗留 OPEN-1~4 状态不变（OPEN-5 已于 v1.5.1 冻结期关闭 → §8.8））  
   21: > **v1.5 方法论来源**: GitNexus分析项目（42K星代码知识图谱工具全量分析+9-agent workflow+三轮独立审查+证据分类实战）。详见 §14 变更记录。  
   22: > **v1.3 更新**: 新增 §3.7 漂移检测层——将 OPEN-1"离散审查测不出连续漂移"从候选草案升级为正式化的连续监测层（五类漂移信号 + 告警聚合 + 规则退役自动化 + 宪法审计 + 闭环策展 + 完整监测模板），设计受 headroom CacheAligner 的 detector-only 哲学启发（只检测不阻断），经 ChatGPT-5.5 独立裁决确认边界。同步更新 §1.6 OPEN-1 为"已操作化 → §3.7，待试跑验证"。详见 §14 变更记录。  
   23: > **v1.2 更新**: 经三模型独立审查链（ChatGPT-5.5 审查 → DeepSeek-v4-pro 再审查 → ChatGPT-5.5 回应 → Opus 4.8 再再审查）校准。本版改动：(1) 状态从"已定稿"改为"草案冻结，等待试跑验证"；(2) 新增 §1.4 使用强度分档（最低强制版/默认版/完整版）；(3) 新增 §1.5 框架自身死亡判据；(4) 新增 §1.6 已知待决项登记 + §3.6 连续漂移与 Human Gate 频率-覆盖缺口（OPEN-1，审查链判定的最高杀伤发现）；(5) 修正 §13.1 外部对标"独特贡献"表述并补个人级/组织级对照表。详见 §14 变更记录。  
   24: > **v1.1 更新**: 新增第 10 章"跨层产物：开发手册（Dev Log）"——基于 ETF 项目 V3.6 代码头部注释实践 + 网友经验，形式化为累积式变更日志 + FK 导航 + 独立于代码的持久化产物  
   25: > **配套文件**: `AI协作项目全生命周期框架.json`、`_reviews/AI协作项目全生命周期框架_对ChatGPT-5.5回应的再再审查.md`（审查链最终意见）、`methodological-review-sop.md` + `.json`（独立审查SOP v1.0.3，框架 §9.2 的操作性落地）、`meta-audit-checklist.md` + `.json`（元审查合规清单 v1.0.3，依据框架 §9.2 派生的执行层工具）。**归档说明**：中文名 v1.0 旧版（`独立审查标准操作程序_SOP.{md,json}` + `元审查合规清单.{md,json}`）已被英文名 v1.0.3 取代，移至 `_archive/`；ChatGPT-5.5 headroom 对标三文档审查的 `.json` 配套已在 v1.5.1 冻结期补齐。
   26: 
   27: ---
   28: 
   29: ## 目录
   30: 
   31: 1. [框架总览](#1-框架总览)
   32:    - [1.7 框架自身的架构原则：最小核心 + 示例外挂](#17-框架自身的架构原则最小核心--示例外挂)
   33:    - [1.8 已知局限与诚实声明](#18-已知局限与诚实声明)
   34: 2. [L0: Spec（项目宪法）](#2-l0-spec项目宪法)
   35:    - [2.6 框架自身的维护流程](#26-框架自身的维护流程)
   36: 3. [L-H: Human Gate（人类闸门）](#3-l-h-human-gate人类闸门)
   37:    - [3.6 已知缺口（OPEN-1）](#36-已知缺口待决--open-1连续漂移与-human-gate-频率-覆盖)
   38:    - [3.7 漂移检测层（v1.3 新增）](#37-漂移检测层从离散闸门到连续观测v13-草案)
   39: 4. [L1: Prompt（任务规格）](#4-l1-prompt任务规格)
   40:    - [4.1.1.1 对照实验设计强制检查清单](#4111-对照实验设计强制检查清单)
   41: 5. [L2: Loop（执行迭代）](#5-l2-loop执行迭代)
   42: 6. [L3: Workflow（多任务编排）](#6-l3-workflow多任务编排)
   43: 7. [L4: Retrospect（回顾沉淀）](#7-l4-retrospect回顾沉淀)
   44:    - [7.7 被动观测：意外发现的发现机制](#77-被动观测意外发现的发现机制)
   45: 8. [L5: Closure（项目闭合）](#8-l5-closure项目闭合)
   46: 9. [跨层关切](#9-跨层关切)
   47:    - [9.6.1 证据等级的二维表示](#961-证据等级的二维表示内部强度--跨模型推广性)
   48:    - [9.9 阅读导航与难度分层](#99-阅读导航与难度分层)
   49:    - [9.10 方法论片段模板：三层模型](#910-方法论片段模板三层模型)
   50:    - [9.11 跨层可观测性设计](#911-跨层可观测性设计)
   51: 10. [跨层产物：开发手册（Dev Log）](#10-跨层产物开发手册dev-log)
   52: 11. [与现有系统集成](#11-与现有系统集成)
   53: 12. [附录：模板与检查清单](#12-附录模板与检查清单)
   54:     - [附录 H: 反模式清单](#附录-h-反模式清单)
   55: 13. [外部参考与定位](#13-外部参考与定位)
   56: 14. [变更记录（v1.1 → v1.6.4）](#14-变更记录v11--v164)
   57: 
   58: ---
   59: 
   60: ## 1. 框架总览
   61: 
   62: ### 1.1 核心理念
   63: 
   64: 本框架描述**如何用 AI 协作跑完一个完整项目**——不是某个具体项目的说明书，而是项目方法的元层次规范。
   65: 
   66: 四个核心信念：
   67: 
   68: 1. **方向盘 > 发动机**：方向正确比算力大更重要。Prompt（方向）弱而 Loop/Workflow（算力）强 = 高效奔向错误方向。
   69: 2. **分层不互相替代**：Spec/Prompt/Loop/Workflow 各管各的问题，上层弱不能靠下层强来弥补。
   70: 3. **从失败中反向沉淀**：Spec 不是一次写对的——是从每次失败和惊喜中反向提炼的。
   71: 4. **AI 内部闭环 ≠ 人类审查**：框架覆盖 AI 能做的事，但关键节点必须有人的判断闸门。
   72: 
   73: ### 1.2 完整生命周期视图
   74: 
   75: ```mermaid
   76: flowchart TD
   77:     L0["<b>L0: Spec（项目宪法）</b><br/>跨任务不变项：架构/约定/红线/质量标准<br/>载体：CLAUDE.md + memory/ + .json"]
   78: 
   79:     L0 -.->|约束所有下层| Cross
   80:     L0 -.->|约束所有下层| HG1
   81:     L0 -.->|约束所有下层| L1
   82:     L0 -.->|约束所有下层| L3
   83: 
   84:     L0 --> Cross
   85: 
   86:     subgraph Cross["跨层关切"]
   87:         direction LR
   88:         C1["可复现性环境"]
   89:         C2["评估度量计划"]
   90:         C3["风险依赖登记"]
   91:     end
   92: 
   93:     Cross --> HG1
   94: 
   95:     HG1["<b>L-H: Human Gate（人类闸门）</b><br/>关键决策点 → 等人确认 → 通过/驳回/修改<br/>触发：重大Spec变更 / Workflow关键产出 / 闭合决策"]
   96: 
   97:     HG1 --> L1
   98: 
   99:     subgraph L1["L1: Prompt（任务规格）"]
  100:         direction LR
  101:         L1A["任务A<br/>[探索型/执行型/审查型]"]
  102:         L1B["任务B<br/>..."]
  103:         L1C["任务C<br/>..."]
  104:     end
  105: 
  106:     L1A --> L2A
  107:     L1B --> L2B
  108:     L1C --> L2C
  109: 
  110:     subgraph L2["L2: Loop（执行迭代）"]
  111:         direction LR
  112:         L2A["任务A自主迭代<br/>[探索8/3 执行5/2 修复3/2]"]
  113:         L2B["任务B自主迭代<br/>..."]
  114:         L2C["任务C自主迭代<br/>..."]
  115:     end
  116: 
  117:     L2A --> L3
  118:     L2B --> L3
  119:     L2C --> L3
  120: 
  121:     L3["<b>L3: Workflow（多任务编排）</b><br/>并行执行 + 交叉验证 + 合成<br/>模式：pipeline / parallel / loop-until-dry / judge-panel"]
  122: 
  123:     L3 --> HG2
  124: 
  125:     HG2["<b>L-H: Human Gate（产出审查）</b><br/>人看结果 → 通过/驳回/修改"]
  126: 
  127:     HG2 --> L4
  128:     HG2 --> Back
  129: 
  130:     L4["<b>L4: Retrospect（回顾沉淀）</b><br/>回顾 → 提炼 → 写回 Spec<br/>[深度/轻量两版]"]
  131: 
  132:     Back["回到 L1 / L0<br/>下一轮任务或修正 Spec"]
  133: 
  134:     L4 --> L5
  135: 
  136:     L5["<b>L5: Closure（项目闭合）</b><br/>判定闭合条件 → 终期产物 → 归档 → 标记 CLOSED<br/>最后一步：Retrospect → 写回跨项目方法论"]
  137: ```
  138: 
  139: > **图1**：框架七层生命周期总览。实线箭头 = 数据/控制流；虚线箭头 = Spec 约束关系。L-H 在流程中出现两次：执行前（闸门）和产出后（审查）。
  140: 
  141: ### 1.3 七层 + 四跨层关切速览
  142: 
  143: | 层 | 名称 | 管什么 | 粒度 | 变化频率 | 现有对应物 |

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'AI协作项目全生命周期框架.md'; "'$hit = Select-String -Path '"'AI协作项目全生命周期框架.md' -Pattern '"'^### 9'"\\.9 ' -Encoding UTF8 | Select-Object -First 1; if (-not "'$hit) { throw '"'§9.9 heading not found' }; "'$start=$hit.LineNumber-1; $end=[Math]::Min($lines.Count-1,$start+120); Write-Output "--- Main document lines $($start+1)-$($end+1) ---"; for ($j=$start; $j -le $end; $j++) { '"'{0,5}: {1}' -f ("'$j+1),$lines[$j] }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 203ms:
--- Main document lines 2301-2421 ---
 2301: ### 9.9 阅读导航与难度分层
 2302: 
 2303: > **来源**：[PocketFlow方法论转化，2026-06-18]。PocketFlow 用 ☆☆☆→★★★ 标注 cookbook 难度，让用户知道从哪开始。本框架全文约 3000 行，对无 AI 协作经验的新读者 intimidating——本节提供同类分层导航。
 2304: 
 2305: **定位**：跨层关切——降低框架入门门槛，帮助不同背景的读者按难度梯度选择入口路径，而非被迫逐节通读。难度标注为 `[Sp]`（推测级），基于框架设计者的单一视角，待读者反馈校准。
 2306: 
 2307: **三级难度定义**：
 2308: 
 2309: | 标注 | 含义 | 典型读者画像 |
 2310: |------|------|-------------|
 2311: | ☆☆☆ 入门 | 概念定义/清单类，可独立阅读，无前置依赖 | 无需 AI 协作经验 |
 2312: | ★☆☆ 基础 | 操作流程类，需理解 AI 协作基本流程 | 至少用 AI 辅助写过代码或文档 |
 2313: | ★★☆ 进阶 | 机制设计类，需实际项目经验支撑理解 | 至少完整跑过 1 个 AI 协作项目 |
 2314: | ★★★ 高级 | 方法论/元层次类，需方法论背景 | 理解框架自身的证据分类体系（§9.6）或等效训练 |
 2315: 
 2316: **章节难度对照表**：
 2317: 
 2318: | 章节 | 难度 | 类型 | 建议阅读时机 |
 2319: |------|------|------|-------------|
 2320: | §1 框架总览 | ☆☆☆ 入门 | 概念定义 | 所有人最先读 |
 2321: | §2 L0 Spec | ☆☆☆ 入门 | 清单/模板 | 紧随 §1，可直接套用 |
 2322: | §3 L-H Human Gate | ★☆☆ 基础 | 操作流程 | 开始第一个项目前 |
 2323: | §4 L1 Prompt | ★☆☆ 基础 | 操作流程 | 开始第一个项目前 |
 2324: | §10 Dev Log | ★☆☆ 基础 | 操作流程 | 可独立使用，随时查阅 |
 2325: | §5 L2 Loop | ★★☆ 进阶 | 机制设计 | 跑完首个项目后精读 |
 2326: | §6 L3 Workflow | ★★☆ 进阶 | 机制设计 | 需要多 Agent 编排时 |
 2327: | §7 L4 Retrospect | ★★☆ 进阶 | 机制设计 | 项目至少完成一个里程碑后 |
 2328: | §8 L5 Closure | ★★☆ 进阶 | 机制设计 | 项目收尾阶段 |
 2329: | §9.1-9.5 操作性跨层关切 | ★★☆ 进阶 | 操作规范（复现/评估/交接/风险/安全） | 跑完首个项目后精读 |
 2330: | §9.6-9.10 方法论跨层关切 | ★★★ 高级 | 方法论/元层次（证据分类/二维等级/MF三层模板/经验注入/REO） | 理解基础工作流后精读 |
 2331: | §9.9 阅读导航 | ☆☆☆ 入门 | 导航工具 | 任何人首次阅读框架前 |
 2332: | §9.10 MF 三层模板 | ★★★ 高级 | 方法论/模板设计 | 理解 §9.6 后精读 |
 2333: | §11 与现有系统集成 | ★☆☆ 基础 | 概念对照 | 按需查阅 |
 2334: | §12 附录 A-G（模板/清单） | ☆☆☆ 入门 | 模板/清单 | 首次使用框架时直接套用 |
 2335: | §12 附录 H（反模式清单）+ §13-14 | ★★☆ 进阶 | 反模式/对标/变更 | 按需查阅 |
 2336: 
 2337: **三条推荐阅读路径**：
 2338: 
 2339: | 路径 | 适用人群 | 阅读顺序 | 预计时间 |
 2340: |------|---------|---------|---------|
 2341: | **A: 最小启动** | 首次接触框架、想立刻开跑 | §1 → §2 → 按需跳至目标章节 | 15–20 min |
 2342: | **B: 标准实践** | 已有 AI 协作经验、想系统化 | §1 → §2 → §3 → §4 → §10 → §5（轻量版）→ §8.8（闭合分档） | 45–60 min |
 2343: | **C: 完整方法论** | 方法论研究者、框架贡献者 | 逐章通读 §1–§14，重点覆盖 §9 全系列（9.1–9.10） | 2–3 h |
 2344: | **D: 方法论迁移者** 🆕 | 已有完整方法论体系、想提取可迁移片段到本框架 | §9.6.1（二维证据等级）→ §9.10（三层MF模板）→ §9.6（证据分类）→ §9.2（独立审查标准）→ 按需查阅附录H（反模式）| 30–45 min |
 2345: 
 2346: **使用说明**：
 2347: 
 2348: 1. **☆章节可速览**：入门级章节以概念和清单为主——已熟悉 AI 协作概念的读者可速览 §1 后直接套用 §2 模板
 2349: 2. **★☆章节建议实操后回读**：基础操作流程的"真值"在跑过一个项目后才显现——首次阅读理解架构即可，完成后回读精进
 2350: 3. **★★章节按需激活**：进阶章节不必一口气读完——遇到对应场景时精读（多 Agent 编排→§6、项目收尾→§8、方法论沉淀→§7）
 2351: 4. **★★★章节是框架的"为什么"**：跨层关切回答的不是"怎么做"而是"为什么这样设计"——不影响操作，但影响判断质量
 2352: 5. **标注本身是 [Sp]**：难度分级基于框架设计者的单一视角——不同背景读者的感知可能差异显著。升级到 `[J]` 需收集 ≥3 位不同背景读者的难度感知反馈
 2353: 
 2354: **与 §1.4 使用强度分档的关系**：§1.4 A/B/C 三档定义**框架本身用多少**（使用强度），本节三条路径定义**从哪开始读**（阅读顺序）。两者正交——C 档用户可从路径 A 开始阅读，A 档用户也可走路径 C 以理解设计理由。不要混淆。
 2355: 
 2356: **与 §1.7 核心 vs 外挂的关系**：§1.7 说明框架材料分布在主文档（核心，必须读）和 4 个配套目录（外挂，按需查），本节则在此结构上叠加难度分层导航——§1.7 管"在哪找"，§9.9 管"从哪开始读"。
 2357: 
 2358: **证据等级**：`[Sp]`（推测）。难度分层核心思想源于 PocketFlow cookbook 的实践惯例（来源可追溯、可验证），但应用于本框架的适用性未经读者验证。升级到 `[J]` 需：(a) 收集 ≥3 位不同背景读者的反馈；(b) 将感知难度与标注对照；(c) 若 ≥2 位读者对同一章节的感知偏差 ≥2 级，启动重标。
 2359: 
 2360: ---
 2361: 
 2362: <a id="910-方法论片段模板三层模型"></a>
 2363: ### 9.10 方法论片段模板：三层模型（v1.6 新增）
 2364: 
 2365: > **来源**：A2+A3 深度复盘报告 §6.1 组合洞察——PT-M1（天花板效应预警）在 A2→A3 的跨实验传递中发生了静默失效：设计者识别了天花板风险但选用了无效缓解方案（Hard Mode），因为 PT-M1 仅描述了"何时应该警惕天花板效应"，未独立描述"什么解决方案在什么前提下可用"和"这个方案在什么情况下会失效"。
 2366: 
 2367: **问题**：当前的方法论片段（MF）模板主要是一层的——核心字段围绕"问题识别条件"（何时警惕 X）。解决方案描述嵌入在正文中，但未系统性地将"解决方案适用条件"和"已知反例/失效模式"独立为字段。PT-M1 的 A2→A3 迁移断裂表明：描述"警惕什么"的知识与描述"怎么做"和"什么情况下不可行"的知识具有不同的逻辑模态，需要独立维护。
 2368: 
 2369: **解决方案**：方法论片段模板从一层升级为三层：
 2370: 
 2371: ```
 2372: [Fragment ID] — [名称] — [分类]
 2373: 
 2374: 第一层：问题识别（Problem Space）
 2375: ├── 核心问题描述
 2376: ├── 问题识别条件：何时应警惕此问题
 2377: └── 检测方法：如何确认问题确实存在（而非类似但不同的问题）
 2378: 
 2379: 第二层：解决方案（Solution Space）
 2380: ├── 推荐解决方案
 2381: ├── 解决方案适用条件（关键新增）：方案在什么前提下可用
 2382: ├── 替代方案（当首选方案不适用时）
 2383: └── 方案选择决策树（可选）
 2384: 
 2385: 第三层：已知反例与失效模式（Failure Space）（关键新增）
 2386: ├── 已知反例：方案在什么情况下被观察到失效
 2387: ├── 失效模式：方案为什么会失效（机制层面）
 2388: ├── 静默失效信号：如何检测方案正在失效但未报告错误
 2389: └── 与其他 MF 的冲突/交互（可选）
 2390: ```
 2391: 
 2392: **三层独立维护规则**：
 2393: 
 2394: 1. **三层回答不同的问题**：第一层回答"警惕什么"（信号），第二层回答"怎么做"（行动的前提），第三层回答"什么时候不该这么做"（已知的陷阱）。三者不可互相替代。
 2395: 2. **第三层是第二层的"测试覆盖"**：每个解决方案的适用条件必须有对应的已知反例覆盖——如果适用条件声称"前提 X 满足时可用"，必须至少有一个反例说明"前提 X 不满足时失效"或"前提 X 满足但前提 Y 冲突时可能失效"。
 2396: 3. **静默失效信号是强制字段**：对于有自动化检测潜力的失效模式，必须在第三层指定可操作的检测信号（如"A2→A3 迁移时，若目标 DV 为二分类且任务可供性=1，则 PT-M1 的标准方案不可用"）。
 2397: 4. **三层可独立更新**：某层的证据增强不要求其他层同步更新——例如跨模型复现确认了第二层的适用条件（跨模型推广性提升），不需要第一层的问题描述也随之改变。
 2398: 
 2399: **示例：PT-M1 的三层表示**：
 2400: 
 2401: ```
 2402: [PT-M1] — 天花板效应预警与解决方案 — [设计审查]
 2403: 
 2404: 第一层：问题识别
 2405: - 核心问题：对照实验中的天花板效应——所有实验条件表现一致接近满分，没有方差可供区分条件
 2406: - 识别条件：(a) 任一条件的准确率/得分接近满分（>95%）；(b) 或条件间方差趋零
 2407: - 检测方法：Tier 0 试点测试（n≥8/条件），计算每个条件的得分均值和方差，若 >95% 天花板 → 正式实验前必须调整
 2408: 
 2409: 第二层：解决方案
 2410: - 推荐方案：切换替代因变量（DV）——找到有足够方差且与原始DV正相关的替代测量维度
 2411: - 适用条件：(a) 任务存在 ≥2 个正交评估维度；(b) 替代维度在实验条件下有足够的期望方差（需在 Tier 0 中预检验）；(c) 替代维度的测量误差可接受
 2412: - 替代方案：(a) 增加任务难度（仅当任务可供性 >1 个维度时有效）；(b) 降级为描述性实验（当任务可供性=1 且无替代DV时）
 2413: - 方案选择决策树：连续DV + 多维度 → 切换替代DV / 二分类DV + 多维度 → 引入辅助连续指标 / 任何DV + 单维度 → 禁止仅靠增加难度
 2414: 
 2415: 第三层：已知反例与失效模式
 2416: - 已知反例（A3 静默失效）：A3 的路由任务是二分类单维度任务——PT-M1 的标准方案（切换替代DV）不可用，但设计者未收到警告 → 选用了无效缓解方案（Hard Mode）
 2417: - 失效机制：不是 PT-M1 "错误"——是它的知识表示不完整。当任务可供性=1 时，"切换DV"的前提不成立，但模板未独立声明这一前提
 2418: - 静默失效信号：若任务可供性=1（单一评估维度），设计者仍选择"增加任务难度/Hard Mode"作为天花板缓解方案（而非降级为描述性实验）→ 触发静默失效告警。A3 的问题不是"选了非标准方案"——是选了形式上像替代方案（增加难度）、前提条件上不适用的方案（单维度任务上增加难度不增加区分度）
 2419: - 跨模型推广性：PT-M1 的失效机制（任务可供性=1）是任务结构层面的约束，不依赖特定模型——预期跨模型可推广（待验证）
 2420: ```
 2421: 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; git diff -- README.md' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 133ms:
diff --git a/README.md b/README.md
index 36f047b..a8c825e 100644
--- a/README.md
+++ b/README.md
@@ -1,12 +1,13 @@
 # AI 协作项目全生命周期框架
 
-**版本**：v1.6.4（2026-06-22）  
-**状态**：Working Paper（持续更新中，引用请注明版本号）  
-**许可**：CC BY 4.0  
-**语言**：简体中文（其他语言译本以简体中文原文为准）  
-**编码**：UTF-8（全部文本文件）  
-**翻译**：[正體中文](zh-Hant/README.md) · [English](en/README.md)  
-**AI 生成声明**：本仓库大部分内容由人机协作生成（详见 [PUBLISHING.md](PUBLISHING.md)）
+这套框架帮助独立创作者把零散的 AI 对话转化为可执行、可验证、可复盘、可封存的完整项目流程。
+
+**适用对象 / For**：个人独立使用 AI 工具推进项目的创作者（solo creators）。  
+**你将获得 / Get**：六层生命周期方法、Prompt-TDD 实验规范、独立审查流程与项目闭合清单。  
+**最快入口 / Start**：打开 [`AI协作项目全生命周期框架.md`](AI协作项目全生命周期框架.md)，先读 §1.4–§1.7。
+
+**版本 / Version**：v1.6.4（2026-06-22）· **状态 / Status**：Working Paper（持续更新；引用请注明版本）· **许可 / License**：CC BY 4.0 · **编码 / Encoding**：UTF-8  
+**语言 / Languages**：简体中文为准 · [正體中文](zh-Hant/README.md) · [English](en/README.md) · **AI 生成 / AI-assisted**：本仓库大部分内容由人机协作生成，详见 [PUBLISHING.md](PUBLISHING.md)
 
 > **English Abstract**: A comprehensive methodology framework for **full-lifecycle human-AI collaboration** — from project initiation, execution, and independent review through to archival. ~68,000 Chinese characters; empirically tested through **3 controlled prompt engineering experiments** (Prompt-TDD) and **50+ rounds of multi-model independent review** across 5 LLM backends. Covers: specification-driven development (Spec Coding), prompt experiment design with evidence grading, multi-agent workflow orchestration, passive observation mechanisms for serendipitous discovery, and project closure protocols. Full **[English translation](en/)** available. The independent review methodology has been extracted as a standalone toolkit: **[Independent Review Toolkit](https://github.com/redamancy231-create/independent-review-toolkit)** — SOP + prompt templates + adversarial challenge framework + real examples. Licensed **CC BY 4.0**.
 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'AI协作项目全生命周期框架.md'; for ("'$i=28; $i -le 56; $i++) { '"'{0,4}: {1}' -f ("'$i+1),$lines[$i] }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 169ms:
  29: ## 目录
  30: 
  31: 1. [框架总览](#1-框架总览)
  32:    - [1.7 框架自身的架构原则：最小核心 + 示例外挂](#17-框架自身的架构原则最小核心--示例外挂)
  33:    - [1.8 已知局限与诚实声明](#18-已知局限与诚实声明)
  34: 2. [L0: Spec（项目宪法）](#2-l0-spec项目宪法)
  35:    - [2.6 框架自身的维护流程](#26-框架自身的维护流程)
  36: 3. [L-H: Human Gate（人类闸门）](#3-l-h-human-gate人类闸门)
  37:    - [3.6 已知缺口（OPEN-1）](#36-已知缺口待决--open-1连续漂移与-human-gate-频率-覆盖)
  38:    - [3.7 漂移检测层（v1.3 新增）](#37-漂移检测层从离散闸门到连续观测v13-草案)
  39: 4. [L1: Prompt（任务规格）](#4-l1-prompt任务规格)
  40:    - [4.1.1.1 对照实验设计强制检查清单](#4111-对照实验设计强制检查清单)
  41: 5. [L2: Loop（执行迭代）](#5-l2-loop执行迭代)
  42: 6. [L3: Workflow（多任务编排）](#6-l3-workflow多任务编排)
  43: 7. [L4: Retrospect（回顾沉淀）](#7-l4-retrospect回顾沉淀)
  44:    - [7.7 被动观测：意外发现的发现机制](#77-被动观测意外发现的发现机制)
  45: 8. [L5: Closure（项目闭合）](#8-l5-closure项目闭合)
  46: 9. [跨层关切](#9-跨层关切)
  47:    - [9.6.1 证据等级的二维表示](#961-证据等级的二维表示内部强度--跨模型推广性)
  48:    - [9.9 阅读导航与难度分层](#99-阅读导航与难度分层)
  49:    - [9.10 方法论片段模板：三层模型](#910-方法论片段模板三层模型)
  50:    - [9.11 跨层可观测性设计](#911-跨层可观测性设计)
  51: 10. [跨层产物：开发手册（Dev Log）](#10-跨层产物开发手册dev-log)
  52: 11. [与现有系统集成](#11-与现有系统集成)
  53: 12. [附录：模板与检查清单](#12-附录模板与检查清单)
  54:     - [附录 H: 反模式清单](#附录-h-反模式清单)
  55: 13. [外部参考与定位](#13-外部参考与定位)
  56: 14. [变更记录（v1.1 → v1.6.4）](#14-变更记录v11--v164)
  57: 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines=Get-Content -Encoding UTF8 -LiteralPath '"'README.md'; for("'$i=90;$i -le 150;$i++){ '"'{0,4}: {1}' -f ("'$i+1),$lines[$i] }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 144ms:
  91: │   ├── 框架级成熟度评估表.{md,json}       — 框架自身成熟度评估 v0.4
  92: │   ├── 外部依赖登记表.{md,json}          — 工具链/模型/平台依赖追踪
  93: │   ├── 可调参数索引.md                   — 魔法数字集中索引
  94: │   ├── import_integrity_check.py        — Python 导入检查工具（已弃用，见主文档 §9.1）
  95: │   ├── AI协作项目全生命周期框架_OPEN4试读计时协议.{md,json}
  96: │   └── AI协作项目全生命周期框架_人类专家verify包.{md,json}
  97: │
  98: ├── _research/                          ← 🔬 案例研究材料
  99: │   ├── CCR作为逃生口案例研究.{md,json}
 100: │   ├── CacheAligner与AI框架OPEN-1对标分析.{md,json}
 101: │   ├── ChatGPT-5.5独立审查_headroom对标三文档.{md,json}
 102: │   ├── SmartCrusher方法论提取.{md,json}
 103: │   ├── headroom对标分析_封存说明.{md,json}
 104: │   ├── 通用框架可行性讨论_20260621.md
 105: │   ├── 两次试跑对比_2026-06-22.md
 106: │   └── drafts/                         — 废弃草案（v1.3.2 / v1.5.1）
 107: │
 108: ├── _reviews/                           ← 🔍 多后端独立审查报告
 109: │   ├── (各版本审查报告 + 交叉验证记录 .md/.json/.txt)
 110: │   ├── prompts/                        — 审查提示词
 111: │   ├── last_messages/                  — CLI 输出片段
 112: │   └── retrospects/                    — 复盘记录
 113: │
 114: ├── _workflows/                         ← ⚙ 构建 + 同步 + 翻译脚本
 115: │   ├── regenerate_docx.py               — DOCX 全量重生成（Mermaid + pandoc + 样式）
 116: │   ├── regenerate_inventory.py          — 重生成 inventory.csv
 117: │   ├── count_chars_v164.py              — 字符级统计
 118: │   ├── sync_v16{1,2,3,4}_docx.py        — 各版本 DOCX 同步（历史）
 119: │   ├── i18n/                            — 翻译管道（术语表 + 翻译/检查脚本 + 审查报告）
 120: │   └── *.js                            — Workflow 定义脚本
 121: │
 122: ├── en/                                  ← 🌐 English translation
 123: │   ├── README.md
 124: │   ├── AI协作项目全生命周期框架.md
 125: │   └── reference_files.md
 126: │
 127: └── zh-Hant/                            ← 🌏 正體中文翻譯
 128:     ├── README.md
 129:     ├── AI协作项目全生命周期框架.md
 130:     └── reference_files.md
 131: ```
 132: 
 133: ---
 134: 
 135: ## 快速导航
 136: 
 137: | 你想…… | 从这里开始 |
 138: |---------|-----------|
 139: | 了解框架内容 | [`AI协作项目全生命周期框架.md`](AI协作项目全生命周期框架.md) |
 140: | 机器处理/交叉分析 | [`AI协作项目全生命周期框架.json`](AI协作项目全生命周期框架.json) |
 141: | 了解项目当前状态和待办 | [`project_status.md`](project_status.md) |
 142: | 查找特定文件 | [`reference_files.md`](reference_files.md) |
 143: | 查看独立审查记录 | [`_reviews/`](_reviews/) |
 144: | 查看审查 SOP | [`_protocols-and-tools/methodological-review-sop.md`](_protocols-and-tools/methodological-review-sop.md) |
 145: | 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |
 146: 
 147: ---
 148: 
 149: ## 子目录命名约定
 150: 
 151: | 前缀 | 含义 |

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $path = Join-Path (Get-Location) '"'README.md'; "'$utf8Strict = [System.Text.UTF8Encoding]::new($false, $true); $text = [System.IO.File]::ReadAllText($path, $utf8Strict); if ($text.Contains('"'## 时间限阅读路径 | Time-Boxed Reading Paths')) { throw 'Target section already exists.' }; "'$marker = "---`r`n`r`n## 子目录命名约定"; if (($text.Split(@($marker), [System.StringSplitOptions]::None).Count - 1) -ne 1) { throw '"'Expected insertion marker exactly once.' }; "'$sectionLines = @('"'## 时间限阅读路径 | Time-Boxed Reading Paths','','> **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。','','### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?','- **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）','- **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.','','### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms','- **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆☆☆ 入门）','- **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.','','### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment','- **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）','- **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.','','### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery','- **阅读 / Read**：按顺序通读 §1–§14，再阅读 "'`_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）'"','- **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.','','<"'!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->'"','','---','','## 子目录命名约定'); "'$replacement = [string]::Join("`r`n", $sectionLines); $newText = $text.Replace($marker, $replacement); [System.IO.File]::WriteAllText($path, $newText, [System.Text.UTF8Encoding]::new($false));' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 165ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'README.md'; "'$start = (Select-String -Path '"'README.md' -Pattern '"'^## 时间限阅读路径 '"\\| Time-Boxed Reading Paths"'$'"' -Encoding UTF8).LineNumber; "'$end = (Select-String -Path '"'README.md' -Pattern '"'^## 子目录命名约定$'"' -Encoding UTF8).LineNumber; Write-Output \"--- README lines "'$($start-3)-$($end+2) ---"; for ($i=$start-4; $i -le $end+1; $i++) { '"'{0,4}: {1}' -f ("'$i+1),$lines[$i] }; $bytes=[System.IO.File]::ReadAllBytes((Join-Path (Get-Location) '"'README.md')); "'$bom=($bytes.Length -ge 3 -and $bytes[0]-eq 239 -and $bytes[1]-eq 187 -and $bytes[2]-eq 191); $text=[System.Text.Encoding]::UTF8.GetString($bytes); $crlf=([regex]::Matches($text,"`r`n")).Count; $lfOnly=([regex]::Matches($text,"(?<!`r)`n")).Count; Write-Output "`nEncoding check: BOM=$bom CRLF=$crlf LF-only=$lfOnly"; Write-Output "`n--- git status --short ---"; git status --short; Write-Output "`n--- diff for inserted section ---"; git diff --unified=3 -- README.md | Select-String -Pattern '"'"'^@@|''^'"\\+## 时间限|"'^'"\\+> \\*\\*难度|"'^'"\\+### 🕐|"'^'"\\+- \\*\\*阅读|"'^'"\\+- \\*\\*目标|"'^'"\\+<"'!-- GPT|''^'"\\+---'" in E:\workspace\projects\ai-collaboration-framework
 succeeded in 234ms:
--- README lines 144-173 ---
 144: | 查看审查 SOP | [`_protocols-and-tools/methodological-review-sop.md`](_protocols-and-tools/methodological-review-sop.md) |
 145: | 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |
 146: 
 147: ## 时间限阅读路径 | Time-Boxed Reading Paths
 148: 
 149: > **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。
 150: 
 151: ### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?
 152: - **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）
 153: - **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.
 154: 
 155: ### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms
 156: - **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆☆☆ 入门）
 157: - **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.
 158: 
 159: ### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment
 160: - **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）
 161: - **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.
 162: 
 163: ### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery
 164: - **阅读 / Read**：按顺序通读 §1–§14，再阅读 `_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）
 165: - **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.
 166: 
 167: <!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->
 168: 
 169: ---
 170: 
 171: ## 子目录命名约定
 172: 
 173: | 前缀 | 含义 |

Encoding check: BOM=False CRLF=217 LF-only=0

--- git status --short ---
 M README.md
 M project_status.md
?? _review/
?? _reviews/retrospect_2026-07-09.md

--- diff for inserted section ---

@@ -1,12 +1,13 @@
@@ -143,6 +144,28 @@ AI协作项目全生命周期框架/
+## 时间限阅读路径 | Time-Boxed Reading Paths
+> **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。
+### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?
+- **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）
+- **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.
+### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms
+- **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆
☆☆ 入门）
+- **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.
+### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment
+- **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）
+- **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.
+### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery
+- **阅读 / Read**：按顺序通读 §1–§14，再阅读 `_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）
+- **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.
+<!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->



exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $path = Join-Path (Get-Location) '"'README.md'; "'$utf8Strict = [System.Text.UTF8Encoding]::new($false, $true); $text = [System.IO.File]::ReadAllText($path, $utf8Strict); $old = "| 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |`r`n`r`n## 时间限阅读路径 | Time-Boxed Reading Paths"; $new = "| 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |`r`n`r`n---`r`n`r`n## 时间限阅读路径 | Time-Boxed Reading Paths"; if (($text.Split(@($old), [System.StringSplitOptions]::None).Count - 1) -ne 1) { throw '"'Expected target exactly once.' }; "'$text = $text.Replace($old, $new); [System.IO.File]::WriteAllText($path, $text, [System.Text.UTF8Encoding]::new($false));' in E:\workspace\projects\ai-collaboration-framework
2026-07-17T10:43:38.144960Z ERROR codex_core::tools::router: error=Exit code: 1
Wall time: 0.2 seconds
Output:
Expected target exactly once.
At line:2 char:727
+ ... ne).Count - 1) -ne 1) { throw 'Expected target exactly once.' }; $tex ...
+                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (Expected target exactly once.:String) [], RuntimeException
    + FullyQualifiedErrorId : Expected target exactly once.
 

 exited 1 in 181ms:
Expected target exactly once.
At line:2 char:727
+ ... ne).Count - 1) -ne 1) { throw 'Expected target exactly once.' }; $tex ...
+                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : OperationStopped: (Expected target exactly once.:String) [], RuntimeException
    + FullyQualifiedErrorId : Expected target exactly once.
 

exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $path = Join-Path (Get-Location) '"'README.md'; "'$utf8Strict = [System.Text.UTF8Encoding]::new($false, $true); $text = [System.IO.File]::ReadAllText($path, $utf8Strict); $old = "`r`n`r`n## 时间限阅读路径 | Time-Boxed Reading Paths"; $new = "`r`n`r`n---`r`n`r`n## 时间限阅读路径 | Time-Boxed Reading Paths"; if (($text.Split(@($old), [System.StringSplitOptions]::None).Count - 1) -ne 1) { throw '"'Expected target exactly once.' }; "'$text = $text.Replace($old, $new); [System.IO.File]::WriteAllText($path, $text, [System.Text.UTF8Encoding]::new($false));' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 151ms:
exec
"C:\\windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command 'chcp 65001 > $null; [Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; $OutputEncoding = [System.Text.Encoding]::UTF8; $lines = Get-Content -Encoding UTF8 -LiteralPath '"'README.md'; "'$start = (Select-String -Path '"'README.md' -Pattern '"'^## 时间限阅读路径 '"\\| Time-Boxed Reading Paths"'$'"' -Encoding UTF8).LineNumber; "'$end = (Select-String -Path '"'README.md' -Pattern '"'^## 子目录命名约定$'"' -Encoding UTF8).LineNumber; for ("'$i=$start-5; $i -le $end+1; $i++) { '"'{0,4}: {1}' -f ("'$i+1),$lines[$i] }; Write-Output "`n--- diff check ---"; git diff --check -- README.md; Write-Output "`n--- changed files ---"; git status --short; $mainStatus = git status --short -- '"'AI协作项目全生命周期框架.md'; if ([string]::IsNullOrWhiteSpace(("'$mainStatus -join '"''))) { Write-Output 'Main document unchanged.' } else { Write-Output "'$mainStatus }' in E:\workspace\projects\ai-collaboration-framework
 succeeded in 254ms:
 145: | 了解框架成熟度 | [`_protocols-and-tools/框架级成熟度评估表.md`](_protocols-and-tools/框架级成熟度评估表.md) |
 146: 
 147: ---
 148: 
 149: ## 时间限阅读路径 | Time-Boxed Reading Paths
 150: 
 151: > **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。
 152: 
 153: ### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?
 154: - **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）
 155: - **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.
 156: 
 157: ### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms
 158: - **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆☆☆ 入门）
 159: - **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.
 160: 
 161: ### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment
 162: - **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）
 163: - **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.
 164: 
 165: ### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery
 166: - **阅读 / Read**：按顺序通读 §1–§14，再阅读 `_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）
 167: - **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.
 168: 
 169: <!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->
 170: 
 171: ---
 172: 
 173: ## 子目录命名约定
 174: 
 175: | 前缀 | 含义 |

--- diff check ---
README.md:5: trailing whitespace.
+**适用对象 / For**：个人独立使用 AI 工具推进项目的创作者（solo creators）。  
README.md:6: trailing whitespace.
+**你将获得 / Get**：六层生命周期方法、Prompt-TDD 实验规范、独立审查流程与项目闭合清单。  
README.md:9: trailing whitespace.
+**版本 / Version**：v1.6.4（2026-06-22）· **状态 / Status**：Working Paper（持续更新；引用请注明版本）· **许可 / License**：CC BY 4.0 · **编码 / Encoding**：UTF-8  

--- changed files ---
 M README.md
 M project_status.md
?? _review/
?? _reviews/retrospect_2026-07-09.md
Main document unchanged.

codex
Implemented in `E:/workspace/projects/ai-collaboration-framework/README.md`.

### Exact insertion point

Immediately after the existing `---` following the **“快速导航”** table and before:

```markdown
## 子目录命名约定
```

The inserted section is currently at **README lines 149–171**.

### Exact markdown inserted

```markdown
## 时间限阅读路径 | Time-Boxed Reading Paths

> **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。

### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?
- **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）
- **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.

### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms
- **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆☆☆ 入门）
- **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.

### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment
- **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）
- **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.

### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery
- **阅读 / Read**：按顺序通读 §1–§14，再阅读 `_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）
- **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.

<!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->

---
```

The main methodology document was not modified, no files were added, and the README’s UTF-8-without-BOM and CRLF formatting were preserved.
tokens used
101,539
Implemented in `E:/workspace/projects/ai-collaboration-framework/README.md`.

### Exact insertion point

Immediately after the existing `---` following the **“快速导航”** table and before:

```markdown
## 子目录命名约定
```

The inserted section is currently at **README lines 149–171**.

### Exact markdown inserted

```markdown
## 时间限阅读路径 | Time-Boxed Reading Paths

> **难度 / Difficulty**：沿用主文档 §9.9 的 ☆☆☆ 入门、★☆☆ 基础、★★☆ 进阶、★★★ 高级。

### 🕐 5 分钟 | 5 minutes — 判断是否适合我 / Is this for me?
- **阅读 / Read**：本 README + §1.1「核心理念」+ §1.8「已知局限与诚实声明」（§1：☆☆☆ 入门）
- **目标 / Goal**：判断这套框架是否适合你的需求 / Decide if this framework fits your needs.

### 🕐 30 分钟 | 30 minutes — 理解核心机制 / Understand the core mechanisms
- **阅读 / Read**：§1「框架总览」→ §2「L0: Spec（项目宪法）」→ §3「L-H: Human Gate（人类闸门）」+ §9.9「阅读导航与难度分层」（§1–§2：☆☆☆ 入门；§3：★☆☆ 基础；§9.9：☆☆☆ 入门）
- **目标 / Goal**：理解最重要的两个层级，以及如何导航其余内容 / Understand the two most important layers and how to navigate the rest.

### 🕐 2 小时 | 2 hours — 跑通一个实验 / Run one experiment
- **阅读 / Read**：§4「L1: Prompt（任务规格）」+ §4.1.1.1「对照实验设计强制检查清单」+ §6「L3: Workflow（多任务编排）」（§4：★☆☆ 基础；§6：★★☆ 进阶）
- **目标 / Goal**：设计并执行你的第一个受控 Prompt 实验 / Design and execute your first controlled prompt experiment.

### 🕐 完整采纳 | Full Adoption — 端到端掌握 / End-to-end mastery
- **阅读 / Read**：按顺序通读 §1–§14，再阅读 `_protocols-and-tools/` 补充材料（覆盖 §9.9 的 ☆☆☆→★★★ 全部难度层级）
- **目标 / Goal**：将完整框架应用于一个真实项目，从启动一直推进到闭合 / Apply the full framework to a real project from start to closure.

<!-- GPT-5.6-Sol (via Codex CLI), 2026-07-17 -->

---
```

The main methodology document was not modified, no files were added, and the README’s UTF-8-without-BOM and CRLF formatting were preserved.

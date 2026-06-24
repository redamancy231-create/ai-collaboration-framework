# Provenance Erratum — "ChatGPT-5.5" → "GPT-5.5"

> **生成模型**: DeepSeek-v4-pro (via Claude Code CLI shell)
> **生成日期**: 2026-06-17
> **类型**: Provenance 勘误
> **影响范围**: 框架 v1.3–v1.5.2 及其衍生项目（方法论提取方法论、Small_Scale、PilotDeck、GitNexus、Evolver、PocketFlow、agent-harness-survey、CLAUDE-md-generation 等）中所有将 OpenAI Codex CLI 后端标注为 "ChatGPT-5.5" 的位置

---

## 勘误内容

**错误标签**: `ChatGPT-5.5`
**正确标签**: `GPT-5.5 (via Codex CLI)`

## 根因

"ChatGPT" 是 OpenAI 的**消费者产品名**（手机 App、网页端 chatgpt.com），而非底层模型名。OpenAI 的模型家族名为 **GPT**（Generative Pre-trained Transformer）。

Codex CLI 调用的是 OpenAI API 的 GPT 系列模型，与 ChatGPT 产品共享同一套模型引擎，但 Codex CLI 本身不叫 "ChatGPT"。

将产品名 "ChatGPT" 误用作模型名，类似于把 "Google App" 称为搜索引擎模型名——混淆了产品包装与底层引擎。

模型名的 ".5" 后缀本身是正确的——Codex CLI 模型选择界面（v0.138.0）明确显示当前模型为 `gpt-5.5`（Frontier model for complex coding, research, and real-world work）。唯一错误是多余的 "Chat" 前缀。

## 证据

Codex CLI v0.138.0 模型选择菜单：

```yaml
model: gpt-5.5 xhigh /model to change
```

```
1. gpt-5.5 (current) Frontier model for complex coding, research, and real-world work.
2. gpt-5.4
3. gpt-5.4-mini
4. gpt-5.3-codex
5. gpt-5.2
```

多份 Codex CLI 审查报告中，审查者自述为 "GPT-5"（省略了 .5 子版本号），但 CLI 界面确认实际模型为 `gpt-5.5`。

## 修正范围

### 已修正（活跃项目，2026-06-17）

1. **`meta-audit-checklist.json`** — P-004/I-001 的条件和通过标准；reflexivity_note；version_note
2. **`meta-audit-checklist.md`** — 同上 + B-020 的预判来源
3. **`方法论提取框架_v0.1_trial.md`** — R1/R5 审查记录中的审查者标签 + P5/P6 证据描述中的模型对比引用
4. **`方法论提取框架_v0.1_trial.json`** — `review_backends` 和 `review_chain` 中的审查者标签 + P5 limitations

### 不修正（已归档项目）

以下项目的 "ChatGPT-5.5" 标签**保留不改**，原因：
- 项目已 CLOSED/归档，批量编辑 178+ 文件边际收益极低
- 各审查报告**内部已嵌入 provenance 免责声明**，读者可自行识别
- 文件名（如 `独立审查_ChatGPT-5.5_审查报告.md`）为历史产物，修改会破坏引用链

涉及的项目：
- agent-harness-survey-analysis（CLOSED）
- PilotDeck-analysis（CLOSED）
- GitNexus-analysis（CLOSED-ARCHIVED）
- Evolver-analysis（CLOSED）
- small-scale-analysis（CLOSED）
- PocketFlow-analysis（CLOSED）
- CLAUDE-md-generation（CLOSED）
- LIT（已封存）
- AI协作项目全生命周期框架/_reviews/ 下的历史审查报告（文件名保留）
- AI协作项目全生命周期框架/_research/ 下的研究笔记

### 未来规范

此后所有产出中，涉及 OpenAI Codex CLI 后端的模型声明统一使用：

- **模型名**: `GPT-5.5`
- **调用方式**: `via Codex CLI`
- **完整标注**: `GPT-5.5 (via Codex CLI)`

禁止使用 `ChatGPT` 作为模型标识（可作产品/服务上下文说明，但不可替代模型名）。

---

## 元审查影响

本勘误涉及 `meta-audit-checklist` 的 P-004 和 I-001 两项，已同步修正。按框架 §9.2 标准，此修正操作由框架作者（DeepSeek-v4-pro）执行，非独立操作——属作者按发现修正，非元审查执行。

## 关联记忆

- [[feedback_model_provenance]] — 模型 provenance 当场记录规则
- [[feedback_generated_files_model_provenance.md]] — 生成文件模型声明规范
- [[feedback_workflow_agent_model_provenance.md]] — agent({model}) 参数是意图非事实

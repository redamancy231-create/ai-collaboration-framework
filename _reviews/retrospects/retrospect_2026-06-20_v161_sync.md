# Retrospect: v1.6.1 三件套同步会话（2026-06-20）

## 1. 生效清单（Keep doing）

- **Codex 异后端交叉验证在同步后执行**：17/17 检查项全 PASS，捕获了 2 个 caveat（DOCX非完全内容级同步、JSON双changelog结构）。验证在同步后而非同步前执行，避免了"修完再修"的循环
- **先修 MD 源再同步衍生文件**：修复 Codex 审查残留 → 同步 JSON → 同步 DOCX 的顺序避免了重复修正
- **session-end 复查 CLAUDE.md**：发现 CLAUDE.md 仍有"三角验证"残留（主 MD 已修但 CLAUDE.md 漏了）——说明措辞修正应 grep 全项目非仅主文件

## 2. 失效清单（Stop doing / Change）

- **VERSION 文件被遗忘**：自 v1.5.4 起跳了三个版本未更新。根因：三件套同步协议只有 .md/.json/.docx 三项，VERSION 不在检查清单中。已修复（§2.6 新增第 4 项）
- **pandoc 未预装**：Windows 环境 pandoc 需 winget 安装，首次会话耗时。以后新机器应预检 pandoc 可用性

## 3. 意外发现（Surprises）

- **JSON 存在双 changelog 结构**：root `changelog` (dict, v1.2→v1_5_3) 与 `metadata.changelog` (list, v1.5.4→v1.6.1) 并存，历史 sync 脚本选择了 metadata 路径但未清理 root。Codex 交叉验证捕获
- **DOCX 元数据级同步 vs 全文重新生成差距大**：元数据更新的 DOCX 版本头仍显示旧 v1.6 描述。全文 pandoc 重新生成后版本头才与 MD 一致——证明元数据级同步只是权宜之计
- **pandoc 3.10 + mmdc 管道一次性跑通**：6/6 Mermaid 渲染 + 92 表格 + TOC 域 + 7 图片 resize，无报错

## 4. 方法论片段候选

- **MF: 多文件版本一致性检查清单** — 当项目有多个格式的同一文档（.md/.json/.docx）和一个纯文本版本标签（VERSION）时，同步协议必须显式列出所有文件。遗漏任何一项都会导致漂移
- **MF: CLAUDE.md 作为第二检查点** — CLAUDE.md 的版本/状态摘要行是独立于主文档的第二检查点，措辞修正时须同步更新

## 5. 跨项目通用教训

- **纯文本 VERSION 文件**：作为脚本/CI 可免解析读取的快速版本标识，应与主文档同步更新。已写回 §2.6
- **grep 全项目再声称"已修"**：措辞修正后应 grep 全项目（含 CLAUDE.md/README/辅助文件）确认零残留，非仅检查主文档

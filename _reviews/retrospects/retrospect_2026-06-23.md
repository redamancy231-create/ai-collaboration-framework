# Retrospect — 2026-06-23 P0清理 + 翻译管道 + 发布准备

## 完成

- 9项P0修复（Codex R1 9 FAIL → R2 7/9 → R3 5 PASS/4 FAIL → 4项全部修复 → 9/9 PASS）
- 40文件绝对路径两轮清理（`_attic/框架发布前备份_20260623/` 原始备份）
- 个人标识统一为 Acerolaorion（路径用户名→`<USER_HOME>`，公开署名保留 Acerolaorion）
- 术语表 Codex+Qwen 双后端审查 → v1.1（188→190条，33项覆盖生效）
- docx_pipeline 6处bug修复 + regenerate_docx.py mmdc路径泛化
- 正体中文翻译完成（OpenCC s2twp + glossary → Qwen qwen3.7-max 通读审校 8/10 → 4类问题全部修正）
- 英文 README 已删（之前未按双翻译互校流程），待 Opus 会话从零开始
- 翻译管道设计草案 `_workflows/i18n/DESIGN.md`
- 检查清单 O6→O7 + §6 spec_over_vibe + §7 text_generation_two_phase
- `en/` 目录删除 + `zh-Hant/project_status.md` 迁阁楼

## 教训

### 1. Spec Coding 不能只写在框架里
框架自身主张 Spec > Vibe，但本次翻译管道的执行过程全面违反——模型分工被简化（OpenCC+Qwen→OpenCC+自检）、文件范围被扩大（2→4份）、流程步骤被跳过（Qwen通读/英文互校）。**已写入检查清单 §6 和 memory。**

### 2. 面向人类的文本产出需要两阶段
翻译/README/PUBLISHING.md 等一次性全部生成完毕，用户原本想讨论方案但没机会。**已写入检查清单 §7 和 memory。**

### 3. 自扫自夸不可靠——禁止基于自有 pattern 声称零残留
P0 清理后三次声称"全清零"，三次被追问后扒出新残留（Acerolaorion 用户名变体/JSON转义/PowerShell三重反斜杠）。同一脑子的同一 pattern 扫十遍也是相同盲区。**已写入检查清单 O7 和 memory。** 正确做法：发布前让异后端用其自有搜索策略独立确认。

### 4. OpenCC s2twp 两个陷阱
- **二次转换擦除**：已繁中文本会被 s2twp 再次处理（"誠實聲明"→"誠實宣告"），术语表覆盖须在 OpenCC 之后执行，且 override map 须基于 OpenCC 输出而非简体原文
- **文档→文件重新引入**：s2twp 将"文档"→"文件"（台湾用语），重新引入了已被预替换清除的"文件"。根因是预替换只覆盖了"文件"未覆盖"文档"

### 5. 路径清理须穷举转义变体
`C:/Users/X` 在审查输出中会出现多种形式：`C:/Users/X`（正斜杠）、`C:\Users\X`（反斜杠）、`C:\\Users\\X`（JSON转义）、`C:\\\Users\\\X`（PowerShell三重转义）。清理脚本须覆盖所有转义层级。

## 待下次

- 英文 README + 主文档翻译（Opus 会话，GPT-5.5 + Opus 双翻译互校）
- git init + push（英文翻译完成后）
- 仓库命名/tag/描述/topics 讨论
- mmdc渲染宽度1200→2400

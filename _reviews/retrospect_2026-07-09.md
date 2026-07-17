# Retrospect 2026-07-09

> GitHub 知名度提升会话 —— awesome 列表提交 + traffic 审计

## 失误 1：用 `gh search code` 断言 README 无交叉引用

**做了什么**：`gh search code --repo ... "redamancy231-create"` 返回空，便断言 5 个仓库 README 之间没有互相链接。

**为什么错了**：GitHub Code Search API 不索引仓库的 README.md 内容（或索引不完整）。用 `gh api .../readme --jq '.content' | base64 -d` 直接读 README 后发现每个仓库都有 4-10 个跨仓库引用。搜索返回空 ≠ 实际不存在。

**教训**：用搜索工具做"断言不存在"类判断时——尤其 `gh search code`——须先了解该工具的索引覆盖范围。不确定时用直接读取验证。

## 失误 2：同会话内自相矛盾——homepage 设置

**做了什么**：在方案中建议为 `ai-collaboration-framework` 设置 `homepage` 字段指向 GitHub Pages URL，称能改善 Google 索引。

**为什么错了**：之前在更早的会话中已判断过不需要设 homepage，本次会话忘了这个判断，又重新建议。被用户指出。

**教训**：建议之前先核对自己之前是否已有过相反判断——尤其在跨会话时。同会话内的记忆一致性是基础要求。

## 关联

- [GitHub知名度提升_next-steps.md](E:/workspace/projects/GitHub知名度提升_next-steps.md) — 更新后的 next steps
- [[reference_github_fork_commit_laziness]] — 同会话发现的 fork commit 延迟问题

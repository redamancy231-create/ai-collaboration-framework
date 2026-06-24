# Retrospect 2026-06-21 (session 2)

## 触发
v1.6.3 三件套全量对齐 + 字符统计 + DOCX 边距调整。

## 做了什么
1. 主文档字符全量重统计（163,479 字符），含内容分区（正文/表格/代码/块引用）
2. DOCX v1.6.3 全量 pandoc 重生成 + Mermaid 6 图 PNG 嵌入
3. 边距迭代调整 2.54cm → 2.0cm → 1.8cm（人工目视确认）
4. 修复两处代码问题（见下）
5. 关联文件全量同步

## 出了什么问题
1. **count_chars_v163.py regex 遗漏 `·`（U+00B7）**：字符集注释写了但 regex 模式漏了间隔号 → 中文标点少计 3 字符（8,179 vs 实际 8,182）。被 `verify_chars_v163.py` 的 unicodedata 逐字符方法交叉验证发现。
2. **embed_mermaid_png.py 路径漂移**：引用 `_workflows/style_v16_docx.py` 但文件已归档至 `_archive/docx_legacy_scripts/` → 下次重生成会报错。本次临时复制才跑通，事后修正了脚本路径。
3. **Windows subprocess GBK 编码**：`sync_v163_docx.py` 用 `subprocess.run()` 调用管线脚本时 stdout 读取因中文编码崩溃——但管线本身已跑完，产物正常。根因是 Windows 上 subprocess 默认 GBK，需显式 `encoding='utf-8'`。

## 为什么 #1 自查没发现
regex 和 unicodedata 两套方法看起来都"应该正确"——但 regex 字符类 `[　-〿...]` 的写法让人不容易验证每个 Unicode 字符是否都在类内。代码 review 时人眼看不出 `·` 的缺席。

## 教训
**字符统计脚本的单方法计数有静默错误风险，需独立方法交叉验证。** regex 方法（快但可能有字符类遗漏）和 unicodedata 逐字符方法（慢但覆盖完整）应互为校验。这和 2026-06-21 Retrospect 中"机械检查只覆盖部分维度"是同一模式的新实例。

## 关联
- [[feedback_verify_before_asserting]]
- [[methodology_review_prompt_mechanical_checks]]
- retrospect_2026-06-21.md — 同日的目录整理教训（自查盲区）

# Retrospect: AI协作框架 v1.6 升级（2026-06-20）

## 1. 生效清单（Keep doing）

- **异后端审查闭环**：v1.6 初版由 DeepSeek-V4-Pro 单后端完成，事后 Codex 审查发现 2 MAJOR（Qwen来源归因错误+强制门过度），证明异后端交叉验证不可或缺
- **先审查再同步**：md审核→修正→再同步三件套的顺序被验证正确——如果在审查前就同步了 .json/.docx，修正成本翻三倍
- **来源必须当场核实**：Qwen P1 建议标注为"Qwen R2审查"但实际来源文件只是md→json忠实度审查——来源归因在编辑时通胀，审查时暴露

## 2. 失效清单（Stop doing / Change）

- **单后端编辑后不立即触发独立审查**：违反项目启动清单 E3——触及方法论资产且无zero-involvement审查时应主动提醒，本会话未触发
- **headroom_compress 使用延迟**：长会话应在 Workflow/大批量agent前压缩，本会话在用户提醒后才执行

## 3. 意外发现（Surprises）

- **pandoc `--reference-doc` 不继承 run 级字体格式**：仅继承样式定义，中文 微软雅黑 需 python-docx 后处理全量 run
- **Mermaid→EMF 矢量路径不可行**：Inkscape SVG/PDF→EMF 均丢失文字，最终只能高DPI PNG。这一发现已写入新 memory `reference_docx_generation_pipeline.md`
- **v1.6 .docx 生成经历了 6+ 轮迭代**：双目录/表格无边框/图片消失/字丢/切分过多/宽度不够——每条都是独立教训

## 4. Spec 更新候选

- v1.6 维护流程 §2.6 中的 Minor 升级审查门（≥2 后端）自 v1.6 通过后的下一版生效
- CLAUDE.md 需更新 v1.5.5→v1.6

## 5. 跨项目方法论候选

- .docx 生成管道经验 → 已写 memory `reference_docx_generation_pipeline.md`

# i18n 翻译管道设计草案

**状态**: 草案，待英文翻译经验积累后实现  
**生成日期**: 2026-06-23  
**生成模型**: DeepSeek-V4-Pro (via Claude Code CLI)

## 现状

当前仅实现 zh-Hant（正体中文台湾习惯）翻译：

| 文件 | 职责 | 泛化程度 |
|------|------|----------|
| `translate_zh-Hant.py` | OpenCC s2twp + glossary 覆盖 + 代码块保护 | 管道骨架可抽离，引擎部分焊在脚本里 |
| `check_translation.py` | 代码块/表格/引用/证据标注/术语覆盖率检查 | 除术语表路径外基本语言无关 |
| `glossary.json` | 简中→正体→英文三元组 + do_not_translate | 模型可复用，数据语言绑定 |
| `glossary.md` | 人类可读版 | 同上 |

## 目标架构（v2.0，至少跑通 2 个语言对后实现）

```
_workflows/i18n/
├── DESIGN.md                    ← 本文件
├── pipeline.py                  ← 通用翻译管道框架
├── verify.py                    ← 通用验证器
├── glossary.json                ← 多语言术语表（扩展现有结构）
│
├── engines/
│   ├── base.py                  ← 翻译引擎抽象基类
│   ├── opencc_zh_hant.py        ← zh-Hant：OpenCC 确定性引擎
│   └── ai_translator.py         ← 通用：调 AI API 翻译（GPT/Opus/Qwen）
│
├── configs/
│   ├── zh-Hant/
│   │   ├── glossary.json        ← 简中→正体术语（已存在）
│   │   ├── pre_replace.py       ← 预替换规则（解决 OpenCC 二义性）
│   │   └── style.md             ← 风格指南
│   └── en/
│       ├── glossary.json        ← 待建：简中→英文术语对照
│       └── style.md             ← 美式英语风格指南（-ize, -or, behavior…）
│
└── prompts/
    ├── translate_zh-Hant.txt
    └── translate_en.txt
```

## 组件职责

### pipeline.py — 通用管道框架

```python
class TranslationPipeline:
    def __init__(self, engine, config_dir):
        self.engine = engine           # 翻译引擎
        self.protections = [           # 保护规则（语言无关）
            CodeBlockProtection(),
            MermaidProtection(),
            HtmlCommentProtection(),
            TableStructureProtection(),
            CrossReferenceProtection(),  # §X.X 格式
            EvidenceAnnotationProtection(),  # [E-][Sp] 等
        ]
    
    def translate(self, source_path, output_path):
        # 1. 解析 + 保护区域标记
        # 2. 逐段送引擎翻译
        # 3. 应用 glossary overrides
        # 4. 还原保护区域
        # 5. 写入输出
```

### engines/base.py — 引擎抽象

```python
class TranslationEngine(ABC):
    @abstractmethod
    def translate(self, text: str, context: dict) -> str: ...
    
    @abstractmethod
    def pre_process(self, text: str) -> str: ...    # 预替换
    
    @abstractmethod  
    def post_process(self, text: str) -> str: ...   # 术语覆盖
```

### verify.py — 通用验证器

语言无关检查：
- 代码块配对 + Mermaid 计数
- 表格行数 / § 引用数 / 证据标注计数
- 行数 / 无乱码

语言相关检查（通过 config 注入）：
- 术语覆盖率（对照 glossary）
- 禁译项是否被错误翻译
- 预替换是否全部生效

## 知识来源

- zh-Hant 翻译管道：两轮迭代（OpenCC 二次转换擦除修复 + `文档→文件` 重新引入修复）
- 术语表驱动覆盖模型：29 项 post-OpenCC 覆盖 + 2 项预替换
- Qwen 审校发现的四类问题：文件名链接 / 文件→檔案 / 模板→範本 / 实现→實作

## 实现前置条件

1. ✅ zh-Hant 翻译经验（已积累）
2. ❌ en 翻译经验（待 Opus 会话）
3. ❌ 至少一个 AI API 引擎的经验（en 翻译会提供）

## 约束

- 代码块、Mermaid 图表、表格结构、交叉引用 `§X.X`、证据标注 `[E-]` `[Sp]` 等——所有语言均不翻译
- 文件名、项目名——所有语言均不翻译
- 术语表是单一事实源：翻译时锁定，验证时对照

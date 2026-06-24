# Codex Naked Audit 2026-06-24

> 角色：独立发布安全审查者  
> 范围：当前工作树中除 `.git/` 外的可见文件；同时检查 `.gitignore` 排除的 `_pipeline_output/` 作为本地残留风险。  
> 脱敏说明：为避免本报告自身制造新的个人残留，真实本机用户名、本机路径前缀在片段中以 `<LOCAL_WIN_USER>`、`<LOCAL_WORKSPACE_PREFIX>` 表示；文件名与行号保留。

## 总体裁决

**FIX_REQUIRED**

理由：候选发布文件 `pre_push_check.py` 中仍有真实本机用户名示例和本机路径前缀示例。未发现实际 API key/token/密码/私钥，但该个人环境标识足以阻断公开发布。另有公开署名 `Acerolaorion` 与个人工作环境说明，是否保留需要人类确认。

## 审查策略

- 枚举当前工作树：包含未跟踪文件、隐藏文件、忽略文件；排除 `.git/`。
- 定向扫描：本机用户名、机器名、Windows/Unix 绝对路径、邮箱、手机号、内网地址、localhost、常见 API key/token/私钥/JWT/AWS/GitHub/Google/Slack 形态。
- 敏感文件名扫描：`.env`、key/pem/p12/pfx、credential/secret/token/password、日志与备份名。
- `.docx` 容器检查：读取 OOXML `docProps/*`、rels、正文 XML，查作者字段、本机路径、用户名、凭据形态。
- 发布边界检查：`git status --short --ignored` 显示当前文件基本为未跟踪；`_pipeline_output/` 被 `.gitignore` 忽略但本地存在。

## 必须修复

| 文件:行号 | 内容片段 | 判断 | 理由 |
|---|---|---|---|
| `pre_push_check.py:33` | `PRE_PUSH_PATH_PREFIX="<LOCAL_WORKSPACE_PREFIX>" PRE_PUSH_USERNAME="<LOCAL_WIN_USER>" python pre_push_check.py` | 必须修复 | 示例中包含真实本机工作区前缀和 Windows 用户名。即使只是注释示例，公开仓库仍会暴露个人环境标识。建议改为 `PRE_PUSH_PATH_PREFIX="<PATH_PREFIX>" PRE_PUSH_USERNAME="<USERNAME>"` 或说明从私有 shell 环境注入。 |

## 需确认

| 文件:行号 | 内容片段 | 判断 | 理由 |
|---|---|---|---|
| `PUBLISHING.md:13` | `the author (Acerolaorion) retains editorial control` | 需确认 | `Acerolaorion` 是公开作者署名/账号标识。若这是有意公开的 GitHub 身份，可接受；若目标是匿名发布或去身份化，应替换为 `the author` 或项目维护者。 |
| `_protocols-and-tools/meta-audit-checklist.md:43` | `作者（Acerolaorion）的个人工作环境` | 需确认 | 同上，同时明确提到个人工作环境、memory、硬件记录、skill 清单等；若该清单面向外部读者，建议弱化为“维护者本地环境”。 |
| `_reviews/retrospects/retrospect_2026-06-23.md:7` | `个人标识统一为 Acerolaorion（路径用户名→<USER_HOME>，公开署名保留 Acerolaorion）` | 需确认 | 这行保留了发布去标识化过程与公开署名决策。若公开 retrospects 是预期的一部分，可接受；否则建议归档到非发布区。 |
| `_reviews/retrospects/retrospect_2026-06-23.md:25` | `扒出新残留（Acerolaorion 用户名变体/JSON转义/...）` | 需确认 | 披露了过往清理失败与个人标识变体，非密钥但属于身份治理痕迹；是否公开取决于项目透明度策略。 |
| `_reviews/independent_review_v1.4_codex_20260613.md:20` | `` `<USER_HOME>/.claude/skills/kill-test-first/SKILL.md` `` | 需确认 | 使用占位符，不暴露真实路径；但公开了本地 skill 名称和个人工具结构。若不希望暴露个人 Codex/Claude 工作流，应移入私有审查归档。 |
| `_reviews/independent_review_v1.4_codex_20260613.json:20` | `"<USER_HOME>/.claude/skills/kill-test-first/SKILL.md"` | 需确认 | 同上，JSON 版本重复。 |
| `_reviews/independent_review_v1.4_kimi_20260613.md:17` | `` `<USER_HOME>\.claude\skills\kill-test-first\SKILL.md` `` | 需确认 | 同上，Windows 路径占位形式。 |
| `_reviews/independent_review_v1.4_kimi_20260613.json:22` | `"path": "C:<USER_HOME>\\.claude\\skills\\kill-test-first\\SKILL.md"` | 需确认 | 使用占位符但格式像 Windows 盘符路径；不泄露真实用户名，但可能暴露个人工具结构。 |

## 可接受命中

| 文件:行号 | 内容片段 | 判断 | 理由 |
|---|---|---|---|
| `pre_push_check.py:8` | `C:/Users/X 等已知占位符显式排除` | 可接受 | `X` 是占位符，不是本机用户名。 |
| `pre_push_check.py:80` | `re.compile(r'C:/Users/X\b')` | 可接受 | 占位符白名单规则，不含真实路径。 |
| `_reviews/retrospects/retrospect_2026-06-23.md:32` | `` `C:/Users/X` ... `C:\Users\X` ... `` | 可接受 | 展示占位符路径转义形态；不含真实用户目录。 |
| `_workflows/qwen_r2_sync_verify_output.txt:29` | `schema://user:password@host:port` | 可接受 | CLI 帮助文本中的代理 URL 示例，不是实际密码。 |
| `_workflows/qwen_r2_sync_verify_output.txt:51` | `--openai-api-key ... OpenAI API key to use` | 可接受 | CLI 帮助文本中的选项名，不含实际 key 值。 |
| `_reviews/codex_v164_json_sync_review_output.txt:489` | `_workflows/qwen_r2_sync_verify_output.txt:29 ... schema://user:password@host:port` | 可接受 | 旧审查输出引用同一 CLI 帮助文本，不含实际凭据。 |
| `_reviews/O7_R3_final_verification_20260624.md:6` | `<LOCAL_WORKSPACE_PREFIX> / <WIN_USER_TOKEN> / <LOCAL_PROFILE_PREFIX>` | 可接受 | 前次审查报告主动脱敏说明，不含真实值。 |
| `_reviews/O7_R3_final_verification_20260624.md:69` | `硬编码 <LOCAL_WORKSPACE_PREFIX>` | 可接受 | 旧报告中的脱敏占位符；不是当前实际路径。内容准确性可另行审阅，但不构成泄露。 |
| `_reviews/O7_R3_final_verification_20260624.md:78` | `<LOCAL_WORKSPACE_PREFIX>、<WIN_USER_TOKEN>、<LOCAL_PROFILE_PREFIX>` | 可接受 | 脱敏占位符。 |
| `_reviews/O7_R3_final_verification_20260624.md:184` | `<LOCAL_PROFILE_PREFIX>/X` | 可接受 | 脱敏占位符。 |
| `_reviews/O7_R3_final_verification_20260624.md:275` | `--openai-api-key` | 可接受 | 说明 CLI 帮助文本命中，不含实际 key。 |
| `_reviews/O7_R3_final_verification_20260624.md:305` | `<LOCAL_WORKSPACE_PREFIX>` | 可接受 | 脱敏占位符。 |
| `_reviews/codex_review_v1.5.1_三件套同步审查.md:39` | `DOCX OOXML 正文出现 ...` | 可接受 | `DOCX OOXML` 是文件格式/正文检查描述，不是路径或密钥。 |
| `_reviews/codex_review_v1.5.1_三件套同步审查.json:81` | `DOCX OOXML 正文出现 ...` | 可接受 | 同上。 |
| `_reviews/codex_review_v1.5.1_三件套同步审查.json:82` | `DOCX OOXML 正文出现 ...` | 可接受 | 同上。 |

## 未发现

- 未发现实际 OpenAI/Anthropic/GitHub/AWS/Google/Slack/JWT 形态的 key、token 或私钥。
- 未发现硬编码 `api_key = ...`、`password = ...`、`access_token = ...` 等赋值形态的实际凭据。
- 未发现 `.env`、`.pem`、`.key`、`id_rsa`、`id_ed25519`、credential/secret/password 命名的敏感文件。
- 未发现邮箱、手机号、内网 IP、`localhost:port`、机器名命中。
- `.docx` 检查未发现真实作者名、本机用户名、本机绝对路径或凭据形态；主发布 docx 的 `lastModifiedBy` 为 `Anonymous`，可接受。

## 发布边界观察

- `git ls-files` 当前为空，`git status --short --ignored` 显示候选文件均为未跟踪文件，`_pipeline_output/` 为忽略目录。因此本审查按“如果当前可见文件被加入公开仓库”评估。
- `_pipeline_output/` 本地存在但被 `.gitignore` 忽略；未将其作为主发布阻断项。若未来手动强制添加，需重新审计其构建产物。

## 建议

1. 修复 `pre_push_check.py:33`，删除真实本机用户名和本机路径前缀示例。
2. 人工确认是否公开 `Acerolaorion` 作为作者署名；若需要匿名发布，需统一替换所有公开署名和 retrospects 中的相关说明。
3. 决定 `_reviews/retrospects/` 和含 `<USER_HOME>/.claude/skills/...` 的旧审查报告是否属于公开材料；若只是内部过程证据，建议移入非发布归档。

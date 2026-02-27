# 多语言翻译助手

> 覆盖单文档翻译、实时会议翻译和批量翻译，保持术语统一与格式保留。

## 这个案例能帮你做什么

- 把“文档翻译 + 实时沟通 + 批量处理”放进一套统一流程。
- 自动维护术语库，减少同一术语在不同文档里来回变形。
- 支持格式保留与并行任务，适合跨国团队协作场景。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | `translator` | 通用多语言翻译 | ClawHub |
| 外部 | `straker-verify` | 专业翻译与质量保证 | ClawHub |
| 外部 | `japanese-translation-and-tutor` | 日英翻译与学习辅助 | ClawHub |
| 外部 | `lyric-translator` | 歌词翻译场景 | ClawHub |
| 外部 | `tamil-whatsapp` | WhatsApp 泰米尔语处理 | ClawHub |
| 外部 | `language-learning` | 语言学习辅助 | ClawHub |

## 快速体验版（先跑一轮）

先跑一个“单文档翻译 + 术语对照”：

```text
你是我的 OpenClaw 助手。
请帮我做“多语言翻译助手”的预演版：
1. 把一份中文技术文档翻译成英文。
2. 输出术语对照表（中文/英文/说明）。
3. 评估准确性、流畅度、专业性。
4. 本轮不做批量任务，只验证单文档质量。
```

## 稳定自动版（可长期运行）

### 1) 安装示例

```bash
npx clawhub@latest install translator
npx clawhub@latest install straker-verify
npx clawhub@latest install japanese-translation-and-tutor
npx clawhub@latest install lyric-translator
npx clawhub@latest install tamil-whatsapp
npx clawhub@latest install language-learning
```

### 2) 配置方法

```bash
# 1. 配置翻译引擎
clawhub install translator
openclaw config set translate.engine "deepl"
openclaw config set translate.quality "high"

# 2. 配置术语库
openclaw config set translate.glossary "团队术语库.csv"
openclaw config set translate.auto-update-glossary true

# 3. 配置批量翻译
openclaw config set translate.batch-size 10
openclaw config set translate.parallel-tasks 3

# 4. 配置格式保留
openclaw config set translate.keep-format true
openclaw config set translate.keep-links true
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“多语言翻译助手”。
请使用 translator 相关 Skills。

执行能力要求：
1. 单文档翻译：保留格式并输出术语对照表。
2. 实时会议翻译：中英双向，记录完整翻译日志。
3. 批量翻译：支持多语言并行处理与进度汇报。
4. 每次翻译后更新术语库。

质量要求：
- 准确翻译
- 术语统一
- 保持格式
- 支持批量处理
```

## 成功标准

| 任务类型 | 使用前 | 使用后 | 节省时间 | 提升比例 |
|---|---:|---:|---:|---:|
| 单文档翻译 | 120分钟 | 2分钟 | 118分钟 | 98.3% |
| 实时翻译 | 人工翻译 | 自动 | 100% | 100% |
| 批量翻译 | 2,400分钟 | 12.5分钟 | 2,387.5分钟 | 99.5% |
| 平均 | 2,520分钟 | 14.5分钟 | 2,505.5分钟 | 99.4% |

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

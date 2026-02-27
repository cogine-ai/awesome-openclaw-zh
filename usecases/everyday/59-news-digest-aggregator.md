# 新闻摘要聚合器

> 自动汇总多源新闻、去重分组，并每天推送一页可读晨报。

## 这个案例能帮你做什么

- 省去反复刷多个站点的成本，统一在 Telegram 获取今日重点。
- 同事件去重，避免“同一新闻看三遍”。
- 按主题优先级输出，先看你最关心的类别。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `RSS Reader Skill` | 拉取 RSS 新闻源 | [clawhub.ai/skills/hacker-news](https://clawhub.ai/skills/hacker-news) |
| 内置 | `Web Fetch` | 抓取站点头条与正文片段 | OpenClaw Built-in |
| 内置 | AI 分析能力 | 去重、聚类、摘要与优先级排序 | OpenClaw Built-in |
| 外部（需安装） | `Memory/Notes Skill` | 记录你已看过内容与偏好 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram 通道 | 发送日报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的新闻编辑。
请从我给定 3 个 RSS 源抓取今天新闻，完成：
1) 去重
2) 按 世界/商业科技/政治/科学/文化 分类
3) 每条输出标题 + 2 句摘要 + 来源链接
总长度控制在 5 分钟可读。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Personal News Curator. Every day, gather news from my favorite sources, remove duplicates, and send me one clean digest.

DAILY TASK (7:45 AM):
1. Fetch from RSS + selected websites
2. Deduplicate stories (same event reported by multiple sources = one entry)
3. Categorize by priority:
   🌍 World
   💼 Business/Tech
   🏛️ Politics
   🧪 Science
   🎭 Culture
   ⚽ Sports (optional)
4. For each story output:
   - Headline
   - 2-3 sentence summary
   - Why it matters
   - Source link
5. Send Telegram digest

RULES:
- Include source for every story
- Never editorialize, stick to facts
- Keep digest within Telegram-friendly length
- If too many stories, prioritize and append "+ [X] more stories"
```

### 调度配置

```json
{
  "schedule": "45 7 * * *",
  "name": "Daily News Digest",
  "prompt": "[paste the prompt template above here]",
  "timezone": "Your/Timezone"
}
```

可选周报：

```json
{
  "schedule": "0 18 * * 5",
  "name": "Weekly News Review",
  "prompt": "Generate weekly news review with top stories and trends"
}
```

## 成功标准

- [ ] 每天 7:45 前收到日报。
- [ ] 5 分钟内读完且信息完整。
- [ ] 关键新闻覆盖率稳定，重复率明显下降。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/59-news-digest-aggregator.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/59-news-digest-aggregator.md)

# AI 财报追踪器

> 每周自动扫财报日历，你只确认名单，后续财报摘要自动推送。

## 这个案例能帮你做什么

- 周日自动产出下周科技/AI 公司财报预览，不用手动翻日历。
- 你选定关注公司后，自动创建“单次 cron 任务”，到点抓取财报结果。
- 推送统一格式摘要：`beat/miss`、营收、EPS、AI 相关亮点、指引。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_search` | 获取财报日历与财报结果 | OpenClaw Built-in |
| 内置 | `cron` | 周任务 + 单次任务调度 | OpenClaw Built-in |
| 渠道 | Telegram 话题 | 接收预览与财报总结 | Telegram |

## 快速体验版（先跑一轮）

把下面提示词直接发给 OpenClaw，先跑“预览 + 人工确认”闭环：

```text
Every Sunday at 6 PM, run a cron job to:
1. Search for the upcoming week's earnings calendar for tech and AI companies
2. Filter for companies I care about (NVDA, MSFT, GOOGL, META, AMZN, TSLA, AMD, etc.)
3. Post the list to my Telegram "earnings" topic
4. Wait for me to confirm which ones I want to track

When I reply with which companies to track:
1. Schedule one-shot cron jobs for each earnings date/time
2. After each report drops, search for earnings results
3. Format a summary including: beat/miss, revenue, EPS, key metrics, AI-related highlights, guidance
4. Post to Telegram "earnings" topic

Keep a memory of which companies I typically track so you can auto-suggest them each week.
```

## 稳定自动版（可长期运行）

### 1) 先建好接收通道

- 在 Telegram 建立话题：`earnings`
- 先手动测试一次消息是否能到该话题

### 2) 固定节奏

- 周日 18:00：自动发下周预览
- 你回复“本周跟踪公司清单”后：自动注册对应的一次性财报任务

### 3) 建议输出格式（便于复盘）

```markdown
## 公司：NVDA
- 财报结论：Beat / Miss
- Revenue：...
- EPS：...
- 关键指标：...
- AI 相关亮点：...
- 指引（Guidance）：...
- 来源链接：...
```

## 成功标准

- [ ] 每周都能按时收到“下周财报预览”。
- [ ] 确认名单后，财报后总结可自动到达 Telegram。
- [ ] 常跟踪公司会被系统自动建议，减少重复输入。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/earnings-tracker.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/earnings-tracker.md)

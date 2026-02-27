# 定制早间简报

> 每天固定时间自动推送你的晨间信息包（新闻、任务、创作草稿、AI建议）。

## 这个案例能帮你做什么

- 把起床后“找信息”的时间前置到夜间自动准备。
- 早上直接收到结构化简报，不用来回切换应用。
- 可持续微调简报字段（天气、股票、仅 AI 新闻等）。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | Telegram / Discord / iMessage 通道 | 接收简报 | OpenClaw Built-in |
| 外部（可选） | Todoist / Apple Reminders / Asana | 读取当日任务 | 官方 API / 集成 |
| 外部（可选） | `x-research-v2` | 趋势研究补充 | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的晨报助手。
请先生成今天的简报样稿，包含：
1) AI/创业/科技相关新闻
2) 今日待办优先级
3) 1条可直接执行的内容草稿
4) 你建议我今天交给你代做的任务
本轮只输出，不定时发送。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（源案例）

```text
I want to set up a regular morning brief. Every morning at 8:00 AM,
send me a report through Telegram.

I want this report to include:
1. News stories relevant to my interests (AI, startups, tech)
2. Ideas for content I can create today
3. Tasks I need to complete today (pull from my to-do list)
4. Recommendations for tasks you can complete for me today

For the content ideas, write full draft scripts/outlines — not just titles.
```

### 迭代口令（源案例）

```text
Add weather forecast to my morning brief.
Stop including general news, focus only on AI.
Include a motivational quote each morning.
```

## 成功标准

- [ ] 简报每天按时送达。
- [ ] 内容可直接执行，而不是只给方向。
- [ ] 调整需求可以通过对话快速生效。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/custom-morning-brief.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/custom-morning-brief.md)

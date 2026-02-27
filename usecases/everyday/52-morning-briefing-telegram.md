# Telegram 每日晨报

> 每天固定时间把天气、日程、新闻、待办汇总成一条可读消息。

## 这个案例能帮你做什么

- 早晨只看一条消息就能掌握当天全局，不用切换 4-5 个 App。
- 自动按你关心的主题抓新闻，减少信息噪音。
- 消息结构固定，1 分钟内即可读完。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Weather` | 获取天气和降雨信息 | OpenClaw Built-in |
| 外部（需安装） | `Web Search` | 抓取新闻头条 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | Telegram 通道 | 推送晨报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的晨报助手。
请基于今天的信息输出一条 Telegram 晨报，包含：
1) 我所在城市天气
2) 今日日程
3) 3-5 条我关注领域新闻
4) 今日待办提醒
总字数控制在 300 词以内。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my morning briefing assistant. Every day at 6:30 AM:

1. **Weather**: Get today's weather for [YOUR CITY]. Include temperature, conditions, and whether I need an umbrella.
2. **Calendar**: List my events for today with times.
3. **News**: Find 3-5 top headlines relevant to [YOUR INTERESTS: e.g., tech, finance, local news].
4. **Reminders**: Check my pending to-dos and remind me of anything due today.

Format as a clean Telegram message with emoji headers:
☀️ Weather | 📅 Calendar | 📰 News | ✅ To-Do

Keep it under 300 words. No fluff.
```

### 调度配置

```text
Schedule: 30 6 * * *
Action: Compile briefing → Send via Telegram
```

## 成功标准

- [ ] 每天起床前收到晨报。
- [ ] 覆盖天气、日程、新闻、待办四块核心信息。
- [ ] 1 分钟内可读完，不冗长。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/52-morning-briefing-telegram.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/52-morning-briefing-telegram.md)

# 社区版每日简报（Daily Brief）

> 使用官方 cron job 配置，把天气、日程和任务合成 30 秒可读晨报。

## 这个案例能帮你做什么

- 给你一个可直接复制的 `cron.jobs` 配置，不用从零搭。
- 标准化晨报结构，减少格式漂移和冗余信息。
- 支持 Telegram / Discord / Slack 等投递渠道。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `weather` | 获取天气 | OpenClaw Built-in |
| 外部（按需） | Calendar 访问 | 获取未来 24h 日程 | Google/CalDAV/Nextcloud |
| 外部（按需） | Todoist/Trello/文件任务系统 | 拉取任务清单 | 官方 API |
| 内置 | `message` | 发送晨报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```bash
openclaw cron run daily-brief
```

## 稳定自动版（可长期运行）

### 1) `cron.jobs` 配置（源案例）

```json
{
  "name": "daily-brief",
  "schedule": {
    "kind": "cron",
    "expr": "30 9 * * *",
    "tz": "UTC"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Generate a daily brief. 1) Get weather for [YOUR_CITY]. 2) Check calendar for next 24 hours. 3) Get active tasks from [YOUR_TASK_SYSTEM]. 4) Check for stalled tasks >24h. Format as clean, scannable message with clear headers. Deliver to [YOUR_CHANNEL]."
  },
  "sessionTarget": "isolated"
}
```

### 2) 工具配置（源案例）

```yaml
tools:
  weather: {}
  calendar: {}
  message: {}
```

### 3) 全量提示词（可选）

```text
Generate a daily brief for me.

1. WEATHER: Get current weather for [YOUR_CITY]
2. CALENDAR: Check calendar for next 24 hours
3. TASKS: Get active tasks from [YOUR_TASK_SYSTEM]
4. REMINDERS: Check if anything needs attention

Format as a clean, scannable message with clear headers.
Skip sections that have nothing notable.
Keep it brief enough to read in 30 seconds.
Deliver to [YOUR_CHANNEL].
```

## 成功标准

- [ ] 简报在预设时区按时触发。
- [ ] 内容 30 秒内可读完。
- [ ] 关键提醒（卡住任务/紧急日程）可见。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/daily-brief.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/daily-brief.md)

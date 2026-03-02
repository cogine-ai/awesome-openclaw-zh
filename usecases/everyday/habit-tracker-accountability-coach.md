# 习惯追踪与督促教练（Habit Tracker & Accountability Coach）

> 用 OpenClaw 主动发起每日打卡，持续追踪习惯完成情况和连续天数。

## 这个案例能帮你做什么

- 在固定时间通过 Telegram（或短信）主动提醒你打卡。
- 自动记录每个习惯的 streak，并根据表现调整提醒语气。
- 每周输出完成率、最佳/最差日期和行为模式总结。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `telegram` channel | 发送与接收每日打卡消息 | OpenClaw Built-in |
| 外部（按需） | `Twilio SMS API` | 通过短信执行打卡提醒 | Twilio |
| 内置 | `cron` | 定时触发打卡与周报 | OpenClaw Built-in |
| 内置 | `filesystem`（或外部数据库） | 保存习惯日志与 streak | OpenClaw Built-in |
| 外部（可选） | [`gog`（Google Workspace CLI）](https://clawhub.ai/skills/gog) | 把数据写入 Google Sheets 做可视化 | ClawHub |

## 快速体验版（先跑一轮）

1. 先配置 Telegram 通道并定义 3-4 个习惯。
2. 先只跑一天，验证提醒时间与反馈节奏。
3. 本轮先用本地文件记录，不做复杂看板。

```text
I want you to be my accountability coach. Track these daily habits for me:

1. Morning workout (check in at 7:30 AM)
2. Read for 30 minutes (check in at 8:00 PM)
3. No social media before noon (check in at 12:30 PM)
4. Drink 8 glasses of water (check in at 6:00 PM)

Send me a Telegram message at each check-in time asking if I completed
the habit. Keep track of my streaks in a local file.
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 完成后给简短激励并带上当前 streak；连续漏打时改为温和提醒并建议调整目标。
2. 超过 2 小时未回复只补发一次 follow-up，不做高频骚扰。
3. 每周固定输出总结，包含完成率、streak、模式观察和下周建议。

## 成功标准

- [ ] 每天能按时收到打卡提醒。
- [ ] 每个习惯都有可追踪的 streak 记录。
- [ ] 每周都有结构化总结可复盘。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/habit-tracker-accountability-coach.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/habit-tracker-accountability-coach.md)

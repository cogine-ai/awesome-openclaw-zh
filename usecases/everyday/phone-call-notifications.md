# 电话外呼提醒（Phone Call Notifications）

> 让 OpenClaw 在真正重要的时候直接给你打电话，而不是只发一条容易被忽略的消息。

## 这个案例能帮你做什么

- 在价格异动、紧急邮件、预约提醒等场景里，主动拨打你的真实手机号。
- 通话过程中可以继续追问，不只是单向播报。
- 把“晨间简报”“高优先级告警”这类场景升级成更不容易错过的通知方式。

## 你需要的 Skills（按类型）

| 类型 | Skill / 服务 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`clawr.ing`](https://clawhub.ai/marcospgp/clawring) | 让 OpenClaw 主动拨打真实手机号，并支持双向通话 | ClawHub |
| 外部服务 | [clawr.ing dashboard](https://clawr.ing) | 提供 setup prompt 和托管电话服务 | clawr.ing |

## 快速体验版（先跑一轮）

1. 先把 `clawr.ing` 接好，只演练一个固定场景。
2. 推荐从“晨间电话简报”开始，最容易判断效果是否合适。
3. 本轮先输出触发条件和通话脚本，不直接拨号。

```text
你是我的 OpenClaw 助手。
请帮我设计一个“电话外呼提醒”的预演版：
1. 工作日 7:30 由你主动给我打电话，做一段不超过 2 分钟的晨间简报。
2. 简报只包含：天气、今天日历、夜间紧急邮件、3 条与我兴趣相关的新闻。
3. 如果我接通，可以继续追问；如果我没接，不要重拨。
4. 本轮先输出需要配置的 clawr.ing 信息、触发条件和通话脚本。
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 让现有的监控、cron 或其他触发条件先判断“这件事是否值得打电话”。
2. 只有满足阈值时，才通过 `clawr.ing` 主动拨打你的手机号。
3. 电话内容保持简短，重要信息先说清楚，剩下的问题让用户在通话里追问。
4. 固定简报类场景可以做成定时电话；异常告警类场景则按事件触发。
5. 不要把电话外呼用成普通通知渠道，避免高频来电让用户失去敏感度。

## 成功标准

- [ ] 电话只在真正需要你立刻注意的时候触发。
- [ ] 用户接通后可以继续追问，而不是只能听一段播报。
- [ ] 晨间简报、价格提醒、紧急邮件这类场景可以稳定复用。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/phone-call-notifications.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/phone-call-notifications.md)

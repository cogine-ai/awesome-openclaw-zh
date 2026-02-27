# 健康与症状追踪器

> 通过固定时段提醒 + 周报分析，找出饮食与症状的潜在关联。

## 这个案例能帮你做什么

- 持续记录饮食和症状，解决“靠记忆回想不准”的问题。
- 每周自动分析触发因素和时段模式。
- 通过专门主题集中记录，降低漏记概率。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron` | 三次提醒 + 周分析触发 | OpenClaw Built-in |
| 内置 | Telegram topic | 日常记录入口 | OpenClaw Built-in |
| 内置 | 文件存储 | 日志保存 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的健康记录助手。
请先基于今天的 3 条饮食/症状输入，
按“时间-食物-症状”格式写入日志，并生成当日简报。
本轮不做周分析。
```

## 稳定自动版（可长期运行）

### 执行提示词（源案例）

```text
When I message in the "health-tracker" topic:
1. Parse the message for food items and symptoms
2. Log to ~/clawd/memory/health-log.md with timestamp
3. Confirm what was logged

Set up 3 daily reminders:
- 8 AM: "🍳 Log your breakfast"
- 1 PM: "🥗 Log your lunch"
- 7 PM: "🍽️ Log your dinner and any symptoms"

Every Sunday, analyze the past week's log and identify patterns:
- Which foods correlate with symptoms?
- Are there time-of-day patterns?
- Any clear triggers?
```

## 成功标准

- [ ] 日志连续记录率可维持。
- [ ] 周报能输出可解释的关联模式。
- [ ] 可逐步形成个人触发因素清单。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/health-symptom-tracker.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/health-symptom-tracker.md)

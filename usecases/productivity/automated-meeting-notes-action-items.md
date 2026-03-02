# 自动会议纪要与行动项分发（Automated Meeting Notes & Action Items）

> 会后自动生成结构化纪要，并把行动项直接写入任务系统。

## 这个案例能帮你做什么

- 从 transcript 自动提取关键决策、行动项、负责人和截止日期。
- 自动在 Jira / Linear / Todoist / Notion 创建任务并分配责任人。
- 自动把摘要推送到 Slack / Discord，并在截止前提醒。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读取会议 transcript 文件 | OpenClaw Built-in |
| 内置 | `slack` / `discord` channel | 发送会议摘要与截止提醒 | OpenClaw Built-in |
| 内置 | `cron` | 定时扫描转写目录与提醒截止项 | OpenClaw Built-in |
| 外部（需配置） | `Jira / Linear / Todoist / Notion API` | 创建并分配行动项任务 | 各平台官方 API |
| 外部（可选） | `Otter.ai / Fireflies.ai / Google Meet API` | 自动获取会议转写 | 各平台官方 API |

## 快速体验版（先跑一轮）

1. 先拿一份真实 transcript 做输入。
2. 验证摘要、行动项、负责人、截止日期是否完整。
3. 本轮先打通一个任务系统（例如 Jira）。

```text
I just finished a meeting. Here's the transcript:

[paste transcript or point to file]

Please:
1. Write a concise summary (max 5 bullet points) covering key decisions and topics.
2. Extract ALL action items. For each one, identify:
   - What needs to be done
   - Who is responsible (match names to my team)
   - Deadline (if mentioned, otherwise mark as "TBD")
3. Create a Jira ticket for each action item, assigned to the right person.
4. Post the full summary to #meeting-notes in Slack.
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 每 30 分钟扫描 `~/meeting-transcripts/` 下新增 `.txt/.vtt` 文件。
2. 自动执行：解析摘要 → 创建任务 → 发到频道 → 移动到 `processed/`。
3. 对有截止日期的行动项，在到期前一天自动提醒负责人。

## 成功标准

- [ ] 每场会议都能产出结构化纪要。
- [ ] 行动项都有负责人和截止日期（或明确 `TBD`）。
- [ ] 任务创建与提醒链路稳定运行。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/meeting-notes-action-items.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/meeting-notes-action-items.md)

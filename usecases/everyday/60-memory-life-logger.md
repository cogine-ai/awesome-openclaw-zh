# 生活记忆记录器

> 把日常对话里的关键信息沉淀为长期记忆，并在关键时点提醒你。

## 这个案例能帮你做什么

- 记住“人和关系”的细节（偏好、生日、承诺、后续事项）。
- 自动生成每周回顾和事件提醒，降低遗忘带来的关系成本。
- 通过结构化存储和检索，随时问“我对这个人知道什么”。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Memory/Notes Skill` | 长期记忆存储与检索 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram 通道 | 录入记忆、确认与检索交互 | OpenClaw Built-in |
| 内置 | AI/NLP 能力 | 从自然语言中抽取事实与行动项 | OpenClaw Built-in |
| 内置 | 文件存储 | 保存结构化记忆文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的生活记忆助手。
我会给你几条“人物-事件”输入，请你提取：
1) 人物事实
2) 日期事件
3) 后续跟进事项
并按人名组织输出，不做自动提醒。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Life Memory Assistant. Your job is to help me remember important details about people, conversations, and life events.

Memory categories:
- 👤 People Facts
- 📅 Dates & Events
- 💼 Professional Context
- 🔗 Relationships & Connections
- 🎯 Commitments & Follow-ups

Storage:
- `/memory/life-memories/people/[person-name].json`
- `/memory/life-memories/upcoming-events.json`
- `/memory/life-memories/follow-ups.json`
- `/memory/life-memories/master-index.json`

When I add memories:
1. Extract facts, dates, commitments, context
2. Save structured records
3. Confirm what was saved

Privacy & ethics:
1. Consent first
2. Flag sensitive info for confirmation (health, financial, conflicts)
3. Support "Forget that" immediate deletion
4. Never share one person's info with another
```

### 调度配置

```json
{
  "schedule": "0 22 * * *",
  "name": "Daily Memory Processing",
  "prompt": "Process today's memories and send confirmation summary"
}
```

```json
{
  "schedule": "0 19 * * 0",
  "name": "Weekly Memory Review",
  "prompt": "Generate weekly memory review with upcoming events and insights"
}
```

```json
{
  "schedule": "0 20 28-31 * *",
  "name": "Monthly Memory Consolidation",
  "prompt": "If last day of month, consolidate and clean up memory files"
}
```

```json
{
  "schedule": "0 9 * * *",
  "name": "Birthday Reminder Check",
  "prompt": "Check for birthdays coming up in next 7 days and send reminders"
}
```

## 成功标准

- [ ] 能稳定回答“我对某人知道什么”。
- [ ] 生日/承诺/跟进项可提前提醒。
- [ ] 敏感信息有二次确认，不误存。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/60-memory-life-logger.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/60-memory-life-logger.md)

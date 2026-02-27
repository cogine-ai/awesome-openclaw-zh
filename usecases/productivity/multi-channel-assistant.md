# 多渠道个人助理

> 一个对话入口，路由到 Telegram 话题、Slack、Google Workspace、Todoist、Asana。

## 这个案例能帮你做什么

- 把跨平台的日常动作集中到统一指令入口。
- 用话题路由减少上下文污染（配置/更新/内容/CRM/财务）。
- 支持提醒类任务自动触发，减少手工跟进。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `gog` CLI | Gmail/Calendar/Drive 操作 | Google Workspace |
| 外部（需配置） | Slack Bot | 团队协作渠道 | Slack API |
| 外部（需配置） | Todoist / Asana | 任务与项目协作 | 官方 API |
| 内置 | Telegram topics | 场景路由入口 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的多渠道助手。
请先演示 5 条路由：
1) "Add [task] to my todo" → Todoist
2) "Create a card for [topic]" → Asana
3) "Schedule [event]" → Calendar
4) "Email [person]" → Gmail
5) "Upload [file]" → Drive
本轮只输出路由结果，不执行外部写操作。
```

## 稳定自动版（可长期运行）

### 1) Telegram 话题划分（源案例）

- `config`
- `updates`
- `video-ideas`
- `personal-crm`
- `earnings`
- `knowledge-base`

### 2) 路由提示词（源案例）

```text
You are my multi-channel assistant. Route requests based on context...
```

### 3) 自动提醒（源案例）

```text
- Monday 6 PM: "🗑️ Trash day tomorrow"
- Friday 3 PM: "✍️ Time to write the weekly company update"
```

## 成功标准

- [ ] 单入口可覆盖主要工作流操作。
- [ ] 路由稳定，无明显错发。
- [ ] 自动提醒按时触发。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-channel-assistant.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-channel-assistant.md)

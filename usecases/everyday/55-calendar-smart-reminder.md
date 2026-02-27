# 智能日历提醒

> 不只提前响铃，而是提前 2 小时给你“会什么、带什么、何时出发”。

## 这个案例能帮你做什么

- 每 30 分钟巡检日历，在关键事件前主动提醒。
- 将提醒从“时间提示”升级为“上下文 + 准备清单 + 路程建议”。
- 自动识别冲突、天气与出行风险，减少迟到与漏准备。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Calendar Access` | 读取 Google Calendar / Outlook | [clawhub.ai/skills/calendar](https://clawhub.ai/skills/calendar) |
| 内置 | `Weather` | 天气和雨具提示 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 发送提醒消息 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的智能日历助手。
请读取我未来 2 小时内的日程，按以下结构输出提醒：
📅 事件名称
📍 地点/会议链接
📋 准备要点
⏱️ 建议出发时间
若检测到日程冲突，请单独标记。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my smart calendar assistant. Check my calendar every 30 minutes during waking hours (8 AM - 10 PM).

For each upcoming event in the next 2 hours:

1. **Context**: What is this meeting about? Who's attending?
2. **Preparation**: What should I review or bring?
   - If it's a client meeting → remind me of last interaction
   - If it's a doctor appointment → remind me to bring insurance card
   - If it's a dinner → check the restaurant and suggest what to wear
3. **Logistics**:
   - How long to get there? (check traffic if it's in-person)
   - Is it raining? Should I bring an umbrella?
4. **Conflicts**: Flag if two events overlap

Send reminders via Telegram. Format:
📅 [Event] in 2 hours
📍 [Location/Link]
📋 [Prep notes]
⏱️ [Leave by X:XX to arrive on time]
```

### 调度配置

- Heartbeat：`8 AM - 10 PM` 每 `30` 分钟检查一次
- 提醒时间：事件开始前 `2` 小时

## 成功标准

- [ ] 不再漏会。
- [ ] 会前准备信息完整可执行。
- [ ] 路程与天气提示能降低迟到风险。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/55-calendar-smart-reminder.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/55-calendar-smart-reminder.md)

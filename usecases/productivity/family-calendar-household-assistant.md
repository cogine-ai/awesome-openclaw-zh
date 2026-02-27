# 家庭日历与家务助理

> 将所有家庭日历聚合到早间简报中，监控消息以获取预约，并管理家庭库存。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/family-calendar-household-assistant.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/family-calendar-household-assistant.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- **Household coordination overhead**: "How much milk do we have?" requires physically checking the fridge, then the basement pantry, then texting back. Multiply this across a week's worth of grocery runs.
- **Missed appointments**: Appointment confirmations arrive via text message and sit there unacted upon — no calendar event, no driving time buffer, no reminder.

### 核心动作（来源提炼）
- **Morning briefing**: Aggregates all family calendars into a single daily summary delivered via your preferred channel
- **Ambient message monitoring**: Watches iMessage/text conversations and automatically creates calendar events when it detects appointments (dentist confirmations, meeting plans, etc.)
- **Driving time buffers**: Adds travel time blocks before and after detected appointments
- **Household inventory**: Maintains a running inventory of pantry/fridge items that either partner can query from anywhere
- **Grocery coordination**: Deduplicates ingredients across recipes, tracks what's running low, and generates shopping lists
- **Photo-based input**: Snap a photo of a school calendar or freezer contents and the agent processes it into structured data

### 技能/工具/渠道（来源提炼）
- Calendar API access (Google Calendar, Apple Calendar via `ical`)
- `imessage` skill for message monitoring (macOS only)
- Telegram or Slack for the shared family chat interface
- File system access for inventory tracking
- Camera/photo processing for OCR of physical calendars

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「家庭日历与家务助理」。

目标（来自来源案例）：将所有家庭日历聚合到早间简报中，监控消息以获取预约，并管理家庭库存。
来源关键动作：**Morning briefing**: Aggregates all family calendars into a single daily summary delivered via your preferred channel；**Ambient message monitoring**: Watches iMessage/text conversations and automatically creates calendar events when it detects appointments (dentist confirmations, meeting plans, etc.)；**Driving time buffers**: Adds travel time blocks before and after detected appointments
优先工具/渠道：ical、imessage、angiolillo、dns_snek、Telegram、Slack、GitHub、Google Calendar
来源节奏信息：8:00；1:30；2:00；3:00；3:30

请按下面流程输出并执行：
1. 先给出“最小可运行版本（MVP）”执行计划（3-5条）
2. 立刻产出第一版结果（不要只讲思路）
3. 缺失的信息统一放到“待我补充信息”里，不要中断整体流程
4. 若涉及高风险操作（删除、外发、改密、生产写操作），先暂停并请求确认

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 待我补充信息
## 风险与边界
```

## 可选补充信息（提高效果）

- 你的常用渠道：[Telegram/飞书/微信/邮箱]
- 你的时区与执行时间：[例如 UTC+8，每天 09:00]
- 你最在意的结果指标：[例如 节省时间、回复率、发布频次]

## 效果检查（非技术版）

- 优先检查：是否比手工更快、是否稳定、是否可持续复用。

## 参考来源

- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- [usecases/family-calendar-household-assistant.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/family-calendar-household-assistant.md)

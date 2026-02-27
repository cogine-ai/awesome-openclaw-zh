# 每日晨间简报

> 天气+日历+新闻一条消息搞定

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/52-morning-briefing-telegram.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/52-morning-briefing-telegram.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- This is the "personal assistant morning report" that executives pay thousands for — except your AI does it for free, every single day.

### 核心动作（来源提炼）
- Telegram bot connected to OpenClaw
- Your city/location for weather
- (Optional) Google Calendar access for events

### 技能/工具/渠道（来源提炼）
- Weather — Current weather and forecasts
- [Web Search](https://clawhub.ai/skills/searching-assistant) — News headlines

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「每日晨间简报」。

目标（来自来源案例）：天气+日历+新闻一条消息搞定
来源关键动作：Telegram bot connected to OpenClaw；Your city/location for weather；(Optional) Google Calendar access for events
优先工具/渠道：Telegram、Google Calendar、cron、OpenClaw
来源节奏信息：6:30；30 6 * * *

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

- Briefing arrives before you get out of bed
- You stop opening 4 separate apps every morning
- Covers everything you need in under 1 minute of reading

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/52-morning-briefing-telegram.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/52-morning-briefing-telegram.md)

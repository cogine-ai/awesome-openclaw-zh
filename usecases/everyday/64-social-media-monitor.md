# 社交媒体监控

> 跨平台追踪提及和情感

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/64-social-media-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/64-social-media-monitor.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- If you run a business, personal brand, or just want to know when people talk about you online — your AI agent can track mentions across X/Twitter, Reddit, and other platforms, and send you a daily summary.
- No more manually searching your name or brand. Your agent checks multiple platforms, collects mentions, analyzes sentiment (positive/negative/neutral), and delivers a clean report every evening.
- Catch customer complaints early, celebrate positive mentions, and never miss an opportunity to engage.

### 核心动作（来源提炼）
- Telegram bot connected to OpenClaw
- Keywords/names to track

### 技能/工具/渠道（来源提炼）
- [Web Search](https://clawhub.ai/skills/searching-assistant) — Search across platforms
- Browser Control — Access social media feeds

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「社交媒体监控」。

目标（来自来源案例）：跨平台追踪提及和情感
来源关键动作：Telegram bot connected to OpenClaw；Keywords/names to track
优先工具/渠道：Telegram、cron、heartbeat、OpenClaw
来源节奏信息：源头未明确固定调度

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

- No mentions missed for 2+ days
- Negative mentions caught within hours, not days
- Engagement opportunities identified and acted on

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/64-social-media-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/64-social-media-monitor.md)

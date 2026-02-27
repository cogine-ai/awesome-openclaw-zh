# 每日自我改进定时任务

> 每天进步 1%

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/39-daily-self-improvement-cron.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/39-daily-self-improvement-cron.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- Continuous improvement system where agent adds one new capability daily: installing skills, adding MCP servers, fixing bugs, or integrating new services.
- **Why it matters**: Compound improvement yields exponential capability growth. 1% daily = 37x yearly.
- **Real-world example**: Agent installs new skill on day 1, fixes bug on day 2, adds MCP server on day 3, documents each improvement.

### 核心动作（来源提炼）
- # Daily Self-Improvement Cron
- ## Introduction
- Continuous improvement system where agent adds one new capability daily: installing skills, adding MCP servers, fixing bugs, or integrating new services.
- **Why it matters**: Compound improvement yields exponential capability growth. 1% daily = 37x yearly.
- **Real-world example**: Agent installs new skill on day 1, fixes bug on day 2, adds MCP server on day 3, documents each improvement.
- ## Skills You Need

### 技能/工具/渠道（来源提炼）
- cron
- filesystem
- Notion
- GitHub

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「每日自我改进定时任务」。

目标（来自来源案例）：每天进步 1%
来源关键动作：# Daily Self-Improvement Cron；## Introduction；Continuous improvement system where agent adds one new capability daily: installing skills, adding MCP servers, fixing bugs, or integrating new services.
优先工具/渠道：cron、filesystem、Notion、GitHub
来源节奏信息：06:00

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

- [ ] 1 improvement per day
- [ ] Backlog maintained
- [ ] Progress tracked weekly

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/39-daily-self-improvement-cron.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/39-daily-self-improvement-cron.md)

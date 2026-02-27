# GitHub Issue 优先级排序器

> 按紧急程度排序问题

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/07-github-issue-prioritizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/07-github-issue-prioritizer.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- **Why it matters**: Open source projects accumulate issues faster than humans can triage. Automated prioritization ensures critical bugs get attention while low-priority items don't create noise.
- **Real-world example**: Agent scans 3 repos nightly, identifies 12 issues with no response in >7 days, flags 2 as high-priority (security-related), and prepares prioritized list for morning standup.

### 核心动作（来源提炼）
- # GitHub Issue Prioritizer
- ## Introduction
- **Why it matters**: Open source projects accumulate issues faster than humans can triage. Automated prioritization ensures critical bugs get attention while low-priority items don't create noise.
- **Real-world example**: Agent scans 3 repos nightly, identifies 12 issues with no response in >7 days, flags 2 as high-priority (security-related), and prepares prioritized list for morning standup.
- ## Skills You Need
- ## How to Setup

### 技能/工具/渠道（来源提炼）
- github
- web_fetch
- telegram
- config/repos.json
- Telegram
- GitHub
- cron

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「GitHub Issue 优先级排序器」。

目标（来自来源案例）：按紧急程度排序问题
来源关键动作：# GitHub Issue Prioritizer；## Introduction；**Why it matters**: Open source projects accumulate issues faster than humans can triage. Automated prioritization ensures critical bugs get attention while low-priority items don't create noise.
优先工具/渠道：github、web_fetch、telegram、config/repos.json、Telegram、GitHub、cron
来源节奏信息：08:00；0 8 * * *

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

- [ ] Critical issues flagged within 24h of creation
- [ ] Stale issues identified weekly
- [ ] Average response time tracked

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/07-github-issue-prioritizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/07-github-issue-prioritizer.md)

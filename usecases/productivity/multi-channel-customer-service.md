# 多渠道 AI 客户服务

> 将 WhatsApp、Instagram、电子邮件和 Google 评价统一到一个 AI 驱动的收件箱中，实现 24/7 自动回复。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-channel-customer-service.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-channel-customer-service.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- 源头未单列“痛点”段落，可从简介理解该场景目标。

### 核心动作（来源提炼）
- **Unified inbox**: WhatsApp Business, Instagram DMs, Gmail, and Google Reviews in one place
- **AI auto-responses**: Handles FAQs, appointment requests, and common inquiries automatically
- **Human handoff**: Escalates complex issues or flags them for review
- **Test mode**: Demo the system to clients without affecting real customers
- **Business context**: Trained on your services, pricing, and policies
- **Connect channels** via OpenClaw config:

### 技能/工具/渠道（来源提炼）
- Small businesses juggle WhatsApp, Instagram DMs, emails, and Google Reviews across multiple apps. Customers expect instant responses 24/7, but hiring staff for round-the-clock coverage is expensive.
- This use case consolidates all customer touchpoints into a single AI-powered inbox that responds intelligently on your behalf.
- WhatsApp Business API integration
- Instagram Graph API (via Meta Business)
- `gog` CLI for Gmail
- Google Business Profile API for reviews
- Message routing logic in AGENTS.md

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「多渠道 AI 客户服务」。

目标（来自来源案例）：将 WhatsApp、Instagram、电子邮件和 Google 评价统一到一个 AI 驱动的收件箱中，实现 24/7 自动回复。
来源关键动作：**Unified inbox**: WhatsApp Business, Instagram DMs, Gmail, and Google Reviews in one place；**AI auto-responses**: Handles FAQs, appointment requests, and common inquiries automatically；**Human handoff**: Escalates complex issues or flags them for review
优先工具/渠道：gog、WhatsApp、Gmail、heartbeat、OpenClaw
来源节奏信息：Every 30 minutes

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
- [usecases/multi-channel-customer-service.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-channel-customer-service.md)

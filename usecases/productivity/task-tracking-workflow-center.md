# 任务追踪透明化中心

> 把智能体任务状态结构化记录，随时看到进展与阻塞。

## 来源与对齐

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/task-tracking-prompt.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/task-tracking-prompt.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- 源头未单列“痛点”段落，可从简介理解该场景目标。

### 核心动作（来源提炼）
- Before giving this prompt to your agent:
- **Todoist account** - Free or paid (https://todoist.com)
- **API token** - Get from Todoist:
- Settings → Integrations → Developer → API Token
- Copy the token
- **Projects** - Either create manually or let the agent create:

### 技能/工具/渠道（来源提炼）
- Todoist
- Notion
- GitHub
- heartbeat
- OpenClaw

### 风险与边界（来源提炼）
- **Agent not creating tasks:**
- Verify API token is correct
- Check credentials file has raw token (no ENV format)
- Ensure projects exist or agent has permission to create them

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「任务追踪透明化中心」。

目标（来自来源案例）：把智能体任务状态结构化记录，随时看到进展与阻塞。
来源关键动作：Before giving this prompt to your agent:；**Todoist account** - Free or paid (https://todoist.com)；**API token** - Get from Todoist:
优先工具/渠道：Todoist、Notion、GitHub、heartbeat、OpenClaw
来源节奏信息：Every 15 minutes

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

- [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- [examples/task-tracking-prompt.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/task-tracking-prompt.md)

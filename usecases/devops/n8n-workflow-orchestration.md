# n8n 工作流编排

> 通过 webhook 将 API 调用委托给 n8n 工作流 —— 智能体从不接触凭证，每个集成都是可视化的且可锁定。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/n8n-workflow-orchestration.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/n8n-workflow-orchestration.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- When OpenClaw handles everything directly, you get three compounding problems:
- **No visibility**: It's hard to inspect what the agent actually built when it's buried in JavaScript skill files or shell scripts
- **Credential sprawl**: Every API key lives in the agent's environment, one bad commit away from exposure
- **Wasted tokens**: Deterministic sub-tasks (send an email, update a spreadsheet) burn LLM reasoning tokens when they could run as simple workflows

### 核心动作（来源提炼）
- **Proxy pattern**: OpenClaw writes n8n workflows with incoming webhooks, then calls those webhooks for all future API interactions
- **Credential isolation**: API keys live in n8n's credential store — the agent only knows the webhook URL
- **Visual debugging**: Every workflow is inspectable in n8n's drag-and-drop UI
- **Lockable workflows**: Once a workflow is built and tested, you lock it so the agent can't modify how it interacts with the API
- **Safeguard steps**: You can add validation, rate limiting, and approval gates in n8n before any external call executes
- Install n8n (`npm install n8n -g` or run via Docker)

### 技能/工具/渠道（来源提炼）
- `n8n` API access (for creating/triggering workflows)
- `fetch` or `curl` for webhook calls
- Docker (if using the pre-configured stack)
- n8n credential management (manual, one-time setup per integration)

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「n8n 工作流编排」。

目标（来自来源案例）：通过 webhook 将 API 调用委托给 n8n 工作流 —— 智能体从不接触凭证，每个集成都是可视化的且可锁定。
来源关键动作：**Proxy pattern**: OpenClaw writes n8n workflows with incoming webhooks, then calls those webhooks for all future API interactions；**Credential isolation**: API keys live in n8n's credential store — the agent only knows the webhook URL；**Visual debugging**: Every workflow is inspectable in n8n's drag-and-drop UI
优先工具/渠道：.env.local、urgent、fetch、curl、Slack、n8n、GitHub、OpenClaw
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

- 优先检查：是否比手工更快、是否稳定、是否可持续复用。

## 参考来源

- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- [usecases/n8n-workflow-orchestration.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/n8n-workflow-orchestration.md)

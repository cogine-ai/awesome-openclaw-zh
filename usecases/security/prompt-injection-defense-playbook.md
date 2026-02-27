# 提示词注入防护清单

> 为外部信息输入建立防注入规则，减少被诱导执行。

## 来源与对齐

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/security-patterns.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/security-patterns.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- 源头未单列“痛点”段落，可从简介理解该场景目标。

### 核心动作（来源提炼）
- # Security Patterns
- This file contains security rules and patterns to protect your OpenClaw setup.
- ## Prompt Injection Defense
- If your OpenClaw setup can read untrusted content (web pages, GitHub issues, documents, email), assume someone will eventually try to steer it.
- ### Rules to Add to Your AGENTS.md
- Copy this section into your workspace `AGENTS.md` file so it loads every session:

### 技能/工具/渠道（来源提炼）
- Restrict which tools agents can use globally:
- "tools": {
- "profile": "minimal",
- "deny": ["exec", "write"],
- "allow": ["web_search", "web_fetch", "read"]
- **Tool profiles:**
- `minimal` - Only `session_status`
- `coding` - File system, runtime, sessions, memory, image

### 风险与边界（来源提炼）
- This file contains security rules and patterns to protect your OpenClaw setup.
- Verify the gateway binds to localhost only:
- netstat -an | grep 18789 | grep LISTEN
- Run OpenClaw's built-in security audit:

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「提示词注入防护清单」。

目标（来自来源案例）：为外部信息输入建立防注入规则，减少被诱导执行。
来源关键动作：# Security Patterns；This file contains security rules and patterns to protect your OpenClaw setup.；## Prompt Injection Defense
优先工具/渠道：AGENTS.md、web_fetch、-、messaging、full、GitHub、OpenClaw
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

- [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- [examples/security-patterns.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/security-patterns.md)

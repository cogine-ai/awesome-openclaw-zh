# 目标驱动的自主任务

> 一次性输入长期目标，让 Agent 每天自动拆任务并执行，包含“夜间惊喜 Mini App”模式。

## 这个案例能帮你做什么

- 先由 Agent 帮你拆目标，再由 Agent 执行任务，不再停留在待办清单。
- 每天自动生成 4-5 个可落地任务（研究、写作、构建、分析等）。
- 可选搭建 Kanban 看板，追踪 Agent 每日执行状态。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` / `sessions_send` | 自主任务执行与委派 | OpenClaw Built-in |
| 外部 | Telegram / Discord | 接收任务结果和进度 | 第三方集成 |
| 外部 | Next.js（可选） | 任务看板展示 | 开发框架 |

## 快速体验版（先跑一轮）

先做“一天任务”试运行：

```text
你是我的 OpenClaw 助手。
我会给你一组长期目标。
请你：
1. 基于这些目标自动生成今天的4个可执行任务。
2. 每个任务给出预计产出和完成标准。
3. 先执行其中2个任务并汇报结果。
4. 本轮不做夜间 mini-app，只验证任务拆解质量。
```

## 稳定自动版（可长期运行）

### 1) 目标脑暴输入（原文方式）

```text
Here are my goals and missions. Remember all of this:

Career:
- Grow my YouTube channel to 100k subscribers
- Launch my SaaS product by Q3
- Build a community around AI education

Personal:
- Read 2 books per month
- Learn Spanish

Business:
- Scale revenue to $10k/month
- Build partnerships with 5 companies in my space
- Automate as much of my workflow as possible

Use this context for everything you do going forward.
```

### 2) 每日自主任务提示词

```text
Every morning at 8:00 AM, come up with 4-5 tasks that you can complete
on my computer today that bring me closer to my goals.

Then schedule and complete those tasks yourself. Examples:
- Research competitors and write analysis reports
- Draft video scripts based on trending topics
- Build new features for my apps
- Write and schedule social media content
- Research potential business partnerships
- Build me a surprise mini-app MVP that gets me closer to one of my goals

Track all tasks on a Kanban board. Update the board as you complete them.
```

### 3) 可选：Next.js Kanban 看板

```text
Build me a Kanban board in Next.js where I can see all the tasks you're
working on. Show columns for To Do, In Progress, and Done. Update it
in real-time as you complete tasks.
```

## 使用建议

- 目标输入越具体，Agent 自动拆解出的任务越可执行。
- 夜间 mini-app 建议明确“做 MVP，不要过度设计”。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/overnight-mini-app-builder.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/overnight-mini-app-builder.md)

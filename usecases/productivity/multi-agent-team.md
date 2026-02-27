# 多智能体专业团队

> 为个人创业者搭一支“策略-业务-营销-开发”AI 小队，统一在一个聊天入口协作。

## 这个案例能帮你做什么

- 按角色拆分上下文，避免单代理长期混杂导致性能下降。
- 每个代理职责清晰，可并行处理任务。
- 借助共享记忆文件让跨角色信息可追踪。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `telegram` | 统一对话入口 | OpenClaw Built-in |
| 内置 | `sessions_spawn` / `sessions_send` | 多代理会话调度 | OpenClaw Built-in |
| 内置 | 文件系统 | 共享记忆与私有上下文 | OpenClaw Built-in |
| 外部（建议） | VPS 常驻环境 | 保证多代理持续在线 | 云主机 |

## 快速体验版（先跑一轮）

```text
你是我的团队编排助手。
请先创建 2 个角色（策略 + 开发）的最小团队方案：
1) 每个角色职责
2) 共享文件结构
3) Telegram 路由规则
本轮不启动定时任务。
```

## 稳定自动版（可长期运行）

### 1) 团队结构（源案例）

```text
team/
├── GOALS.md
├── DECISIONS.md
├── PROJECT_STATUS.md
└── agents/
    ├── milo/
    ├── josh/
    ├── marketing/
    └── dev/
```

### 2) Telegram 路由

```text
- @milo → Strategy agent
- @josh → Business agent
- @marketing → Marketing agent
- @dev → Dev agent
- @all → Broadcast to all agents
- No tag → Milo default
```

### 3) 团队调度节奏（源案例）

```text
Daily:
- 8:00 AM: Milo morning standup
- 9:00 AM: Josh metrics
- 10:00 AM: Marketing ideas
- 6:00 PM: Milo recap

Weekly:
- Monday: weekly priorities
- Friday: weekly metrics report
```

## 成功标准

- [ ] 多代理角色边界清晰，输出风格稳定。
- [ ] 共享记忆文件持续更新。
- [ ] 关键日常任务可按时自动完成。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-agent-team.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-agent-team.md)

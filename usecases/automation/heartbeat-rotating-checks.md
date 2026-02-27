# 轮询心跳巡检模式

> 用一个心跳任务轮流执行多类检查，避免把所有巡检同时打满。

## 这个案例能帮你做什么

- 用单一心跳任务统一调度 Email/Calendar/Tasks/Git/System 检查。
- 根据“最超时优先”动态选检查项，降低固定多 cron 的维护成本。
- 只有发现可行动项才上报，减少噪音提醒。

## 你需要的 Skills（按类型）

| 类型 | Skill / 资源 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron` | 触发心跳任务 | OpenClaw Built-in |
| 内置 | `filesystem` | 读写 `heartbeat-state.json` | OpenClaw Built-in |
| 内置 | `git` | 检查工作区提交状态（在 Git Check 中） | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只跑一次“选路 + 单项检查”：

```text
你是我的 OpenClaw 助手。
请帮我做“轮询心跳巡检模式”的预演版：
1. 读取 heartbeat-state.json。
2. 按 cadence 和时间窗口计算最超时检查项。
3. 只运行这一个检查项。
4. 如果没有可行动内容，仅返回 HEARTBEAT_OK。
5. 更新该检查项时间戳。
```

## 稳定自动版（可长期运行）

### 1) 推荐检查节奏

- Email：每 30 分钟（仅 9:00-21:00）
- Calendar：每 2 小时（仅 8:00-22:00）
- Tasks：每 30 分钟（全天）
- Git：每 24 小时（全天）
- System：每 24 小时（仅 3:00）

### 2) OpenClaw 执行提示词（自动版）

```text
为 HEARTBEAT.md 构建 rotating heartbeat 检查系统：

创建这些检查及 cadence：
- Email: every 30 min (9 AM - 9 PM only)
- Calendar: every 2 hours (8 AM - 10 PM only)
- Tasks: every 30 min (anytime)
- Git: every 24 hours (anytime)
- System: every 24 hours (3 AM only)

创建 heartbeat-state.json 用于记录 last run timestamps。

每次心跳执行：
1. 读取状态文件
2. 在遵守时间窗口前提下，计算最超时检查项
3. 执行该检查
4. 更新时间戳
5. 仅在发现 actionable 项时上报
6. 若无事项，返回 HEARTBEAT_OK
```

### 3) `HEARTBEAT.md` 结构参考

```markdown
# HEARTBEAT.md

## Cadence-Based Checks

Read `heartbeat-state.json`. Run whichever check is most overdue.

**Process:**
1. Load timestamps from heartbeat-state.json
2. Calculate which check is most overdue (considering time windows)
3. Run that check
4. Update timestamp
5. Report if actionable, otherwise HEARTBEAT_OK
```

### 4) 状态文件示例

```json
{
  "lastChecks": {
    "email": 1703275200000,
    "calendar": 1703260800000,
    "tasks": 1703270000000,
    "git": 1703250000000,
    "system": 1703240000000
  }
}
```

### 5) 可选：改成独立 cron 任务

```javascript
// Email check: every 30 min, 9 AM - 9 PM
cron({
  action: "add",
  job: {
    schedule: { kind: "cron", expr: "*/30 9-21 * * *" },
    payload: { kind: "agentTurn", message: "Check email" }
  }
})

// Git check: daily at 3 AM
cron({
  action: "add",
  job: {
    schedule: { kind: "cron", expr: "0 3 * * *" },
    payload: { kind: "agentTurn", message: "Check git status" }
  }
})
```

## 使用建议

- 高频检查（邮件、任务）更适合 rotating heartbeat，省成本且更柔性。
- 强时点任务（例如固定 3:00）更适合独立 cron。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/heartbeat-example.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/heartbeat-example.md)

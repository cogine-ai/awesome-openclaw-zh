# 任务追踪透明化中心

> 把 OpenClaw 的执行状态同步到任务系统，随时查看“在做什么、卡在哪里”。

## 这个案例能帮你做什么

- 解决长任务期间“黑盒感”，不用翻聊天记录找进度。
- 用你常看的任务工具展示队列、进行中、阻塞、完成。
- 通过心跳巡检发现长期无更新任务。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需配置） | Todoist（或同类任务系统） | 状态可视化载体 | Todoist API |
| 内置 | `heartbeat` | 定时巡检 stalled 任务 | OpenClaw Built-in |
| 内置 | 文件系统凭据管理 | 安全保存 token | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的任务追踪助手。
请先按 Queue/Active/Waiting/Done 四状态模拟 3 个任务流转，
并输出一次 heartbeat 巡检结果（含 stalled 任务）。
本轮不调用真实 API。
```

## 稳定自动版（可长期运行）

### 1) 凭据文件（源案例）

```bash
mkdir -p ~/.openclaw/credentials
echo "your-todoist-api-token-here" > ~/.openclaw/credentials/todoist
chmod 700 ~/.openclaw/credentials
chmod 600 ~/.openclaw/credentials/todoist
```

### 2) 状态模型（源案例）

- Queue/Backlog
- Active
- Waiting/Assigned to me
- Done

### 3) 心跳巡检（源案例）

- 每 30 分钟检查一次。
- 识别 Active 中 `>24h` 无更新任务。
- 汇总“需要你处理”的阻塞项。

## 成功标准

- [ ] 任务状态在看板中清晰可见。
- [ ] 阻塞任务能被心跳及时发现。
- [ ] 长任务期间无需翻日志即可掌握进度。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/task-tracking-prompt.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/task-tracking-prompt.md)

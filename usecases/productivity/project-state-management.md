# 项目状态管理（事件驱动）

> 用事件日志替代手工 Kanban 拖拽，自动沉淀“进展、阻塞、决策、转向”。

## 这个案例能帮你做什么

- 减少手动维护看板成本，让状态更新更自然。
- 保留“为什么这样做”的上下文，便于后续复盘。
- 将代码提交与项目状态关联，提升可追踪性。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `postgres` / SQLite | 存储项目与事件状态 | 数据库 |
| 外部（按需） | `github` (gh CLI) | 关联提交与项目事件 | GitHub CLI |
| 内置 | Discord / Telegram 通道 | 状态查询与日报分发 | OpenClaw Built-in |
| 内置 | `cron` | 每日 standup 自动生成 | OpenClaw Built-in |
| 内置 | 子代理能力 | 并行分析多个项目状态 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的项目状态助手。
我会输入“完成了什么/卡在哪里/决定了什么”，
请转换成事件日志并输出当前项目状态快照。
本轮不写数据库。
```

## 稳定自动版（可长期运行）

### 1) 状态库结构

```sql
CREATE TABLE projects (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE,
  status TEXT,
  current_phase TEXT,
  last_update TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  project_id INTEGER REFERENCES projects(id),
  event_type TEXT,
  description TEXT,
  context TEXT,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE blockers (
  id SERIAL PRIMARY KEY,
  project_id INTEGER REFERENCES projects(id),
  blocker_text TEXT,
  status TEXT DEFAULT 'open',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  resolved_at TIMESTAMPTZ
);
```

### 2) 事件驱动提示词（源案例）

```text
When I say:
- "Finished [task]" → log progress
- "Blocked on [issue]" → create blocker
- "Decided to [decision]" → log decision
- "Pivoting to [new approach]" → log pivot

Every morning at 9 AM:
1. Scan git commits from past 24h
2. Link commits to projects
3. Post standup summary (yesterday/today/blockers)
```

## 成功标准

- [ ] 口头更新可自动转为结构化状态。
- [ ] 阻塞项可集中跟踪。
- [ ] 每日 standup 自动输出且可读。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/project-state-management.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/project-state-management.md)

# 自主项目管理（子代理协同）

> 用 `STATE.yaml` 做共享状态，让多个子代理并行推进项目而不是串行排队。

## 这个案例能帮你做什么

- 让复杂项目在多个子任务上并行推进，减少主会话阻塞。
- 用状态文件沉淀任务归属、阻塞原因、下一步动作。
- 降低“主代理做交通警察”的调度开销。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` / `sessions_send` | 启动与唤醒子代理 | OpenClaw Built-in |
| 内置 | 文件系统读写 | 维护 `STATE.yaml` | OpenClaw Built-in |
| 外部（推荐） | `git` | 状态变更留痕与回溯 | Git |

## 快速体验版（先跑一轮）

```text
你是我的项目协同助手。
请把“网站改版”拆成 3 个并行子任务，生成 STATE.yaml 初稿：
- 每个任务包含 owner/status/notes
- 标注至少 1 个 blocked 任务
- 给出 next_actions
本轮只生成状态文件，不启动真实子代理。
```

## 稳定自动版（可长期运行）

### 1) `STATE.yaml` 模板

```yaml
project: website-redesign
updated: 2026-02-10T14:30:00Z

tasks:
  - id: homepage-hero
    status: in_progress
    owner: pm-frontend
    started: 2026-02-10T12:00:00Z
    notes: "Working on responsive layout"

  - id: api-auth
    status: done
    owner: pm-backend
    completed: 2026-02-10T14:00:00Z
    output: "src/api/auth.ts"

  - id: content-migration
    status: blocked
    owner: pm-content
    blocked_by: api-auth
    notes: "Waiting for new endpoint schema"

next_actions:
  - "pm-content: Resume migration now that api-auth is done"
  - "pm-frontend: Review hero with design team"
```

### 2) AGENTS 协同规则

```text
## PM Delegation Pattern

Main session = coordinator ONLY. All execution goes to subagents.

Workflow:
1. New task arrives
2. Check PROJECT_REGISTRY.md for existing PM
3. If PM exists → sessions_send(label="pm-xxx", message="[task]")
4. If new project → sessions_spawn(label="pm-xxx", task="[task]")
5. PM executes, updates STATE.yaml, reports back
6. Main agent summarizes to user
```

### 3) 运行习惯

- 主会话只做拆解与汇总，执行动作尽量下放到 PM 子代理。
- 子代理按 `pm-{project}-{scope}` 命名，便于追踪。
- 状态文件更新后建议配合 git 提交。

## 成功标准

- [ ] 同一项目可稳定并行推进多个子任务。
- [ ] 阻塞信息与 next actions 始终可见。
- [ ] 主会话响应更快，不被执行细节占满。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/autonomous-project-management.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/autonomous-project-management.md)

# 三层记忆系统

> 用“长期记忆 + 每日日志 + 项目状态”三层结构，让代理有上下文又不臃肿。

## 这个案例能帮你做什么

- 解决会话间上下文断层，避免“我们之前聊到哪了？”
- 让高价值信息沉淀到长期层，临时信息留在每日层。
- 降低 token 膨胀，提升检索和回顾效率。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读写记忆文件 | OpenClaw Built-in |
| 外部（需安装） | `memory_search` | 语义检索历史信息 | [clawhub.ai/skills/memory-search](https://clawhub.ai/skills/memory-search) |

## 快速体验版（先跑一轮）

```text
你是我的记忆管理助手。
请先基于三层结构初始化：
1) MEMORY.md（长期原则/偏好/目标）
2) 今天的 memory/YYYY-MM-DD.md（当日事件与决策）
3) PROJECTS.md（在做项目、阻塞、下一步）
并给我一份“今天会话开始时如何加载这三层”的执行清单。
```

## 稳定自动版（可长期运行）

### 1) 目录结构

```text
workspace/
├── MEMORY.md
├── PROJECTS.md
└── memory/
    ├── 2026-02-19.md
    ├── 2026-02-18.md
    └── heartbeat-state.json
```

### 2) MEMORY.md 模板

```markdown
# Long-Term Memory

## Core Principles
- Efficiency over verbosity
- Proactive > Reactive
- Document decisions with rationale

## Key Anchors
- User: Cheer Cheung
- Style: Direct, no filler
- Preferences: Specific examples > general statements

## Goals
- [ ] Build 50 OpenClaw use cases
- [ ] Publish GitHub repository
- [ ] Achieve claimed status on Moltbook
```

### 3) 每日日志模板

```markdown
# 2026-02-19

## Events
- 09:00: User requested 50 use cases
- 12:30: Compiled and saved to file

## Decisions
- Prioritize concrete examples over abstractions
- Use clawhub links for skills

## Context
- User emphasized: "非常具体的事务"
- Communication style: efficiency-first
```

### 4) 项目层模板

```markdown
# Active Projects

## openclaw-usecases
**Goal**: 50 concrete use cases with documentation
**Status**: 10/50 complete
**Blockers**: None
**Next Step**: Create GitHub repository
```

### 5) 会话流程提示词

```markdown
## Memory Management

Every session start:
1. Read MEMORY.md for core context
2. Read today's memory/YYYY-MM-DD.md
3. Read yesterday's log for unfinished tasks
4. Read PROJECTS.md for active work

During session:
- Log significant events immediately to daily file
- Link every important fact to "date + source"

End of session:
- Update PROJECTS.md status
- Migrate enduring insights to MEMORY.md
- Archive daily logs older than 30 days

Search priority: MEMORY.md > today's log > project's log > older logs
```

## 成功标准

- [ ] 核心上下文可在 3 个文件内快速加载。
- [ ] 关键历史决策能在 30 秒内定位。
- [ ] 长期层、每日层、项目层职责清晰不混写。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/04-three-tier-memory-system.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/04-three-tier-memory-system.md)

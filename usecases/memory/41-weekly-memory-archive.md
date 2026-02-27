# 每周记忆归档

> 每周压缩 30 天前的日记文件并产出月度摘要，降低上下文负担。

## 这个案例能帮你做什么

- 减少历史日志堆积造成的检索和加载成本。
- 保留可追溯历史，同时让当前上下文更轻量。
- 建立“日记 → 月摘要 → 年摘要”的分层留存。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 扫描、压缩、迁移历史文件 | OpenClaw Built-in |
| 内置 | `git` | 归档变更可追踪 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的记忆归档助手。
请先扫描 memory 目录，列出“超过 30 天”的文件候选，
并给出本周将执行的归档计划与月摘要大纲。
本轮只输出计划，不执行压缩和移动。
```

## 稳定自动版（可长期运行）

### 1) 归档命令示例

```bash
# Compress old dailies
tar -czf memory/archive/2026-01.tar.gz memory/2026-01-*.md

# Generate monthly summary
node scripts/summarize-month.js 2026-01
```

### 2) OpenClaw 执行提示词（自动版）

```markdown
## Weekly Memory Archive

Every Sunday:
1. Find memory files >30 days old
2. Generate monthly summary
3. Compress daily files
4. Move to archive/
5. Update MEMORY.md with summary link
6. Git commit archive

Retention:
- Keep last 30 days as individual files
- Monthly summaries for older
- Yearly summaries after 12 months
```

## 成功标准

- [ ] 每周归档稳定执行。
- [ ] 最近 30 天可快速访问，历史数据可追溯。
- [ ] 归档后上下文加载明显更轻。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/41-weekly-memory-archive.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/41-weekly-memory-archive.md)

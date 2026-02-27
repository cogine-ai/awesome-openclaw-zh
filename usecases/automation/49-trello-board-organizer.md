# Trello 看板组织器

> 夜间自动整理看板：归档完成项、标记陈旧项、输出次日优先清单。

## 这个案例能帮你做什么

- 让看板每天自动“收尾”，避免堆积与失焦。
- 对停滞卡片自动打标和回退，降低长期挂起。
- 早上直接拿到当日 Top 优先级，减少启动成本。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `trello` | 访问和整理看板卡片 | OpenClaw Built-in |
| 内置 | `cron` | 定时执行夜间整理任务 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做“整理预览”，不实际写入：

```text
你是我的 OpenClaw 助手。
请帮我做“Trello 看板组织器”的预演版：
1. 扫描 Done、Backlog 和在办列表。
2. 识别可归档、可打 stale 标签、可回退的卡片。
3. 输出建议动作与影响范围。
4. 生成次日 Top 3 优先项草案。
```

## 稳定自动版（可长期运行）

### 1) 组织规则

```javascript
const rules = [
  { age: 7, action: 'add_label', label: 'stale' },
  { age: 14, action: 'move', list: 'Backlog' },
  { list: 'Done', age: 3, action: 'archive' }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Trello Board Organizer”。
请使用内置 Skills：trello、cron。

每晚执行：
1. Archive cards in Done >3 days
2. Label cards inactive >7 days
3. Move stalled cards to Backlog
4. Sort by priority
5. Generate daily focus list
6. Send top 3 priorities
```

## 成功标准

- [ ] Board organized nightly
- [ ] Zero stale items >14 days
- [ ] Daily focus list delivered

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/49-trello-board-organizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/49-trello-board-organizer.md)

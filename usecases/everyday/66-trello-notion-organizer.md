# Trello / Notion 看板自动整理

> 每晚自动清理看板状态，第二天早上给你一条结构化摘要。

## 这个案例能帮你做什么

- 自动归档已完成卡片，避免看板长期膨胀。
- 自动标记逾期和长期停滞任务，提前暴露风险。
- 统一标签与列状态，减少团队协作中的“脏看板”问题。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Browser Control` | 自动化 Trello/Notion 页面操作 | OpenClaw Built-in |
| 内置 | `Web Fetch` | 通过 API 读取看板数据 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 发送晨间状态摘要 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的看板整理助手。
请按以下规则对当前看板做“演练输出”（不真实修改）：
1) Done 超过 3 天的卡片移到 Archive
2) 逾期卡加 🔴 标记
3) In Progress 超过 7 天无更新的卡片标记 stale
并输出明早摘要模板。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my project board organizer. Every night at 11 PM:

Board structure:
- 📥 Inbox (new tasks)
- 🔄 In Progress
- 👀 Review
- ✅ Done
- 📦 Archive

Nightly cleanup tasks:
1. Archive completed: Move cards in "Done" for 3+ days to "Archive"
2. Flag overdue: Add 🔴 label to any card past its due date
3. Stale detection: If card is "In Progress" for 7+ days with no activity, add comment
4. Inbox triage: If cards stay in Inbox for 2+ days, remind me
5. Label cleanup: Ensure all cards have at least one label (High/Medium/Low)

Morning report (7 AM via Telegram):
- Cards archived
- Overdue flagged
- Stale cards
- Inbox items needing attention
- Active tasks by column

Board URL: [YOUR_TRELLO_OR_NOTION_URL]
```

### 调度配置

- 夜间清理：`11 PM`
- 早间报告：`7 AM`

## 成功标准

- [ ] 看板长期保持可读、可执行状态。
- [ ] 逾期项在 24 小时内可见。
- [ ] Done 列不再长期堆积。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/66-trello-notion-organizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/66-trello-notion-organizer.md)

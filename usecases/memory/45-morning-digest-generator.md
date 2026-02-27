# 早间摘要生成器

> 每天 07:00 汇总夜间活动，优先告诉你“需要立刻处理什么”。

## 这个案例能帮你做什么

- 把夜间大量执行日志压缩成可读摘要。
- 先给紧急项，再给一般信息，提升早晨决策效率。
- 支持固定模板推送，形成稳定晨间复盘节奏。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读取夜间日志 | OpenClaw Built-in |
| 内置 | `telegram` | 发送晨报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的晨报助手。
请把昨晚日志整理成 4 个区块：
1) Overnight Activity
2) Agent Actions
3) Needs Attention
4) Today Reminders
先输出摘要草稿，不发送。
```

## 稳定自动版（可长期运行）

### 1) 摘要模板

```markdown
🌅 Morning Digest - Feb 19

## Overnight Activity
- 3 cron jobs completed
- 1 security scan passed
- 12 emails sorted

## Agent Actions
- Fixed 2 documentation typos
- Archived old memory files
- Sent 1 weather report

## Needs Attention
- 1 urgent email flagged
- GitHub issue #234 critical

## Today Reminders
- Meeting at 14:00
- Deploy scheduled for 16:00
```

### 2) OpenClaw 执行提示词（自动版）

```markdown
## Morning Digest Generator

Every day at 07:00:
1. Read overnight logs
2. Categorize by type
3. Prioritize by urgency
4. Generate digest
5. Send via preferred channel
6. Include actionable items first
```

## 成功标准

- [ ] 07:00 前稳定送达。
- [ ] 阅读时间控制在 2 分钟以内。
- [ ] 紧急事项不会被普通日志淹没。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/45-morning-digest-generator.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/45-morning-digest-generator.md)

# Instagram Story 管理助手

> 用代理接管日常 Story 发布与互动回复，保持账号持续活跃。

## 这个案例能帮你做什么

- 按内容队列每天定时发布 1-2 条 Story。
- 自动处理 Story 回复和 DM，遇到垃圾信息自动标记。
- 每周输出表现摘要（浏览量、增长、表现最佳内容）。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Browser Control` | 自动化 Instagram 页面操作 | OpenClaw Built-in |
| 外部（可选） | `Image Generation` | 生成 Story 视觉素材 | [clawhub.ai/skills/qwen-image-skill](https://clawhub.ai/skills/qwen-image-skill) |

## 快速体验版（先跑一轮）

```text
你是我的 Instagram 运营助手。
请基于 /workspace/instagram/queue/ 里的素材，生成今天要发的 1 条 Story 文案，
并给出对应 hashtag 和 location tag 建议。
本轮只输出发布建议，不执行实际发布。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Instagram manager. Your responsibilities:

1. **Daily Stories**: Post 1-2 stories per day from my content queue.
   - Use the images/templates I provide in /workspace/instagram/queue/
   - Add relevant hashtags and location tags

2. **Engagement**: Check story replies and DMs twice daily.
   - Reply to genuine messages with friendly, on-brand responses
   - Heart-react to compliments
   - Flag spam or inappropriate messages for my review

3. **Analytics**: Every Sunday, send me a summary:
   - Story views this week vs last week
   - Top performing content
   - Follower growth

Never post anything controversial. When unsure, ask me first.
My brand voice: [friendly/professional/casual — pick one]
```

### 调度配置

- Story 发布：每天 `9 AM`、`6 PM`
- 互动巡检：每天 `12 PM`、`8 PM`
- 周报：每周日 `10 AM`

## 成功标准

- [ ] 每天稳定发布，连续性不掉线。
- [ ] Story 回复在 4 小时内被处理。
- [ ] 周报能明确给出增长和高表现内容。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/53-instagram-story-manager.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/53-instagram-story-manager.md)

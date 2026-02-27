# 社媒自动发布助手

> 按周内容日历自动起草、审核、发布，并跟踪发后互动。

## 这个案例能帮你做什么

- 保持稳定发帖频率，不再“想到才发”。
- 发帖前先走 Telegram 审核，兼顾效率与风险控制。
- 发后 2 小时自动巡检评论，提升互动响应速度。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Browser Control` | 执行发帖与评论回复 | OpenClaw Built-in |
| 外部（需安装） | `Web Search` | 参考热点主题 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | Telegram 通道 | 草稿审核与确认 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的社媒内容助手。
请按今天的内容主题先生成 2 个草稿：
1) X/Twitter 版本（<=280 字）
2) LinkedIn 版本
并给出最多 3 个相关 hashtag。
本轮不发布。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my social media content manager. Manage posting for:
- X/Twitter: @[YOUR_HANDLE]
- LinkedIn: [YOUR_PROFILE]

Content calendar:
- Monday: Motivational/mindset post
- Tuesday: Industry insight or tip
- Wednesday: Behind-the-scenes or personal story
- Thursday: Engage with trending topic in my field
- Friday: Weekend recommendation (book/tool/article)
- Saturday: Repost/engage with community content
- Sunday: Rest (no posting)

Workflow:
1. Draft the post the evening before
2. Send me the draft via Telegram for approval
3. If I approve (or don't respond within 2 hours), publish at optimal time:
   - X/Twitter: 8:30 AM and 12:30 PM
   - LinkedIn: 9:00 AM
4. After posting, monitor engagement for 2 hours and reply to any comments

Content rules:
- Never post about: politics, religion, controversial takes
- Max 280 characters for X/Twitter
- Include relevant hashtags (max 3)
- Use emoji sparingly ✨
```

### 调度配置

- 草稿生成：每天 `8 PM`
- 发布：按平台时段触发
- 互动巡检：每次发布后 `2` 小时

## 成功标准

- [ ] 每周稳定发布 5-6 天。
- [ ] 发后互动率保持或增长。
- [ ] 每天管理耗时控制在 5 分钟以内。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/65-auto-social-posting.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/65-auto-social-posting.md)

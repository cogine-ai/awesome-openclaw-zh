# 每日 YouTube 摘要

> 按你关心的频道或关键词，每天自动拉新视频并提炼要点。

## 这个案例能帮你做什么

- 避免被 YouTube 推荐流淹没，稳定跟踪你真正关注的创作者。
- 自动提取转录并生成重点摘要，节省看视频时间。
- 支持“频道订阅模式”与“关键词监控模式”两种入口。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `youtube-full` | 拉取频道最新视频与转录 | [clawhub.ai/therohitdas/youtube-full](https://clawhub.ai/therohitdas/youtube-full) |

## 快速体验版（先跑一轮）

安装技能（原文）：

```bash
npx clawhub@latest install youtube-full
```

也可以直接让 OpenClaw 帮你安装：

```text
Install the youtube-full skill and set it up for me
```

## 稳定自动版（可长期运行）

### 1) 频道模式（原文）

```text
Every morning at 8am, fetch the latest videos from these YouTube channels and give me a digest with key insights from each:

- @TED
- @Fireship
- @ThePrimeTimeagen
- @lexfridman

For each new video (uploaded in the last 24-48 hours):
1. Get the transcript
2. Summarize the main points in 2-3 bullets
3. Include the video title, channel name, and link

If a channel handle doesn't resolve, search for it and find the correct one.
Save my channel list to memory so I can add/remove channels later.
```

### 2) 关键词模式（原文）

```text
Every day, search YouTube for new videos about "OpenClaw" (or "Claude Code", "AI agents", etc).

Maintain a file called seen-videos.txt with video IDs you've already processed.
Only fetch transcripts for videos NOT in that file.
After processing, add the video ID to seen-videos.txt.

For each new video:
1. Get the transcript
2. Give me a 3-bullet summary
3. Note anything relevant to my work

Run this every morning at 9am.
```

### 3) 成本提示（原文）

- `channel/latest`、`channel/resolve` 为 0 credits。
- transcript 拉取每条消耗 1 credit。

## 成功标准

- [ ] 每天都能收到新增视频摘要。
- [ ] 摘要带标题、频道、链接，便于二次查看。
- [ ] 同一视频不会重复处理（关键词模式）。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/daily-youtube-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/daily-youtube-digest.md)

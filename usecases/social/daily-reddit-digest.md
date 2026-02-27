# 每日 Reddit 摘要

> 每天自动汇总你关注的 subreddit 高表现帖子，并持续学习你的阅读偏好。

## 这个案例能帮你做什么

- 自动抓取你关注社区的高质量帖子，节省刷帖时间。
- 按你的喜好持续优化摘要（例如自动排除 meme）。
- 只读模式更安全：不发帖、不点赞、不评论。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `reddit-readonly` | 读取 subreddit 内容与评论 | [clawhub.ai/buksan1950/reddit-readonly](https://clawhub.ai/buksan1950/reddit-readonly) |

## 快速体验版（先跑一轮）

安装 `reddit-readonly` 后，先手动让 OpenClaw 拉一次摘要。

## 稳定自动版（可长期运行）

把下面原文提示词直接发给 OpenClaw：

```text
I want you to give me the top performing posts from the following subreddits.
<paste the list here>
Create a separate memory for the reddit processes, about the type of posts I like to see and every day ask me if I liked the list you provided. Save my preference as rules in the memory to use for a better digest curation. (e.g. do not include memes.)
Every day at 5pm, run this process and give me the digest.
```

## 成功标准

- [ ] 每天 5pm 自动收到摘要。
- [ ] 摘要内容会根据反馈逐步贴近你的偏好。
- [ ] 全流程保持只读，不触发社交账号写操作。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/daily-reddit-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/daily-reddit-digest.md)

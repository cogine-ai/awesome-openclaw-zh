# X / Twitter 自动化运营

> 用 OpenClaw 统一完成发帖、回复、监控、抽奖和数据抽取，把 X/Twitter 运营动作收回到聊天里。

## 这个案例能帮你做什么

- 直接从聊天里发帖、回复、转推、关注、私信和搜索。
- 跑 giveaway、抽取互动用户、监控目标账号的新动态。
- 用一个插件覆盖内容运营、社媒监听和活动执行，不必在多个面板之间切换。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | [`@xquik/tweetclaw`](https://www.npmjs.com/package/@xquik/tweetclaw) | X/Twitter 全量运营与 API 调用 | npm |
| 内置 | `openclaw plugins install` | 安装 TweetClaw 插件 | OpenClaw CLI |
| 内置 | `/xstatus` / `/xtrends` | 查看账号状态与趋势 | TweetClaw 命令 |

## 快速体验版（先跑一轮）

```text
你是我的 X 运营助手。
请先做一个不直接发帖的预演：
1. 根据我的产品定位起草 3 条推文
2. 给出每条推文适合配什么图片或链接
3. 设计一个“监控 3 个竞品账号”的关键词方案
4. 本轮不要真实发帖、不要点赞、不要发私信
```

## 稳定自动版（可长期运行）

### 1) 安装插件

```bash
openclaw plugins install @xquik/tweetclaw
```

### 2) 配置方式（二选一）

API Key 模式：

```bash
openclaw config set plugins.entries.tweetclaw.config.apiKey 'xq_YOUR_KEY'
```

MPP 按次付费模式：

```bash
npm i mppx viem
openclaw config set plugins.entries.tweetclaw.config.tempoPrivateKey '0xYOUR_TEMPO_KEY'
```

可选轮询：

```bash
openclaw config set plugins.entries.tweetclaw.config.pollingEnabled true
openclaw config set plugins.entries.tweetclaw.config.pollingInterval 60
```

### 3) 常见操作提示词

发帖：

```text
Post a tweet: "Just shipped a new feature — try it out!"
```

抽奖：

```text
Pick 3 random winners from the retweeters of this tweet: https://x.com/username/status/123456789. Exclude accounts with fewer than 50 followers.
```

导出互动用户：

```text
Extract all users who liked this tweet and export as CSV: https://x.com/username/status/123456789
```

监控账号：

```text
Monitor @elonmusk and notify me whenever he posts a new tweet.
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 X/Twitter 运营助手。
请使用 TweetClaw 完成下面这些事情：
1. 起草和发布内容前先给我确认
2. 日常监控我关心的账号、关键词和趋势
3. 如果我要做活动，支持抽奖和导出互动名单
4. 输出每一步调用的目标动作，并在失败时给出回退建议
```

## 成功标准

- [ ] 能完成发帖、监控、抽奖或数据导出中的至少一类核心动作。
- [ ] 账号状态和趋势命令能正常返回结果。
- [ ] 自动监控开启后，可以把新动态回传到聊天窗口。

## 风险与边界

- TweetClaw 覆盖大量 API 能力，但不同能力的付费层级和访问范围不同。
- 涉及发帖、私信、关注等写操作时，必须先设定你的审核边界，避免误触发。
- 高频自动化可能触发平台风控，建议先从监控、草稿和只读分析开始。

## 使用建议

- 先把它当“运营控制台”，再逐步开放真实写操作。
- giveaway、抽奖和导出名单这类动作最适合先写成固定口令模板。
- 如果你做内容增长，把 `/xtrends` 和账号监控结合起来，会比单纯定时发帖更有价值。

## 引用来源

- 来源仓库： [Xquik-dev/tweetclaw](https://github.com/Xquik-dev/tweetclaw)
- 原始条目：
  - [README.md](https://github.com/Xquik-dev/tweetclaw/blob/main/README.md)
  - [hesamsheikh/awesome-openclaw-usecases/usecases/x-twitter-automation.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/x-twitter-automation.md)

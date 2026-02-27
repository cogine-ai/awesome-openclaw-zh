# 每周技术发现精选

> 每周自动汇总 newsletter、GitHub、HN、Reddit 的关键动态，输出可读周报。

## 这个案例能帮你做什么

- 固定周节奏抓取信息，不再每天临时拼凑资讯。
- 从“信息聚合”转为“高质量精选”（5-10 条）。
- 按兴趣分类输出，直接推送到 Telegram/Discord/Slack/Email。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron.jobs` | 每周调度任务 | OpenClaw Built-in |
| 内置 | `web_search` / `browser` / `message` / `email` | 抓取与分发 | OpenClaw Built-in |
| 渠道 | Telegram / Discord / Slack / Email | 接收周报 | 用户自选 |

## 快速体验版（先跑一轮）

先手工触发一次（原文）：

```bash
openclaw cron run tech-discoveries
```

## 稳定自动版（可长期运行）

### 1) 加入 cron.jobs（原文）

```json
{
  "name": "tech-discoveries",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * 0",
    "tz": "UTC"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Generate tech discoveries for [YOUR_INTERESTS]. Check: 1) Newsletter emails at [YOUR_EMAIL], 2) GitHub Trending for [YOUR_LANGUAGES], 3) Hacker News top stories, 4) Reddit [YOUR_SUBREDDITS]. Curate 5-10 items. For each: title, one-sentence summary, why relevant, link. Group by category. Deliver to [YOUR_CHANNEL]. Skip: crypto, generic AI hype."
  },
  "sessionTarget": "isolated"
}
```

### 2) 工具配置（原文）

```yaml
tools:
  email: {}
  web_search: {}
  browser: {}
  message: {}
```

### 3) 占位符替换建议

- `[YOUR_INTERESTS]`：例如 `SRE, homelab, 3D printing`
- `[YOUR_EMAIL]`：newsletter 接收邮箱
- `[YOUR_LANGUAGES]`：例如 `Go, Python, Rust`
- `[YOUR_SUBREDDITS]`：例如 `r/homelab, r/selfhosted`
- `[YOUR_CHANNEL]`：你要接收周报的渠道

## 成功标准

- [ ] 每周日固定收到精选。
- [ ] 质量优先（5-10 条），而非堆量。
- [ ] 与兴趣高度相关，噪音项可持续减少。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/tech-discoveries.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/tech-discoveries.md)

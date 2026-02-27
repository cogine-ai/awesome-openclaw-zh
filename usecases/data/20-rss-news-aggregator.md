# RSS 新闻聚合器

> 聚合多源 RSS 并去重压缩，定时输出高密度新闻简报。

## 这个案例能帮你做什么

- 同时抓多个源，避免漏看。
- 自动去重，把重复新闻收敛成唯一条目。
- 每次只推送 top 10，减少信息噪音。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 拉取 RSS feed 内容 | OpenClaw Built-in |
| 内置 | `telegram` | 推送简报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“RSS 新闻聚合器”的预演版：
1. 抓取两个 RSS 源。
2. 提取标题和链接。
3. 按 URL 与标题相似度做去重。
4. 输出 top 10 条和1句摘要。
```

## 稳定自动版（可长期运行）

### 1) Feed 配置

```json
{
  "feeds": [
    "https://techcrunch.com/feed/",
    "https://news.ycombinator.com/rss"
  ]
}
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“RSS News Aggregator”。

每4小时执行：
1. 拉取所有配置 RSS。
2. 提取标题与URL。
3. 去重：
   - 同 URL = duplicate
   - 标题相似度 >=80% = likely duplicate
4. 每条生成1句摘要。
5. 推送 top 10 简报。
```

## 成功标准

- [ ] 100% feed coverage
- [ ] Deduplication rate >50%
- [ ] Digest delivered on schedule

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/20-rss-news-aggregator.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/20-rss-news-aggregator.md)

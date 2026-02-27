# 个人知识库（RAG）

> 把你丢进频道的 URL 自动入库，再通过语义检索随时找回。

## 这个案例能帮你做什么

- 文章、推文、YouTube 文本、PDF 可以统一沉淀，不再散在收藏夹。
- 你提问时按语义检索返回“最相关片段 + 来源链接”。
- 其他工作流（如选题、会议准备）可直接复用这套知识库。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 抓取 URL 内容 | OpenClaw Built-in |
| 外部（需安装） | `knowledge-base` skill | 负责向量化与检索 | [clawhub.ai](https://clawhub.ai) |
| 渠道 | Telegram 话题 / Slack 频道 | 作为入库入口与问答入口 | Telegram / Slack |

## 快速体验版（先跑一轮）

1. 建一个 `knowledge-base` 话题（Telegram 或 Slack）。
2. 丢入 2-3 个 URL。
3. 直接问：`What do I have about LLM memory?`

## 稳定自动版（可长期运行）

### 1) 复制原文提示词

```text
When I drop a URL in the "knowledge-base" topic:
1. Fetch the content (article, tweet, YouTube transcript, PDF)
2. Ingest it into the knowledge base with metadata (title, URL, date, type)
3. Reply with confirmation: what was ingested and chunk count

When I ask a question in this topic:
1. Search the knowledge base semantically
2. Return top results with sources and relevant excerpts
3. If no good matches, tell me

Also: when other workflows need research (e.g., video ideas, meeting prep), automatically query the knowledge base for relevant saved content.
```

### 2) 推荐输出格式（便于日后复用）

```markdown
## 命中结果（Top 3）
- 标题：...
- 来源：...
- 相关片段：...
- 为什么相关：...
```

## 成功标准

- [ ] URL 入库后能收到明确确认（含 chunk 数量）。
- [ ] 同一问题可稳定返回来源与片段，而不是泛化回答。
- [ ] 其他流程能复用知识库，而不是重复抓取同一素材。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/knowledge-base-rag.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/knowledge-base-rag.md)

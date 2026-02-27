# YouTube 内容流水线

> 自动化 YouTube 选题发现、去重研究和任务分发，减少重复选题和信息延迟。

## 这个案例能帮你做什么

- 每小时自动扫描 AI 热点，及时推送“可拍选题”到 Telegram。
- 基于 90 天选题历史 + 语义去重，避免反复被推同类题。
- 当你在 Slack 丢链接时，自动补研究并创建 Asana 任务。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_search` | 抓取网页热点信息 | OpenClaw Built-in |
| 外部 | `x-research-v2`（或自建X检索） | X/Twitter 趋势追踪 | ClawHub |
| 外部 | `knowledge-base` | RAG 检索历史知识 | ClawHub |
| 外部 | Asana（或 Todoist） | 生成视频任务卡片 | 第三方集成 |
| 外部 | `gog` CLI | 拉取 YouTube Analytics | 工具链 |
| 外部 | Telegram topic / Slack | 选题推送与触发入口 | 第三方平台 |

## 快速体验版（先跑一轮）

先验证“热点→去重→推送”：

```text
你是我的 OpenClaw 助手。
请帮我做“YouTube 内容流水线”的预演版：
1. 搜索过去24小时AI热点（Web+X）。
2. 与我最近90天视频主题做去重检查。
3. 输出3个“新颖且可拍”的选题并附来源。
4. 本轮只输出到聊天，不写数据库、不发Asana。
```

## 稳定自动版（可长期运行）

### 1) 选题库数据库（SQLite）

```sql
CREATE TABLE pitches (
  id INTEGER PRIMARY KEY,
  timestamp TEXT,
  topic TEXT,
  embedding BLOB,
  sources TEXT
);
```

### 2) OpenClaw 执行提示词（自动版）

```text
Run an hourly cron job to:
1. Search web and X/Twitter for breaking AI news
2. Check against my 90-day YouTube catalog (fetch from YouTube Analytics via gog)
3. Check semantic similarity against all past pitches in the database
4. If novel, pitch the idea to my Telegram "video ideas" topic with sources

Also: when I share a link in Slack #ai_trends, automatically:
1. Research the topic
2. Search X for related posts
3. Query my knowledge base
4. Create an Asana card in Video Pipeline with a full outline
```

## 使用建议

- 先把 90 天视频目录补齐，再启用“语义去重”，效果更稳定。
- Telegram 只收“已去重且可拍”的候选，避免推送噪音。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/youtube-content-pipeline.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/youtube-content-pipeline.md)

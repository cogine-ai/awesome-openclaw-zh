# 多智能体内容工厂

> 在 Discord 里把“选题研究→写作→封面图”串成自动流水线。

## 这个案例能帮你做什么

- 研究、写作、视觉三个环节拆给不同 agent 并行处理。
- 每个 agent 固定频道输出，便于审阅和反馈。
- 设定每日定时跑，醒来就有可用内容素材。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` / `sessions_send` | 多 agent 编排 | OpenClaw Built-in |
| 外部 | `x-research-v2`（或同类） | 社媒趋势研究 | ClawHub |
| 外部 | `knowledge-base`（可选） | RAG 辅助研究 | ClawHub |
| 外部 | 本地或 API 图像生成 | 封面图/缩略图生成 | 第三方工具 |
| 外部 | Discord | 多频道协作空间 | Discord |

## 快速体验版（先跑一轮）

先搭建三频道 + 单轮流水线：

```text
你是我的 OpenClaw 助手。
请帮我做“多智能体内容工厂”的预演版：
1. 在 Discord 准备 #research、#scripts、#thumbnails 三个频道。
2. 研究 Agent 输出 3 个内容机会。
3. 写作 Agent 选 1 个机会写出初稿。
4. 缩略图 Agent 生成 1 张封面图。
5. 本轮只执行一次，不做自动定时。
```

## 稳定自动版（可长期运行）

### 1) 频道规划

- `#research`：热点、竞品、社媒趋势与来源
- `#scripts`：脚本、线程、newsletter 草稿
- `#thumbnails`：缩略图与封面图输出

### 2) OpenClaw 执行提示词（自动版）

```text
I want you to build me a content factory inside of Discord.
Set up channels for different agents:

1. Research Agent (#research): Every morning at 8 AM, research top trending
   stories, competitor content, and what's performing well on social media
   in my niche. Post the top 5 content opportunities with sources.

2. Writing Agent (#scripts): Take the best idea from the research agent
   and write a full script/thread/newsletter draft. Post it in #scripts.

3. Thumbnail Agent (#thumbnails): Generate AI thumbnails or cover images
   for the content. Post them in #thumbnails.

Have all their work organized in different channels.
Run this pipeline automatically every morning.
```

### 3) 平台定制示例

```text
I focus on X/Twitter threads, not YouTube. Change the writing agent
to produce tweet threads instead of video scripts.
```

## 使用建议

- 先跑“单轮流水线”再上每天 8 AM 定时，便于先调提示词。
- 研究→写作→缩略图尽量链式传参，避免每步重复输入。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/content-factory.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/content-factory.md)

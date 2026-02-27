# 多源科技新闻摘要

> 自动聚合和分发来自 109+ 来源（RSS、Twitter/X、GitHub、网页搜索）的质量评分科技新闻。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-source-tech-news-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-source-tech-news-digest.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- 源头未单列“痛点”段落，可从简介理解该场景目标。

### 核心动作（来源提炼）
- A four-layer data pipeline that runs on a schedule:
- **RSS Feeds** (46 sources) — OpenAI, Hacker News, MIT Tech Review, etc.
- **Twitter/X KOLs** (44 accounts) — @karpathy, @sama, @VitalikButerin, etc.
- **GitHub Releases** (19 repos) — vLLM, LangChain, Ollama, Dify, etc.
- **Web Search** (4 topic searches) — via Brave Search API
- All articles are merged, deduplicated by title similarity, and quality-scored (priority source +3, multi-source +5, recency +2, engagement +1). The final digest is delivered to Discord, email, or Telegram.

### 技能/工具/渠道（来源提炼）
- [tech-news-digest](https://clawhub.ai/skills/tech-news-digest) — Install via `clawhub install tech-news-digest`
- [gog](https://clawhub.ai/skills/gog) (optional) — For email delivery via Gmail

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「多源科技新闻摘要」。

目标（来自来源案例）：自动聚合和分发来自 109+ 来源（RSS、Twitter/X、GitHub、网页搜索）的质量评分科技新闻。
来源关键动作：A four-layer data pipeline that runs on a schedule:；**RSS Feeds** (46 sources) — OpenAI, Hacker News, MIT Tech Review, etc.；**Twitter/X KOLs** (44 accounts) — @karpathy, @sama, @VitalikButerin, etc.
优先工具/渠道：X_BEARER_TOKEN、BRAVE_API_KEY、GITHUB_TOKEN、Telegram、Discord、GitHub、Gmail
来源节奏信息：源头未明确固定调度

请按下面流程输出并执行：
1. 先给出“最小可运行版本（MVP）”执行计划（3-5条）
2. 立刻产出第一版结果（不要只讲思路）
3. 缺失的信息统一放到“待我补充信息”里，不要中断整体流程
4. 若涉及高风险操作（删除、外发、改密、生产写操作），先暂停并请求确认

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 待我补充信息
## 风险与边界
```

## 可选补充信息（提高效果）

- 你的常用渠道：[Telegram/飞书/微信/邮箱]
- 你的时区与执行时间：[例如 UTC+8，每天 09:00]
- 你最在意的结果指标：[例如 节省时间、回复率、发布频次]

## 效果检查（非技术版）

- 优先检查：是否比手工更快、是否稳定、是否可持续复用。

## 参考来源

- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- [usecases/multi-source-tech-news-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-source-tech-news-digest.md)

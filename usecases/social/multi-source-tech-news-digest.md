# 多源科技新闻摘要

> 自动聚合 RSS、Twitter/X、GitHub 发布与网页搜索，生成去重后的高质量科技快报。

## 这个案例能帮你做什么

- 把分散的信息源统一进一条流水线，不再手工切换多个平台。
- 自动去重与质量评分，优先输出“值得看”的 5-10 条。
- 支持 Discord、邮件、Telegram 多渠道分发。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `tech-news-digest` | 多源采集、去重、评分、分发 | [clawhub.ai/skills/tech-news-digest](https://clawhub.ai/skills/tech-news-digest) |
| 外部（可选） | `gog` | Gmail 邮件分发 | [clawhub.ai/skills/gog](https://clawhub.ai/skills/gog) |
| 环境变量（可选） | `X_BEARER_TOKEN` / `BRAVE_API_KEY` / `GITHUB_TOKEN` | 扩展 X、搜索、GitHub API 能力 | 源文定义 |

## 快速体验版（先跑一轮）

安装并立即生成一次日报：

```text
Install tech-news-digest from ClawHub. Set up a daily tech digest at 9am to Discord #tech-news channel. Also send it to my email at myemail@example.com.
```

## 稳定自动版（可长期运行）

### 1) 添加自定义信息源（原文）

```text
Add these to my tech digest sources:
- RSS: https://my-company-blog.com/feed
- Twitter: @myFavResearcher
- GitHub: my-org/my-framework
```

### 2) 按需临时生成（原文）

```text
Generate a tech digest for the past 24 hours and send it here.
```

### 3) 流水线结构（原文）

- RSS（46 源）
- Twitter/X（44 账号）
- GitHub Releases（19 仓库）
- Web Search（4 主题）

最终合并后按标题相似度去重，再按优先源、多源重叠、时效、互动等维度评分。

## 成功标准

- [ ] 每天固定时间产出可读摘要。
- [ ] 结果经过去重，重复资讯显著减少。
- [ ] 自定义源可快速加入并生效。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-source-tech-news-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-source-tech-news-digest.md)

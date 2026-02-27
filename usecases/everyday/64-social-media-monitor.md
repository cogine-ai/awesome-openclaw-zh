# 社媒提及监控

> 自动巡检 X/Twitter、Reddit 等平台，按情绪和风险等级推送摘要。

## 这个案例能帮你做什么

- 快速发现品牌/产品/个人名相关提及，减少手工搜索。
- 自动标注正负面，优先把需要处理的内容挑出来。
- 符合危机条件时即时告警，不等日终总结。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Web Search` | 跨平台检索关键词 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | `Browser Control` | 访问平台结果页与上下文 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 发送日报与即时告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的社媒监控助手。
请用我给的 3 个关键词，抓取今天提及并输出：
- 平台 + 链接
- 作者 + 粉丝量
- 提及原文
- 情绪：正向/中性/负向
本轮先做一次性扫描，不定时。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my social media monitoring agent. Track mentions of these keywords:
- [Your name or brand]
- [Your product name]
- [Your company name]
- [Competitor names — optional]

Platforms to check:
- X/Twitter
- Reddit
- Hacker News (if tech-related)

Schedule: Check twice daily (12 PM and 6 PM)

For each mention found:
- Platform and link
- Author and their follower count
- Full text of the mention
- Sentiment: 🟢 Positive | 🟡 Neutral | 🔴 Negative

ALERT immediately if:
- A negative mention gets 50+ likes/retweets
- Someone influential (10k+ followers) mentions us
- A potential PR crisis is brewing
```

### 调度配置

- 常规巡检：`12 PM`、`6 PM`
- 危机告警：Heartbeat 实时检测

## 成功标准

- [ ] 关键提及不漏检。
- [ ] 负面内容能在小时级被发现。
- [ ] 日报可直接指导当日互动动作。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/64-social-media-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/64-social-media-monitor.md)

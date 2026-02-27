# 阅读清单整理助手

> 随手保存链接，周五自动收到分主题的“周末阅读清单”。

## 这个案例能帮你做什么

- 把碎片链接自动归档，避免“稍后阅读”越积越多。
- 每篇自动提取标题和简要内容，周末可快速筛选值不值得读。
- 每周清空活跃清单并归档，长期积累更可管理。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Web Fetch` | 抓取 URL 标题与正文开头 | OpenClaw Built-in |
| 外部（需安装） | `Memory Management` | 存储分类与归档 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram/Signal 通道 | 接收“save this/read later”与周报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的阅读清单助手。
我发你 3 个链接后，请为每个链接输出：
1) 标题
2) 2 句摘要
3) 分类（Tech/Business/Health/Culture/Fun/Other）
本轮只做预览，不归档。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my reading list curator.

When I send you a URL with "save this" or "read later":
1. Fetch the article title and first paragraph
2. Categorize it (Tech, Business, Health, Culture, Fun, Other)
3. Save to memory/reading-list.md with date and category

Every Friday at 3 PM, send me my Weekly Reading List:

📚 Weekend Reading | [Date Range]

🤖 Tech (3 articles)
• [Title] — [2-sentence summary]
  [URL]

💼 Business (2 articles)
• [Title] — [2-sentence summary]
  [URL]

⭐ Editor's Pick: [The one article I'd recommend most]

After sending, archive the list to memory/reading-archive/YYYY-WXX.md
and clear the active reading list.
```

### 调度配置

- 实时：接收 `save this` / `read later` 后立即入清单
- 周报：每周五 `3 PM`

## 成功标准

- [ ] 不再出现大量遗忘链接。
- [ ] 每周至少完成 3-5 篇实际阅读。
- [ ] 归档记录可长期追踪兴趣变化。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/61-reading-list-curator.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/61-reading-list-curator.md)

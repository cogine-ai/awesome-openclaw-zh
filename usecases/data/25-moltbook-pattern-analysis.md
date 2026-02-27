# Moltbook 模式分析

> 每周分析 Moltbook 内容表现，输出数据驱动的发布策略建议。

## 这个案例能帮你做什么

- 从“凭感觉发内容”转成“基于数据调策略”。
- 识别高互动内容类型与发布时间规律。
- 周环比跟踪，持续优化内容方向。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 拉取 feed/API 数据 | OpenClaw Built-in |
| 内置 | `filesystem` | 保存分析结果与报告 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“Moltbook 模式分析”的预演版：
1. 抓取 top 100 帖子数据。
2. 按内容类型分类。
3. 计算互动率并输出前3类。
4. 给出本周内容策略建议。
```

## 稳定自动版（可长期运行）

### 1) 数据抓取示例

```javascript
const posts = await fetch('https://www.moltbook.com/api/v1/feed');
// Analyze: upvotes, comments, content type
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Moltbook Pattern Analysis”。

每周执行：
1. 获取按 upvotes 排序的 top 100 帖子。
2. 按内容类型分类。
3. 计算互动率。
4. 识别本周趋势主题。
5. 输出周环比变化。

报告必须包含：
- Top content categories
- Best posting times
- Engagement trends
- Recommended strategy
```

## 成功标准

- [ ] Weekly reports generated
- [ ] Strategy recommendations actionable
- [ ] Engagement improvement tracked

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/25-moltbook-pattern-analysis.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/25-moltbook-pattern-analysis.md)

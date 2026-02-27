# Token 使用优化器

> 统计心跳任务 token 消耗，用差分检查替代盲目轮询，降低 API 成本。

## 这个案例能帮你做什么

- 量化每类检查任务的 token 使用量与命中率。
- 当命中率过低时自动降频，优先保留高价值检查。
- 周报化展示节省效果，避免“省了多少不清楚”。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 记录 token 日志 | OpenClaw Built-in |
| 内置 | `system` | 计算命中率与成本变化 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```javascript
const tokenLog = {
  timestamp: Date.now(),
  tokensUsed: response.usage.total_tokens,
  endpoint: 'email_check'
};
```

先按检查类型打点一轮，确认日志结构可用。

## 稳定自动版（可长期运行）

### 1) 心跳内置优化流程（原文）

```text
Every heartbeat:
1. Log tokens used per check type
2. Calculate hit rate (actionable/total)
3. If hit rate <5%: reduce check frequency
4. Implement differential checking
5. Weekly report: savings achieved
```

### 2) 优化策略（原文）

- State-based vs polling
- Check rotation (high/medium/low freq)
- Adaptive intervals

## 成功标准

- [ ] token 消耗下降 60% 以上。
- [ ] 响应能力不明显下降。
- [ ] 每周有可核对的节省报告。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/27-token-usage-optimizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/27-token-usage-optimizer.md)

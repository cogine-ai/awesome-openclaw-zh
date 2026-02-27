# 客户信号扫描器

> 持续扫描 Telegram/Discord 对话，提取可行动的客户反馈信号。

## 这个案例能帮你做什么

- 把分散在多个社群里的反馈统一收集。
- 自动归类为功能诉求/缺陷/好评，方便产品团队处理。
- 按互动强度排序，优先处理高价值信号。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `telegram` | 监控 Telegram 频道消息 | OpenClaw Built-in |
| 内置 | `discord` | 监控 Discord 频道消息 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“客户信号扫描器”的预演版：
1. 扫描指定频道过去24小时消息。
2. 提取包含关键词的反馈。
3. 归类为 feature request / bug / praise。
4. 输出 top 10 信号（附上下文）。
```

## 稳定自动版（可长期运行）

### 1) 关键词配置

```javascript
const keywords = [
  "feature request", "would be nice", "missing",
  "bug", "broken", "not working"
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Customer Signal Scanner”。

每小时执行：
1. 扫描配置频道关键词。
2. 提取消息及上下文。
3. 分类：feature request / bug / praise。
4. 按回复和反应数评分。
5. 每日输出 top 10 信号报告。

Privacy:
- Only public channels
- Anonymize usernames
- Aggregate by topic
```

## 成功标准

- [ ] 100% channel coverage
- [ ] Signals categorized accurately
- [ ] Report delivered daily

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/23-customer-signal-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/23-customer-signal-scanner.md)

# Pump.fun 扫描器

> 每15分钟扫描新币，按市值和成交量筛选并带风险提示告警。

## 这个案例能帮你做什么

- 更早发现新发代币，缩短“发现到评估”的时间。
- 通过基础过滤条件减少明显噪音项目。
- 每条告警附带风险提醒，避免盲目操作。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 抓取 pump.fun 列表页 | OpenClaw Built-in |
| 内置 | `telegram` | 推送扫描告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“Pump.fun 扫描器”的预演版：
1. 抓取当前新币列表。
2. 过滤上线1小时内项目。
3. 按市值和成交量排序。
4. 输出3条候选并附风险提醒。
```

## 稳定自动版（可长期运行）

### 1) 扫描逻辑

```javascript
async function scanNewTokens() {
  const page = await web_fetch('https://pump.fun');
  // Extract new listings
  // Filter by age < 1 hour
  // Sort by volume
}
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Pump.fun Scanner”。

每 15 分钟执行：
1. 抓取新上市代币。
2. 过滤上线 <1 小时项目。
3. 检查市值与交易量。
4. 若 MC < $100K 且 volume > $10K，触发提醒。
5. 告警附 token address 和链接。

Risk warning:
- Most new tokens are scams
- Do your own research
- Never invest more than you can lose
```

## 成功标准

- [ ] Detection within 15 min of launch
- [ ] False positive rate <50%
- [ ] All alerts include risk warning

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/24-pump-fun-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/24-pump-fun-scanner.md)

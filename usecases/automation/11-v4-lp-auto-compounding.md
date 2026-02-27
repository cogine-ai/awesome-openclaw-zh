# V4 LP 自动复利

> 自动监控 Uniswap V4 头寸，在“手续费收益明显高于 gas 成本”时自动复利。

## 这个案例能帮你做什么

- 让 LP 头寸在夜间也能自动判断是否值得复利，不用盯盘。
- 用“收益 vs gas”阈值控制执行时机，减少低效交易。
- 失败连续出现时自动告警，避免问题长时间未发现。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`web3`](https://clawhub.ai/skills/claw-fi) | 链上交互与数据读取 | ClawHub |
| 外部 | [`uniswap`](https://clawhub.ai/skills/execute-swap) | V4 头寸管理与执行 | ClawHub |
| 内置 | `telegram` | 推送复利结果与异常通知 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做“判断建议”，不发交易：

```text
你是我的 OpenClaw 助手。
请帮我做“V4 LP 自动复利”的预演版：
1. 每 15 分钟读取已追踪头寸的 pending fees。
2. 估算当前复利交易 gas 成本。
3. 按“fees 是否超过阈值 * gas”输出是否建议复利。
4. 本轮不要发送交易，只输出判断结果、理由和下一次检查时间。
```

## 稳定自动版（可长期运行）

### 1) 头寸配置

```javascript
const positions = [
  {
    pool: "0x...", // V4 pool address
    tokenId: 123,
    minCompoundThreshold: "50", // USD value
    gasBuffer: 1.2
  }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“V4 LP 自动复利”。
请使用 Skills：web3、uniswap、telegram。

每 15 分钟执行：
1. 查询追踪头寸的 pending fees。
2. 计算当前复利交易的 gas 成本。
3. 当 fees > threshold * gas 时执行复利。
4. 记录交易哈希与 gas 使用量。
5. 如果复利连续失败 3 次，立即告警。

安全规则：
- Max gas price: 50 gwei
- Only compound during low volatility
- Emergency pause if TVL drops >20%
```

## 成功标准

- [ ] Position efficiency >95%
- [ ] Gas costs <10% of compounded fees
- [ ] Zero missed compound opportunities

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/11-v4-lp-auto-compounding.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/11-v4-lp-auto-compounding.md)

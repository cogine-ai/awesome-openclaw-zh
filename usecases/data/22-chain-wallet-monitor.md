# 链上钱包监控器

> 定时巡检重点地址，发现大额转账与合约交互时立即提醒。

## 这个案例能帮你做什么

- 7x24 监控关键钱包，不错过夜间大额异动。
- 按阈值筛选告警，减少无效噪音。
- 自动记录链上动作，便于复盘。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`web3`](https://clawhub.ai/skills/claw-fi) | 查询链上交易与交互 | ClawHub |
| 内置 | `telegram` | 推送实时告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“链上钱包监控器”的预演版：
1. 监控1个测试钱包10分钟。
2. 检查新交易与合约交互。
3. 按阈值判断是否触发告警。
4. 输出一份简版监控日志。
```

## 稳定自动版（可长期运行）

### 1) 钱包配置

```javascript
const wallets = [
  { address: "0x...", label: "Whale A", threshold: 1000 }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Chain Wallet Monitor”。

每 10 分钟执行：
1. 查询监控钱包新交易。
2. 检测超过阈值的转账。
3. 识别新的合约交互。
4. 标记治理投票行为。
5. 发现大额动作立即告警。

Thresholds:
- Whale wallets: 1000 ETH
- Portfolio: 10% of holdings
- Known entities: any movement
```

## 成功标准

- [ ] Detection within 10 minutes
- [ ] False positive rate <5%
- [ ] All movements logged

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/22-chain-wallet-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/22-chain-wallet-monitor.md)

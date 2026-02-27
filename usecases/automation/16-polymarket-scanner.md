# Polymarket 扫描器

> 夜间每 15 分钟巡检预测市场，跟踪价格异动与持仓盈亏。

## 这个案例能帮你做什么

- 在你休息时持续跟踪关键市场，不错过夜间变化。
- 自动识别大幅波动并及时预警。
- 早上直接看到隔夜 P&L、机会点和建议动作。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `polymarket` | 读取市场价格与仓位数据 | OpenClaw Built-in |
| 内置 | `telegram` | 推送异动告警与晨报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先跑一次“只观测不操作”：

```text
你是我的 OpenClaw 助手。
请帮我做“Polymarket 扫描器”的预演版：
1. 读取已追踪市场当前价格。
2. 计算当前持仓 P&L。
3. 标记价格变化超过 10% 的市场。
4. 输出一份简版晨报（价格变化、P&L、建议动作）。
```

## 稳定自动版（可长期运行）

### 1) 市场追踪配置

```javascript
const markets = [
  { id: "0x...", alertThreshold: 0.1 }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Polymarket Scanner”。
请使用内置 Skills：polymarket、telegram。

每 15 分钟执行：
1. 获取追踪市场最新价格。
2. 计算当前持仓 P&L。
3. 识别显著波动（>10%）。
4. 清理 dust positions。
5. 记录巡检数据。

晨报内容：
- Overnight price changes
- Current P&L
- Recommended actions
- New opportunities
```

## 成功标准

- [ ] 100% position coverage
- [ ] Alerts within 15 min of events
- [ ] Accurate P&L calculations

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/16-polymarket-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/16-polymarket-scanner.md)

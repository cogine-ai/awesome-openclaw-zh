# Polymarket 自动驾驶（模拟盘）

> 自动监控预测市场并执行纸面交易（paper trading），每天输出策略表现与复盘摘要。

## 这个案例能帮你做什么

- 把“盯盘 + 手工记录 + 复盘”变成自动化闭环。
- 同时跑 TAIL / BONDING / SPREAD 三类策略，比较真实效果。
- 在不使用真实资金前提下，先验证策略再决定是否迭代。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_search` 或 `web_fetch` | 抓取 Polymarket 市场数据 | OpenClaw Built-in |
| 外部（需安装） | `postgres`（或 SQLite） | 交易日志、仓位与 P&L 存储 | PostgreSQL / SQLite |
| 内置 | Discord 通道 | 每日推送交易摘要 | OpenClaw Built-in |
| 内置 | `cron` | 每 15 分钟轮询策略 | OpenClaw Built-in |
| 内置 | 子代理并发能力 | 高成交时并行分析多个市场 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 Polymarket 模拟交易助手。
请基于当前市场数据做一次“仅分析不下单”的策略演练：
1. 用 TAIL / BONDING / SPREAD 各给出 1 个候选机会。
2. 输出入场逻辑、风险点、预期收益区间。
3. 不执行真实交易，只记录为 paper trade 建议。
```

## 稳定自动版（可长期运行）

### 1) 初始化数据库

```sql
CREATE TABLE paper_trades (
  id SERIAL PRIMARY KEY,
  market_id TEXT,
  market_name TEXT,
  strategy TEXT,
  direction TEXT,
  entry_price DECIMAL,
  exit_price DECIMAL,
  quantity DECIMAL,
  pnl DECIMAL,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE portfolio (
  id SERIAL PRIMARY KEY,
  total_value DECIMAL,
  cash DECIMAL,
  positions JSONB,
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### 2) Discord 频道

- 建议创建独立频道：`#polymarket-autopilot`
- 只发模拟盘结果，便于和真实交易日志隔离。

### 3) OpenClaw 执行提示词（自动版）

```text
You are a Polymarket paper trading autopilot. Run continuously (via cron every 15 minutes):

1. Fetch current market data from Polymarket API
2. Analyze opportunities using these strategies:
   - TAIL: Follow strong trends (>60% probability + volume spike)
   - BONDING: Contrarian plays on overreactions (sudden drops >10% on news)
   - SPREAD: Arbitrage when YES+NO > 1.05
3. Execute paper trades in the database (starting capital: $10,000)
4. Track portfolio state and update positions

Every morning at 8 AM, post a summary to Discord #polymarket-autopilot:
- Yesterday's trades (entry/exit prices, P&L)
- Current portfolio value and open positions
- Win rate and strategy performance
- Market insights and recommendations

Use sub-agents to analyze multiple markets in parallel during high-volume periods.

Never use real money. This is paper trading only.
```

## 成功标准

- [ ] 每 15 分钟可稳定执行一次市场扫描。
- [ ] 每天 8:00 有完整日报（交易、仓位、胜率、策略表现）。
- [ ] 始终保持 paper trading，不触发真实资金操作。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/polymarket-autopilot.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/polymarket-autopilot.md)

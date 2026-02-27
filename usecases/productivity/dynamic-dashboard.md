# 动态仪表板（子代理并行）

> 每 15 分钟并行抓取多源数据并汇总成一条动态看板。

## 这个案例能帮你做什么

- 把 GitHub、社媒、市场、系统状态放进同一视图。
- 用子代理并发抓取，降低串行轮询延迟。
- 告警条件内置，指标异常可即时提醒。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | 子代理并发能力 | 并行采集各数据源 | OpenClaw Built-in |
| 外部（按需） | `github` (gh CLI) | GitHub 指标 | GitHub CLI |
| 外部（按需） | `bird` | X/Twitter 数据 | ClawHub / 社媒集成 |
| 内置 | `web_search` / `web_fetch` | 外部 API 数据抓取 | OpenClaw Built-in |
| 外部（需安装） | `postgres` | 历史指标存储 | PostgreSQL |
| 内置 | Discord/Canvas | 看板分发与展示 | OpenClaw Built-in |
| 内置 | `cron` | 周期调度 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的看板助手。
请并行抓取 4 类指标（GitHub、社媒、市场、系统），
输出一版 Dashboard 文本预览，并标记 1 个可配置告警条件。
本轮不入库、不定时。
```

## 稳定自动版（可长期运行）

### 1) 指标库

```sql
CREATE TABLE metrics (
  id SERIAL PRIMARY KEY,
  source TEXT,
  metric_name TEXT,
  metric_value NUMERIC,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE alerts (
  id SERIAL PRIMARY KEY,
  source TEXT,
  condition TEXT,
  threshold NUMERIC,
  last_triggered TIMESTAMPTZ
);
```

### 2) OpenClaw 执行提示词（源案例）

```text
You are my dynamic dashboard manager. Every 15 minutes, run a cron job to:

1. Spawn sub-agents in parallel to fetch data from:
   - GitHub: stars, forks, open issues, commits (past 24h)
   - Twitter: mentions of "@username", sentiment analysis
   - Polymarket: volume for tracked markets
   - System: CPU, memory, disk usage via shell commands

2. Each sub-agent writes results to the metrics database.
3. Aggregate and format dashboard.
4. Post to Discord #dashboard.
5. Check alert conditions.
```

## 成功标准

- [ ] 15 分钟节奏稳定刷新。
- [ ] 各数据源并行抓取有效，延迟可控。
- [ ] 告警命中时能立即通知。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/dynamic-dashboard.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/dynamic-dashboard.md)

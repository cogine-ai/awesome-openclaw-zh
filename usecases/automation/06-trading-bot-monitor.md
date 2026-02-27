# 交易机器人监控器

> 自动发现机器人异常，重启并修复数据，早上直接看健康报告。

## 这个案例能帮你做什么

- 持续监控交易机器人进程、数据文件和健康接口，减少夜间“挂了没人看见”。
- 机器人异常时自动执行恢复动作，降低停机时间和漏单风险。
- 每天固定产出晨报，快速看到 uptime、P&L 和夜间处理记录。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `process` | 检查机器人进程状态 | OpenClaw Built-in |
| 内置 | `docker` | 查看日志与重启容器 | OpenClaw Built-in |
| 内置 | `telegram` | 推送健康状态与告警 | OpenClaw Built-in |
| 内置 | `cron` | 定时执行巡检与晨报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先做“只检查不改动”的预演版：

```text
你是我的 OpenClaw 助手。
请帮我做“交易机器人监控器”的预演版：
1. 每 5 分钟检查一次所有机器人：进程是否运行、数据文件是否异常、健康接口是否可用。
2. 本轮不要执行重启和修复，只输出检查结果。
3. 对每个机器人给出：运行状态、异常项、建议动作。
4. 最后给出 08:00 晨报样例（包含 uptime、P&L、夜间事件）。
```

## 稳定自动版（可长期运行）

### 1) 配置文件：`config/bots.json`

```json
{
  "bots": [
    {
      "name": "doge-long",
      "type": "spot",
      "check_interval": 300,
      "process_name": "doge_long_bot",
      "data_file": "data/doge_trades.csv",
      "health_endpoint": "http://localhost:8080/health"
    },
    {
      "name": "btc-optimized",
      "type": "futures",
      "check_interval": 60,
      "process_name": "btc_v1_bot",
      "data_file": "data/btc_trades.csv"
    }
  ]
}
```

### 2) 监控脚本：`scripts/bot-monitor.js`

```javascript
const { exec } = require('child_process');
const fs = require('fs');

async function checkBot(bot) {
  // Check if process running
  const isRunning = await processExists(bot.process_name);

  // Check data file health
  const dataHealth = await checkDataFile(bot.data_file);

  // Check API responsiveness
  const apiHealth = await checkApi(bot.health_endpoint);

  return { isRunning, dataHealth, apiHealth };
}

async function recoverBot(bot) {
  if (!bot.isRunning) {
    await restartBot(bot);
  }
  if (bot.dataHealth.corrupted) {
    await fixCorruptedData(bot.data_file);
  }
  await logRecovery(bot);
}
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“交易机器人监控器”。
请使用内置 Skills：process、docker、telegram、cron。

每 5 分钟执行：
1. 检查配置内所有机器人是否在线。
2. 校验数据文件是否损坏。
3. 如有健康接口，检查接口响应。
4. 如果机器人下线：立刻重启。
5. 如果数据损坏：从备份恢复并按日志回放。
6. 记录所有动作到 memory/bot-operations.md。

08:00 生成晨报，包含：
- 最近 24 小时 uptime
- 每个机器人 P&L
- 所有重启/修复动作
- 当前持仓概览

立即告警条件：
- 机器人离线超过 5 分钟
- 发现数据损坏
- API key 错误
- 异常交易频率
```

### 4) 调度配置

```json
[
  {
    "schedule": "*/5 * * * *",
    "task": "bot_health_check"
  },
  {
    "schedule": "0 8 * * *",
    "task": "bot_morning_report"
  }
]
```

### 5) 恢复手册（可直接复用）

```markdown
## Recovery Playbook

### Bot Not Running
1. Check logs: `docker logs ${bot_name}`
2. If OOM error: increase memory limit
3. If API error: check credentials
4. Restart: `docker-compose restart ${bot_name}`
5. Verify: wait 30s, check process again

### Data Corruption
1. Stop bot
2. Backup corrupted file: `mv trades.csv trades.csv.bak`
3. Restore from last good backup
4. Replay trades from exchange API
5. Verify data integrity
6. Restart bot

### API Errors
1. Check rate limits
2. Rotate API keys if needed
3. Reduce polling frequency temporarily
```

### 6) 晨报模板

```markdown
🤖 Bot Health Report - {{date}}

Uptime (24h):
- doge-long: 99.8% (1 restart at 03:15)
- btc-optimized: 100%
- hummingbot-mm: 99.2% (2 restarts)

P&L:
- doge-long: +$12.40 (+2.1%)
- btc-optimized: +$45.80 (+1.8%)
- hummingbot-mm: -$3.20 (-0.4%)

Actions Taken:
- 03:15: Restarted doge-long (memory limit)
- 05:42: Fixed btc data corruption

Current Status: ✅ All bots operational
```

## 成功标准

- [ ] Bot uptime > 99.5% per week
- [ ] Recovery time < 2 minutes
- [ ] Zero missed trades due to downtime
- [ ] Data corruption detected within 1 hour

## 风险与边界

| 风险 | 缓解策略 |
|---|---|
| Cascading restarts | Exponential backoff（5min、15min、30min） |
| Data loss | Hourly backups to S3 |
| API bans | Rate limit tracking per exchange |
| False positives | Require 2 failed checks before action |

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/06-trading-bot-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/06-trading-bot-monitor.md)

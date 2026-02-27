# API 配额监控与提醒

> 用 `check-quotas` 统一检查多家 API 配额，提前发现额度告急。

## 这个案例能帮你做什么

- 一条命令看 Anthropic / OpenRouter / Synthetic 等额度状态。
- 在高消耗任务前先做配额判断，自动切换到保底策略。
- 用 `jq` 直接做阈值判断，便于接入 cron/告警。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `check-quotas.sh` | 聚合多 provider 配额 | [openclaw-runbook 示例](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/check-quotas-README.md) |
| 外部（系统） | `bash` / `curl` / `jq` | 脚本运行与 JSON 解析 | 系统工具 |
| 外部（macOS） | `security` | 读取 Keychain（Claude Code） | macOS |

## 快速体验版（先跑一轮）

### 1) 安装脚本（原文）

```bash
cp check-quotas.sh ~/.local/bin/check-quotas
chmod +x ~/.local/bin/check-quotas
```

### 2) 配置凭证目录并设置权限（原文）

```bash
mkdir -p ~/.openclaw/credentials
chmod 700 ~/.openclaw/credentials
chmod 600 ~/.openclaw/credentials/*
```

### 3) 运行

```bash
check-quotas
check-quotas | jq .
```

## 稳定自动版（可长期运行）

### 1) 环境变量覆盖（原文）

```bash
export OPENCLAW_CREDENTIALS_DIR="/path/to/your/credentials"
export CLAUDE_KEYCHAIN_ITEM="Your-Keychain-Item"
```

### 2) 常用判断语句（原文）

```bash
check-quotas | jq '.openrouter | (.usage / .limit) > 0.9'
check-quotas | jq -r '.synthetic.credits_remaining'
```

### 3) 高消耗任务前的守门逻辑（原文）

```bash
QUOTAS=$(check-quotas)
OPENROUTER_USAGE=$(echo $QUOTAS | jq -r '.openrouter.usage // 0')

if [ "$OPENROUTER_USAGE" -gt 90 ]; then
    echo "OpenRouter quota high, using fallback"
fi
```

## 成功标准

- [ ] 每天都能自动获取配额快照。
- [ ] 超过阈值时能触发降级策略。
- [ ] 无“任务中途才发现额度耗尽”的中断。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/check-quotas-README.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/check-quotas-README.md)

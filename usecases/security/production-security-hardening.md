# 生产级安全加固包

> 用最小权限、成本保护与备份机制，把 OpenClaw 运行环境收敛到可控状态。

## 这个案例能帮你做什么

- 降低 API Key 泄露、误用高价模型、网关暴露、设备残留配对等高频风险。
- 提供“先备份、再改造、边改边验”的安全加固路径。
- 形成应急处置动作：密钥泄露、异常账单、紧急停机。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | OpenClaw 配置与设备管理命令 | 执行网关/设备/通道安全控制 | OpenClaw CLI |
| 外部（系统） | `bash` / `git` / `chmod` / `tar` | 秘钥排查、权限收敛、备份恢复 | 系统工具 |

## 快速体验版（先跑一轮）

### 1) 先备份（原文）

```bash
tar -czf ~/openclaw-backup-$(date +%Y%m%d).tar.gz ~/.openclaw/
```

### 2) 先做三项高价值检查

```bash
# 查历史是否泄露 key
git log --all -p | grep -i "sk-ant-\|sk-\|api_key"

# 检查网关监听
netstat -an | grep 18789 | grep LISTEN

# 查看已配对设备
openclaw devices list
```

## 稳定自动版（可长期运行）

### 1) API Key 与配置隔离（原文）

```json
{
  "env": {
    "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
    "OPENAI_API_KEY": "${OPENAI_API_KEY}",
    "BRAVE_API_KEY": "${BRAVE_API_KEY}",
    "GATEWAY_TOKEN": "${GATEWAY_TOKEN}"
  }
}
```

### 2) 默认工具策略（原文）

```json
{
  "agents": {
    "defaults": {
      "tools": {
        "allow": ["read", "write", "edit", "web_search", "web_fetch", "memory_search", "memory_get"],
        "deny": ["exec", "process", "cron", "gateway", "nodes"]
      }
    }
  }
}
```

### 3) 成本保护（原文核心）

- 在 provider 控制台设置硬上限与告警（50%、80%）。
- 监控/cron/public agent 不使用高价模型（如 Opus）。
- 仅把 Opus 给明确需要高质量推理的人工触发任务。

### 4) 网关与权限（原文）

```json
{
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "auth": { "mode": "token", "token": "${GATEWAY_TOKEN}" }
  },
  "logging": {
    "redactSensitive": "tools"
  }
}
```

```bash
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 700 ~/.openclaw/credentials
```

### 5) 设备配对卫生（原文）

```bash
openclaw devices list
openclaw devices remove <device-id>
openclaw devices clear --yes
openclaw devices clear --yes --pending
```

### 6) 备份与应急（原文）

```bash
# 停机开关
openclaw gateway stop

# 关闭高风险通道
openclaw config set channels.telegram.enabled false
openclaw config set channels.discord.enabled false
```

## 成功标准

- [ ] API Key 不硬编码，历史泄露可追溯并已轮换。
- [ ] 默认策略阻断危险工具，按 agent 最小授权。
- [ ] 网关仅本地监听，设备配对定期清理。
- [ ] 备份与应急动作可在演练中跑通。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/security-hardening.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/security-hardening.md)

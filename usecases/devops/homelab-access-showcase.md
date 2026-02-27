# 家庭实验室远程安全访问

> 用 Telegram + Tailscale + SSH 远程管理 homelab，危险操作必须二次确认。

## 这个案例能帮你做什么

- 不开公网端口也能远程看状态、重启服务、做基础排障。
- 把命令分级（允许 / 需确认 / 禁止），降低误操作风险。
- 在一个聊天入口管理多台设备，适合家庭实验室日常运维。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `message` | 接收和回复 Telegram 指令 | OpenClaw Built-in |
| 内置 | `exec` | 执行 SSH 指令 | OpenClaw Built-in |
| 外部（需安装） | Tailscale（或 WireGuard / ZeroTier） | 私网连通与加密传输 | 官方安装包 |
| 外部（需准备） | Telegram Bot | 指令入口与通知 | @BotFather |

## 快速体验版（先感受效果）

先只开放只读状态命令：

```text
你是我的 homelab 访问助手。
只允许执行以下状态命令：uptime、df -h、free -m、systemctl status。
收到高风险命令时直接拒绝，并提示“需要人工 SSH 处理”。
```

## 稳定自动版（可长期运行）

### 1) Tailscale 与 SSH 准备

```bash
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up
tailscale ip -4
ssh homelab-router uptime
```

`~/.ssh/config` 示例：

```text
Host homelab-router
    HostName [TAILSCALE_IP]
    User [USERNAME]
    IdentityFile ~/.ssh/homelab_key
    StrictHostKeyChecking accept-new
```

### 2) Telegram 机器人凭据

写入 `~/.openclaw/credentials/`：

```text
TELEGRAM_BOT_TOKEN=[YOUR_BOT_TOKEN]
TELEGRAM_CHAT_ID=[YOUR_CHAT_ID]
```

### 3) Agent 安全策略

```yaml
agents:
  homelab:
    model: anthropic/claude-sonnet-4-5
    tools:
      - message
      - exec
    system: |
      You are a homelab access controller. Handle SSH commands from Telegram.

      VALIDATION RULES:
      1. Verify sender is authorized ([YOUR_TELEGRAM_USERNAME])
      2. Parse command from message
      3. Check command against allowlist

      ALLOWLIST (no confirmation):
      - Status: uptime, df -h, free -m, systemctl status [service]
      - Network: ping, curl -I, ip addr
      - Info: ls, cat (read-only files)

      REQUIRES CONFIRMATION (ask "Execute? Reply YES"):
      - Service restart: systemctl restart
      - Package install: apt install, pip install
      - File changes: sed, echo >, editing configs
      - Reboot: reboot, shutdown

      FORBIDDEN (always reject):
      - rm -rf, dd, disk wiping
      - Password changes, user management
      - Firewall changes without explicit context

      EXECUTION:
      - SSH via Tailscale: ssh [host] [command]
      - Timeout: 30 seconds
      - Return output to Telegram
```

### 4) 测试命令

```text
/homelab status router
```

## 成功标准

- [ ] 只读命令可立即返回结果。
- [ ] 高风险命令会触发 `YES` 二次确认。
- [ ] 禁止命令始终被拒绝，不会落地执行。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/homelab-access.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/homelab-access.md)

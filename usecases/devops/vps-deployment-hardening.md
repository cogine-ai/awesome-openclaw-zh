# VPS 部署与加固流程

> 按“先打通 Tailscale，再封公网 SSH”的顺序部署 OpenClaw，避免把自己锁在门外。

## 这个案例能帮你做什么

- 在 VPS 上快速完成 OpenClaw 基线部署并做首轮安全加固。
- 降低公网暴露面，把 SSH 通道收敛到 Tailscale 私网。
- 建立“改配置前后可对比、可回滚”的运维习惯。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw doctor` | 配置体检与常见问题修复 | OpenClaw CLI |
| 内置 | `openclaw security audit` | 深度安全扫描 | OpenClaw CLI |
| 外部（需安装） | Tailscale | 私网 SSH 通道 | [Tailscale](https://tailscale.com/) |
| 外部（推荐） | `git` | 跟踪配置并可回滚 | Git |

## 快速体验版（先感受效果）

先完成最关键的安全顺序验证：

```bash
ssh user@your-vps-ip
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh=true
tailscale ip -4
ssh user@100.64.1.2
```

确认上面最后一条成功后，再去防火墙封公网 `22`。

## 稳定自动版（可长期运行）

### 1) OpenClaw 首次体检

```bash
openclaw doctor --fix
openclaw security audit --deep
```

### 2) 权限与监听面收敛

```bash
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 700 ~/.openclaw/credentials

netstat -an | grep 18789 | grep LISTEN
```

目标是 `127.0.0.1:18789`，而不是 `0.0.0.0:18789`。

`openclaw.json` 示例：

```json
"gateway": {
  "bind": "loopback"
}
```

```bash
openclaw gateway restart
```

### 3) 最小权限工具策略（示例）

```json
"tools": {
  "profile": "minimal",
  "deny": ["exec"],
  "allow": ["web_search", "web_fetch", "read"]
}
```

### 4) 配置 Git 化（可回滚）

```bash
cd ~/.openclaw && git init
printf 'agents/*/sessions/\nagents/*/agent/*.jsonl\n*.log\n' > .gitignore
git add .gitignore openclaw.json
git commit -m "config: baseline"
```

## 成功标准

- [ ] 公网 SSH 已关闭，Tailscale SSH 可稳定连接。
- [ ] `openclaw security audit --deep` 无 critical 问题。
- [ ] 关键配置有 git 提交记录，故障时可快速回滚。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/vps-setup.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/vps-setup.md)

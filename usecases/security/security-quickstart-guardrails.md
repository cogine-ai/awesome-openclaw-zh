# 安全快速启动模板

> 用 4 组可复制提示词，快速完成审计、加固、成本保护与备份。

## 这个案例能帮你做什么

- 新部署时先有一套可执行的安全起步流程。
- 先查问题再改配置，减少“改完不可用”的概率。
- 把安全、成本与备份统一纳入同一套上手动作。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | OpenClaw 配置读写能力 | 审计与更新 `openclaw.json` | OpenClaw Built-in |
| 外部（系统） | `tar` / `cron` | 备份与定时执行 | 系统工具 |

## 快速体验版（先跑一轮）

先备份（原文）：

```bash
tar -czf ~/openclaw-backup-$(date +%Y%m%d).tar.gz ~/.openclaw/
```

## 稳定自动版（可长期运行）

### Prompt 1：安全审计（原文）

```text
Check my OpenClaw deployment at ~/.openclaw/ for security issues:

1. In openclaw.json, check:
   - Are API keys hardcoded or using env vars (${VAR})?
   - Which tools are allowed? List dangerous ones (exec, cron, gateway)
   - Is logging.redactSensitive enabled?
   - Is gateway.bind set to loopback?

2. Check file permissions on ~/.openclaw/ and openclaw.json

Report as:
- CRITICAL: Fix immediately
- HIGH: Fix today
- MEDIUM: Fix this week
```

### Prompt 2：基础加固（原文）

- 使用 `${VAR}` 管理密钥
- 默认禁止 `exec`/`cron`/`gateway`/`nodes`
- 开启 `logging.redactSensitive`
- 网关 `bind: loopback` + token 认证

### Prompt 3：成本保护（原文）

- 配置模型成本字段
- 按 agent 分配模型层级
- 禁止 cron/public agent 默认走高价模型

### Prompt 4：备份自动化（原文）

```text
Create a backup script at ~/.openclaw/scripts/backup.sh:

Requirements:
1. Backup location: ~/backups/openclaw/YYYY-MM-DD/
2. Include:
   - openclaw.json
   - workspace/*.md (AGENTS.md, SOUL.md, etc)
   - memory/*.md (last 30 days)
3. Encrypt with gpg
4. Make executable
5. Set up cron for daily 2 AM runs

Provide the complete script and cron line.
```

## 成功标准

- [ ] 四组提示词都能执行并产出结果。
- [ ] 安全基线（密钥、网关、工具权限、日志脱敏）已落地。
- [ ] 备份任务能定时运行并可恢复。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/security-quickstart.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/security-quickstart.md)

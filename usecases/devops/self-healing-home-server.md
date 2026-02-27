# 自愈家庭服务器

> 让 OpenClaw 在家庭服务器上持续巡检、自动修复，并按节奏输出系统简报。

## 这个案例能帮你做什么

- 自动做健康检查、日志巡检、邮件分流，减少手动值守。
- 常见故障可自动执行修复动作（如服务重启、资源调整）。
- 用固定 cron 节奏沉淀“巡检 → 修复 → 汇总”的闭环。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `ssh` | 连接家庭网络机器执行运维动作 | OpenClaw Built-in |
| 外部（需安装） | `kubectl` | K3s/Kubernetes 集群管理 | Kubernetes CLI |
| 外部（需安装） | `terraform`、`ansible` | IaC 变更与配置管理 | 官方 CLI |
| 外部（需安装） | `1password` CLI | 密钥读取（建议只读） | 1Password |
| 外部（需安装） | `gog` | 邮件接入与分拣 | gog CLI |

## 快速体验版（先感受效果）

先做“只检测不修复”的安全预演：

```text
你是我的基础设施助手。
每小时检查一次：磁盘、内存、关键服务状态。
只输出异常清单和建议操作，不自动执行变更。
每天 8:00 输出一条晨间健康简报。
```

## 稳定自动版（可长期运行）

### 1) Agent 基础约束（示例）

```text
## Infrastructure Agent

You are Reef, an infrastructure management agent.

Access:
- SSH to all machines on the home network (192.168.1.0/24)
- kubectl for the K3s cluster
- 1Password vault (read-only for credentials, dedicated AI vault)
- Gmail via gog CLI
- Calendar (yours + partner's)
- Obsidian vault at ~/Documents/Obsidian/

Rules:
- NEVER hardcode secrets — always use 1Password CLI or environment variables
- NEVER push directly to main — always create a PR
- Run `openclaw doctor` as part of self-health checks
- Log all infrastructure changes to ~/logs/infra-changes.md
```

### 2) Cron 节奏（源案例核心）

```text
Every 15 minutes:
- Check kanban board for in-progress tasks → continue work

Every hour:
- Monitor health checks (Gatus, ArgoCD, service endpoints)
- Triage Gmail (label actionable items, archive noise)
- Check for unanswered alerts or notifications

Every 6 hours:
- Knowledge base data entry (process new Obsidian notes)
- Self health check (openclaw doctor, disk usage, memory, logs)

Every 12 hours:
- Code quality and documentation audit
- Log analysis via Loki/monitoring stack

Daily:
- 4:00 AM: Nightly brainstorm
- 8:00 AM: Morning briefing
- 1:00 AM: Velocity assessment

Weekly:
- Knowledge base QA review
- Infrastructure security audit
```

### 3) 安全底线（必做）

- 所有仓库加 secret scanning（如 TruffleHog）预提交拦截。
- 只读优先，主分支强制 PR，禁止代理直推 main。
- 高风险网络/权限变更必须人工审批。

## 成功标准

- [ ] 巡检节奏稳定运行，异常可在当天被发现。
- [ ] 常见故障可自动修复，失败时有明确告警。
- [ ] 密钥不硬编码，配置变更可追踪可回滚。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/self-healing-home-server.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/self-healing-home-server.md)

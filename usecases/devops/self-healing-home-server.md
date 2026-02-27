# 自愈家庭服务器

> 运行一个始终在线的基础设施智能体，具有 SSH 访问权限、自动化 cron 作业，以及跨家庭网络的自愈能力。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/self-healing-home-server.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/self-healing-home-server.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- Home lab operators and self-hosters face a constant maintenance burden:
- Health checks, log monitoring, and alerting require manual setup and attention
- When something breaks, you have to SSH in, diagnose, and fix — often from your phone
- Infrastructure-as-code (Terraform, Ansible, Kubernetes manifests) needs regular updates

### 核心动作（来源提炼）
- **Automated health monitoring**: Cron-based checks on services, deployments, and system resources
- **Self-healing**: Detects issues via health checks and applies fixes autonomously (restart pods, scale resources, fix configs)
- **Infrastructure management**: Writes and applies Terraform, Ansible, and Kubernetes manifests
- **Morning briefings**: Daily summary of system health, calendar, weather, and task board status
- **Email triage**: Scans inbox, labels actionable items, archives noise
- **Knowledge extraction**: Processes notes and conversation exports into a structured, searchable knowledge base

### 技能/工具/渠道（来源提炼）
- `ssh` access to home network machines
- `kubectl` for Kubernetes cluster management
- `terraform` and `ansible` for infrastructure-as-code
- `1password` CLI for secrets management
- `gog` CLI for email access
- Calendar API access
- Obsidian vault or notes directory (for knowledge base)
- `openclaw doctor` for self-diagnostics

### 风险与边界（来源提炼）
- This is non-negotiable. Before giving your agent SSH access:
- Pre-push hooks:
- Install TruffleHog or similar secret scanner on ALL repositories
- Block any commit containing hardcoded API keys, tokens, or passwords

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「自愈家庭服务器」。

目标（来自来源案例）：运行一个始终在线的基础设施智能体，具有 SSH 访问权限、自动化 cron 作业，以及跨家庭网络的自愈能力。
来源关键动作：**Automated health monitoring**: Cron-based checks on services, deployments, and system resources；**Self-healing**: Detects issues via health checks and applies fixes autonomously (restart pods, scale resources, fix configs)；**Infrastructure management**: Writes and applies Terraform, Ansible, and Kubernetes manifests
优先工具/渠道：ssh、kubectl、terraform、ansible、1password、gog、n8n、GitHub
来源节奏信息：4:00；8:00；1:00；Every 15 minutes；Every 6 hours

请按下面流程输出并执行：
1. 先给出“最小可运行版本（MVP）”执行计划（3-5条）
2. 立刻产出第一版结果（不要只讲思路）
3. 缺失的信息统一放到“待我补充信息”里，不要中断整体流程
4. 若涉及高风险操作（删除、外发、改密、生产写操作），先暂停并请求确认

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 待我补充信息
## 风险与边界
```

## 可选补充信息（提高效果）

- 你的常用渠道：[Telegram/飞书/微信/邮箱]
- 你的时区与执行时间：[例如 UTC+8，每天 09:00]
- 你最在意的结果指标：[例如 节省时间、回复率、发布频次]

## 效果检查（非技术版）

- 优先检查：是否比手工更快、是否稳定、是否可持续复用。

## 参考来源

- [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- [usecases/self-healing-home-server.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/self-healing-home-server.md)

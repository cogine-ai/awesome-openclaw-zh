# SSH 密钥扫描器

> 查找暴露的 SSH 密钥

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/09-ssh-key-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/09-ssh-key-scanner.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- **Why it matters**: SSH keys are often copied to wrong locations, committed to git, or left with insecure permissions. Automated scanning catches these before attackers do.
- **Real-world example**: Agent scans ~/.ssh, ~/Downloads, project directories, finds 3 keys with 644 permissions and 1 AWS key in plain text, generates security report with remediation steps.

### 核心动作（来源提炼）
- # SSH Key Scanner
- ## Introduction
- **Why it matters**: SSH keys are often copied to wrong locations, committed to git, or left with insecure permissions. Automated scanning catches these before attackers do.
- **Real-world example**: Agent scans ~/.ssh, ~/Downloads, project directories, finds 3 keys with 644 permissions and 1 AWS key in plain text, generates security report with remediation steps.
- ## Skills You Need
- ## How to Setup

### 技能/工具/渠道（来源提炼）
- filesystem
- git
- telegram
- config/security-scan.json
- Telegram
- cron

### 风险与边界（来源提炼）
- 🔒 SSH Key Security Scan - 2026-02-19

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「SSH 密钥扫描器」。

目标（来自来源案例）：查找暴露的 SSH 密钥
来源关键动作：# SSH Key Scanner；## Introduction；**Why it matters**: SSH keys are often copied to wrong locations, committed to git, or left with insecure permissions. Automated scanning catches these before attackers do.
优先工具/渠道：filesystem、git、telegram、config/security-scan.json、Telegram、cron
来源节奏信息：02:00

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

- [ ] 100% of SSH keys have 600 permissions
- [ ] Zero keys in git repositories
- [ ] All keys in ~/.ssh directory

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/09-ssh-key-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/09-ssh-key-scanner.md)

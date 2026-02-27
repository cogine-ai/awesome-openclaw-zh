# 链上钱包监控器

> 链上变动警报

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/22-chain-wallet-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/22-chain-wallet-monitor.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- On-chain wallet surveillance tracking unusual movements, new contract deployments, and governance proposals affecting tracked addresses.
- **Why it matters**: Blockchain events happen 24/7. Early detection of suspicious activity or opportunities requires constant monitoring.
- **Real-world example**: Agent detects 10K ETH movement from whale wallet, alerts within minutes, human evaluates trading opportunity.

### 核心动作（来源提炼）
- # Chain Wallet Monitor
- ## Introduction
- On-chain wallet surveillance tracking unusual movements, new contract deployments, and governance proposals affecting tracked addresses.
- **Why it matters**: Blockchain events happen 24/7. Early detection of suspicious activity or opportunities requires constant monitoring.
- **Real-world example**: Agent detects 10K ETH movement from whale wallet, alerts within minutes, human evaluates trading opportunity.
- ## Skills You Need

### 技能/工具/渠道（来源提炼）
- web3
- telegram
- Telegram

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「链上钱包监控器」。

目标（来自来源案例）：链上变动警报
来源关键动作：# Chain Wallet Monitor；## Introduction；On-chain wallet surveillance tracking unusual movements, new contract deployments, and governance proposals affecting tracked addresses.
优先工具/渠道：web3、telegram、Telegram
来源节奏信息：Every 10 minutes

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

- [ ] Detection within 10 minutes
- [ ] False positive rate <5%
- [ ] All movements logged

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/22-chain-wallet-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/22-chain-wallet-monitor.md)

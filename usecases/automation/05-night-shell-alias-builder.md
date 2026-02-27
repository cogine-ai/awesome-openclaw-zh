# 夜间 Shell 别名构建器

> 从使用模式创建快捷方式

## 来源与对齐

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/05-night-shell-alias-builder.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/05-night-shell-alias-builder.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- Proactive friction reduction: while the human sleeps, the agent observes repeated command patterns and creates shell aliases to speed up common operations. The human wakes up to a more efficient terminal environment.
- **Why it matters**: Small daily friction compounds. A 5-second command that runs 10x daily = 3+ hours saved per year. Agents can observe patterns humans don't notice.
- **Real-world example**: Agent notices repeated `docker-compose logs -f app | grep ERROR` and creates alias `dclerr` overnight. Human discovers it in morning and uses it 50x that week.

### 核心动作（来源提炼）
- # Night Shell Alias Builder
- ## Introduction
- Proactive friction reduction: while the human sleeps, the agent observes repeated command patterns and creates shell aliases to speed up common operations. The human wakes up to a more efficient terminal environment.
- **Why it matters**: Small daily friction compounds. A 5-second command that runs 10x daily = 3+ hours saved per year. Agents can observe patterns humans don't notice.
- **Real-world example**: Agent notices repeated `docker-compose logs -f app | grep ERROR` and creates alias `dclerr` overnight. Human discovers it in morning and uses it 50x that week.
- ## Skills You Need

### 技能/工具/渠道（来源提炼）
- dclerr
- shell
- filesystem
- git
- scripts/analyze-history.js
- gst
- cron

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「夜间 Shell 别名构建器」。

目标（来自来源案例）：从使用模式创建快捷方式
来源关键动作：# Night Shell Alias Builder；## Introduction；Proactive friction reduction: while the human sleeps, the agent observes repeated command patterns and creates shell aliases to speed up common operations. The human wakes up to a more efficient terminal environment.
优先工具/渠道：dclerr、shell、filesystem、git、scripts/analyze-history.js、gst、cron
来源节奏信息：3:00；0 3 * * *

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

- [ ] 1 new alias per week minimum
- [ ] Human uses alias within 48 hours
- [ ] Zero conflicts with existing commands

## 参考来源

- [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- [usecases/05-night-shell-alias-builder.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/05-night-shell-alias-builder.md)

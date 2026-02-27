# 每日 YouTube 摘要

> 获取你关注频道的每日新视频摘要 —— 不错过你关注创作者的任何内容。

## 来源与对齐

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/daily-youtube-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/daily-youtube-digest.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- Plus: it's fun to start the day with curated content insights instead of doom-scrolling a recommendation feed.

### 核心动作（来源提炼）
- Fetches the latest videos from a list of your favorite channels
- Summarizes or extracts key insights from each video's transcript
- Delivers a digest to you daily (or on demand)

### 技能/工具/渠道（来源提炼）
- Install the [youtube-full](https://clawhub.ai/therohitdas/youtube-full) skill.
- Just tell your OpenClaw:
- "Install the youtube-full skill and set it up for me"
- npx clawhub@latest install youtube-full
- That's it. The agent handles the rest — including account creation and API key setup. You get **100 free credits on signup**, no credit card required.
- > Note: After creating the account, the skill auto-stores the API key securely in correct locations based on the OS, so the API will work in all contexts.
- Prompt OpenClaw:
- Every morning at 8am, fetch the latest videos from these YouTube channels and give me a digest with key insights from each:

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「每日 YouTube 摘要」。

目标（来自来源案例）：获取你关注频道的每日新视频摘要 —— 不错过你关注创作者的任何内容。
来源关键动作：Fetches the latest videos from a list of your favorite channels；Summarizes or extracts key insights from each video's transcript；Delivers a digest to you daily (or on demand)
优先工具/渠道：or、channel/latest、channel/resolve、OpenClaw
来源节奏信息：源头未明确固定调度

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
- [usecases/daily-youtube-digest.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/daily-youtube-digest.md)

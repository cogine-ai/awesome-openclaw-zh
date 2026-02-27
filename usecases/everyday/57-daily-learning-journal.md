# 每日学习日志

> 每晚 5 分钟复盘学习，周报和月报自动生成。

## 这个案例能帮你做什么

- 固定提问框架，降低“想写复盘但不知道写什么”的阻力。
- 自动落盘到结构化日志，方便后续检索与长期追踪。
- 每周/每月自动汇总学习模式，帮助你看到真实进展。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Memory/Notes Skill` | 保存日志与汇总 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram 通道 | 每日提问与反馈 | OpenClaw Built-in |
| 内置 | 文件存储 | 写入日/周/月日志文件 | OpenClaw Built-in |
| 内置 | AI 分析能力 | 生成周报、月报与学习模式洞察 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的学习日志助手。
请先发我今晚的 4 个复盘问题：
1) 今天学到了什么
2) 今天遇到什么挑战
3) 今天最值得肯定的进展
4) 明天准备做什么改进
我回复后，请按固定格式生成当天日志。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Learning Journal Assistant. Your job is to help me reflect on what I learned today and track my progress over time.

DAILY PROMPT (Sent via Telegram at 8:00 PM):
1) What did you learn today?
2) What challenged you?
3) What are you proud of?
4) What will you do differently tomorrow?

When I reply:
1. Extract my answers
2. Save to `/memory/learning-journal/YYYY-MM-DD.md`
3. Reply: "✅ Journal entry saved! Great work reflecting today."
4. Track keywords (skills, topics, emotions, progress signals)

Daily file format:
# Learning Journal — [Date]
## What I Learned Today
## What Challenged Me
## What I'm Proud Of
## Tomorrow's Intention
```

### 调度配置

```json
{
  "schedule": "0 20 * * *",
  "name": "Daily Learning Journal Prompt",
  "prompt": "Send daily learning journal prompt via Telegram"
}
```

```json
{
  "schedule": "0 19 * * 0",
  "name": "Weekly Learning Summary",
  "prompt": "Generate and send weekly learning report"
}
```

```json
{
  "schedule": "0 20 28-31 * *",
  "name": "Monthly Learning Reflection",
  "prompt": "If last day of month, generate monthly learning summary"
}
```

### 建议目录结构

```text
/memory/learning-journal/
  /daily/
  /weekly/
  /monthly/
```

## 成功标准

- [ ] 每周至少形成 5 条有效日志。
- [ ] 周报能提炼出明确的学习主题与模式。
- [ ] 月报能反映连续进步而非碎片记录。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/57-daily-learning-journal.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/57-daily-learning-journal.md)

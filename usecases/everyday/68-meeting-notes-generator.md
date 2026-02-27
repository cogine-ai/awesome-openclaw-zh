# 会议纪要自动生成

> 把原始笔记或转写稿自动整理成可执行纪要，并跟踪行动项截止时间。

## 这个案例能帮你做什么

- 会议后 1 分钟内得到结构化纪要，避免人工二次整理。
- 自动提取决策项、行动项、未决问题，减少遗漏。
- 根据截止日期自动提醒跟进，提高会议闭环率。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Memory Management` | 保存纪要与历史检索 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram/Signal 通道 | 投喂原始笔记与接收结果 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的会议纪要助手。
我会给你一段原始会议笔记，请按以下结构输出：
- 参会人
- 会议主题
- 3-5 句摘要
- 关键决策
- 行动项（任务/负责人/截止日期）
本轮不写入文件。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my meeting notes assistant. When I paste raw notes or a transcript:

1. Generate structured meeting minutes:
- Attendees
- Duration
- Topic
- Summary
- Key Decisions
- Action Items (Task | Owner | Deadline)
- Open Questions
- Next Meeting

2. Save to `memory/meetings/YYYY-MM-DD-[topic].md`

3. On deadline dates, remind me about pending action items.

Rules:
- Keep it concise
- Bold important decisions
- Flag action items without clear owners
- If raw notes are messy, ask clarifying questions
```

### 调度配置

- 纪要生成：按需触发（粘贴后立即处理）
- 行动项提醒：每天 `9 AM` 检查截止日期

## 成功标准

- [ ] 会议后 1 分钟内可产出纪要。
- [ ] 行动项有责任人、有截止时间。
- [ ] 后续跟进提醒稳定触发。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/68-meeting-notes-generator.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/68-meeting-notes-generator.md)

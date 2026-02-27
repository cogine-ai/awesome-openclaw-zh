# 邮件自动分拣器

> 每 2 小时自动整理未读邮件，按 Urgent / Today / Later / Junk 分桶。

## 这个案例能帮你做什么

- 把“堆满 100+ 未读”的焦虑，变成可执行优先级清单。
- 重要邮件即时告警，普通邮件按节奏处理，不再被噪音拖走。
- 每晚自动发送当日分拣摘要，便于复盘与调规则。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Email Skill` | 读取、分类、移动邮件 | [clawhub.ai/skills/agentmail-wrapper](https://clawhub.ai/skills/agentmail-wrapper) |
| 外部（需安装） | `Memory/Notes Skill` | 学习你的分拣偏好 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | AI/NLP 能力 | 理解邮件语义和紧急程度 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 发送紧急告警与日报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的邮件分拣助手。
请对我最近 20 封未读邮件做试分拣，分类为：
INBOX-Urgent / INBOX-Today / INBOX-Later / INBOX-Junk。
每封邮件给出“分类结果 + 1 行理由”，本轮不做真实移动。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Email Sorting Assistant. Your job is to organize my inbox so I only see what matters.

TASK: Scan my inbox every 2 hours and categorize all unread emails.

CATEGORY SYSTEM:
1. 📬 INBOX-Urgent — Needs action within 2 hours
2. 📥 INBOX-Today — Handle by end of day
3. 📑 INBOX-Later — Review when convenient
4. 🗑️ INBOX-Junk — Newsletters, promotions, notifications
5. ✅ INBOX-Done — Already handled (optional auto-archive)

SORTING RULES:
- URGENT: manager/CEO/key clients, "urgent/ASAP/deadline today/emergency", same-day meeting invites, bank/fraud alerts
- TODAY: this-week meeting invites, project updates needing response, submissions due within 48 hours
- LATER: industry newsletters, non-urgent updates, event invitations > 1 week
- JUNK: promotional emails, social notifications, no-reply automation, cold outreach

SMART DETECTION:
1) Sender analysis (VIP list, internal domain)
2) Content analysis (action words, deadlines, questions)
3) Thread context (direct recipient > CC)
4) Learning from history (reply/archive behavior)

For URGENT emails:
- Send immediate Telegram alert:
  "🚨 URGENT: [Sender] - [Subject] - [Brief summary]"

At 6 PM, send digest:
📧 Email Summary for Today
🔴 Urgent: [X]
🟡 Today: [X]
🟢 Later: [X]
⚫ Junk: [X]
```

### 调度配置

```json
{
  "schedule": "0 8,10,12,14,16,18 * * 1-5",
  "name": "Email Auto-Sorter",
  "prompt": "[paste the prompt template above here]"
}
```

```json
{
  "schedule": "0 18 * * *",
  "name": "Email Daily Summary",
  "prompt": "Send email sorting daily digest via Telegram"
}
```

### 邮箱文件夹

- `INBOX-Urgent`
- `INBOX-Today`
- `INBOX-Later`
- `INBOX-Junk`

## 成功标准

- [ ] 重要邮件不再被 newsletter 淹没。
- [ ] 每晚能收到分类摘要并快速复盘。
- [ ] 主收件箱未读压力显著下降。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/56-email-auto-sorter.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/56-email-auto-sorter.md)

# 个人 CRM（自动联系人发现）

> 每天自动从邮件和日历更新联系人关系，会议前自动生成人物简报。

## 这个案例能帮你做什么

- 解决“见过的人很多，但跟进脉络容易丢”的问题。
- 每天自动更新联系人与互动记录。
- 会议前输出背景简报，减少临时翻邮件。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `gog` CLI | Gmail + Calendar 扫描 | Google Workspace |
| 外部（需准备） | SQLite / CRM DB | 联系人与互动记录存储 | 本地数据库 |
| 内置 | Telegram topic | CRM 查询入口 | OpenClaw Built-in |
| 外部（可选） | `crm-query` | 自然语言查询 CRM | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的 CRM 助手。
请先扫描过去 24 小时邮件和日历，
输出：新增联系人、更新联系人、待跟进对象。
本轮只输出结果，不写数据库。
```

## 稳定自动版（可长期运行）

### 1) CRM 表结构

```sql
CREATE TABLE contacts (
  id INTEGER PRIMARY KEY,
  name TEXT,
  email TEXT,
  first_seen TEXT,
  last_contact TEXT,
  interaction_count INTEGER,
  notes TEXT
);
```

### 2) 调度提示词（源案例）

```text
Run a daily cron job at 6 AM to:
1. Scan my Gmail and Calendar for the past 24 hours
2. Extract new contacts and update existing ones
3. Log interactions (meetings, emails) with timestamps and context

Also, every morning at 7 AM:
1. Check my calendar for today's meetings
2. For each external attendee, search my CRM and email history
3. Deliver a briefing to Telegram with: who they are, when we last spoke, what we discussed, and any follow-up items
```

## 成功标准

- [ ] 联系人增量可自动发现并更新。
- [ ] 会议前简报稳定输出。
- [ ] 追踪问题可通过 topic 即时查询。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/personal-crm.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/personal-crm.md)

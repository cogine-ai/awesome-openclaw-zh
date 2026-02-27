# LinkedIn 周更草稿助手

> 每周自动起草 2-3 条 LinkedIn 草稿，先入库待审，不自动发布。

## 这个案例能帮你做什么

- 从你最近一周真实工作记录里提炼“可发内容”，降低起稿门槛。
- 固定节奏产出 2-3 条草稿，解决“有内容但总是拖着不发”。
- 先草稿后人工审核，保证风格和质量底线。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron.jobs` | 定时触发每周草稿任务 | OpenClaw Built-in |
| 内置 | `memory_search` | 从最近活动中提取素材 | OpenClaw Built-in |
| 内置 | `notion` / `airtable` / `sheets` | 保存草稿数据库 | OpenClaw Built-in |
| 内置 | `todoist`（可选） | 提取已完成任务作为素材 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先执行一次手动草稿：

```text
你是我的 OpenClaw 助手。
请帮我做“LinkedIn 周更草稿助手”的预演版：
1. 回顾我最近 7 天工作活动。
2. 提炼 2 条可发主题。
3. 生成 2 条 150-300 词草稿（不加 emoji，不加 em dash）。
4. 本轮只输出草稿，不写入数据库、不发布。
```

## 稳定自动版（可长期运行）

### 1) Cron 配置

```json
{
  "name": "linkedin-drafter",
  "schedule": {
    "kind": "cron",
    "expr": "0 10 * * 2",
    "tz": "UTC"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Draft 2-3 LinkedIn posts. Review my recent activity from [YOUR_ACTIVITY_SOURCE]. Identify post-worthy insights. Draft in my voice: direct, no fluff, professional but human, no em dashes/emojis. Rotate topics: [YOUR_TOPIC_1], [YOUR_TOPIC_2], [YOUR_TOPIC_3]. Save drafts to [YOUR_DATABASE] with status 'Draft'."
  },
  "sessionTarget": "isolated"
}
```

### 2) 本地测试命令

```bash
openclaw cron run linkedin-drafter
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“LinkedIn Drafter”。

每周二 10:00 UTC：
1. 从 [YOUR_ACTIVITY_SOURCE] 回顾最近 7 天活动。
2. 识别值得分享的真实洞察。
3. 生成 2-3 条 LinkedIn 草稿（150-300 words）。
4. 轮换 [YOUR_TOPIC_1/2/3]。
5. 将草稿写入 [YOUR_DATABASE]，状态为 Draft。

写作规则：
- 直接、专业、少废话
- no em dashes, no emojis
- 第一行要有 hook
- 不写 hashtags
- 不写“engage with this post”式句子
```

### 4) Notion 表结构（示例）

| 字段 | 类型 | 说明 |
|---|---|---|
| Title | Title | 草稿主题 |
| Content | Text | 正文草稿 |
| Status | Select | Draft / Ready / Posted |
| Topic | Select | 主题分类 |
| Created | Date | 创建日期 |
| Posted | Date | 实际发布时间 |

## 使用建议

- 活动来源尽量真实（任务、提交、会议），草稿质量会明显更高。
- 默认不要自动发布，保留人工审核缓冲。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/linkedin-drafter.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/linkedin-drafter.md)

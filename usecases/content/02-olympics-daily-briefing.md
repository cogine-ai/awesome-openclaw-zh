# 奥运会每日简报

> 每天 07:00 自动汇总参赛名单、奖牌结果和热点争议，直接推送到 Telegram 话题帖。

## 这个案例能帮你做什么

- 自动追踪当天参赛选手与前一天奖牌信息，减少多站点来回查。
- 自动识别争议/危机类新闻，优先标注高关注事件。
- 统一格式输出到 Telegram，形成稳定晨报流程。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`web_search`](https://clawhub.ai/skills/searching-assistant) | 搜索赛程与选手动态 | ClawHub |
| 内置 | `web_fetch` | 抓取结果页和新闻正文 | OpenClaw Built-in |
| 内置 | `telegram` | 发送晨报到话题线程 | OpenClaw Built-in |
| 内置 | `cron` | 每日定时执行 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先跑一次手动版晨报：

```text
你是我的 OpenClaw 助手。
请帮我做“奥运会每日简报”的预演版：
1. 搜索今天意大利选手赛程。
2. 抓取昨天奖牌结果。
3. 抽取 2-3 条争议/危机新闻。
4. 输出一版 Telegram 晨报草稿，不发送。
```

## 稳定自动版（可长期运行）

### 1) 数据源准备

```text
Identify:
- Official Olympics results API
- Italian athlete roster
- Sports news RSS feeds
- Social media monitoring for controversies
```

### 2) 晨报模板

```markdown
## 🏅 Olympics Briefing - {{date}}

### Today's Italian Competitors
{{#athletes}}
- {{name}} - {{event}} at {{time}}
{{/athletes}}

### Yesterday's Medals
{{#medals}}
- {{type}}: {{event}} - {{athlete}}
{{/medals}}
Total: {{gold}}🥇 {{silver}}🥈 {{bronze}}🥉

### 🔥 Hot Stories
{{#stories}}
- {{headline}}: {{summary}}
{{/stories}}

### Historic Moments
{{#records}}
- {{description}}
{{/records}}
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Olympics Daily Briefing”。
请使用 Skills：web_search、web_fetch、telegram、cron。

每天 07:00（Europe/Rome）执行：
1. 搜索今天意大利选手参赛信息。
2. 抓取昨天奖牌结果。
3. 扫描争议/危机新闻。
4. 检查是否出现历史纪录。
5. 格式化为 Telegram 消息。
6. 发送到 #olympics-briefing 话题线程。

编辑规则：
- 社交提及数 >1000 的故事加 🔥 标记。
```

### 4) 调度配置

```json
{
  "schedule": "0 7 * * *",
  "timezone": "Europe/Rome",
  "task": "olympics_briefing",
  "steps": [
    "fetch_competitors",
    "fetch_medals",
    "scan_controversies",
    "format_telegram",
    "send_notification"
  ]
}
```

### 5) Telegram 发送示例

```javascript
// Send to specific topic
await telegram.sendMessage({
  chat_id: human.telegram_chat,
  message_thread_id: 12345, // Olympics topic
  text: briefing,
  parse_mode: "Markdown"
});
```

## 成功标准

- [ ] Delivered by 07:00 Rome time daily
- [ ] All Italian competitors listed
- [ ] Medal count accurate within 1 hour of events
- [ ] Controversy stories flagged before mainstream media

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/02-olympics-daily-briefing.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/02-olympics-daily-briefing.md)

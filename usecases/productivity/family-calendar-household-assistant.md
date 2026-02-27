# 家庭日历与家务助理

> 聚合多源家庭日程，并通过消息监听自动创建事件与家务提醒。

## 这个案例能帮你做什么

- 统一工作、家庭、学校、邮件附件等分散日历来源。
- 自动识别消息中的“预约/承诺”并写入日历。
- 支持家务库存问答与购物清单协同。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（按需） | Calendar API / `ical` | 聚合多日历源 | Google/Apple/CalDAV |
| 外部（按需） | `imessage` | 被动监听预约类消息（macOS） | OpenClaw Skill |
| 内置 | Telegram/Slack 通道 | 家庭共享通知与查询 | OpenClaw Built-in |
| 内置 | 文件系统 | 库存文件维护（JSON） | OpenClaw Built-in |
| 外部（可选） | OCR/视觉能力 | 识别纸质日历/库存照片 | 视觉模型 |

## 快速体验版（先跑一轮）

```text
你是我的家庭协调助手。
请先生成一份“明日家庭总览”演示，包含：
1) 各日历来源事件聚合
2) 冲突提示
3) 需提前出发的行程建议
本轮不自动写日历，只输出汇总。
```

## 稳定自动版（可长期运行）

### 1) 日历聚合规则

```text
On morning briefing (8:00 AM):
1. Fetch my Google Work Calendar
2. Fetch shared Family Google Calendar
3. Fetch partner's calendar
4. Check school calendar PDFs and extract events
5. Check recent emails for event invitations
```

### 2) 消息监听（源案例）

```text
Every 15 minutes:
1. Check new iMessages
2. Detect appointment-like patterns
3. Create calendar event + 30-min driving buffer before/after
4. Send confirmation to family channel
```

### 3) 家庭库存文件

- 文件示例：`~/household/inventory.json`
- 记录字段：`item / quantity / location / threshold / updated_at`

## 成功标准

- [ ] 早间家庭日程汇总稳定送达。
- [ ] 预约类消息可被识别并写入日历。
- [ ] 库存查询与购物补货可闭环。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/family-calendar-household-assistant.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/family-calendar-household-assistant.md)

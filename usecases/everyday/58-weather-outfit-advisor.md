# 天气穿搭顾问

> 每天早上结合天气 + 日程给出可直接照穿的穿搭建议。

## 这个案例能帮你做什么

- 把“今天穿什么”从临场纠结，变成固定时间收到建议。
- 同时考虑温度、降雨、风力和当天场景（开会/通勤/居家）。
- 支持基于你反馈持续调整，减少“今天穿错了”的概率。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `Weather` | 获取天气、降雨、风力 | OpenClaw Built-in |
| 外部（需安装） | `Calendar Skill` | 读取当日日程语境 | [clawhub.ai/skills/calendar](https://clawhub.ai/skills/calendar) |
| 外部（需安装） | `Memory/Notes Skill` | 记住你的穿衣偏好 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | Telegram 通道 | 推送建议 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的穿搭助手。
请根据我今天所在城市天气和日程，输出：
1) 上装/下装/鞋子/外套/配件建议
2) 为什么这么搭
3) 雨天或大风提醒
本轮按“通勤 + 办公室”场景给出。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my Personal Outfit Advisor. Every morning, check the weather and my schedule, then recommend what I should wear today.

DAILY TASK (7:15 AM):
1. Get weather data for [YOUR CITY]
2. Check calendar context (in-person meetings, outdoor plans, video calls)
3. Send outfit recommendation via Telegram:

👔 Today's Outfit Recommendation
🌤️ Weather Forecast
📅 Today's Context
👕 Recommended Outfit (Top / Bottom / Shoes / Layers / Accessories)
💡 Styling Notes
⚠️ Weather Alert

OUTFIT LOGIC RULES:
- Rain: umbrella or waterproof jacket, avoid suede shoes
- Wind: avoid flowy items, add layers
- Sun/heat: breathable fabrics, lighter colors
- Formality follows calendar context (client meeting > office day > WFH)

Always mention umbrella if rain chance > 40%.
```

### 调度配置

```json
{
  "schedule": "15 7 * * *",
  "name": "Daily Outfit Advisor",
  "prompt": "[paste the prompt template above here]",
  "timezone": "Your/Timezone"
}
```

可选周预览：

```json
{
  "schedule": "0 19 * * 0",
  "name": "Weekly Wardrobe Preview",
  "prompt": "Send weekly weather and wardrobe planning summary"
}
```

## 成功标准

- [ ] 每天 7:15 前收到建议。
- [ ] 当天穿搭与天气变化匹配。
- [ ] 正式度与当天日程匹配，不再“场景错位”。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/58-weather-outfit-advisor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/58-weather-outfit-advisor.md)

# 旅行行程规划助手

> 输入目的地和预算，输出按天可执行的完整行程方案。

## 这个案例能帮你做什么

- 快速完成“机酒行吃玩”全链路行程草案。
- 每日安排包含时间、费用、交通与餐饮建议，直接可用。
- 自动补齐签证、天气、货币、通讯等出发前清单。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Web Search` | 搜索景点、价格、评论与交通 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | `Web Fetch` | 抓取攻略与预订站点细节 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 下发行程和行前提醒 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的旅行规划助手。
请基于“目的地 + 天数 + 预算 + 兴趣”输出 2 天样例行程，
每一天包含：上午/中午/下午/晚上安排、预计花费、交通建议。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my travel planning agent. When I tell you about an upcoming trip:

Gather this info:
- Destination
- Dates (or number of days)
- Budget
- Travelers
- Interests
- Travel style
- Must-see places

Then create itinerary:
✈️ Trip to [Destination] | [Dates]
📋 Pre-Trip Checklist (visa, vaccines, currency, weather, SIM)
🗓️ Day-by-day plan:
- Morning / Lunch / Afternoon / Dinner / Evening
- Transport tips
- Estimated day cost

Also include:
- Local customs
- Tourist traps to avoid
- Money-saving tips
- Useful apps
```

### 调度配置

- 按需触发：收到旅行需求后生成
- 可选提醒：出发前 7 天与 1 天各提醒一次检查清单

## 成功标准

- [ ] 10 分钟内生成完整行程草案。
- [ ] 预算估算与实际偏差控制在 20% 左右。
- [ ] 行程可直接执行，无需大量二次补充。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/70-travel-itinerary-planner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/70-travel-itinerary-planner.md)

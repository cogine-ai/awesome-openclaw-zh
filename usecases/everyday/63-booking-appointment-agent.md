# 预约与订位助手

> 你只提需求，代理完成搜索、比价、下单确认并同步日历。

## 这个案例能帮你做什么

- 将“找店 + 问档期 + 填信息 + 记录确认号”变成一次请求。
- 输出可比较的 Top 3 选项，减少来回切换页面。
- 预订完成后自动补齐地址、联系方式和变更信息。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Web Search` | 搜索服务商与可预约时段 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | `Browser Control` | 填表与下单操作 | OpenClaw Built-in |
| 内置 | `Web Fetch` | 读取商家详情和条款 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的预约助手。
请在 [YOUR CITY/AREA] 帮我找“周五晚餐 2 人位”，
先给 Top 3（评分、价格区间、可预约时间、距离），
本轮不执行预订。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my booking assistant. When I ask you to book something:

1. **Search**: Find available options near [YOUR CITY/AREA]
2. **Compare**: Show me top 3 options with:
   - Name, rating, price range
   - Available times that match my request
   - Distance from my location
3. **Book**: Once I pick one, complete the reservation:
   - Fill out online booking forms via browser
   - If no online booking, provide the phone number and a script I can use
4. **Confirm**: Add the appointment to my calendar with:
   - Location and address
   - Confirmation number
   - Contact info for changes/cancellation

Types of bookings I'll ask for:
- Restaurant reservations
- Doctor/dentist appointments
- Hair salon appointments
- Home services (plumber, electrician, cleaner)
- Car service/mechanic

Always confirm with me before finalizing any booking.
```

### 调度配置

- 按需触发：收到预约请求时执行
- 不做自动定时任务

## 成功标准

- [ ] 10 分钟内产出可选方案并完成预约。
- [ ] 最终确认信息完整可追踪。
- [ ] 无需反复来回沟通档期。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/63-booking-appointment-agent.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/63-booking-appointment-agent.md)

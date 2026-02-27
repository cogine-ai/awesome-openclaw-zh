# 活动嘉宾确认（语音外呼）

> 用 SuperCall 逐个电话确认嘉宾出席，并自动汇总 RSVP 结果。

## 这个案例能帮你做什么

- 把婚礼、聚会、活动前的“逐个确认”流程自动化。
- 电话确认响应率通常高于纯文本消息。
- 自动沉淀“确认/拒绝/未接通/备注”结果表。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `@xonder/supercall` | 批量语音呼叫与结果记录 | [clawhub.ai/xonder/supercall](https://clawhub.ai/xonder/supercall) |
| 外部（需准备） | Twilio 号码 | 外呼线路 | Twilio |
| 外部（需准备） | OpenAI Realtime Key | 通话语音模型 | OpenAI |
| 外部（需安装） | ngrok | webhook 隧道 | ngrok |

## 快速体验版（先跑一轮）

```text
你是我的活动协调助手。
请先用 3 位嘉宾做测试流程：
1. 读取姓名+电话
2. 以“Jamie, event coordinator”身份拨打
3. 收集出席与备注（忌口/可带人/到场时间）
4. 输出汇总（confirmed/declined/no-answer）
本轮只做小样本测试。
```

## 稳定自动版（可长期运行）

### 1) 安装与准备

- 安装：`openclaw plugins install @xonder/supercall`
- 完成 SuperCall README 的配置步骤（Twilio、OpenAI、ngrok、hooks）。

### 2) 执行提示词（源案例）

```text
I need you to confirm attendance for my event. Here are the details:

Event: Summer BBQ
Date: Saturday, June 14th at 4 PM
Location: 23 Oak Street

Here is my guest list:
<paste your guest list here>

For each guest, use supercall to call them. Use the persona "Jamie, event coordinator
for [your name]". The goal for each call is to confirm whether they're attending,
and note any dietary restrictions, plus-ones, or other comments.

After each call, log the result. Once all calls are done, give me a full summary:
- Who confirmed
- Who declined
- Who didn't answer
- Any notes or special requests from each guest
```

## 成功标准

- [ ] 每位嘉宾都有明确状态记录。
- [ ] 备注信息完整可用于后续安排。
- [ ] 小样本测试通过后再放大到全量名单。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/event-guest-confirmation.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/event-guest-confirmation.md)

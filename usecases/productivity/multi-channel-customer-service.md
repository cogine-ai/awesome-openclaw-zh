# 多渠道 AI 客服平台

> 把 WhatsApp、Instagram、邮件、评论统一进一个 AI 客服收敛层。

## 这个案例能帮你做什么

- 把分散渠道统一到一处处理，缩短响应时间。
- 常见问题自动回复，复杂问题升级人工。
- 支持测试模式，先演练再上线真实通道。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需配置） | WhatsApp Business API | 客服消息接入 | Meta/360dialog |
| 外部（需配置） | Instagram Graph API | IG 私信接入 | Meta |
| 外部（需安装） | `gog` CLI | Gmail 接入 | Google Workspace |
| 外部（需配置） | Google Business Profile API | 评论管理 | Google |
| 内置 | 路由与分类能力 | FAQ/预约/投诉分流 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的客服助手。
请先对 10 条模拟消息做分类演练：
- FAQ
- Appointment
- Complaint
- Review
并给出对应回复草稿。
本轮不发送到真实渠道。
```

## 稳定自动版（可长期运行）

### 1) 客服路由规则（源案例）

```text
1. Identify channel
2. Check if test mode is enabled
3. Classify intent (FAQ/Appointment/Complaint/Review)
4. Respond from knowledge base or escalate to human
```

### 2) 测试模式要求（源案例）

```text
Test mode:
- Prefix responses with [TEST]
- Log but don't send to real channels
```

### 3) 心跳检查

```text
Every 30 minutes:
- Check for unanswered messages > 5 min old
- Alert if response queue is backing up
- Log daily response metrics
```

## 成功标准

- [ ] 多渠道消息可统一处理。
- [ ] 80% 左右常见问题可自动闭环。
- [ ] 超时与投诉可及时升级人工。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/multi-channel-customer-service.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/multi-channel-customer-service.md)

# 冷关系重启助手

> 自动发现“30 天没联系”的人，先出暖场草稿，再由你确认发送。

## 这个案例能帮你做什么

- 把“想联系但总拖着”的关系维护动作变成固定节奏。
- 每条消息都带个性化细节，降低机械感。
- 默认先审后发，避免误发和尴尬。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | Messaging（WhatsApp/Telegram/Signal） | 检查历史消息并生成草稿 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的关系维护助手。
请从我给定联系人里找出 30 天未联系的人，
为其中 2 个人分别生成自然、温和的重启消息草稿，
每条都引用对方一个具体兴趣点。
仅输出草稿，不发送。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my relationship maintenance assistant. Your job is to help me stay connected with people I care about.

Contact list (check in monthly):
- [Name 1] — old college friend, loves hiking
- [Name 2] — former colleague, into photography
- [Name 3] — cousin, just had a baby

Rules:
1. Check who I haven't messaged in 30+ days
2. Draft a natural, warm message referencing something specific about them
3. Show me the draft BEFORE sending — never send without my approval
4. Keep it casual: "Hey! Been thinking about you..." not "Dear Sir/Madam"
5. If they reply, notify me immediately so I can continue the conversation

Examples of good messages:
- "Hey [Name]! Saw this hiking trail and thought of you 🏔️ How've you been?"
- "Just came across an amazing photo and remembered your photography. What have you been shooting lately?"

Never send more than 2 revival messages per week.
```

### 调度配置

- 每周检查：每周日 `10 AM`
- 发送策略：仅草稿，人工确认后发送

## 成功标准

- [ ] 每月至少重启 2 段沉默关系。
- [ ] 草稿语气自然，不像模板群发。
- [ ] 对方回复后能及时收到提醒并延续对话。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/54-cold-relationship-revival.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/54-cold-relationship-revival.md)

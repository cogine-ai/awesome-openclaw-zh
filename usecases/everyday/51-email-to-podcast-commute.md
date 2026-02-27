# 邮件通讯转播客

> 把每天收件箱里的重点通讯自动转成 3-5 分钟通勤音频。

## 这个案例能帮你做什么

- 自动筛选最近 24 小时的 newsletter，不再“收藏后永远不看”。
- 先生成口语化播客稿，再转语音推送到 Telegram/Signal。
- 每天固定时段推送，通勤、做饭、运动时可直接收听。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `TTS / ElevenLabs` | 文本转语音 | [clawhub.ai/skills/beware-piper-tts](https://clawhub.ai/skills/beware-piper-tts) |
| 外部（需安装） | `Email Access` | 读取邮件（Gmail/Outlook） | [clawhub.ai/skills/agentmail-wrapper](https://clawhub.ai/skills/agentmail-wrapper) |
| 内置 | Telegram/Signal 消息通道 | 下发语音结果 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的个人播客制作助手。
请从我最近 24 小时邮件里挑选最有价值的 3-5 条 newsletter，
写一份 3-5 分钟可朗读脚本（口语化、无广告、无营销段落），
本轮只输出脚本，不做语音转换。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my personal podcast producer. Every morning at 7 AM:

1. Check my email for newsletters received in the last 24 hours
2. Pick the most interesting 3-5 stories
3. Write a conversational podcast script (3-5 minutes reading time)
4. Convert to audio using TTS
5. Send the audio to me via Telegram

Style: Warm, conversational, like a friend catching you up over coffee.
Keep it under 5 minutes. Skip ads and promotional content.
```

### 调度配置

```text
Schedule: 0 7 * * *
Action: Check email → Generate script → TTS → Send audio
```

## 成功标准

- [ ] 音频在通勤前送达。
- [ ] 覆盖当天最相关的 3-5 条信息。
- [ ] 时长控制在 5 分钟内。
- [ ] 听完后能直接掌握重点，不需要再回看原邮件。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/51-email-to-podcast-commute.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/51-email-to-podcast-commute.md)

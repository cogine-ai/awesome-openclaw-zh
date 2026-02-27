# 医学邮件转播客

> 把医学通讯邮件自动转成 5 分钟音频简报，通勤时直接听。

## 这个案例能帮你做什么

- 自动读取医学通讯邮件并提取文章链接，不再手动逐条看。
- 自动补充链接上下文后生成口语化播客脚本，再转成音频。
- 音频会直接发送到 Signal，早上拿起手机就能听。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`email`](https://clawhub.ai/skills/agentmail-wrapper) | 读取并解析邮件 | ClawHub |
| 内置 | `web_fetch` | 拉取链接正文补充上下文 | OpenClaw Built-in |
| 外部 | [`elevenlabs`](https://clawhub.ai/skills/beware-piper-tts) | 文本转语音 | ClawHub |
| 内置 | `ffmpeg` | 合并音频分片 | OpenClaw Built-in |
| 内置 | `signal` | 发送最终音频 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做单封邮件演示：

```text
你是我的 OpenClaw 助手。
请帮我做“医学邮件转播客”的预演版：
1. 读取最近一封医学通讯邮件，提取标题与链接。
2. 抓取每个链接的正文要点并整合。
3. 写一版 5 分钟口语化脚本（家庭医学语境）。
4. 本轮只输出脚本，不生成音频、不发送消息。
```

## 稳定自动版（可长期运行）

### 1) 邮件识别配置

```text
Set up email forwarding from medical newsletter to agent's Gmail.
Configure auto-detection during heartbeats for newsletters matching:
- Sender: doctors@bcnews.com
- Subject contains: "Newsflash"
```

### 2) 安装 Skills

```bash
npx molthub@latest install email
npx molthub@latest install web_fetch
npx molthub@latest install elevenlabs
npx molthub@latest install ffmpeg
npx molthub@latest install signal
```

### 3) 处理脚本：`skills/email-podcast/index.js`

```javascript
// Parse email → extract stories → research URLs → write script → TTS → deliver
async function processMedicalEmail(email) {
  const stories = parseStories(email.body);
  const enriched = await Promise.all(
    stories.map(s => web_fetch(s.url).then(enhanceStory))
  );
  const script = writePodcastScript(enriched, "family_medicine");
  const audio = await generateTTS(script); // chunk if > 4000 chars
  await signal.sendAudio({ to: human.phone, audio });
}
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Medical Email to Podcast”。
请使用 Skills：email、web_fetch、elevenlabs、ffmpeg、signal。

当收到医学通讯邮件时按顺序执行：
1. 解析邮件正文，提取新闻标题和 URL。
2. 对每个 URL 抓取全文并补充背景。
3. 写一版 5 分钟播客脚本（专业但口语化，面向家庭医学）。
4. 使用 ElevenLabs 生成语音；若文本超过 4000 字符，分片后用 ffmpeg 合并。
5. 通过 Signal 发送音频文件。
6. 记录到 memory/medical-podcasts/YYYY-MM-DD.md。
```

### 5) 调度配置

```json
{
  "schedule": "0 6 * * *",
  "task": "check_medical_emails",
  "action": "process_and_deliver_podcast"
}
```

## 成功标准

- [ ] Newsletter processed within 1 hour of receipt
- [ ] Audio length: 5-7 minutes
- [ ] Human listens within 24 hours
- [ ] Zero manual steps required

## 常见问题

| 问题 | 处理方式 |
|---|---|
| TTS fails (text too long) | Split into 4000-char chunks, concat with ffmpeg |
| URL returns paywall | Use web_fetch with textise dot iitty |
| Audio quality poor | Switch ElevenLabs voice to 'Antoni' or 'Bella' |

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/01-medical-email-to-podcast.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/01-medical-email-to-podcast.md)

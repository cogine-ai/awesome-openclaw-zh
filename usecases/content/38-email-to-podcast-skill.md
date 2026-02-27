# 邮件转播客 Skill

> 把“任意邮件转音频”做成可复用 Skill，一次配置，多场景复用。

## 这个案例能帮你做什么

- 把邮件转音频能力模块化，不再每个场景重复开发。
- 同一个 Skill 可复用在医学通讯、新闻摘要、工作邮件等场景。
- 支持通过配置切换语音、长度、输出格式。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`email`](https://clawhub.ai/skills/agentmail-wrapper) | 读取邮件内容 | ClawHub |
| 外部 | [`elevenlabs`](https://clawhub.ai/skills/beware-piper-tts) | 文本转语音 | ClawHub |
| 内置 | `ffmpeg` | 音频处理与合并 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先把结构搭起来，验证配置可读：

```text
你是我的 OpenClaw 助手。
请帮我做“Email-to-Podcast Skill”的预演版：
1. 创建 skills/email-podcast 目录结构。
2. 生成 SKILL.md 和 config.json 初版。
3. 用一封测试邮件跑通 process 流程（仅输出中间结果，不发音频）。
```

## 稳定自动版（可长期运行）

### 1) Skill 目录结构

```text
skills/
└── email-podcast/
    ├── SKILL.md
    ├── index.js
    └── config.json
```

### 2) SKILL.md 模板

```markdown
# Email to Podcast

Converts emails to audio podcasts.

## Configuration
{
  "voice": "Antoni",
  "maxLength": 4000,
  "outputFormat": "mp3"
}

## Usage
email-podcast.process(email)
```

### 3) 安装命令

```bash
npx molthub@latest install email-podcast
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Email-to-Podcast Skill”。
请使用 Skills：email、elevenlabs、ffmpeg。

执行目标：
1. 把邮件读取与解析封装到 email-podcast Skill。
2. 支持配置 voice / maxLength / outputFormat。
3. 当文本超过 maxLength 时自动分片处理。
4. 输出可复用接口：email-podcast.process(email)。
```

## 成功标准

- [ ] Reusable across projects
- [ ] Configurable per use case
- [ ] Published to ClawdHub

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/38-email-to-podcast-skill.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/38-email-to-podcast-skill.md)

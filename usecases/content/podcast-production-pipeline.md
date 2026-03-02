# 播客生产流水线（Podcast Production Pipeline）

> 从录制前调研到录制后分发素材，一次产出完整播客生产包。

## 这个案例能帮你做什么

- 录制前完成嘉宾研究、主题研究和访谈提纲。
- 录制后自动生成时间戳 show notes、节目简介和 highlights。
- 一次输出 X / LinkedIn / Instagram 的宣发文案。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_search` / `browser` | 录制前嘉宾与主题调研 | OpenClaw Built-in |
| 内置 | `filesystem` | 读取 transcript、写入产物目录 | OpenClaw Built-in |
| 内置 | `telegram` / `slack` / `discord` channel | 分发内容包和提醒 | OpenClaw Built-in |
| 内置（可选） | `sessions_spawn` | 并行跑调研与写作任务 | OpenClaw Built-in |
| 外部（可选） | `RSS feed skill` | 监控竞品播客更新 | hesamsheikh/awesome-openclaw-usecases |

## 快速体验版（先跑一轮）

1. 先选 1 个主题和 1 位嘉宾做录制前预演。
2. 验证提纲质量后再进入录制后流程。
3. 本轮先只输出文本，不直接发布。

```text
I'm recording a podcast episode about [TOPIC]. My guest is [NAME].

Please:
1. Research the guest — their background, recent work, hot takes, and
   anything controversial or interesting they've said publicly.
2. Research the topic — key trends, recent news, common misconceptions,
   and what the audience likely already knows vs. what would surprise them.
3. Generate an episode outline:
   - Cold open hook (1-2 sentences to grab attention)
   - Intro script (30 seconds, casual tone)
   - 5-7 interview questions, ordered from easy/rapport-building to deep/provocative
   - 2-3 "back pocket" questions in case the conversation stalls
   - Closing segment with call-to-action

Save everything to ~/podcast/episodes/[episode-number]/prep/
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 录制后自动读 transcript，生成时间戳 show notes、简介和 highlights。
2. 自动生成多平台宣发文案，并统一写入 `publish` 目录。
3. 可选接入 RSS 监控，持续跟踪相关播客新内容。

## 成功标准

- [ ] 每期都能稳定产出录制前提纲。
- [ ] 每期都能稳定产出录制后 show notes 与简介。
- [ ] 多平台宣发文案可一次生成并复用。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/podcast-production-pipeline.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/podcast-production-pipeline.md)

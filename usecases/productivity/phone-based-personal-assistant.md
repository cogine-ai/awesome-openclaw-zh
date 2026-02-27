# 基于电话的个人助理

> 用普通电话直接接入 OpenClaw，对语音查询和提醒场景更友好。

## 这个案例能帮你做什么

- 在驾驶、行走等不方便打字场景下直接语音调用助手。
- 无需依赖手机 App，任何可拨号设备都能用。
- 可扩展到日程、工单、搜索等语音查询。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | ClawdTalk | 电话语音接入 OpenClaw | [github.com/team-telnyx/clawdtalk-client](https://github.com/team-telnyx/clawdtalk-client) |
| 外部（需配置） | Telnyx | 电话网络连接 | [telnyx.com](https://telnyx.com/) |
| 外部（按需） | Calendar / Jira / Web Search | 电话查询数据源 | 各系统 API |

## 快速体验版（先跑一轮）

```text
你是我的电话助手。
当我来电时：
1) 先问候并询问需求
2) 支持“今日日程 / Jira待办 / AI新闻”三类查询
3) 用简短语音回复
本轮只做对话脚本演练。
```

## 稳定自动版（可长期运行）

### 通话提示词（源案例）

```text
You are available via phone. When I call, greet me and ask how I can help.

For calendar queries: "What's on my calendar today?"
For Jira updates: "Show me my open tickets"
For web search: "Search for latest news on AI agents"
```

## 成功标准

- [ ] 电话接入稳定可用。
- [ ] 常见语音查询可在通话内完成。
- [ ] 免手操作场景下体验顺畅。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/phone-based-personal-assistant.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/phone-based-personal-assistant.md)

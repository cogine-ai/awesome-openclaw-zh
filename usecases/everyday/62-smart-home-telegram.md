# Telegram 智能家居控制

> 用自然语言在 Telegram 里统一控制灯光、温控、门锁与场景模式。

## 这个案例能帮你做什么

- 不用在多个智能家居 App 之间来回切换。
- 支持场景指令（如 Movie mode / Good night / I’m leaving）。
- 离家模式下可做高频传感器巡检并推送安全告警。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | Home Assistant | 接入家庭设备控制 API | Home Assistant |
| 内置 | `Browser Control` | 无 API 时走网页回退控制 | OpenClaw Built-in |
| 内置 | Telegram 通道 | 指令入口与回执提醒 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的智能家居控制助手。
请先模拟解析以下 5 条命令，并输出将执行的动作：
- Turn off all lights
- Set bedroom to 21 degrees
- Is the garage door open?
- Good night
- I'm leaving
本轮不实际控制设备。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my smart home controller. I'll send commands via Telegram in natural language.

Connected systems:
- Home Assistant at http://[YOUR_HA_IP]:8123
- API Token: [YOUR_TOKEN]

Understand commands like:
- "Turn off all lights"
- "Set bedroom to 21 degrees"
- "Is the garage door open?"
- "Turn on movie mode"
- "Good night"
- "I'm leaving"

Scenes I use:
- "Movie mode": Living room lights 20%, TV on
- "Good morning": Kitchen lights on, coffee maker on, thermostat 22°C
- "Good night": All lights off, doors locked, thermostat 18°C

Rules:
- Confirm every action with a short response
- If a command is ambiguous, ask for clarification
- Never unlock doors without double confirmation
- Send me an alert if a door/window sensor triggers while I'm away
```

### 调度配置

- 常驻：Telegram 指令即时响应
- 离家模式：每 `5` 分钟检查一次安全传感器（Heartbeat）

## 成功标准

- [ ] 一个聊天入口可覆盖主要家居控制。
- [ ] 指令响应稳定在秒级。
- [ ] 安全告警可靠触发，不漏报。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/62-smart-home-telegram.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/62-smart-home-telegram.md)

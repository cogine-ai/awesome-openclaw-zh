# 一个 OpenClaw 管多个飞书机器人

> 用多账号、多 Agent、可选多 Gateway 的方式，把不同飞书机器人稳定路由到不同 OpenClaw 身份。

## 这个案例能帮你做什么

- 把主助理、编码助理、研究助理拆成不同飞书机器人，避免上下文串台。
- 在一个 Gateway 内做多账号路由，或在同一台机器上跑多个 Gateway 做更强隔离。
- 让不同飞书机器人各自绑定独立 workspace、agentDir 和 session store，长期保持各自人格与记忆。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw agents add` | 创建独立 Agent 与 workspace | OpenClaw CLI |
| 内置 | `bindings` / `accountId` 路由 | 把不同飞书账号绑定到不同 Agent | OpenClaw Gateway |
| 内置 | `--profile` 多 Gateway | 在同机上跑多个相互隔离的 Gateway | OpenClaw Gateway |
| 外部（需配置） | 飞书机器人应用 | 为每个 Agent 提供独立聊天入口 | 飞书开放平台 |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 架构助手。
请先帮我设计一个最小可用的双机器人方案：
1. 一个飞书机器人负责日常助理
2. 一个飞书机器人负责编码任务
3. 两个机器人各自绑定不同 Agent
4. 说明是单 Gateway 多账号更适合，还是双 Gateway 更适合
本轮先不要生成全量生产配置，只输出最小落地方案。
```

## 稳定自动版（可长期运行）

### 1) 先准备两个隔离 Agent

```bash
openclaw agents add main
openclaw agents add coding
openclaw agents list --bindings
```

如果你需要更强隔离，可以按 profile 分开运行 Gateway：

```bash
# main
openclaw --profile main setup
openclaw --profile main gateway --port 18789

# coding
openclaw --profile coding setup
openclaw --profile coding gateway --port 19001
```

```bash
openclaw --profile main gateway install
openclaw --profile coding gateway install
```

### 2) 在飞书侧创建多个机器人账号

- 为主助理和编码助理分别创建飞书应用。
- 每个应用都拿到各自的 `App ID` 和 `App Secret`。
- 如果只是单 Gateway 多账号，分别把两个账号加到同一个 `channels.feishu.accounts` 下。

### 3) OpenClaw 路由配置（核心）

```json5
{
  session: {
    dmScope: "per-account-channel-peer"
  },
  agents: {
    list: [
      {
        id: "main",
        workspace: "~/.openclaw/workspace-main",
        default: true
      },
      {
        id: "coding",
        workspace: "~/.openclaw/workspace-coding"
      }
    ]
  },
  bindings: [
    {
      agentId: "main",
      match: { channel: "feishu", accountId: "default" }
    },
    {
      agentId: "coding",
      match: { channel: "feishu", accountId: "coding" }
    }
  ],
  channels: {
    feishu: {
      enabled: true,
      defaultAccount: "default",
      dmPolicy: "pairing",
      accounts: {
        default: {
          appId: "cli_main_xxx",
          appSecret: "main_secret"
        },
        coding: {
          appId: "cli_coding_xxx",
          appSecret: "coding_secret"
        }
      }
    }
  }
}
```

关键点：

- `bindings[].match.accountId` 决定哪个飞书账号的消息路由到哪个 Agent。
- `defaultAccount` 让未显式指定账号的出站动作有稳定默认值。
- `session.dmScope = "per-account-channel-peer"` 能避免同一个人分别给两个飞书机器人发消息时共用同一条 DM 会话。

### 4) 启动、配对与验证

```bash
openclaw channels add
openclaw gateway restart
openclaw channels status --probe
openclaw agents list --bindings
```

在两个飞书机器人里分别发一条测试消息，收到 pairing code 后批准：

```bash
openclaw pairing approve feishu <PAIRING_CODE>
```

### 5) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 多机器人运维助手。
请维护下面这套飞书多账号路由：
1. default 账号只服务 main Agent
2. coding 账号只服务 coding Agent
3. 所有 direct message 都用 per-account-channel-peer 做隔离
4. 如果我新增第三个飞书机器人，请先给出 accountId、agentId、workspace、binding 的最小补丁
5. 每次改动前先说明会影响哪个账号和哪个 Agent
```

## 成功标准

- [ ] 不同飞书机器人之间不会串会话。
- [ ] 每个机器人都能稳定进入自己绑定的 Agent。
- [ ] 新增账号时只需要补 `accounts` 和 `bindings`，不必重做整套配置。

## 风险与边界

- 多 Gateway 只有在你确实需要更强隔离或救援机器人时才值得上，官方文档默认仍建议优先用单 Gateway。
- 如果多个实例复用了相同 `OPENCLAW_STATE_DIR`、`OPENCLAW_CONFIG_PATH` 或端口，容易出现配置冲突和会话碰撞。
- 如果 `bindings` 省略 `accountId`，默认只会匹配默认账号。

## 使用建议

- 先用“单 Gateway + 多飞书账号”跑通，再决定是否升级到“多 Gateway + 多账号”。
- 给每个 Agent 单独准备 `SOUL.md`、`USER.md`、`IDENTITY.md`，这样多机器人分工才会稳定。
- 把主助理、编码助理、研究助理拆开时，优先按“长期人格/长期记忆”来拆，不要只按一次性任务拆。

## 引用来源

- 来源仓库： [openclaw/openclaw](https://github.com/openclaw/openclaw)
- 原始条目：
  - [docs/channels/feishu.md](https://github.com/openclaw/openclaw/blob/main/docs/channels/feishu.md)
  - [docs/concepts/multi-agent.md](https://github.com/openclaw/openclaw/blob/main/docs/concepts/multi-agent.md)
  - [docs/gateway/multiple-gateways.md](https://github.com/openclaw/openclaw/blob/main/docs/gateway/multiple-gateways.md)
  - [docs/gateway/configuration-reference.md](https://github.com/openclaw/openclaw/blob/main/docs/gateway/configuration-reference.md)

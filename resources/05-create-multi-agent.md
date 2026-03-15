# 如何创建多个 OpenClaw Agent

OpenClaw 默认有一个 `main` agent，以及一套默认 workspace。

如果你希望拥有一个新的 Agent，让它具备：

- 一套独立的人设和行为规则
- 一套独立的长期记忆和会话上下文
- 一套独立的认证配置和工作目录
- 专门负责某类任务，例如编码、运营、投研、客服

那么正确做法不是“在 main 里多写一点提示词”，而是创建一个**与 `main` 并列的持久 Agent**。

核心就是两件事：

1. 新增一个 agent 定义，并给它独立 workspace
2. 给它加 routing / binding，让某些 channel、account 或 peer 路由到它

这篇文档优先讲**最小可跑通**的方式：用 CLI 完成，不手改配置。

## 先理解 3 个概念

### 1. workspace

每个 Agent 都应该有自己的 workspace。

这是它的默认工作目录，会放：

- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `TOOLS.md`
- 本地笔记、规则、上下文文件

### 2. agentDir

这是每个 Agent 的状态目录。

根据官方文档，多 Agent 模式下每个 Agent 都有自己独立的：

- `auth-profiles.json`
- 会话存储
- 运行状态

默认路径类似：

```text
~/.openclaw/agents/<agentId>/agent
~/.openclaw/agents/<agentId>/sessions
```

这意味着：**主 Agent 的认证不会自动共享给新 Agent。**

如果你想复用认证，需要显式复制对应的 `auth-profiles.json`，不要让两个 Agent 共用同一个 `agentDir`。

### 3. binding

binding 决定“某条入站消息到底进哪个 Agent”。

OpenClaw 官方文档把路由拆成三层：

- `channel`：例如 `feishu`、`telegram`、`discord`
- `accountId`：同一个渠道下的不同账号实例
- `peer`：具体私聊用户、群组、频道

如果你创建了新 Agent，但**没有配置 binding**，消息仍然会继续落到默认 Agent，一般就是 `main`。

## 最小配置步骤

### 第 1 步：创建独立 workspace

以 macOS 为例，假设你要创建一个新的 Agent：`supercoder`

```bash
mkdir -p /Users/xxx/.openclaw/workspace-supercoder
```

建议先把这几个基础文件准备好，明确这个 workspace 的定位：

- `AGENTS.md`：这个 Agent 的长期规则和工作方式
- `SOUL.md`：这个 Agent 的性格、价值取向、边界
- `USER.md`：这个 Agent 面向的用户是谁
- `IDENTITY.md`：名称、emoji、主题、头像等身份信息
- `TOOLS.md`：工具使用规范、允许范围、禁区

一个最小目录可以长这样：

```text
/Users/xxx/.openclaw/workspace-supercoder/
  AGENTS.md
  SOUL.md
  USER.md
  IDENTITY.md
  TOOLS.md
```

### 第 2 步：注册新 Agent

用 OpenClaw 官方命令注册它：

```bash
openclaw agents add supercoder \
  --workspace /Users/xxx/.openclaw/workspace-supercoder \
  --model openai-codex/gpt-5.4 \
  --non-interactive \
  --json
```

几点说明：

- `openclaw agents add <name>` 是官方支持的多 Agent 入口
- `--workspace` 明确指定这个 Agent 的独立目录
- `--model` 可以直接给它单独指定默认模型
- `--json` 只表示输出机器可读结果，**不等于非交互**
- 真正用于脚本化的是 `--non-interactive`

这一步完成后，`supercoder` 就会成为一个正式的独立 Agent，与 `main` 并列。

官方文档确认：一个独立 Agent 至少会拥有自己独立的：

- workspace
- `agentDir`
- sessions store

后续消息如果路由到它，就会持续使用它自己的上下文。

如果对应的渠道账号已经存在，官方也支持在创建时直接带上绑定：

```bash
openclaw agents add supercoder \
  --workspace /Users/xxx/.openclaw/workspace-supercoder \
  --model openai-codex/gpt-5.4 \
  --bind feishu:feishu_supercoder \
  --non-interactive \
  --json
```

### 第 3 步：设置它的身份

如果你已经在 `workspace-supercoder/IDENTITY.md` 里写好了身份信息，最直接的方式是从文件导入：

```bash
openclaw agents set-identity \
  --workspace /Users/xxx/.openclaw/workspace-supercoder \
  --from-identity \
  --json
```

如果你只想先手动指定名称和 emoji，也可以直接写：

```bash
openclaw agents set-identity \
  --agent supercoder \
  --name "Supercoder Engineer" \
  --emoji "🤖" \
  --json
```

根据官方 CLI 文档，`set-identity` 会把这些字段写入 `agents.list[].identity`：

- `name`
- `theme`
- `emoji`
- `avatar`

### 第 4 步：确认 Agent 已注册成功

建议先跑这几个命令：

```bash
openclaw agents list
openclaw agents bindings
```

如果你只想看 `supercoder` 的绑定情况：

```bash
openclaw agents bindings --agent supercoder
```

这时候通常会看到：

- `supercoder` 已存在
- 但它还没有接到任何真实消息流量

这很正常，因为你还没做渠道绑定。

## 把渠道流量路由到新的 Agent

真正让一个 Agent “活起来”的，不只是创建它，而是把某个渠道入口绑定给它。

最常见的就是：

- 一个新的飞书机器人
- 一个新的 Telegram 机器人
- 一个新的 Discord 服务器 / 频道
- 同一渠道下的第二个账号实例

### 两种做法

#### 做法 A：在新增渠道账号时，直接绑定给 Agent

官方 `openclaw channels add` 支持在交互式流程里：

- 创建新的 channel account
- 立即询问是否要把这个 account 绑定给某个 Agent

也就是说，最顺手的流程其实是：

1. 先 `openclaw agents add supercoder`
2. 再 `openclaw channels add`
3. 在 wizard 里新建账号
4. 当它询问“Bind configured channel accounts to agents now?” 时，直接选 `supercoder`

这是最少踩坑的方式。

#### 做法 B：渠道账号已经存在，再手动 bind

如果渠道账号已经配好了，也可以后补绑定：

```bash
openclaw agents bind --agent supercoder --bind feishu:feishu_supercoder
```

也可以继续加更多绑定：

```bash
openclaw agents bind \
  --agent supercoder \
  --bind feishu:feishu_supercoder \
  --bind telegram:supercoder
```

如果之后要解除绑定：

```bash
openclaw agents unbind --agent supercoder --bind feishu:feishu_supercoder
```

## 飞书示例：给 `supercoder` 绑定第二个飞书机器人

这是最适合中文用户的一条路线。

目标是：

- `main` 继续接原来的飞书机器人
- `supercoder` 接一个新的飞书机器人
- 两边会话隔离，不串上下文

### 1. 先完成第一个飞书机器人的绑定

这一步你应该已经完成。

仓库内的飞书初始配置文档后续补充；在补充之前，可先参考 OpenClaw 官方飞书渠道文档：

- https://docs.openclaw.ai/zh-CN/channels/feishu

### 2. 再新增一个飞书机器人

例如你新建一个飞书机器人：

- 机器人名：`超级开发虾`
- account 名：`feishu_supercoder`

拿到新的：

- `APPID`
- `APPSECRET`

### 3. 把新飞书账号加到 OpenClaw

最推荐直接走交互式 CLI：

```bash
openclaw channels add
```

然后：

1. 选择 `Feishu`
2. 新建一个 account
3. 账号名填写：`feishu_supercoder`
4. 输入这个新机器人的 `APPID`
5. 输入 `APPSECRET`
6. 当 CLI 问你要不要现在绑定给某个 Agent 时，选择 `supercoder`

如果你已经把新账号加好了，也可以补一个显式绑定：

```bash
openclaw agents bind --agent supercoder --bind feishu:feishu_supercoder
```

### 4. 设置 DM 隔离

如果你在**同一个渠道下配置了多个 account**，官方文档建议把：

```json5
{
  session: {
    dmScope: "per-account-channel-peer",
  },
}
```

原因很简单：

- `per-channel-peer` 只按 “渠道 + 用户” 隔离
- 当同一个渠道里有多个 account 时，最好再把 `accountId` 也纳入 session key

否则虽然路由可能已经分流，但 DM 会话隔离仍然不够彻底。

### 第 5 步：完成飞书 pairing

配置完成后，在新的飞书机器人里发起会话。

你通常会看到一条 pairing 消息，类似：

```text
OpenClaw: access not configured.
Your Feishu user id: ou_017549cd62bbxxx
Pairing code: 8R7EXXXX
Ask the bot owner to approve with:
openclaw pairing approve feishu 8R7EXXXX
```

这时候在 OpenClaw 所在机器执行：

```bash
openclaw pairing approve feishu 8R7EXXXX
```

批准后，这个飞书机器人入口就能稳定落到 `supercoder`。

## 一个新 Agent 真正独立，至少要满足哪些条件

如果你想让它成为一个“真正独立的人格”，至少确认下面几项：

- 有自己的 workspace
- 有自己的 `IDENTITY.md`
- 有自己的 `AGENTS.md / SOUL.md / TOOLS.md`
- 有自己的 `agentDir`
- 有自己的 session store
- 至少有一个独立 binding
- 如果是多账号同渠道，`dmScope` 已设置为 `per-account-channel-peer`

做到这一步，它就不再只是 `main` 的一个临时 prompt，而是一个长期可复用的独立 Agent。

## 最小检查清单

创建完之后，建议按这个顺序检查：

```bash
openclaw agents list
openclaw agents bindings --agent supercoder
openclaw channels list
openclaw gateway status
```

如果你用的是飞书，再补一次真实验证：

1. 向新机器人发消息
2. 收到 pairing code
3. 执行 `openclaw pairing approve feishu <CODE>`
4. 再次发消息，确认回复来自 `supercoder`

## 常见误区

### 1. 只建了 workspace，没有注册 Agent

仅仅创建 `workspace-supercoder/` 不够。

只要没执行 `openclaw agents add supercoder`，它就不是 OpenClaw 配置中的正式 Agent。

### 2. 建了 Agent，但没有 binding

这是最常见的问题。

Agent 已经存在，但没有任何 channel / account / peer 路由给它，消息仍然会落到 `main`。

### 3. 同一渠道多个账号，但没调 `dmScope`

如果你准备做“一个 OpenClaw，多个飞书机器人 / 多个账号入口”，请优先使用：

```json5
session.dmScope = "per-account-channel-peer"
```

### 4. 误以为主 Agent 的认证会自动共享

官方文档明确说明：认证配置文件是 per-agent 的。

如果新 Agent 需要某些模型或 OAuth 认证，要重新配置，或者显式复制对应的 `auth-profiles.json`。

## 参考资料

- OpenClaw 官方：`openclaw agents`
  - https://docs.openclaw.ai/zh-CN/cli/agents
- OpenClaw 官方：多智能体路由
  - https://docs.openclaw.ai/zh-CN/concepts/multi-agent
- OpenClaw 官方：飞书渠道
  - https://docs.openclaw.ai/zh-CN/channels/feishu
- OpenClaw 官方：Session Management
  - https://docs.openclaw.ai/concepts/session
- OpenClaw 官方：Configuration
  - https://docs.openclaw.ai/gateway/configuration

# 飞书接入对话（基础篇）

这篇文档适合：

- 你已经把 OpenClaw 部署好了
- 你想先用**最省事**的方式把 OpenClaw 接到飞书
- 你只想先跑通一个飞书机器人，不准备一开始就做多账号、多 Agent、多路由

这篇文档会完成什么：

- 使用飞书官方提供的 OpenClaw 专页，快速完成飞书机器人侧配置
- 拿到 `App ID` 和 `App Secret`
- 在 OpenClaw 里添加 Feishu channel
- 跑通第一次配对和第一次对话

## 先说结论

飞书现在已经有一个专门给 OpenClaw 准备的官方入口：

- [飞书 OpenClaw 专页](https://open.feishu.cn/page/openclaw)

如果你只是想快速完成飞书基础接入，优先走这条路。

相比旧版“自己在飞书开放平台里手动创建应用、手动补权限、手动开机器人能力”的流程，这条路更适合仓库里的基础篇。

## 这篇不讲什么

这篇只讲**基础接入**，不展开：

- 多个飞书机器人绑定到不同 Agent
- 多账号路由
- `accountId` 级别 binding
- `session.dmScope = "per-account-channel-peer"` 的多账号隔离
- 更复杂的配置文件直写

这些后面单独拆成高级篇。

## 前置条件

开始之前，请先确认：

1. 已经完成 OpenClaw 基础部署
2. 本机或服务器上的 Gateway 可以正常运行
3. 你有可登录的飞书账号
4. 你的 OpenClaw 版本已经包含当前的 Feishu 支持

如果你是新版 OpenClaw，官方文档说明 Feishu 插件通常已经内置，不需要单独安装。

只有在旧版或自定义安装里，才需要手动安装：

```bash
openclaw plugins install @openclaw/feishu
```

## 第一步：打开飞书官方 OpenClaw 专页

直接访问：

- [https://open.feishu.cn/page/openclaw](https://open.feishu.cn/page/openclaw)

这一步的目标很简单：

- 让飞书侧帮你完成 OpenClaw 所需的基础机器人配置
- 最终拿到一组可用的：
  - `App ID`
  - `App Secret`

这两个值就是 OpenClaw 侧配置飞书接入所需要的核心凭证。

## 第二步：在 OpenClaw 里添加飞书渠道

最推荐的方式还是官方 CLI：

```bash
openclaw channels add
```

然后按提示操作：

1. 选择 `Feishu`
2. 输入刚才拿到的 `App ID`
3. 输入 `App Secret`
4. 选择正确的域名

域名一般这样选：

- 国内飞书：`Feishu (feishu.cn)`
- 国际版：`Lark (larksuite.com)`

如果你用的是中国区飞书，大多数情况下就选 `feishu.cn`。

## 第三步：确认 Gateway 正常运行

配置完成后，先检查运行状态：

```bash
openclaw gateway status
openclaw logs --follow
```

如果需要重启让配置生效：

```bash
openclaw gateway restart
```

## 第四步：在飞书里发起第一次会话

当你第一次在飞书里给这个机器人发消息时，如果当前采用的是默认安全策略，通常会进入 pairing 流程。

OpenClaw 官方文档里，Feishu 默认就是走 `dmPolicy: "pairing"` 这类安全模式。

你在飞书里第一次发消息后，通常会看到类似提示：

```text
OpenClaw: access not configured.
Your Feishu user id: ou_xxxxxxxx
Pairing code: 8R7EXXXX
Ask the bot owner to approve with:
openclaw pairing approve feishu 8R7EXXXX
```

这时候在 OpenClaw 所在机器执行：

```bash
openclaw pairing approve feishu 8R7EXXXX
```

如果你忘了刚才的 code，也可以先看待处理列表：

```bash
openclaw pairing list feishu
```

## 第五步：发送第一条测试消息

完成 pairing 后，回到飞书里重新发一条消息，例如：

```text
你好，请确认你已经在飞书中成功接入。
```

如果机器人能正常回复，就说明基础接入已经打通。

## 最小可用配置长什么样

如果你想理解 OpenClaw 里最终大概会是什么配置，官方 Feishu 文档给出的最小形态类似这样：

```json5
{
  channels: {
    feishu: {
      enabled: true,
      dmPolicy: "pairing",
      accounts: {
        main: {
          appId: "cli_xxx",
          appSecret: "xxx",
          botName: "我的AI助手",
        },
      },
    },
  },
}
```

但基础篇不建议你一开始手改配置文件，先用 `openclaw channels add` 跑通更稳。

## 常见问题

### 1. 为什么这里不再推荐“手工建飞书应用”

因为现在有更直接的官方入口：

- [飞书 OpenClaw 专页](https://open.feishu.cn/page/openclaw)

基础篇的目标不是“学会飞书开放平台的每一个配置细节”，而是先把机器人接进来。

### 2. 配完 `App ID / App Secret` 之后，还是收不到消息

先按这个顺序检查：

1. `openclaw gateway status` 是否正常
2. `openclaw logs --follow` 里有没有 Feishu 相关错误
3. 域名是不是选错了：`feishu.cn` 还是 `larksuite.com`
4. 当前 OpenClaw 是否是新版，Feishu 支持是否已内置
5. 是否已经完成 pairing

### 3. 为什么我发消息后没有立刻拿到 pairing code

先确认两件事：

1. 你真的给机器人发了一条消息，而不是只完成了机器人创建
2. 当前 Feishu channel 的 DM 策略是 `pairing`

如果还是不确定，可以先看待处理请求：

```bash
openclaw pairing list feishu
```

### 4. 基础篇和后续高级篇的边界是什么

基础篇只解决：

- 一个飞书机器人
- 一个 OpenClaw
- 一条稳定对话链路

后续高级篇再拆这些主题：

- 多个飞书机器人绑定不同 Agent
- 飞书多账号 routing / binding
- 多 Agent 会话隔离
- 飞书高级安全与权限边界

## 参考资料

- 飞书官方 OpenClaw 专页：
  - [https://open.feishu.cn/page/openclaw](https://open.feishu.cn/page/openclaw)
- OpenClaw 官方飞书文档：
  - [https://docs.openclaw.ai/zh-CN/channels/feishu](https://docs.openclaw.ai/zh-CN/channels/feishu)
- OpenClaw 官方 channels CLI：
  - [https://docs.openclaw.ai/cli/channels](https://docs.openclaw.ai/cli/channels)
- OpenClaw 官方 pairing 文档：
  - [https://docs.openclaw.ai/zh-CN/channels/pairing](https://docs.openclaw.ai/zh-CN/channels/pairing)

## 说明

- 这篇是基础篇，优先强调“最快跑通”。
- OpenClaw 侧的操作顺序参考了官方 Feishu 文档，并结合我们团队的实际使用经验做了中文整理。

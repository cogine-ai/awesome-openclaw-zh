---
published: 2026-10-11
updated: 2026-10-11
status: "文档组合，待实测"
source_date: 2026-10-11
---

# Crabbox 临时应用实验室：边聊天边看远程界面

> 让 Agent 在临时机器上打开应用，把界面放到聊天旁边，并在需要时接管操作。

## 来源与验证状态

| 项目 | 说明 |
|---|---|
| 内容性质 | 文档组合：官方 Cloud Worker Desktop 与 Crabbox 配置指南 |
| 文档基线 | OpenClaw `v2026.10.1` 标签下的云工作机文档 |
| 查阅日期 | 2026-10-11 |
| 最近更新证据 | `v2026.9.6` 于台湾时间 2026-09-24 发布，加入当前会话旁打开临时应用的路径 |
| 本仓库验证 | 已核对配置与权限边界；未租用云机器、未验证桌面交互或释放过程 |

## 这个案例能帮你做什么

- 在一次对话中试用 Web 原型或原生 Linux 应用，直接查看它的界面。
- 保留同一台附属临时机器，在后续轮次继续调试、修改和查看结果。
- 需要人工操作时接管桌面，随后明确要求 Agent 继续。

Agent 的主工作区仍在原来的机器上。临时环境是当前会话的附属机器，所需文件必须显式复制或准备过去。

## 开始前需要什么

| 依赖 | 用途与限制 |
|---|---|
| OpenClaw 内置 Crabbox provider | 管理临时环境、远程命令与停止流程 |
| Crabbox 后端或协调器账户 | 提供机器、网络与额度；由 Crabbox 管理授权 |
| 一个有效 `cloudWorkers.profiles` 配置 | 让 Agent 可以创建环境 |
| 持久会话，且当前会话不在 sandbox 中 | 官方 `crabbox` 工具的可用条件 |
| Cloud Worker Desktop lab + `settings.desktop: true` | 打开原生桌面的额外条件 |
| 支持视觉的模型与允许 `computer` 的工具策略 | 由 Agent 观察、控制桌面 |

Web 应用可通过 Portal 显示；原生应用需要桌面能力。能看到桌面画面，不足以证明 Agent 已获得电脑控制能力。

## 最小设置

可以从官方 Homebrew 分发安装完整 Crabbox CLI：

```bash
brew install openclaw/tap/crabbox
crabbox --version
crabbox doctor
```

OpenClaw `v2026.10.1` 的 provider 要求 Crabbox `0.69.0` 或更新版本。缺失或版本不满足时，官方插件也有校验后安装托管副本的路径。

先按 [Crabbox 后端说明](https://crabbox.sh/providers/index.html) 完成账户与网络准备，再在 **Settings → Connections → Cloud workers** 新建一个 profile。

下面是根据官方字段组合的 AWS Linux 实验配置；它不包含云凭证，也不会替你配置 AWS：

```json5
{
  cloudWorkers: {
    profiles: {
      playground: {
        provider: "crabbox",
        suspendAfter: "45m",
        readyWorkers: 0,
        settings: {
          provider: "aws",
          class: "standard",
          ttl: "24h",
          idleTimeout: "60m",
          warmImage: false,
          desktop: true,
        },
      },
    },
  },
}
```

`readyWorkers: 0` 关闭这个 profile 的备用机器；`warmImage: false` 不为该配置启用镜像复用。实际规格、费用和可用区域由 Crabbox 后端决定。

原生 Linux 应用还需启用 **Cloud Worker Desktop** lab。所用 Gateway 地址必须能被工作机连接，provider 显式禁用或工具 allowlist 缺少所需工具时也不会自动恢复权限。

## 快速体验：先打开一个 Web 原型

准备一个可运行的项目路径，或者明确要求 Agent 生成一个最小示例：

```text
请使用 playground profile，在 Crabbox 打开一个待办列表 Web 原型并展示给我。
先说明要准备或复制的文件，以及启动命令。
生成最小示例时只包含新增、勾选、删除测试待办三个动作。
应用启动后在聊天旁打开 Portal，告诉我访问地址和环境 ID。
保留当前环境供下一轮修改；完成后提醒我保存结果并停止机器。
```

这是一种文档组合的原型玩法，未验证某个框架或应用。需安装的依赖、服务端口和可访问性取决于项目本身。

## 第二轮：观察桌面应用与人工接管

已有桌面环境后，可以使用官方描述的请求方式：

```text
Open this in Crabbox and show me.
请打开这个环境里已经安装的应用，展示 Desktop 面板。
先列出应用是否可用；需要安装时先给我具体方案。
```

在 Desktop 面板接管时，Agent 输入会暂停，但仍可观察画面。你完成操作后再发：

```text
我已完成手动操作，请恢复控制。
先重新观察当前界面，再从这里继续，不重放刚才中断的输入。
```

官方 `computer` 工具的 `take_control` 用于明确交接；普通点击输入不会自动夺回手动控制。

## 输出与结束流程

你应看到应用对应的 Portal 或 Desktop，而不仅是一句“已启动”。后续轮次应继续使用当前会话绑定的环境。

结束时请 Agent：保存或导出需要保留的文件，说明保存位置，停止附属机器，并报告实际清理结果。关闭面板只隐藏界面，应用与机器可能仍在运行。

如果停止失败，官方文档给出的检查入口是：

```bash
crabbox leases list
crabbox stop <lease>
```

用状态返回的精确 lease 标识替换占位符，并重新确认清理结果；未确认释放时不要认定计费已停止。

## 常见失败与边界

- **没有创建入口：** 检查 profile、当前会话是否持久、是否在 sandbox，以及 provider 和工具策略。
- **应用启动但不显示：** 核对应用服务、Portal 路由和所选 presentation；桌面需要相应 lab 与 profile。
- **找不到主工作区文件：** 附属机器不会自动同步主工作区；先复制所需文件或在远端准备项目。
- **桌面可看不可点：** 视觉模型、电脑工具、桌面 runtime 与系统权限需要同时满足。
- **macOS / Windows：** 需要专门准备的工作机镜像和活跃桌面；macOS 要求 15+ 与单独签名的 Cloud Worker app，Windows 需要桌面 launcher。不能直接套用 Linux 配置。
- **保存与成本：** 机器是临时资源，停止前保存结果；镜像、运行机器和未完成清理可能产生费用。

## 引用来源

- [固定版本：Cloud Worker Desktop](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/gateway/cloud-workers/desktop.md)
- [固定版本：Crabbox profile 配置](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/gateway/config-cloud-workers.md)
- [官方 2026.9.6 发布说明](https://docs.openclaw.ai/releases/2026.9.6)
- [Crabbox 安装与准备指南](https://github.com/openclaw/crabbox/blob/main/docs/getting-started.md)
- [Crabbox v0.74.0 发布记录：2026-10-11](https://github.com/openclaw/crabbox/releases/tag/v0.74.0)

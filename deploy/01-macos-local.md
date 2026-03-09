# macOS 本地部署（推荐）

这篇文档适合：

- 你有一台自己的 Mac
- 你想先把 OpenClaw 在本地跑起来
- 你希望最快看到 Web UI 和第一条回复

这也是最推荐的新手路径。

![OpenClaw 安装界面](../assets/deploy/openclaw-installation-interface.png)

## 这篇会完成什么

完成后你应该能做到：

- 在 Mac 上安装 OpenClaw CLI
- 跑完初始化向导
- 启动本地 Gateway
- 在浏览器打开 `http://127.0.0.1:18789/`
- 发送第一条测试消息

## 系统要求

- macOS 12 或更高版本
- 建议 8 GB 以上内存
- 建议 10 GB 以上可用空间
- 可以联网

说明：

- 如果你只是跑 CLI + Gateway，不需要先手动装 Node，官方安装器会处理。
- 如果你后面要折腾源码构建或 macOS 配套应用，再考虑 Xcode Command Line Tools。

## 路线总览

主线只有 4 步：

1. 安装 OpenClaw
2. 跑初始化向导
3. 启动并验证 Gateway
4. 在浏览器测试

## 第 1 步：安装 OpenClaw

打开终端，执行：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

这是官方推荐安装方式。它会：

- 检查系统环境
- 安装或修复 Node 22+
- 安装 `openclaw` CLI
- 在安装完成后进入新手引导流程

如果你想跳过引导，稍后自己跑：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
```

## 第 2 步：确认安装成功

执行：

```bash
openclaw --version
openclaw doctor
```

如果能输出版本号，并且 `doctor` 没有致命错误，就可以继续。

## 第 3 步：运行初始化向导

如果安装时没有自动进入向导，执行：

```bash
openclaw onboard --install-daemon
```

推荐按下面的思路选：

- Gateway 位置：`local`
- 安装后台服务：`yes`
- 运行时：优先 `Node`
- 模型认证：按你的实际情况选择
- 聊天渠道：如果你还没准备好，先跳过，后面再接

这一步完成后，OpenClaw 会写入本地配置，并把 Gateway 作为后台服务装好。

## 第 4 步：验证 Gateway 是否正常

先看状态：

```bash
openclaw gateway status
openclaw status
openclaw health
```

再打开本地仪表盘：

```bash
openclaw dashboard
```

如果命令没有自动打开浏览器，也可以手动访问：

```text
http://127.0.0.1:18789/
```

如果控制 UI 要求输入令牌，按照命令行提示粘贴即可。

## 第 5 步：发送第一条测试消息

在 Web UI 中直接发一条最简单的消息：

```text
你好，请确认你已经正常运行，并告诉我当前你能做什么。
```

你只需要确认两件事：

- 能收到回复
- 回复不是报错或“未配置认证”

如果你看到“未配置认证”，回到：

```bash
openclaw onboard
```

把模型认证补完整。

## 日常常用命令

```bash
openclaw --version
openclaw doctor
openclaw status
openclaw health
openclaw dashboard
openclaw gateway status
```

如果你需要重新配置：

```bash
openclaw configure
```

## 建议的下一步

部署成功后，不要立刻折腾多渠道和复杂自动化。

先做这 3 件事：

1. 在 Web UI 里确认能稳定对话
2. 只接 1 个聊天入口
3. 跑 1 个最简单的场景

然后再回到：

- [5分钟快速上手](../quickstart/00-5min-quickstart.md)
- [7天上手路径](../quickstart/01-7day-path.md)

## 常见问题

### 1. 终端里提示找不到 `openclaw`

先执行：

```bash
node -v
npm -v
echo "$PATH"
```

如果 npm 全局路径没有进入 `PATH`，优先重新打开终端；如果还不行，再按官方安装文档排查。

### 2. `doctor` 正常，但浏览器打不开 `127.0.0.1:18789`

先检查：

```bash
openclaw gateway status
openclaw health
```

如果 Gateway 没跑起来，重新执行：

```bash
openclaw onboard --install-daemon
```

### 3. 我一定要先装 macOS 配套应用吗？

不用。

这篇文档的目标只是让你把 CLI + Gateway 跑起来。macOS 菜单栏应用是后续增强，不是本地部署的前置条件。

## 上游参考

- OpenClaw 官方中文： [入门指南](https://docs.openclaw.ai/start/getting-started)
- OpenClaw 官方中文： [安装](https://docs.openclaw.ai/install)
- OpenClaw 官方中文： [macOS 应用](https://docs.openclaw.ai/platforms/macos)
- OpenClaw 官方中文： [配置](https://docs.openclaw.ai/gateway/configuration)
- 中文开源教程： [xianyu110/awesome-openclaw-tutorial - 环境搭建](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/01-basics/02-installation.md)

截图说明：

- 本文顶部截图整理自上游开源教程仓库 `xianyu110/awesome-openclaw-tutorial`

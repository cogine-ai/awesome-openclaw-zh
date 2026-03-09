# Linux VPS 通用部署

这篇文档解决的是“通用 Linux 服务器怎么把 OpenClaw 跑起来”，不是某一家云厂商的控制台教程。

它适合：

- 你希望 OpenClaw 24 小时在线
- 你已经有一台 Linux VPS，或者准备去买
- 你后面还想接飞书、钉钉、企业微信、QQ

后续阿里云 / 腾讯云 / 火山引擎的差异，只在各自的“控制台差异篇”里补，不塞进这篇。

## 先说推荐方案

如果你是第一次在 VPS 上部署 OpenClaw，建议用这个组合：

- 系统：Ubuntu 24.04 LTS
- 规格：2 核 2 GB 内存起步
- 运行时：Node
- 访问方式：SSH 隧道访问 `127.0.0.1:18789`
- 对外暴露策略：默认不要把 Gateway 直接暴露到公网

这套组合最接近上游官方默认路径，也最容易长期维护。

## 这篇会完成什么

完成后你应该能做到：

- 在 Linux VPS 上安装 OpenClaw
- 跑完初始化向导并安装后台服务
- 确认 Gateway 正常运行
- 从你自己的电脑通过 SSH 隧道访问控制台
- 在浏览器打开本地映射的 `http://127.0.0.1:18789/`

## 机器要求

最低建议：

- Ubuntu 22.04 / 24.04
- 2 vCPU
- 2 GB RAM
- 20 GB 磁盘
- 可用公网 IP

额外建议：

- 只开放 `22` 端口给 SSH
- 不把 `18789` 直接公开到公网
- 使用独立用户运行 OpenClaw

## 第 1 步：登录服务器并更新系统

通过 SSH 登录：

```bash
ssh <user>@<your-server-ip>
```

更新系统：

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git wget
```

## 第 2 步：安装 OpenClaw

官方推荐安装器：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

如果你想先只安装，不马上跑引导：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
```

安装后检查：

```bash
openclaw --version
openclaw doctor
```

## 第 3 步：运行初始化向导并安装服务

执行：

```bash
openclaw onboard --install-daemon
```

建议按这个思路选择：

- Gateway 位置：`local`
- 安装后台服务：`yes`
- 运行时：`Node`
- 渠道：暂时可以先不绑
- 认证：按你自己的模型供应商完成

完成后再检查一次：

```bash
openclaw gateway status
openclaw status
openclaw health
```

## 第 4 步：不要直接暴露 18789，先用 SSH 隧道

这是这篇文档最重要的默认建议。

在 VPS 上，Gateway 默认最好只监听本机回环地址。你在自己电脑上通过 SSH 隧道访问它，而不是把控制台直接公开到公网。

在你的本地电脑执行：

```bash
ssh -N -L 18789:127.0.0.1:18789 <user>@<your-server-ip>
```

保持这个终端窗口不要关。

然后在你本地电脑浏览器打开：

```text
http://127.0.0.1:18789/
```

这样你访问到的其实是远端 VPS 上的 Gateway。

## 第 5 步：在浏览器里验证

打开 UI 后，发送一条最简单的测试消息：

```text
你好，请确认你已经在 Linux VPS 上正常运行。
```

只要能稳定回复，这条主线就算打通。

## 第 6 步：日常维护命令

```bash
openclaw --version
openclaw doctor
openclaw status
openclaw health
openclaw gateway status
openclaw dashboard
```

如果需要重新配置：

```bash
openclaw configure
```

## 第 7 步：升级与回滚的基本原则

如果你要长期跑，升级前至少先做两件事：

1. 备份 `~/.openclaw/`
2. 记录当前版本号

升级方式优先参考官方安装与更新文档，不建议在生产 VPS 上频繁做无计划升级。

## 可选路线：Docker

如果你明确想做容器化部署，可以走官方 Docker 路线。

适合用 Docker 的情况：

- 你要隔离环境
- 你更习惯 Compose
- 你后面还会把它接进自己的容器体系

不适合用 Docker 的情况：

- 你只是想最快跑通
- 你不想额外理解镜像、卷、Compose、容器网络

官方 Docker 文档入口：

- [Docker](https://docs.openclaw.ai/install/docker)

对大多数第一次部署的用户来说，先用本文的“安装器 + SSH 隧道”路线更合适。

## systemd 说明

上游文档默认会把 OpenClaw 安装为 systemd 用户服务。

如果你执行过：

```bash
openclaw onboard --install-daemon
```

通常不需要你自己手写 unit 文件。

只有在这些情况下，才考虑自己管 systemd：

- 你要跑多个 profile
- 你在做团队共享服务器
- 你要精细控制重启策略

## 常见问题

### 1. 我能不能把 18789 直接开到公网？

不建议。

默认最安全的姿势是：

- Gateway 保持 loopback
- 你通过 SSH 隧道访问

只有你明确知道自己在做什么，才考虑公网暴露，并且必须同时配好认证。

### 2. 小机器会不会很慢？

会。

低配 VPS 可以先跑起来，但如果你后面要接更多渠道、更多模型、更多自动化，2C2G 只是起步，不是长期上限。

### 3. 我已经有一台云服务器，能不能直接装？

可以。

这篇本来就是“存量 VPS 通用部署基线”，核心不是买哪家云，而是：

- Ubuntu
- OpenClaw 安装器
- Gateway 后台服务
- SSH 隧道访问

## 这篇之后应该接什么

这篇打通以后，再去看：

- 阿里云控制台差异篇
- 腾讯云控制台差异篇
- 火山引擎控制台差异篇
- 飞书 / 钉钉 / 企业微信 / QQ 接入篇

## 上游参考

- OpenClaw 官方中文： [Linux 应用](https://docs.openclaw.ai/platforms/linux)
- OpenClaw 官方中文： [入门指南](https://docs.openclaw.ai/start/getting-started)
- OpenClaw 官方中文： [安装](https://docs.openclaw.ai/install)
- OpenClaw 官方中文： [远程访问](https://docs.openclaw.ai/gateway/remote)
- OpenClaw 官方英文： [VPS Hosting](https://github.com/openclaw/openclaw/blob/main/docs/vps.md)
- OpenClaw 官方中文： [Docker](https://docs.openclaw.ai/install/docker)
- 中文开源教程： [xianyu110/awesome-openclaw-tutorial - 环境搭建](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/01-basics/02-installation.md)
- 中文文章： [腾讯云开发者 - 手把手教你在云上搭建和使用 OpenClaw](https://cloud.tencent.com/developer/article/2625605)

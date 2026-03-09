# 安装与部署入口（小白版）

这页现在只做一件事：

- 帮你快速跳到正确的部署文档

如果你是第一次来本仓库，优先看：

- [部署与安装中心](../deploy/README.md)

## 按你的设备或场景选

### 有 Mac

- [macOS 本地部署](../deploy/01-macos-local.md)

适合：

- 个人使用
- 想先最快跑通
- 希望本地体验最好

### 用 Windows

- [Windows 部署（WSL2 主线）](../deploy/02-windows.md)

适合：

- 日常主力机是 Windows
- 希望按官方更稳的路线安装
- 能接受在 WSL2 里运行 OpenClaw

### 想 24 小时在线

- [Linux VPS 通用部署](../deploy/03-linux-vps-baseline.md)

适合：

- 没有 Mac
- 想让 OpenClaw 常驻运行
- 后续要接飞书、钉钉、企业微信、QQ

## 部署完成后看什么

按这个顺序继续：

1. [部署后 5 分钟快速体验](../quickstart/00-5min-quickstart.md)
2. [7 天上手路径](../quickstart/01-7day-path.md)
3. [模型、渠道、技能怎么选](./02-model-channel-skill-guide.md)
4. [低成本稳定运行（精简版）](../playbooks/01-low-cost-stable-run.md)

## 官方入口

- [OpenClaw Docs](https://docs.openclaw.ai/)
- [Getting Started](https://docs.openclaw.ai/start/getting-started)
- [Install](https://docs.openclaw.ai/install)

## 一句建议

- 你是新手：先本地或单机部署，先用 Web UI 跑通第一条消息
- 你要长期跑：再迁移到 VPS
- 你要团队使用：先把部署和权限边界跑稳，再考虑多渠道接入

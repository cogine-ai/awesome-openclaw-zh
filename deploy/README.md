# 部署与安装中心

如果你还没有装好 OpenClaw，请先从这里开始。

本目录只解决两件事：

- 把 OpenClaw 装起来
- 把 Gateway 跑起来并能在浏览器里验证成功

渠道接入（飞书、钉钉、企业微信、QQ）后续单独放到 `channels/`。

## 先选你的路线

- 有 Mac：看 [macOS 本地部署](./01-macos-local.md)
- 用 Windows：看 [Windows 部署（WSL2 主线）](./02-windows.md)
- 想 24 小时在线：看 [Linux VPS 通用部署](./03-linux-vps-baseline.md)

## 这几篇文档的关系

- `01-macos-local.md`：适合个人本地使用，体验最好。
- `02-windows.md`：以 WSL2 + Ubuntu 为主线，兼容性更稳。
- `03-linux-vps-baseline.md`：先把“通用 Linux 基线”讲清楚，后续再补阿里云 / 腾讯云 / 火山引擎差异篇。

## 完成部署后的下一步

部署成功后，继续按这个顺序走：

1. 绑定 1 个聊天入口
2. 跑通第一个场景
3. 回到 [5分钟快速上手](../quickstart/00-5min-quickstart.md)
4. 再看 [7天上手路径](../quickstart/01-7day-path.md)

## 说明

- 这几篇文档以 OpenClaw 官方文档为命令基线，结合开源中文教程补充小白叙述和截图思路。
- 不同云厂商的控制台差异，后续单独补充，不塞进这 3 篇通用文档里。

# Windows 部署候选资料卡

## 推荐等级

推荐作为主来源，但发布前要做官方校验。

## 主来源

- 中文教程： [xianyu110/awesome-openclaw-tutorial - 第2章：环境搭建](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/01-basics/02-installation.md)
- 重点小节：`Windows本地部署`

## 为什么它值得参考

- 同时给了两条路线：`WSL2 + Ubuntu` 和 `PowerShell 原生部署`。
- 对中文用户真正关键的步骤都写到了：启用 WSL2、安装 Ubuntu、安装 Node.js、安装 OpenClaw、端口访问、初始化向导。
- 还有 Windows 常见命令速查和常见问题，适合你后续拆成“主流程 + 故障排查”。

## 辅助校验源

- OpenClaw 官方： [Windows](https://docs.openclaw.ai/platforms/windows)
- OpenClaw 官方： [Getting Started](https://docs.openclaw.ai/start/getting-started)
- OpenClaw 官方： [Plugin](https://docs.openclaw.ai/tools/plugin)

## 适合你怎么用

- 你自己的标准库建议优先写 `WSL2 + Ubuntu` 路线，把它定义成主线安装方式。
- `PowerShell 原生部署` 可以保留，但更适合作为备选方案，而不是推荐路径。
- 如果你想做“给小白”的版本，Windows 文章最好单独配一张架构图：`Windows -> WSL2 Ubuntu -> OpenClaw Gateway -> 浏览器 / 渠道桥接`。

## 主要缺口

- 文中包含部分插件安装示例，但这些不属于你当前这篇“部署”文章的重点，后面应拆到渠道接入文档。
- 某些插件名和配置命令更像社区方案，不宜当成“官方默认标准”。
- Windows 端口访问、服务守护、开机启动等细节发布前需要用官方文档和本地实测确认。

## 我的判断

如果你要先做一篇 `Windows 部署`，这篇可以直接作为中文底稿，但你自己的版本应更克制，聚焦 `WSL2 主线`，少讲插件，多讲安装与验证。

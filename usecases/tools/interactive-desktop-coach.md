---
title: "让 Agent 举起教学卡：人来选择，桌面回传答案"
description: "把操作说明拆成三张桌面教学卡，引导读者看成果、选路线、准备输入。"
category: "工具开发"
published: "2026-10-27"
updated: "2026-10-27"
showcase:
  verification: script-reproduced
  platforms: [macos]
  account: none
  cost: local-free
  artifactPath: "assets/examples/interactive-desktop-coach/index.html"
  artifactLabel: "查看三步教学卡"
  previewPath: "assets/examples/interactive-desktop-coach/preview.svg"
  bundlePath: "assets/bundles/interactive-desktop-coach-2026-10-27.zip"
  testedAt: "2026-10-27"
  testedVersion: "bigarrow 0.5.1 / 4ad1ce1d82368139b2ceec7b2e29ade837acc722"
  beginner: false
---

# 让 Agent 举起教学卡：人来选择，桌面回传答案

> Agent 需要你看一份成果、选择一条路线或确认运行条件时，可以把问题放到桌面卡片上，再读取你的实际回答。

## 先看成果

[打开三步教学卡预览](../../assets/examples/interactive-desktop-coach/index.html)：看经验卡成果 → 选择离线重放或真实访谈 → 核对公开输入与 Python 条件。

预览由三份原创公开 JSON 和 Bigarrow 实际 `--dry-run` 输出生成。它是自含 HTML，展示问题和选项；没有模拟用户作答，也不是 macOS 截图。你可以下载相同输入，在自己的 Mac 上弹出真正的桌面卡。

## 这次新在哪里

[Bigarrow v0.5.1](https://github.com/franzenzenhofer/big-arrow-on-the-screen/releases/tag/v0.5.1) 于 2026-10-26 发布，本例固定提交 [`4ad1ce1d82368139b2ceec7b2e29ade837acc722`](https://github.com/franzenzenhofer/big-arrow-on-the-screen/tree/4ad1ce1d82368139b2ceec7b2e29ade837acc722)，MIT 许可。

它是社区 macOS 工具，可以从能运行本地命令的 Agent 调用；不是 OpenClaw 官方插件。除了箭头，现在还可用 `card` 展示复制内容、选择题、输入框和检查项，再用 `wait` 读取回答。v0.5.1 的重要边界是：有问题的卡在全部回答后关闭，`--keep` 可保留；纯展示卡需要点击 X 或明确关闭。卡片没有 `--duration`，打字回 Agent 或普通 `stop --all` 不会顺手关掉卡片。

这很适合新手陪练、公开工具演示和操作交接。读者可以一边看卡片，一边选择下一步。

## 前置条件

| 体验 | 要求 | 账号与费用 |
|---|---|---|
| 看 HTML 或重放本例记录 | 浏览器；离线重放需 Python 3.10+ | 无需账号、模型或网络 |
| 构建并解析真实卡片 | macOS 14+、Swift 6 的 Command Line Tools 或 Xcode，首次获取源码和 Swift 依赖需联网 | Bigarrow 本地免费，无账号 |
| 真正显示与回答桌面卡 | 已构建的 Bigarrow，同一 Mac 的可交互桌面会话 | 本例不含登录、秘密、权限变更或自动点击 |
| 让 OpenClaw 发起教学卡 | 自己已配置的 Agent，允许执行明确的本地 CLI | Agent 模型费用按自己的配置 |

本例使用 Bigarrow 的卡片功能。若继续使用按元素名称定位箭头，需要为宿主终端配置辅助功能权限。

## 不用模型，先离线重放

在本仓库根目录运行：

```bash
python3 assets/examples/interactive-desktop-coach/reproduce.py --verify
```

它核对三份输入的 SHA-256、对应真实 CLI 输出及 HTML 的可重现性，不重新启动 Bigarrow，不打开桌面，不伪造回答。要生成独立副本：

```bash
python3 assets/examples/interactive-desktop-coach/reproduce.py --out /tmp/desktop-coach-replay
```

输出目录必须尚不存在；打开其中的 `index.html` 即可。Python 重放器是本项目原创适配，保留的 Bigarrow 输出见 [dry-run-results.json](../../assets/examples/interactive-desktop-coach/dry-run-results.json)。

## 用真实固定版本检查输入

以下命令获取上游并在指定目录构建，不安装到全局，也不安装 Agent Skill：

```bash
git clone https://github.com/franzenzenhofer/big-arrow-on-the-screen.git /tmp/bigarrow-coach-source
git -C /tmp/bigarrow-coach-source checkout --detach 4ad1ce1d82368139b2ceec7b2e29ade837acc722
swift build --package-path /tmp/bigarrow-coach-source -c release
swift test --package-path /tmp/bigarrow-coach-source --filter CardDocumentTests
python3 assets/examples/interactive-desktop-coach/reproduce.py \
  --cli /tmp/bigarrow-coach-source/.build/release/bigarrow --verify
```

最小卡片只需一个标题和问题：

```json
{
  "title": "这次先尝试哪条路线？",
  "rows": [{"type": "choice", "id": "route", "items": [
    {"id": "offline", "label": "离线重放"},
    {"id": "interview", "label": "真实访谈"}
  ]}]
}
```

三份完整输入：[看成果](../../assets/examples/interactive-desktop-coach/cards/01-open.json)、[选路线](../../assets/examples/interactive-desktop-coach/cards/02-choose.json)、[查条件](../../assets/examples/interactive-desktop-coach/cards/03-check.json)。

## 亲自弹出一张教学卡

下面的命令会弹出桌面卡片，请在自己的 Mac 前运行：

```bash
python3 assets/examples/interactive-desktop-coach/reproduce.py \
  --cli /tmp/bigarrow-coach-source/.build/release/bigarrow --desktop --step 1
```

命令先检查三张卡，再启动第 1 张并返回 `pid`。继续使用同一个已构建二进制的显式路径读取回答；本例不要求全局安装：

```bash
/tmp/bigarrow-coach-source/.build/release/bigarrow wait <pid> --timeout 30
```

第 2、3 张分别使用 `--step 2` 与 `--step 3`。不要把文档里的 `<pid>` 原样执行，替换为刚返回的数字；如果你换了源码目录，也要同步替换二进制路径。

回答时 exit 0；点击 X 且没有回答时 exit 1；超时的 JSON 为 `pending`，不是完成。只关闭自己这张卡时使用同一个路径：

```bash
/tmp/bigarrow-coach-source/.build/release/bigarrow stop --pid <pid>
```

收到回答后，继续执行对应步骤，并查看产物。版本检查和 dry-run 各最多等待 20 秒，超时可先检查二进制路径和输入。

供 Agent 的最小提示词：

```text
我要做公开经验卡教程。先核对 bigarrow --version 是 0.5.1；
用现成三份 card JSON dry-run，不要操作我的窗口或读取秘密。
在我正在 Mac 前做这份教程时，每次只显示一张卡，记录实际 pid，再 wait 该 pid。
收到 pause / X / pending 时停止推进；只有收到实际回答才继续。
所有勾选只是我的自报确认，仍需核对实际命令结果。
不要安装全局 Skill、设置 hooks，或把测试输入当成我本人的经历。
```

## 常见问题

版本不符或卡片解析失败时，先检查二进制版本与 JSON 字段。输出目录已存在时，换一个新目录；桌面卡没有回传答案时，确认卡片仍打开，再查看 `wait` 的返回状态。

## 来源与许可

- [固定版本 README](https://github.com/franzenzenhofer/big-arrow-on-the-screen/blob/4ad1ce1d82368139b2ceec7b2e29ade837acc722/README.md)
- [作者 Skill 与调用约定](https://github.com/franzenzenhofer/big-arrow-on-the-screen/blob/4ad1ce1d82368139b2ceec7b2e29ade837acc722/skill/big-arrow/SKILL.md)
- [真实 card CLI 实现](https://github.com/franzenzenhofer/big-arrow-on-the-screen/blob/4ad1ce1d82368139b2ceec7b2e29ade837acc722/Sources/bigarrow/CardCommand.swift)
- [上游 MIT 许可副本](../../assets/examples/interactive-desktop-coach/LICENSE-upstream.txt)

由 Cogine 团队整理三步教学输入、重放脚本和 HTML 预览。
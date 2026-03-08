# AionUi 桌面协作与远程救援（OpenClaw Cowork）

> 把 OpenClaw 放进可视化桌面协作界面里，并在离开电脑时继续远程使用和远程修复。

## 这个案例能帮你做什么

- 用桌面 Cowork 界面直接看到 OpenClaw 读写文件、执行命令和浏览网页。
- 人不在机器旁时，仍可通过 Telegram / WebUI 进入同一个实例处理任务。
- OpenClaw 连不上或配置异常时，可借助 AionUi 内置的 OpenClaw deployment expert 做远程救援。

## 你需要的 Skills（按类型）

| 类型 | Skill / 服务 | 用途 | 来源 |
|---|---|---|---|
| 外部应用 | `AionUi` | 提供桌面 Cowork 工作台，并把 OpenClaw 作为一等 agent 接入 | iOfficeAI/AionUi |
| 本机工具 | `OpenClaw` | 作为被 AionUi 调用和协作的核心 agent | OpenClaw |
| AionUi 内置 | `OpenClaw Setup` assistant | 协助安装、接入和检查 OpenClaw | AionUi |
| AionUi 内置 | `OpenClaw deployment expert` | 用于远程诊断、运行 `openclaw doctor`、修配置和重启 gateway | AionUi |
| 远程通道（按需） | `Telegram / WebUI / Lark / DingTalk` | 从外部设备接入同一个 AionUi / OpenClaw 实例 | AionUi |

## 快速体验版（先跑一轮）

1. 先安装 AionUi，并确认本机已有 OpenClaw。
2. 先在本机确认 AionUi 能自动识别 OpenClaw。
3. 预演一次“OpenClaw 连不上”的排查流程，本轮先不改配置。

```text
你是我的 OpenClaw 助手。
请帮我做一次“AionUi 桌面协作与远程救援”的预演：
1. 检查当前机器上的 OpenClaw 是否已被 AionUi 识别。
2. 如果没有识别，列出缺失的安装或配置项。
3. 模拟一次 OpenClaw 无法连接时的排查流程：先检查什么，什么时候运行 `openclaw doctor`，什么时候需要修配置或重启 gateway。
4. 本轮先不要改配置或重启服务，只输出诊断结论和下一步。
```

## 稳定自动版（可长期运行）

### 1) 一次性准备命令

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon   # optional: daemon for 24/7
```

### 2) 推荐流程

1. 安装 AionUi 后，创建一个 Cowork session，并选择 OpenClaw。
2. 把 Telegram / WebUI / Lark / DingTalk 接到同一个 AionUi 实例上，方便离开电脑后继续操作。
3. 一旦 OpenClaw 出现异常，优先用 OpenClaw deployment expert 做远程排查：运行 `openclaw doctor`、检查配置、必要时重启 gateway。
4. MCP 只在 AionUi 配一次，再同步给 OpenClaw 和其他 agent，减少多端重复配置。
5. 需要 24/7 任务时，再启用 AionUi cron 去跑定时任务。

## 成功标准

- [ ] AionUi 能稳定识别并运行 OpenClaw。
- [ ] 远程通道能接入同一个实例，而不是多套分离环境。
- [ ] OpenClaw 异常时，可以通过 AionUi 远程完成诊断与恢复。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/aionui-cowork-desktop.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/aionui-cowork-desktop.md)

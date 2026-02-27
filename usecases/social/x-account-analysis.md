# X 账号分析

> 把“只看播放和点赞数字”升级为“内容质量与风格模式分析”。

## 这个案例能帮你做什么

- 找出你高互动帖子的共性模式与低表现帖的问题点。
- 聚焦“内容质量与选题匹配”，而不仅是后台统计数字。
- 用 OpenClaw 做定制化分析，替代高价订阅分析工具。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（预置/可安装） | `bird` | 读取 X 账号内容并分析 | 源文说明（`clawhub install bird`） |
| 凭证 | `auth-token` / `ct0` | 登录态访问账号内容 | X Cookie |

## 快速体验版（先跑一轮）

先确认 `bird` 可用：

```bash
clawhub install bird
```

## 稳定自动版（可长期运行）

### 1) 准备账号与安全隔离（原文流程）

1. 确认 Bird skill 工作正常。
2. 建议为 ClawdBot 使用单独账号做隔离。
3. 在 Chrome/Brave 登录 x.com，并提供 `auth-token`、`ct0`。

### 2) 让 OpenClaw 开始分析（原文）

- 拉取最近 N 条推文。
- 围绕你的目标提问，例如：
  - 哪类主题更容易高互动？
  - 为什么同样类型内容波动很大？
  - 哪些表达模式值得保留/避免？

## 成功标准

- [ ] 能稳定拉到最近推文样本并完成分析。
- [ ] 输出包含可执行的内容优化建议。
- [ ] 后续复盘可对照“高分帖模式”持续迭代。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/x-account-analysis.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/x-account-analysis.md)

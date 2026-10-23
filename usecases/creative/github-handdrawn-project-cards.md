---
published: 2026-10-23
updated: 2026-10-23
---

# 把 GitHub 公开项目变成三张手绘风战报

> 不用手填数字：把一个公开仓库的真实数据，变成开源小城、语言配比和提交节奏三张 SVG。

## 先看成果

[打开 Cogine 项目战报](../../assets/examples/github-cards/index.html)。本例统计范围是 **单仓库公开快照：`cogine-ai/awesome-openclaw-zh`**，不代表 Cogine 组织或任何个人的全部贡献。

| 产物 | 能看到什么 | 数据边界 |
|---|---|---|
| [开源小城 SVG](../../assets/examples/github-cards/city.svg) | 真实仓库变成一栋楼，目录显示提交数、存储量和 Star | 单项目不作跨项目排名；楼高是作者设计的组合分数，不是增长率 |
| [语言配比 SVG](../../assets/examples/github-cards/languages.svg) | GitHub 识别出的代码语言及字节占比 | 不是 Markdown 正文占比，也不是案例类别分布 |
| [提交节奏 SVG](../../assets/examples/github-cards/rhythm.svg) | 默认分支最近提交按星期和 UTC 小时分布 | 包括合并提交，不代表人数、工时或个人贡献日历 |

2026-10-23 21:08:51（Asia/Taipei；原始 UTC 为 `2026-10-23T13:08:51Z`）采集到 **240 Stars、37 Forks、默认分支累计 49 条提交**，提交时间样本也是 49 条。语言 API 返回 HTML 42,119 字节、Python 8,673 字节。页面没有自动刷新，不用固定快照推断当前数字或增长速度。

## 来源与验证说明

- 类型：上游工具组合 + Cogine 的公开项目数据适配。
- 上游：[Michael Oogwu 的 openclaw-profile-cards](https://github.com/mgkvibez/openclaw-profile-cards)，固定提交 [`bc589498e4cb72dbe29de5121f5009eb95b5a22c`](https://github.com/mgkvibez/openclaw-profile-cards/tree/bc589498e4cb72dbe29de5121f5009eb95b5a22c)，MIT 许可。该项目创建于 2026-10-18，2026-10-23 查询为 2 Stars、0 Forks，属于新颖小项目，不能称为热门或增长迅猛。
- 已运行：先在临时目录使用作者自带 fixture 跑原版 CLI，生成全部 13 张卡；当前提交实际运行的 **29 项 unittest 通过**。作者 fixture 含作者自己的资料，只用于验证，未复制到本仓库。
- 本项目样例：通过 `gh api graphql` 只读取得指定公开仓库数据，再调用原始 `city`、`languages`、`rhythm` 三个渲染器，实际生成本页 SVG。原始数据和复现脚本随样例提供，SVG 不靠手填指标。
- 适配范围：保留上游图形与统计计算；仅把全账户范围说明改为单仓库，把“每小时生成”改为固定快照，并添加来源元数据。未伪造个人画像、全年贡献日历或历史增长。
- 尚未做：未在真实 OpenClaw 会话中安装 Skill 或端到端执行；未启用自动刷新、提交或发布。脚本执行验证与 Agent 执行验证分别说明。

与已有动态仪表板、GitHub 趋势选题案例的区别：这里交付可以嵌进 README、下载和传播的静态图卡；不搭建在线分析系统，也不把项目排名当作选题结论。

## 前置条件与成本

| 条件 | 要求 |
|---|---|
| Python | 3.10+；复现脚本和上游渲染器只使用标准库 |
| 源码访问 | 默认从 GitHub 下载固定提交的渲染器；临时源码执行后自动清理 |
| 刷新数据 | 安装并登录 GitHub CLI `gh`，能读取指定公开仓库；凭证由 `gh` 自己管理，脚本不读取或打印 Token |
| OpenClaw 可选接入 | 能运行本地 Python、读取工作区文件的 Agent；[上游 Skill](https://github.com/mgkvibez/openclaw-profile-cards/blob/bc589498e4cb72dbe29de5121f5009eb95b5a22c/SKILL.md) 是个人主页流程，使用本例时需明确改成单仓库范围 |
| 成本 | 本次生成图卡未调用付费模型。请按自己的 GitHub API 限额及 Agent 模型计费评估 |

原版 `python -m cards.render --login <用户名>` 使用 GraphQL `user(login: …)`，不能把组织名称直接当个人账户。它还会尝试更新当前目录的 README、读取本地 `history.jsonl`；`ubuntu.svg` 有作者个人示例文案。本例因此使用独立数据适配器与三张适用卡片，不直接发布原版 CLI 的整套个人画像。

## 快速体验版

先[下载或查看现成页面](../../assets/examples/github-cards/index.html)，无需登录或提供 Token。要重做这张固定快照，在本仓库根目录执行：

```bash
python3 assets/examples/github-cards/reproduce.py
python3 -m http.server 8765 --bind 127.0.0.1
```

在浏览器打开 `http://127.0.0.1:8765/assets/examples/github-cards/`。默认命令复用已提交的公开数据，不请求新的项目指标；首次下载固定上游源码仍需联网。按 `Ctrl+C` 停止本地服务器。

需要重新采集当前公开数据时，先确认 `gh auth status` 正常，再执行：

```bash
python3 assets/examples/github-cards/reproduce.py --refresh
```

该命令会替换此样例的公开数据、三张 SVG 和展示页面，**不会推送 Git、安装定时任务或发布到网站**。刷新后应以新数据里的 `fetched_at` 为准；正文引用的 10-23 数字不会被脚本自动改写。

想复用已有的固定上游源码、免去再次下载，可先在单独目录准备：

```bash
git clone https://github.com/mgkvibez/openclaw-profile-cards.git /tmp/profile-cards-source
git -C /tmp/profile-cards-source checkout bc589498e4cb72dbe29de5121f5009eb95b5a22c
python3 assets/examples/github-cards/reproduce.py --upstream-dir /tmp/profile-cards-source
```

复现脚本会核对该 checkout 的 HEAD。不要把作者的历史数据文件当成本项目的历史，也不要直接将作者 fixture 的输出发布成自己的战报。

## 可以直接发给 Agent 的请求

```text
请复现 github-handdrawn-project-cards 案例。
只使用这个项目：cogine-ai/awesome-openclaw-zh，且必须确认是公开仓库。
先查看已提交的 public-repositories.json 和 reproduce.py。
默认复用快照生成三张 SVG 和 gallery；如我明确要求刷新，再通过 gh 只读 API 采集。
使用固定上游提交 bc589498e4cb72dbe29de5121f5009eb95b5a22c 的原始渲染器。
说明统计范围、采集时间、样本条数；不要混入组织或个人全部贡献。
不得读取私人仓库、Token、邮件或本地其他项目；不得自动提交、推送或启用定时刷新。
完成后核对 SVG 的数字和输入一致，并打开 gallery 看三张图是否正常显示。
```

## 输入、产物与成功标准

- [公开 API 快照](../../assets/examples/github-cards/public-repositories.json)：仓库可见性、Star/Fork、语言字节、默认分支提交数及最多 100 条提交时间；不包含作者姓名、邮箱、提交正文或凭证。
- [复现脚本](../../assets/examples/github-cards/reproduce.py)：只采集白名单中的公开项目，并拒绝非公开或范围不符的数据。图形来自固定上游渲染器，原始仓库源码不留在工作区。
- [上游 MIT 许可](../../assets/examples/github-cards/LICENSE-upstream.txt)：保留 Michael Oogwu 的版权声明；展示页也标明作者与适配范围。

- [x] 作者 fixture 原版 CLI 实际生成 13 张卡；29 项上游测试通过。
- [x] 公开项目数据实际进入三个渲染器，产出 SVG 和可浏览 gallery。
- [x] 三张 SVG 可作为 XML 解析，不含脚本、外部图片、第三方字体、令牌或本地临时路径。
- [ ] 使用者在自己的 OpenClaw 会话执行并验证；此项仍待真实安装测试。

如果 `gh` 未登录或 API 失败，脚本会停止，不用空数据替代成功结果。仓库变为非公开、返回了错误项目或语言分页不完整，也会停止。已有固定快照可以继续查看；它不会因为刷新失败而变成“当前数据”。

长项目名可能被上游城市图缩写，完整名称以页面数据表为准。语言图只统计 GitHub 的代码语言字节；文档项目的 Markdown 内容不会自动变成代码占比。

## 延伸玩法

以下是待验证的原创选题：

- 为公开项目做“发布前后两张卡”，保留相同范围与采集时间后再比较差异。
- 把一周最重要的三次实际改进配在图卡旁，形成有作品入口的开源周报。
- 对多个**明确公开且获准纳入**的项目做开源小城；不要把缺少数据的项目补成零，也不直接展示私有项目名称。

先人工刷新和检查产物，再单独决定是否需要持续更新。此案例没有自动开启 GitHub Actions 或任何周期任务。

## 引用来源

- [固定上游 README 与作者示例](https://github.com/mgkvibez/openclaw-profile-cards/tree/bc589498e4cb72dbe29de5121f5009eb95b5a22c)
- [原版 CLI 与输出清单](https://github.com/mgkvibez/openclaw-profile-cards/blob/bc589498e4cb72dbe29de5121f5009eb95b5a22c/cards/render.py)
- [数据查询与字段口径](https://github.com/mgkvibez/openclaw-profile-cards/blob/bc589498e4cb72dbe29de5121f5009eb95b5a22c/cards/github_data.py)
- [公开项目仓库](https://github.com/cogine-ai/awesome-openclaw-zh)
- [GitHub GraphQL Repository 字段](https://docs.github.com/en/graphql/reference/objects#repository)

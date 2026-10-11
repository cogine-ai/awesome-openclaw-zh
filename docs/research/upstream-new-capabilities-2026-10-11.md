# 2026-10-11 上游新玩法来源与边界

本文记录本轮新用例的查阅证据。时间以 Asia/Taipei 为用户侧基准；保留 GitHub API 的 UTC 原始值，以便复核。

调研方式：官方文档、固定发布标签下的源文件、作者 PR 与 GitHub API。没有使用第三方排行榜证明热度，没有运行付费媒体任务、云机器或真实会议。

## 版本与近期活动

| 来源 | 查到的事实 | 能支持的结论 |
|---|---|---|
| [OpenClaw v2026.10.1](https://github.com/openclaw/openclaw/releases/tag/v2026.10.1) | `published_at=2026-10-10T23:54:03Z`，台湾时间 2026-10-11 | 本轮用例可固定在该稳定发布版本 |
| [OpenClaw v2026.9.7](https://github.com/openclaw/openclaw/releases/tag/v2026.9.7) | `2026-09-30T04:44:14Z` | 新视频提供者与扩大 Swarm 并发是近期已发布更新 |
| [OpenClaw v2026.9.6](https://github.com/openclaw/openclaw/releases/tag/v2026.9.6) | `2026-09-23T23:21:10Z`，台湾时间 2026-09-24 | 临时应用与云桌面会话路径有发布依据 |
| [OpenClaw v2026.9.5](https://github.com/openclaw/openclaw/releases/tag/v2026.9.5) | `2026-09-19T01:55:23Z` | GPT Live 会议参加与多角色配置有发布依据 |
| [Crabbox releases](https://github.com/openclaw/crabbox/releases) | 0.71.0、0.72.0、0.73.0、0.74.0 分别发布于台湾时间 10-05、10-07、10-09、10-11 | 一周内有四次发布，支持“近期快速迭代” |
| [Peekaboo releases](https://github.com/openclaw/Peekaboo/releases) | v4.7.0、v4.8.0、v4.9.0 API 发布时间分别为 10-04、10-05、10-07 台湾时间 | 有近期背景窗口操作与菜单控制更新 |

2026-10-11 的仓库 API 快照：OpenClaw 391,676 stars，Crabbox 1,456，Peekaboo 5,282。累计数字只说明规模，不证明近期增速。

本次尝试通过 stargazer 时间戳统计最近 7/30 天增长：Crabbox REST stargazers 请求返回 404，GraphQL 返回零条且与仓库总数矛盾。因此没有可信的新增 Star 统计，不使用“本周暴涨”或“增长最快”描述。上述发布活动也不能替代用户采用或 Star 增長证据。

## 已写入的五个案例

### 1. 聊天内原生视频生成

- 页面：[native-video-generation-chat.md](../../usecases/creative/native-video-generation-chat.md)。
- 主要来源：[v2026.10.1 视频工具文档](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/video-generation.md)。
- 已核对：`video_generate` 的三个输入模式、`action=list/status`、后台完成返回原会话、提供者限制、官方 Veo 设置示例。
- 前置条件：至少一个可用视频提供者授权；图片路径、参考数量、音频与时长能力由该提供者决定。
- 近期证据：[2026.9.7 视频提供者更新](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/releases/2026.9.7.md)。
- 区别于已有案例：本次覆盖原生文字/参考素材到视频与异步回传，已有 Tubeify 条目覆盖剪辑，AI 绘画条目覆盖图片生成。
- 未做：真实授权、接口调用、费用与成片评估。

### 2. Crabbox 临时应用实验室

- 页面：[crabbox-disposable-app-playground.md](../../usecases/tools/crabbox-disposable-app-playground.md)。
- 主要来源：[v2026.10.1 Cloud Worker Desktop](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/gateway/cloud-workers/desktop.md)、[固定版本 profile 配置](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/gateway/config-cloud-workers.md)。
- 已核对：同一会话附属环境、Portal/Desktop 展示、主工作区不随附属机器迁移、人工接管与明确恢复、关闭面板不停止机器。
- 前置条件：有效 profile、Crabbox 后端/协调器配置、持久非 sandbox 会话；桌面另需 lab、`settings.desktop: true`、视觉模型与 computer 权限。
- 版本细节：该固定版本要求 Crabbox >=0.69.0；2026.9.7 说明中的 >=0.67.0 是较旧版本要求。
- 配置示例属于字段组合，`readyWorkers: 0` 与 `warmImage: false` 均有官方字段依据；没有配置真实云账户。
- 近期证据：[2026.9.6](https://docs.openclaw.ai/releases/2026.9.6) 描述临时应用旁开；Crabbox 四次近期发布见上表。
- 未做：分配机器、桌面/Portal 访问、运行费用、真实释放确认。

### 3. 实时会议 Agent

- 页面：[live-meeting-agent-participant.md](../../usecases/productivity/live-meeting-agent-participant.md)。
- 主要来源：[v2026.10.1 Meeting plugins](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/plugins/meeting-plugins.md)、[Google Meet 工具与模式](https://docs.openclaw.ai/plugins/google-meet/tool-and-modes)。
- 已核对：`transcribe`、`agent`、`bidi` 的差异；官方插件包名、setup/join 命令；虚拟音频依赖；字幕与约五分钟更新的纪要。
- 前置条件：Chrome、平台准入、可用字幕或语音提供者；说话需要本机音频桥，远端 Chrome node 有单独命令策略。
- 不夸大：`speechOutputVerified` 只验证本机麦克风注入；远端听见与打断仍需要第二位参与者实际验证。
- 不夸大：Teams/Zoom 参加不等于创建会议、厂商 API 或音视频录制；Slack huddle 需要专用已登录用户，bot token 不能替代。
- 近期证据：2026.9.5 扩展 GPT Live 到会议，2026.9.6 更新实时纪要。
- 未做：真实入会、字幕、音频注入、第二参与者可听性和费用。

### 4. Lobster 交互输入与恢复

- 页面：[lobster-interactive-resume-workflow.md](../../usecases/automation/lobster-interactive-resume-workflow.md)。
- 主要来源：[v2026.10.1 Lobster 文档](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/lobster.md)。
- 已核对：[插件 package.json](https://github.com/openclaw/openclaw/blob/v2026.10.1/extensions/lobster/package.json) 固定依赖 runtime 2026.9.14。
- 精确语法：[v2026.9.14 ask.ts](https://github.com/openclaw/lobster/blob/v2026.9.14/src/commands/stdlib/ask.ts) 的 `--prompt`、`--schema`、`--subject-from-stdin`；[pick.ts](https://github.com/openclaw/lobster/blob/v2026.9.14/src/commands/stdlib/pick.ts) 的字段列表。
- 样例范围：仅运行选择题、Schema 回答与字段投影，不接未安装的 `inbox` 等文档占位工具。
- 前置条件：单独安装插件、工具策略放行、非 sandbox 工具上下文、保留恢复令牌与状态。
- 近期证据：[2026.10.1 changelog](https://github.com/openclaw/openclaw/blob/v2026.10.1/CHANGELOG/2026.10.1.md) 的 Interactive Lobster workflows。
- 不夸大：恢复令牌不绑定用户/会话；插件不列出待处理检查点；内嵌 runner 的 `openclaw.invoke` 不自动继承 Gateway/auth。
- 未做：实际 OpenClaw 插件调用、跨进程/跨会话恢复、真实业务写入。

### 5. MCP Apps 交互工作台

- 页面：[mcp-apps-interactive-chat-workbench.md](../../usecases/tools/mcp-apps-interactive-chat-workbench.md)。
- 主要来源：[v2026.10.1 MCP Apps 文档](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/cli/mcp/apps.md)。
- 精确设置：官方 `mcp.apps.enabled` 命令、基础 React server 包名与 stdio 参数、重启要求、独立 sandbox origin。
- 作者证据：[PR #161747](https://github.com/openclaw/openclaw/pull/161747)，`created_at=2026-09-30T08:02:57Z`、`merged_at=2026-10-02T12:02:36Z`；作者报告 Bits & Bolts 0.1.11 与真实 Gateway 的合成数据互通测试。
- 作者验证覆盖：直接入口、资源/图片上下文、STL 编辑、条件保存冲突、36 项选择表单等。没有拿真实 ChatGPT 账户结果作证明。
- 前置条件：兼容 App 的 server、显式开启 host、两端口或独立 origin 可达、有效会话/工具权限；扩展能力要逐项声明。
- 不夸大：基础 React 示例只验证渲染，不能证明所有 server 提供编辑；`ifMatch` 可选，未提供的保存可能覆盖较新内容。
- 未做：当前 npm 包安装、Control UI 渲染、App 交互、真实文件保存与第三方账户授权。

## 另外三个可继续验证的候选

| 候选 | 可复制的来源事实与前提 | 近期证据 | 本轮选择 |
|---|---|---|---|
| 看图生成背景音乐 | [music_generate](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/music-generation.md)；配置音乐提供者，支持图片参考的模型才接受图片；输出为音频与异步状态 | 2026.9.5 更新图片参考 fallback | 与视频生成一起可做后续创作组合，未写入 |
| Mac 背景窗口操作 | [Peekaboo README](https://github.com/openclaw/Peekaboo)、[4.8.0](https://github.com/openclaw/Peekaboo/releases/tag/v4.8.0)；Mac 权限、匹配 Bridge 版本、精确窗口/观察引用 | 4.8.0 新增精确后台拖拽、选字与滚动；4.9.0 更新菜单与文件对话框 | 需要真实 Mac 验证，未写入 |
| Swarm 结构化并行研究 | [Swarm](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/swarm.md)；启用 Code Mode、允许目标 Agent、设置并发预算，`agents.run` 配合 Schema / Promise 控制流 | 2026.9.7 默认组并发由 8 提到 32，collector 与普通 subagent 槽位分开 | 已有 7 子代理/子代理调度条目，先避免重复发布 |

另外查到 Standing intents 与 Self-learning。前者是更早的事件条件记忆；后者 main 在稳定版发布后仍有行为调整。本轮没有仅凭 main 最新提交把行为反推为所有已发布安装版本的能力。

## 可并入索引的条目

```json
[
  {
    "title": "在聊天里生成视频：文字、图片与异步回传",
    "desc": "通过原生 video_generate 从文字或参考素材生成短视频，并在同一会话收取异步结果。",
    "category": "创意与构建",
    "localPath": "usecases/creative/native-video-generation-chat.md",
    "sourceRepo": "openclaw/openclaw",
    "sourcePath": "docs/tools/video-generation.md",
    "sourceUrl": "https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/video-generation.md"
  },
  {
    "title": "Crabbox 临时应用实验室：边聊天边看远程界面",
    "desc": "在会话附属的临时机器上打开 Web 或桌面应用，旁观界面、接管操作并明确保存与停止。",
    "category": "工具开发",
    "localPath": "usecases/tools/crabbox-disposable-app-playground.md",
    "sourceRepo": "openclaw/openclaw",
    "sourcePath": "docs/gateway/cloud-workers/desktop.md",
    "sourceUrl": "https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/gateway/cloud-workers/desktop.md"
  },
  {
    "title": "让 Agent 进入会议：实时听、答与留下纪要",
    "desc": "使用会议插件从只观察字幕逐步到实时语音参加，并区分入会、可听性与纪要验证。",
    "category": "生产力",
    "localPath": "usecases/productivity/live-meeting-agent-participant.md",
    "sourceRepo": "openclaw/openclaw",
    "sourcePath": "docs/plugins/meeting-plugins.md",
    "sourceUrl": "https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/plugins/meeting-plugins.md"
  },
  {
    "title": "Lobster 交互工作流：暂停、补充信息、从原处继续",
    "desc": "用结构化输入检查点暂停流程，验证回答、保留恢复令牌并继续或取消后续步骤。",
    "category": "夜间自动化",
    "localPath": "usecases/automation/lobster-interactive-resume-workflow.md",
    "sourceRepo": "openclaw/openclaw",
    "sourcePath": "docs/tools/lobster.md",
    "sourceUrl": "https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/lobster.md"
  },
  {
    "title": "MCP Apps 交互工作台：在聊天旁查看、选择与编辑",
    "desc": "开启标准 MCP Apps 视图，并在服务声明支持时把选中资源或文件操作接回当前会话。",
    "category": "工具开发",
    "localPath": "usecases/tools/mcp-apps-interactive-chat-workbench.md",
    "sourceRepo": "openclaw/openclaw",
    "sourcePath": "docs/cli/mcp/apps.md",
    "sourceUrl": "https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/cli/mcp/apps.md"
  }
]
```

以上页面均带 `published` / `updated: 2026-10-11` 与“文档组合，待实测”状态。未改写仓库现有索引，由整合任务决定发布顺序与展示标签。

## 本轮文档检查

- 五篇文档分别为 128、148、145、139、138 行；检查了日期、状态、代码围栏配对与 JSON 示例语法。
- 研究文件中的五条 JSON 索引，其本地路径与页面标题一致。
- 五篇引用的 13 个 GitHub blob 路径均通过 GitHub contents API 验证存在，包含全部固定版本文档与 Lobster runtime 源码。
- 上述检查只证明文档结构、参数来源和链接目标存在；不替代运行时、设备、权限、费用或业务结果验证。

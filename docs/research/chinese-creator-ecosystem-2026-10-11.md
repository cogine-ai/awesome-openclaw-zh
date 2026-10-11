# 中文创作者生态选题核查 · 2026-10-11

本轮寻找近期出现、能展示具体成果、与现有案例有明确差异的玩法。核查时间为 2026-10-11（Asia/Taipei）；现有索引共有 192 条，已对照小红书自动化、视频脚本、视频剪辑、绘画、技能构建等条目去重。

## 热度口径

GitHub Stars／Forks、创建日期、最近推送来自本轮 GitHub API 读取。它们是带日期的快照，可能继续变化。创建后短时间累积较多 Star，可以支持「早期获得关注」；不能推出最近七天仍在加速。

本轮查询这些候选的 stargazer 时间戳端点时得到 HTTP 404；Trendshift 页面读取超时。**未获得近七天／近三十天新增或净增数据**，不使用「本周暴涨」「今日最热」或虚构增长率。保留创建时间和累计量，后续取得新快照后再比较。

| 候选 | 创建日期 | 10-11 Star／Fork 快照 | 本轮可核实的时间或版本 | 选择结论 |
|---|---|---|---|---|
| [ZJU-REAL/Easel](https://github.com/ZJU-REAL/Easel) | 2026-08-28 | 3,458／527；后续同日读到 3,459 Stars | v0.2.1 发布 09-24；最近推送 10-11 | 首批：论文证据 → 侦探漫画／知识卡片 |
| [manju-laoli-skill](https://github.com/lixiaoxiao9888-create/manju-laoli-skill) | 2026-08-15 | 1,137／118 | README 顶部 V6.9.8；当前 SKILL.md V6.9.9／10-02；最近推送 10-11 | 首批：一致资产与离线分镜看板；真实离线样例已完成 |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 2026-01-13 | 26,537／2,921 | 最近推送 09-10；comic 有 OpenClaw 元数据 | 候选：多页知识漫画；不假定其为本月新作 |
| [agent-apprenticeship](https://github.com/ray-r-ren/agent-apprenticeship) | 2026-06-19 | 1,618／61 | 最近推送 10-10 | 后续：导师评审、经验导出与复用；安装较重 |
| [VisionClaw](https://github.com/Intent-Lab/VisionClaw) | 2026-02-06 | 2,579／513 | 最近推送 09-26；论文 v2 为 04-08 | 后续：手机／眼镜感知与任务执行，需要完整服务栈 |
| [Star-Office-UI](https://github.com/ringhyacinth/Star-Office-UI) | 2026-02-26 | 7,510／798 | 最近推送 03-11 | 长期视觉灵感；不当成新热点；美术素材非商用 |

另选 [OpenClaw Skill Workshop 的 v2026.10.1 提案流程](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/authoring.md)作为官方能力复现，重点是 `/learn` 提炼方法、审阅应用和换输入验证。Workshop 不是本月首发；2026-10-08 的 [PR #161057](https://github.com/openclaw/openclaw/pull/161057)又重构了主分支接口，但该改动不在本轮核查的 v2026.10.1 标签中，不能混用两套命令。此项依据能力与版本证据入选，不用官方仓库总 Star 推断单功能热度。

## 已整理的三篇与证据边界

| 页面 | 一手来源证明了什么 | 本项目新整理了什么 | 还没有做什么 |
|---|---|---|---|
| [Easel 论文侦探漫画](../../usecases/creative/easel-paper-to-detective-comic.md) | 作者 README 有 KnowU-Bench 侦探漫画等真实产物；paper-explainer 有 PDF 解析与证据骨架；ai-image-gen 有图片调用脚本 | 使用 VisionClaw v2 的四格输入、先证据后叙事、独立提示文件与核对流程 | 未安装 Easel，未调用模型，未生成或发布漫画 |
| [短剧分镜看板](../../usecases/creative/short-drama-consistent-storyboard-board.md) | 作者提供资产规则、提示词校验器与离线 HTML 编译器，说明了模型提示格式 | 原创《深夜失物招领》16 秒项目、两段投喂稿、真实 HTML；包检查与逐段提示词通过，看板编译 0 WARN；浏览器确认按段筛选 | 未安装到 OpenClaw，未出图、调用视频模型或拍摄成片 |
| [成功任务变 Skill](../../usecases/tools/skill-workshop-learn-from-success.md) | v2026.10.1 文档与 CLI 源码提供 /learn → pending，以及 list/inspect/revise/apply/reject | 两组素材检查数据、提案审阅应用与新输入复用实验；标明主分支接口差异 | 未在真实会话执行，不声称效率提升 |

页面中的测试素材与原创小故事已明确标记。上游公开演示不能代替本项目实测，HTML 编译器产生文件不能代替完整质量检查。

## 关键实现细节

- **Easel：**使用 OpenClaw 连接方式；API 直连无法执行本机工具。技能目录为 `skills/openclaw/paper-explainer/` 与 `skills/openclaw/ai-image-gen/`；共享图片脚本在 `skills/shared/scripts/ai_image.py`。论文骨架需要 LLM 填充，不是解析脚本自动完成研究解读。图片配置属于 Easel 项目 `.env`。
- **短剧：**完整安装 `short-drama-director/`。当前作者正式支持 Seedance 2.5／2.0 与 MiniMax H3 提示格式；技能不等于视频渲染服务。`build_board_lite.py` 接受 `--out`，无该参数时输出 `<项目名>_分镜看板.html`。看板会在缺字段时降级并报告 WARN。
- **短剧离线验证：**固定上游提交 `edebc10e4b2aed5e259deff673d58d2080fe5c29`。整份多段项目不能直接当单段投喂稿校验；本轮先得到镜数／字符预算失败，再提取两段独立校验，均 PASS／0 WARN。看板识别 2 段／4 镜头／5 资产／5 组出图词／16 秒；图像仍待生成。[完整结果与复现](short-drama-offline-validation-2026-10-11.md)。
- **Workshop：**本案例固定 v2026.10.1。显式 `/learn` 只产生或修订 pending 提案，不应用；`workshop list` 列出提案。用真实 proposal ID 执行 inspect，审阅后 apply；错误提案 revise 或 reject。活动技能属于单个 Agent，新会话加载应用后的技能，当前运行会话保留原快照。v2026.10.1 的 CLI 注册代码也验证了这些命令；changes/show/archive/restore 属于后续主分支的直接版本化流程，正文只作为扩展说明，不当成稳定版步骤。

## 后续可继续验证的创作方向

- Baoyu 的知识漫画可用明确受众、固定角色、单独分镜与逐页重试做成系列；当前只确认文档能力，不将仓库总 Star 当作 comic 单技能使用量。
- 导师评审玩法可以用同一类公开任务记录结果差异，先设置 Private Internal Only；不要把经验条目数当作自动提升证明。
- VisionClaw 有手机相机模式，但语音需要自己的 Gateway、Agent worker 与 LiveKit 配置；默认 Gateway 是私人试点，不能写成公开开箱即用服务。
- 像素办公室适合衍生原创工作状态小剧场。Star Office 的代码与美术许可不同，面向公司传播时使用原创资产。

## 一手资料

- [Easel README、作者产物与安装说明](https://github.com/ZJU-REAL/Easel)
- [Easel v0.2.1 发布](https://github.com/ZJU-REAL/Easel/releases/tag/v0.2.1)
- [Easel paper-explainer](https://github.com/ZJU-REAL/Easel/blob/main/skills/openclaw/paper-explainer/SKILL.md)
- [Easel ai-image-gen](https://github.com/ZJU-REAL/Easel/blob/main/skills/openclaw/ai-image-gen/SKILL.md)
- [漫剧老李 V6.9.8](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/main/README.md)
- [短剧离线看板契约](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/main/short-drama-director/references/storyboard-board-lite.md)
- [v2026.10.1 Workshop：/learn 与提案 CLI](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/authoring.md)
- [v2026.10.1 Workshop：工具前提与提案内容](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/proposals.md)
- [v2026.10.1 Workshop：应用与 Control UI](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/how-it-works.md)
- [v2026.10.1 Skills CLI 文档](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/cli/skills.md)
- [v2026.10.1 Skills CLI 注册代码](https://github.com/openclaw/openclaw/blob/v2026.10.1/src/cli/skills-cli.ts)
- [2026-10-08 Workshop 主分支重构 PR #161057](https://github.com/openclaw/openclaw/pull/161057)
- [VisionClaw 论文 v2](https://arxiv.org/abs/2604.03486v2)

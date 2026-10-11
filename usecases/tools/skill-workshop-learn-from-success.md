---
title: "把成功任务变成 Skill：审阅提案后再复用"
description: "按 OpenClaw v2026.10.1，用 /learn 提炼检查方法，审阅并应用提案，再换一组输入验证复用。"
category: "工具开发"
published: "2026-10-11"
updated: "2026-10-11"
validation: "依据官方文档组合；OpenClaw 会话未实测"
---

# 把成功任务变成 Skill：审阅提案后再复用

> 把「这次终于做对了」留下来。换一份材料时，龙虾先读已有方法，再执行和检查。

## 这是怎样的新玩法

OpenClaw 的 Skill Workshop 让 Agent 把成功任务提炼成可复用方法。本页按 [v2026.10.1 的提案流程](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/authoring.md)操作：先生成待审阅提案，检查内容后应用，再换一组输入验证。它适合整理素材包、准备简报、核对发布资料等重复工作。

**版本边界：**本文固定到 `v2026.10.1` 的文档和 CLI 源码，2026-10-11 核查。该版本的 `/learn` **只留下 pending 提案，不自动应用**；`workshop list` 列出提案，不代表技能已经启用。当前主分支已改成另一套接口，差异见文末。

**验证状态：**本页是官方文档组合的最小实验；未在真实 OpenClaw 会话运行，不声称节省了多少时间或 Token。下面的素材表为教程自造测试数据。

## 准备条件

- 已经能正常对话与读写本地文件的 OpenClaw `v2026.10.1`；CLI 与 Gateway 使用兼容版本。
- 当前 Agent 可使用内置 `skill_workshop` 工具；文档说明该工具包含在 coding profile 中，沙箱会话可能不提供它。
- 打开 Control UI 的 `Plugins → Workshop → Suggestions`，或能使用下方 CLI 审阅提案。

先运行 `openclaw --version` 和 `openclaw skills workshop --help`。本例使用主动发送的 `/learn`，无需添加定时任务或开启后台学习。下方命令假定 Agent ID 是 `main`；如果不是，统一替换成实际 ID。

## 最小输入：三份素材里有两个问题

将以下内容保存为当前 Agent 工作区的 `examples/asset-review/input-a.md`，或直接粘贴给它：

```markdown
# 公共素材包 A（教程测试数据，不代表真实文件）

| 名称 | 来源 | 说明 | 状态 |
|---|---|---|---|
| cover.png | 我自己的原创素材 | 首页封面 | 待检查 |
| flow.png | 未填写 | 操作流程图 | 待检查 |
| cover.png | 我自己的原创素材 | 同名的第二份封面 | 待检查 |

要求：检查重名、缺来源、描述是否清楚；只出检查报告。
原始文件没有附上，因此不能判断文件是否存在、尺寸或实际许可。
```

第一次任务提示词：

```text
请检查上面的公共素材包 A，把结果保存为 examples/asset-review/report-a.md。
先列检查规则，再逐项检查；把已确认问题与无法核实的项目分开。
需要发现 cover.png 重名、flow.png 缺来源。
「我自己的原创素材」是输入者的声明，不是已经验证的版权证据。
不要编造文件尺寸、文件存在性或许可；不要修改、删除或发布素材。
最后给我一个可用于下一份素材包的检查顺序。
```

先检查报告。如果模型错把空白来源认作合格，明确纠正；这类持久的工作规则适合留下来。

## 提炼方法，先保留提案

在完成并核对任务的同一对话发送：

```text
/learn 将刚才公开素材包的检查方法提炼为 reusable-asset-review 的待审阅提案。
只保存检查顺序、问题分类、无法核实项和报告模板。
以后先读取输入、检查重名与缺来源，再分别列已确认问题和待核实项。
素材名称、个人信息与本次示例结论不要写成固定规则。
如已有同类提案或 Workshop Skill，请修订或提出更新，不要重复创建。
返回实际提案 ID 与技能名；这一步不要应用提案。
```

`/learn` 可以从当前对话或指定材料提炼方法，修订已有提案，或为已有技能提出更新。它也可能判断没有值得保存的内容；以真实回复为准，不能假定必定创建了要求的名字。

列出提案，再将返回的真实 ID 替换到检查命令中：

```bash
openclaw skills workshop list --agent main
openclaw skills workshop inspect <proposal-id> --agent main
```

检查提案保存的是检查顺序、模板和无法核实项，不是 `cover.png` 这道题的标准答案。确认后应用：

```bash
openclaw skills workshop apply <proposal-id> --agent main
openclaw skills info reusable-asset-review --agent main
openclaw skills check --agent main
```

`<proposal-id>` 是占位符，不能原样粘贴；如果实际技能名不同，也替换 `reusable-asset-review`。应用成功才会写入活动 `SKILL.md`；还要检查技能是否对该 Agent 可见。

## 换一组输入，验证真的学会了

开启同一个 Agent 的新会话，使用下面的 B 组。该版本的新会话加载应用后的 Skill；当前运行会话保留原来的技能快照。

```markdown
# 公共素材包 B（教程测试数据，不代表真实文件）

| 名称 | 来源 | 说明 | 状态 |
|---|---|---|---|
| diagram.svg | 我自己的原创素材 | 架构流程图 | 待检查 |
| photo.jpg | 未填写 | 现场照片 | 待检查 |
| notes.md | 我自己的原创素材 |  | 待检查 |
```

发送：

```text
请先查找并读取我们保存的公共素材包检查 Skill，再检查 B 组，
输出 examples/asset-review/report-b.md。报告写明本次用了哪个 Skill。
要求同样只出报告；文件没有附上，不判断真实文件属性或许可。
```

本次应发现 `photo.jpg` 缺来源、`notes.md` 缺说明；**没有重名问题**。如果仍报告 `cover.png` 重名，说明学到的是旧答案，需要修正 Skill。

## 可检查的交付

| 成果 | 核对方法 |
|---|---|
| A 组报告 | 两个明显问题被发现；没有杜撰真实文件属性 |
| 学到的 Skill | 能看见方法、模板和实际名称；不硬编码 A 组答案 |
| 提案与应用结果 | 能指出实际 ID、审阅内容和 applied 状态 |
| B 组报告 | 适用于新输入；写明读取了哪个 Skill |

如果想研究是否更快，记录两轮的总耗时、人工纠错次数和产物质量。不同输入不能直接当成严格性能比较，更不能把这个小样本写成普遍提升比例。

## 提案不合适时怎样处理

还未应用时，在 Suggestions 修订或拒绝；CLI 支持以下命令。`PROPOSAL.md` 是你已经修正的提案文件，需要保留实际技能名和描述：

```bash
openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md --agent main
openclaw skills workshop reject <proposal-id> --reason "方法不适合复用" --agent main
```

这两个命令是两种选择：修订后重新 inspect；不再需要则 reject。提案若因活动技能变更而变成 `stale`，重新读取当前技能再提出更新。已经应用的错误规则应提出新更新并重新审阅；本页不提供该版本不存在的 `workshop restore <name>` 命令。

## 常见卡点

- **`/learn` 只回复无法使用：**检查当前会话是否提供 `skill_workshop`，查看工具策略或使用合适的本地会话；不要静默扩大现有权限。
- **技能已保存，新任务没用：**检查是否同一个 Agent；开启新会话并要求先读取真实技能。Workshop 学到的技能按 Agent 保存，不会自动跨 Agent 分享。
- **新输入仍出现旧答案：**提出修正提案，去掉具体测试名称和结论；审阅、应用后再开新会话验证。
- **希望记住我的个人偏好：**个人事实属于 memory；Workshop 更适合反复执行的方法。
- **提案看得见，技能却没有：**确认已应用，而非只完成 `/learn`；再检查 Agent 与技能可见性。

## 当前主分支的扩展说明

2026-10-08 合并的 [PR #161057](https://github.com/openclaw/openclaw/pull/161057)将 Workshop 改为直接、版本化的学习循环；后续主分支支持 `changes`、`show`、`archive`、`restore` 和新的撤销入口。这些接口不在本页核查的 `v2026.10.1` 标签中。使用主分支构建时，按对应提交的文档操作，不把两套命令混用，也不直接照抄本页的提案命令。

## 来源

- [v2026.10.1：/learn、提案与 CLI](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/authoring.md)
- [v2026.10.1：工具条件与提案内容](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/proposals.md)
- [v2026.10.1：应用规则与 Control UI](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/skill-workshop/how-it-works.md)
- [v2026.10.1 Skills CLI](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/cli/skills.md)
- [当前主分支接口迁移：PR #161057](https://github.com/openclaw/openclaw/pull/161057)

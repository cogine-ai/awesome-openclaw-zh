---
title: "把做成的事沉淀成经验卡：保留原话与版本演进"
description: "用 Easel 记录卡技能整理核心要点、机理、方法和使用边界；附可离线重跑的真实建卡、修订与版本展示样例。"
category: "生产力"
published: "2026-10-23"
updated: "2026-10-23"
validation: "上游建卡与修订CLI离线复现通过；公开资料演练，非完整人工访谈"
---

# 把做成的事沉淀成经验卡：保留原话与版本演进

> 一次具体经历，整理成能继续改进的卡片；分清自己的原话、公开事实与 AI 的建议。

## 先看实际成果

[打开两版经验卡展示页](../../assets/examples/experience-card/gallery.html)，切换 v1／v2 查看同一张卡怎样演进。也可以直接阅读 [v1 Markdown](../../assets/examples/experience-card/card-v1.md) 和 [v2 Markdown，含完整 v1](../../assets/examples/experience-card/card-v2.md)。

本轮素材是维护者用本项目**已完成的一次研究文档链接修复**进行演练。公开内容 Markdown 使用相对研究文档链接；未映射的站内文档路径返回 404，而[当前公开短剧页面](https://www.opcboost.com/usecases/creative/short-drama-consistent-storyboard-board)已把读者引向固定提交的 GitHub 文档。版本和观察出处见[输入来源](../../assets/examples/experience-card/provenance.json)。

这不是用户口述访谈。v1 是助手对公开资料的结构化整理；v2 新增「文件、链接、版本三层分别核对」的编辑提炼，明确标注未经受访者确认。没有模拟用户回答，也没有把编辑建议写成已采纳观点。建卡日期为 2026-10-23，不代表修复发生于当天。

## 上游能力与版本

Easel 的 [skill-record-card](https://github.com/ZJU-REAL/Easel/blob/a097ddfbb704c9d1eeb1db49a056fdbca9c2351a/skills/builtin/skill-record-card/SKILL.md)通过逐段访谈整理四个主题：核心要点、机理、具体方法、使用范围；适用与不适用分别存储，因此脚本要求五个正文字段。它还保存原话、AI 补充说明和同一卡片的历史版本。

[上游 PR #158](https://github.com/ZJU-REAL/Easel/pull/158)于 2026-10-23 合并。本例固定 Easel 提交 `a097ddfbb704c9d1eeb1db49a056fdbca9c2351a`；这是新合并的技能源码，不以 Easel 安装版本号或 OpenClaw 稳定版首发来宣传。

正式访谈时，上游要求一次只问一个问题，先挖用户自己的思考，再呈现 AI 补充，整体确认后才落盘。`card.py` 只负责编号、存档和修订，**不会执行访谈或生成正文，也不能验证用户是否真的确认过**。本页用明确授权的公开资料演练验证脚本，不将它等同于完整上游访谈流程。

## 前置条件

| 体验 | 需要什么 | 成本与边界 |
|---|---|---|
| 重跑本页成果 | Python 3.10+ 与本仓库文件 | 纯标准库、无需网络、模型或 OpenClaw；不会安装依赖 |
| 亲自做一次访谈 | 已配置文本模型的 OpenClaw／Easel 与该固定版本 Skill | 模型按自己的配置计费；需要本人回答和确认，不能用样例代替 |

本页随附复现必要的两份**未修改**上游 Python 文件，校验和保存在 `provenance.json`，并保留 [Apache-2.0 许可](../../assets/examples/experience-card/LICENSE.apache-2.0.txt)。没有打包其他上游资料、账号或机器路径。

## 不用账号，先离线跑通

在本仓库根目录执行：

```bash
python3 assets/examples/experience-card/reproduce.py --verify
```

它会在自动清理的临时目录实际执行固定版本的 `selftest → new → revise → list → show`，将 Markdown 副本文末空行归一后，再逐字比较三份现成产物。成功时输出 `PASS`，不会覆盖仓库中的卡片。

要生成自己的独立副本，指定一个尚不存在的目录：

```bash
python3 assets/examples/experience-card/reproduce.py --out /tmp/experience-card-replay
```

打开新目录中的 `gallery.html`；它不加载外部资源，下载链接指向同目录文件。重复执行时换一个新目录，脚本会拒绝覆盖已有目录。

## 最小输入与实际命令

[v1 输入](../../assets/examples/experience-card/input-v1.json)包含 `title`、`did`、`point`、`mechanism`、`method`、`scope_use`、`scope_nouse`、`quotes` 和 `ai_notes`；本例 `quotes` 为空，所有编辑提炼在正文及 `ai_notes` 中标明。

上游真实建卡接口为：

```bash
EASEL_ROOT=/path/to/easel python3 skills/builtin/skill-record-card/scripts/card.py new \
  --topic "网站研究文档404修复演练" --data /path/to/input-v1.json --date 2026-10-23
```

`EASEL_ROOT` 是存档项目根目录，脚本写入 `outputs/<主题>/assets/cards/card-001.md`。主题要具体，不能使用 `demo`、`test` 等泛化名称。实际访谈中，`--data` 应是本人确认后的文字；不要直接把模型猜测当作确认稿。

`revise` 没有 `--data` 参数。[本例修订输入](../../assets/examples/experience-card/input-v2.json)由复现脚本转换成真实字段参数，并以 `--card 001 --change ... --replace-ai-notes` 更新同一张卡：旧版全文保留，未修改字段继承，新版 AI 说明替换。不要每次理解变深就新建另一张卡。

## 换成自己的真实经历

可以把这段需求发给已加载该 Skill 的 OpenClaw：

```text
我想记录刚做成的一件具体的事。请按 skill-record-card 的访谈流程，
一次只问一个问题，先让我自己说明核心要点、机理、具体步骤和使用边界。
不要替我模拟回答。每次 AI 补充明确标注，由我决定采纳、修改或拒绝。
完整复述并得到我确认后再用 card.py new 存档。
后续新理解用 revise 升级同一张卡，保留原话与历史版本。
```

真正的素材可以是一次故障处理、第一次成功剪片、一次谈判或一次失败尝试。卡片的价值来自具体经历和可解释的边界；没有做过的事，不补成自己的经验。

## 这次验证到了哪里

- 实际执行上游 `selftest/new/revise/list/show`，均成功；五个正文字段与输入一致。
- v2 保留 v1，未改字段正确继承，当前版本为 v2；`--replace-ai-notes` 只替换新版说明。
- 两版均无用户原话；Markdown 的空摘录占位只是脚本默认文案，不表示访谈发生过。
- 展示页由上游解析器读取实际产物后生成；离线重跑与现成两份 Markdown、HTML 逐字匹配。
- 本轮只验证这些公开链接与存档行为，不声称完成全站审计、完整人工访谈或后续分享效果验证。

2026-10-23，本机 OpenClaw 2026.9.8 的端到端调用返回 401，未成功；没有完成模型访谈验证，也没有为此修改全局配置或凭证。

字段为空时应补充真实材料，不能为了通过而写空话；修订失败先保留旧卡，核对编号、历史段落和输入。访谈被打断时，未确认草稿也不能冒充已经存档的确认稿。

由 Cogine 团队整理。欢迎用自己的真实经历重跑，并贡献带来源、版本和验证边界的案例。

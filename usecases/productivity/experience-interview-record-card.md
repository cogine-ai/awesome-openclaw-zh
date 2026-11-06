---
title: "把做成的事沉淀成经验卡：保留原话与版本演进"
description: "用 Easel 记录卡技能整理核心要点、机理、方法和使用边界；附可离线重跑的真实建卡、修订与版本展示样例。"
category: "生产力"
published: "2026-10-23"
updated: "2026-10-23"
showcase:
  verification: script-reproduced
  platforms: [macos, browser]
  account: none
  cost: local-free
  artifactPath: assets/examples/experience-card/gallery.html
  artifactLabel: "查看 v1/v2 经验卡"
  previewPath: assets/examples/experience-card/preview.svg
  bundlePath: assets/bundles/experience-card-2026-10-27.zip
  testedAt: 2026-10-27
  testedVersion: "Python 3.12；Easel a097ddf"
  beginner: true
---

# 把做成的事沉淀成经验卡：保留原话与版本演进

把一次故障处理、成功剪片或项目交付整理成卡片，留下核心要点、原因、步骤和适用场景。以后遇到类似工作，可以直接拿来参考，再随着新经验继续修订。

## 看看一张卡怎样改进

[打开两版经验卡](../../assets/examples/experience-card/gallery.html)，切换 v1／v2 对照修改。也可以阅读 [v1 Markdown](../../assets/examples/experience-card/card-v1.md) 和 [含完整历史的 v2](../../assets/examples/experience-card/card-v2.md)。

本页用公开项目资料中的一次研究文档链接修复做示例。v1 整理排查经过，v2 加入文件、链接和版本三个检查层次，方便下次复用。[输入与出处](../../assets/examples/experience-card/provenance.json)随包提供。

## 准备什么

- 先重跑示例：Python 3.10+ 与本仓库文件，无需额外依赖。
- 整理自己的经历：已配置文本模型的 OpenClaw／Easel，以及 [skill-record-card](https://github.com/ZJU-REAL/Easel/blob/a097ddfbb704c9d1eeb1db49a056fdbca9c2351a/skills/builtin/skill-record-card/SKILL.md)。模型费用按自己的配置计费。

本例使用 Easel 提交 `a097ddfbb704c9d1eeb1db49a056fdbca9c2351a` 的建卡与修订脚本，随包保留 [Apache-2.0 许可](../../assets/examples/experience-card/LICENSE.apache-2.0.txt)。

## 重跑现成卡片

在仓库根目录执行：

```bash
python3 assets/examples/experience-card/reproduce.py --verify
```

脚本会在临时目录完成建卡、修订、列表与读取，并对照现成文件。成功时输出 `PASS`。

想保存一份独立副本，指定新目录：

```bash
python3 assets/examples/experience-card/reproduce.py --out /tmp/experience-card-replay
```

打开新目录里的 `gallery.html`，即可浏览两版卡片和下载对应输入。再次运行时换一个输出目录。

## 换成自己的经历

将这段需求发给已加载该 Skill 的 OpenClaw：

```text
我想记录刚做成的一件具体的事。请按 skill-record-card 的访谈流程，
一次问一个问题，帮我说明核心要点、原因、具体步骤和适用场景。
先听我的回答，再给补充建议。
把整理结果发给我确认后，用 card.py new 存档。
以后有新理解，用 revise 升级同一张卡，保留原话与历史版本。
```

可以先从“最近一次怎么解决问题”开始。讲清当时发生了什么、尝试了什么、哪一步起了作用，卡片就有了可复用的细节。

## 直接使用建卡命令

[v1 输入](../../assets/examples/experience-card/input-v1.json)包含标题、经历和五个正文字段。按自己的经历修改 JSON 后，在仓库或完整材料包根目录运行随包脚本：

```bash
EASEL_ROOT=/path/to/easel python3 assets/examples/experience-card/upstream/skills/builtin/skill-record-card/scripts/card.py new \
  --topic "网站研究文档404修复演练" --data /path/to/input-v1.json
```

`EASEL_ROOT` 是存档项目根目录；命令返回 `card` 编号与 `path` 文件位置，日期默认为当天。主题用具体事件命名，方便以后查找。

修订使用 `revise`：将建卡命令返回的 `card` 值传给 `--card`，再提供 `--change` 和要更新的字段。本例的[修订输入](../../assets/examples/experience-card/input-v2.json)由复现脚本转换成这些参数；旧版全文保留，未修改字段继承。

要把示例图库改成自己的案例，还需一起更新 `provenance.json` 的 `facts`、案例链接与日期，以及 `reproduce.py` 的主题、页面标题和简介；没有对应出处时将 `facts` 设为 `[]`。保留 Easel 的上游提交与脚本校验信息。

## 更新预览图

修改卡片后，在仓库或完整材料包根目录执行：

```bash
python3 scripts/generate-showcase-previews.py --pack experience-card
```

它会读取两版卡片的核心要点，更新 `assets/examples/experience-card/preview.svg`。

由 [Cogine 团队](https://www.cogine.ai/)整理。欢迎[分享自己的卡片](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)，也可以 [Star 收藏中文案例库](https://github.com/cogine-ai/awesome-openclaw-zh)，下次继续使用。

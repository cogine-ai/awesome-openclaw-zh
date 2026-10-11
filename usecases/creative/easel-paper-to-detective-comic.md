---
title: "论文变侦探漫画：Easel 科普创作工作台"
description: "先提炼论文证据，再用侦探分镜讲清一个问题，交付可核对来源的漫画与知识卡片。"
category: "创意与构建"
published: "2026-10-11"
updated: "2026-10-11"
validation: "作者演示已公开；本文组合流程未本地实测"
---

# 论文变侦探漫画：Easel 科普创作工作台

> 让读者跟着角色找线索，把一篇论文的「问题、方法、结果、局限」看明白。先做四格分镜，再决定是否生成图片。

## 这次有什么新玩法

Easel 的作者已经公开了论文知识卡片、KnowU-Bench 侦探漫画与视频素材。[作者产物展示](https://github.com/ZJU-REAL/Easel#%EF%B8%8F-%E7%9C%9F%E5%AE%9E%E4%BA%A7%E7%89%A9)可以直接查看成品；本页将论文提炼与侦探叙事组合成一个更小的入门任务。

这与普通论文摘要的区别，在于读者先看一个疑问，再跟着证据理解答案。最终可以分享漫画，同时保留事实清单和原文定位，便于别人核对。

**来源状态：**Easel 创建于 2026-08-28；2026-10-11 的 GitHub API 快照为 3,458 Stars、527 Forks，即创建约 44 天累计数千 Star。这是早期关注度信号；本次没有取得近七天净增长数据。可核实的最近正式版本为 [v0.2.1，2026-09-24](https://github.com/ZJU-REAL/Easel/releases/tag/v0.2.1)，本文还参考了 2026-10-11 查阅的主分支文档。

**验证状态：**作者示例存在；本文没有安装 Easel、调用模型或生成漫画。下面的示例与提示词属于基于源码文档整理的复现方案。

## 你需要什么

| 项目 | 用途 |
|---|---|
| Easel 的 OpenClaw 模式 | 让 Agent 读取文件、使用技能、保存产物 |
| Python 3.10+、Git、兼容的 Node.js | 作者安装器的基础环境；具体 Node 版本以当前 README 检查为准 |
| 可用的文本模型配置 | 提炼原文、写分镜与核对事实 |
| `paper-explainer` | 解析论文并保存结构化证据材料 |
| `ai-image-gen` 与独立的图片服务配置 | 可选；将已确认的分镜生成图片 |

第一轮只做事实清单和分镜，无需图片服务或社媒账号。需要出图时，再在 Easel 项目自己的 `.env` 配置 `IMG_BASE_URL`、`IMG_MODEL`、`IMG_API_KEY`。凭证不写入提示词或产物。

## 安装与检查

下面是作者针对 Linux/macOS 提供的入口；Windows 用户请使用 README 的 `setup.ps1`。

```bash
git clone https://github.com/ZJU-REAL/Easel.git
cd Easel
bash setup.sh
source .venv/bin/activate
easel doctor
easel ping
easel web
```

打开 `http://localhost:7860`，在模型设置中完成配置。安装器使用独立的 `easel` OpenClaw profile。`doctor` 检查环境，`ping` 才实际检查 Gateway 与 Agent 连通；仅安装命令退出成功不代表模型已经可用。

选择 **OpenClaw 连接方式**。Easel 的 API 直连模式可以聊天，但没有本机文件、浏览器和技能执行能力，不能用来复现这里的产物流程。

## 最小案例：龙虾为什么需要一双眼睛

输入使用公开的 [VisionClaw 论文 v2](https://arxiv.org/abs/2604.03486v2)，首次提交于 2026-04-03、v2 修订于 04-08。论文讨论智能眼镜感知与 OpenClaw 任务执行的结合。本案例只制作科普内容，不运行眼镜或购物操作。

| 设置 | 本轮选择 |
|---|---|
| 原文 | `https://arxiv.org/abs/2604.03486v2` |
| 受众 | 第一次接触 Agent 的中文读者 |
| 问题 | 看见海报之后，为什么还要连接一个能执行任务的 Agent？ |
| 形式 | 四格侦探漫画的分镜，暂不出图 |
| 输出目录 | `outputs/visionclaw-detective/` |

将下面整段发给 Easel：

```text
请把 https://arxiv.org/abs/2604.03486v2 做成中文四格侦探漫画分镜。
项目：visionclaw-detective。受众：第一次接触 Agent 的读者。
本轮只提炼和写分镜，不调用图片或视频服务，不发布。

先读取 paper-explainer 的说明，取得并解析原文。保留 paper.pdf、
解析材料和 asset-library.json；解析不了就明确停止在哪一步。
从原文提炼一个问题、方法、证据和局限，每一项附章节/页码定位。
拿不准的数字不写进漫画，作者主张、研究结果和我的类比要分别标注。

漫画线索：一张活动海报 → 角色产生疑问 → 找到感知与执行的分工
→ 回到原文证据并说明局限。侦探角色可以原创，但不能虚构研究结果。
交付 assets/facts.md、storyboard.md、prompts/01-comic.md、review.md。
storyboard.md 每格写：画面、角色动作、短对白、对应原文证据。
review.md 列出待核对内容与下一步需要的图片服务配置。
```

这些文件名是本案例的交付约定；Easel 上游未承诺有同名的「一键侦探漫画」命令。由 Agent 使用已有技能完成组合。

论文解析步骤可在 Easel 根目录单独检查：

```bash
python3 skills/openclaw/paper-explainer/scripts/paper_ingest.py check
python3 skills/openclaw/paper-explainer/scripts/paper_ingest.py fetch --paper https://arxiv.org/abs/2604.03486v2 -o outputs/visionclaw-detective/assets/paper.pdf
python3 skills/openclaw/paper-explainer/scripts/paper_ingest.py parse -i outputs/visionclaw-detective/assets/paper.pdf -o outputs/visionclaw-detective/assets/parsed/
python3 skills/openclaw/paper-explainer/scripts/paper_ingest.py skeleton -o outputs/visionclaw-detective/assets/asset-library.json
```

`skeleton` 只生成骨架，证据和结论还需要 Agent 读原文填充。没有 MinerU 配置时，上游使用 pdfplumber 路径，公式与复杂图表的解析能力较弱；不要把解析缺失当成论文没有相关内容。

## 从分镜变成可分享的图

确认 `facts.md` 与原文一致后，再发送：

```text
按照已核对的 storyboard.md 生成一张四格漫画。
先读取 ai-image-gen，检查 Easel 项目根目录的图片服务配置。
保持同一位原创角色、同一套配色；对白每格最多一句。
图像服务不可用时，保留独立的完整提示文件，不假装图片已生成。
图片保存到 outputs/visionclaw-detective/，返回真实文件路径与生成参数。
我需要检查角色一致性、中文是否清楚、事实是否被图像改变；本轮不发布。
```

服务配置可以先离线检查：

```bash
python3 skills/shared/scripts/ai_image.py check
```

检查完成后再选择该服务支持的图片模型和尺寸。中文文字错误时改提示重新生成；复杂数字、引用与局限可以放在配文中。

## 怎样知道这轮完成了

| 可检查的成果 | 完成条件 |
|---|---|
| 原文与事实清单 | 每条论文主张能定位到原文，类比明确标注 |
| 四格分镜 | 不读论文也能理解一个问题，每格有对应证据 |
| 独立提示文件 | 可以复核、修改并再次生成 |
| 图片（如果调用了服务） | 文件实际存在；中文、角色与内容通过人工检查 |
| 交付记录 | 写清哪些已生成、哪些失败、哪些待核对 |

先分享一个有来源、能看懂的四格成品。读者需要更多细节时，再链接到完整论文和本案例。

## 常见卡点

- **只有漂亮漫画，没有原文定位：**回到事实清单；删掉无法支持的结论，先修分镜再出图。
- **模型接口可用，但 Agent 不能保存文件：**检查连接方式是否为 OpenClaw，以及 `easel ping` 是否成功。
- **解析失败或公式丢失：**保留错误和失败阶段，检查原 PDF／解析材料，暂时只讲已核对的内容。
- **图片服务缺项：**保留 `prompts/`，补配置后重试出图，避免重新提炼整篇论文。
- **作者示范图很好，自己的第一张不稳定：**先减为四格、一个角色、一个核心问题；效果待实际验证。

## 来源

- [Easel 项目与作者示例](https://github.com/ZJU-REAL/Easel)
- [paper-explainer：输入、解析脚本与结构化产物](https://github.com/ZJU-REAL/Easel/blob/main/skills/openclaw/paper-explainer/SKILL.md)
- [ai-image-gen：图片服务配置与调用](https://github.com/ZJU-REAL/Easel/blob/main/skills/openclaw/ai-image-gen/SKILL.md)
- [VisionClaw 论文 v2](https://arxiv.org/abs/2604.03486v2)

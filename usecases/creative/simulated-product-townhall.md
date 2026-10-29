---
title: "给新品开一场模拟用户大会"
description: "从五种角色的目标出发，比较两种产品介绍，整理用户可能提出的问题与后续需求。"
category: "创意与构建"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/simulated-product-townhall/index.html"
  artifactLabel: "打开角色与讨论情境"
  previewPath: "assets/examples/autumn-makers/simulated-product-townhall/preview.svg"
  bundlePath: "assets/bundles/simulated-product-townhall-2026-10-30.zip"
---

# 给新品开一场模拟用户大会

> 从五种角色的目标出发，比较两种产品介绍，整理用户可能提出的问题与后续需求。

## 从不同角色看同一款产品

[打开角色与讨论页](../../assets/examples/autumn-makers/simulated-product-townhall/index.html) · [下载材料包](../../assets/bundles/simulated-product-townhall-2026-10-30.zip)

以桌面阅读清单工具为示例：支持本地收藏、搜索和Markdown导出，使用范围是单机。学生、研究者、运营、隐私敏感用户和偶尔阅读者各有不同目标。切换两种产品介绍，查看他们会问什么，再把问题变成介绍文案、产品需求或访谈提纲。

材料包含[产品与角色配置](../../assets/examples/autumn-makers/simulated-product-townhall/scenario-config.json)、[讨论时间线](../../assets/examples/autumn-makers/simulated-product-townhall/timeline.json)和交互页面。

## 快速体验版（先跑一轮）

```text
读取 assets/examples/autumn-makers/simulated-product-townhall/input.json。
把示例阅读清单工具替换为我提供的产品，写清主要功能和使用范围。
保留五种角色，为每人写一个目标、一个假设，以及针对A/B两种介绍的问题。
把发言标成提问、需求或提醒，并归纳三个值得继续追问的问题。
运行 python3 assets/examples/autumn-makers/simulated-product-townhall/reproduce.py。
打开 index.html，切换两种介绍并检查角色与发言对应。
输出角色配置、timeline.json和讨论页面。
```

浏览器可直接打开页面。重建需要Python 3.10+：

```bash
python3 assets/examples/autumn-makers/simulated-product-townhall/reproduce.py
python3 assets/examples/autumn-makers/simulated-product-townhall/reproduce.py --check
```

在[input.json](../../assets/examples/autumn-makers/simulated-product-townhall/input.json)里修改`facts`、`roles`与`turns`。脚本为每个角色保留A/B两种情境的发言，并生成配置、时间线和HTML。

## 接入MiroFish开展多角色模拟

准备Node.js 18+、Python 3.11—3.12、uv，以及模型API和Zep配置。按[MiroFish源码说明](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/README.md)在独立目录安装：

```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
git checkout 7657031ac01184afe2cb220f5ee3545573b5e843
cp .env.example .env
```

在`.env`填入`LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL_NAME`与`ZEP_API_KEY`，然后启动：

```bash
npm run setup:all
npm run dev
```

前端默认3000，后端5001。以本例`facts`和`roles`为提纲，在MiroFish界面建立图谱、角色与模拟环境。先运行少量角色与轮次，导出讨论记录，再按角色目标整理提问、分歧和需求。模型与Zep按各自服务计费，运行前设置轮次和预算。

## 输出与排错

- 页面显示五种角色，每种角色在两个情境各有一条发言。
- 修改产品功能后，同时更新角色问题和介绍文案。
- 角色ID或情境编号不匹配时，按脚本报错修正`roles`与`turns`。
- MiroFish启动失败时，检查Python、Node、uv和环境变量。
- 模型或Zep连接失败时，检查服务地址、账号额度和对应日志。
- 汇总讨论时，把角色目标、产品功能和后续需求分列，便于安排下一次产品访谈。

## 来源

- [MiroFish：环境、模拟与报告流程](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/README.md)

[打开／复制提示词](../../assets/examples/autumn-makers/simulated-product-townhall.txt) · [回到六案例专题](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

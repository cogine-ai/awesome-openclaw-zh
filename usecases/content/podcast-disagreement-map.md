---
title: "三期播客变成观点分歧地图"
description: "围绕同一个问题比较三段访谈，把共识、条件差异与补充观点连回原文和时间戳。"
category: "内容转换"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/podcast-disagreement-map/index.html"
  artifactLabel: "打开观点关系图"
  previewPath: "assets/examples/autumn-makers/podcast-disagreement-map/preview.svg"
  bundlePath: "assets/bundles/podcast-disagreement-map-2026-10-30.zip"
---

# 三期播客变成观点分歧地图

> 围绕同一个问题比较三段访谈，把共识、条件差异与补充观点连回原文和时间戳。

## 先看一张观点地图

[打开观点关系页](../../assets/examples/autumn-makers/podcast-disagreement-map/index.html) · [下载材料包](../../assets/bundles/podcast-disagreement-map-2026-10-30.zip)

示例用三段访谈讨论“知识库应该整理，还是直接搜索”：[整理派](../../assets/examples/autumn-makers/podcast-disagreement-map/transcripts/a.md)、[搜索派](../../assets/examples/autumn-makers/podcast-disagreement-map/transcripts/b.md)、[情境派](../../assets/examples/autumn-makers/podcast-disagreement-map/transcripts/c.md)。点击“条件差异”“共识”“补充”筛选关系，再点引文返回对应段落。

逐期摘要回答“每期说了什么”，这张图进一步回答“他们是否在讨论同一个对象、时机和条件”。例如，团队交接需要整理，个人临时收藏先搜索，两者可能只是条件不同。

## 快速体验版（先跑一轮）

```text
读取 assets/examples/autumn-makers/podcast-disagreement-map/input.json。
围绕“知识库应该整理还是直接搜索”，比较三段示例访谈。
为每条关系写出类型、结论、至少两段原文引用与对应ref。
检查两段观点的对象和时间点是否一致，再选择共识、条件差异或补充。
运行 python3 assets/examples/autumn-makers/podcast-disagreement-map/reproduce.py。
打开 index.html，筛选一种关系，检查引文能跳到对应段落。
输出观点页、relations.json和三份访谈文本。
```

运行或重建：

```bash
python3 assets/examples/autumn-makers/podcast-disagreement-map/reproduce.py
python3 assets/examples/autumn-makers/podcast-disagreement-map/reproduce.py --check
```

浏览器可直接打开页面。重建需要Python 3.10+。修改[input.json](../../assets/examples/autumn-makers/podcast-disagreement-map/input.json)中的`episodes`与`relations`，即可换访谈主题；关系数据保存在[relations.json](../../assets/examples/autumn-makers/podcast-disagreement-map/relations.json)。

## 用OpenCLI读取自己的播客清单

准备Node.js ≥20.18.1、[OpenCLI](https://github.com/jackwener/OpenCLI/blob/97dc0cd5214b9602bcda78d7422f231ee8a803e9/README.md)及小宇宙本地凭证。节目ID来自选定的节目链接：

```bash
opencli doctor
opencli xiaoyuzhou transcript --help
opencli xiaoyuzhou transcript <episode_id> --output ./transcripts
```

在本机`~/.opencli/xiaoyuzhou.json`配置账号后，读取三期讨论相同问题的节目文本，整理标题、URL、日期和定位方式。节目没有时间戳时，使用段落号。将文本转成`episodes`结构，按同一问题写关系，再运行构建器。

## 输出与排错

- 页面能按关系筛选，引文能定位到访谈段落。
- 每条关系至少保留两处依据；增加“明确冲突”前，先对齐对象、条件与时间点。
- `transcript`返回空时，换用节目方提供的文字稿或自己的访谈稿。
- 浏览器桥接或认证错误时，先运行`doctor`并检查本地版本帮助。
- 引用不存在或短句不匹配时，先修正`ref`和`quotes`，再重建页面。
- 公开页面保留分析、出处与必要短摘录；完整节目文本留在自己的资料目录。

## 来源

- [OpenCLI：小宇宙文本与本地凭证](https://github.com/jackwener/OpenCLI/blob/97dc0cd5214b9602bcda78d7422f231ee8a803e9/README.md)

[打开／复制提示词](../../assets/examples/autumn-makers/podcast-disagreement-map.txt) · [回到六案例专题](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

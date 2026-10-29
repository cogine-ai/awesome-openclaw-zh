---
title: "三份资料变学习包：测验、闪卡与音频接入"
description: "把同一组资料做成10道带依据的测验、12张闪卡和音频导读，适合复习课程、产品知识与团队资料。"
category: "研究与学习"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/sources-to-learning-kit/index.html"
  artifactLabel: "打开测验与闪卡"
  previewPath: "assets/examples/autumn-makers/sources-to-learning-kit/preview.svg"
  bundlePath: "assets/bundles/sources-to-learning-kit-2026-10-30.zip"
---

# 三份资料变学习包：测验、闪卡与音频接入

> 把同一组资料做成10道带依据的测验、12张闪卡和音频导读，适合复习课程、产品知识与团队资料。

## 从一份学习包开始

[打开学习页](../../assets/examples/autumn-makers/sources-to-learning-kit/index.html) · [下载材料包](../../assets/bundles/sources-to-learning-kit-2026-10-30.zip)

示例主题是“给AI结论做事实核对”，包含三份短文、10道测验和12张闪卡。做题后点击“查看依据”回到原文，再用闪卡复习。学习页直接在浏览器打开；重建文件需要Python 3.10+。

三份资料分别解释[结论与依据](../../assets/examples/autumn-makers/sources-to-learning-kit/sources/s1.md)、[工单样本与比例](../../assets/examples/autumn-makers/sources-to-learning-kit/sources/s2.md)、[学习材料组织](../../assets/examples/autumn-makers/sources-to-learning-kit/sources/s3.md)。

## 快速体验版（先跑一轮）

把下面的任务交给有本地文件与Python工具的OpenClaw：

```text
读取 assets/examples/autumn-makers/sources-to-learning-kit/input.json。
以三份短文为来源，更新10道测验和12张闪卡。
每道题保留正确答案、解释、ref和原文中的evidence；每张闪卡只问一个问题。
运行 python3 assets/examples/autumn-makers/sources-to-learning-kit/reproduce.py。
打开 index.html，完成两道题并翻开两张闪卡，检查依据链接。
输出学习页、quiz.json、flashcards.json和三份来源文件。
```

自己运行：

```bash
python3 assets/examples/autumn-makers/sources-to-learning-kit/reproduce.py
python3 assets/examples/autumn-makers/sources-to-learning-kit/reproduce.py --check
```

修改[input.json](../../assets/examples/autumn-makers/sources-to-learning-kit/input.json)即可换主题。`sources`保存资料与段落，`quiz`保存题目、选项及依据，`cards`保存卡片正反面。运行脚本后得到HTML、JSON和Markdown文件。

## 接入NotebookLM制作音频

准备Google账号、NotebookLM额度和[notebooklm-py](https://github.com/teng-lin/notebooklm-py/blob/956400aa7af6b61b4cb988a24c9a081a3abc4ee8/README.md)。在本例目录执行以下命令，将`<notebook_id>`换成创建笔记本返回的ID：

```bash
notebooklm login
notebooklm auth check --test --json
notebooklm create "事实核对练习"
notebooklm use <notebook_id>
notebooklm source add ./sources/s1.md
notebooklm source add ./sources/s2.md
notebooklm source add ./sources/s3.md
notebooklm generate audio "用中文按概念、例子和复习问题介绍这三份资料" --wait
notebooklm download audio ./audio-guide.m4a
```

音频生成使用账号服务额度。试听后调整讲解顺序，也可以用`generate quiz`和`generate flashcards`为同一组资料制作新的练习题。

## 输出与排错

- 页面包含10道题、12张闪卡；每道题可以跳到原文依据。
- 替换来源后，同时更新题目中的`ref`与`evidence`。引用不存在或引文不匹配时，脚本会指出对应题目。
- 闪卡重复时合并同义问题，把空出的卡片留给其他知识点。
- NotebookLM登录失效时运行`auth check`；生成任务排队时用`--wait`等待，额度不足时调整生成数量。
- 下载后打开`audio-guide.m4a`试听，检查中文术语、例子和题目顺序。

## 来源

- [notebooklm-py：安装、账号与生成命令](https://github.com/teng-lin/notebooklm-py/blob/956400aa7af6b61b4cb988a24c9a081a3abc4ee8/README.md)

[打开／复制提示词](../../assets/examples/autumn-makers/sources-to-learning-kit.txt) · [回到六案例专题](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

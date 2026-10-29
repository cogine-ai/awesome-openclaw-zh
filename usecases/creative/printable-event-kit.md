---
title: "让龙虾做能打印的桌牌、贴纸与折页"
description: "把活动名称、姓名和步骤做成可编辑SVG与三页打印PDF。"
category: "创意与构建"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/printable-event-kit/index.html"
  artifactLabel: "查看桌牌、贴纸与折页"
  bundlePath: "assets/bundles/printable-event-kit-2026-10-30.zip"
  previewPath: "assets/examples/autumn-makers/printable-event-kit/preview.png"
---

# 让龙虾做能打印的桌牌、贴纸与折页

> 把活动名称、姓名和步骤做成可编辑SVG与三页打印PDF。

## 把活动信息变成物料

[打开物料展示页](../../assets/examples/autumn-makers/printable-event-kit/index.html) · [下载材料包](../../assets/bundles/printable-event-kit-2026-10-30.zip) · [三页PDF](../../assets/examples/autumn-makers/printable-event-kit/event-kit.pdf)

示例活动是“龙虾周末工坊”。替换活动名称、姓名和步骤，就能制作桌牌、贴纸和折页，适合读书会、工作坊与小型活动。

## 输入与工具

- Python 3.10+、ReportLab 4.4.9。
- [event.json](../../assets/examples/autumn-makers/printable-event-kit/event.json)：活动、主题、姓名与三个步骤。
- [reproduce.py](../../assets/examples/autumn-makers/printable-event-kit/reproduce.py)：生成SVG和PDF。
- 修改SVG可使用Inkscape或其他SVG编辑器。

## 快速体验版（先跑一轮）

```text
读取 event.json 和 reproduce.py，制作活动打印物料。
将活动名称、姓名和步骤换成我提供的内容，在新输出目录运行生成脚本。
保留A5桌牌210×148mm、A4贴纸210×297mm和A4横向三折页297×210mm。
打开三页PDF检查中文、折线和页面尺寸，再按实际大小打印一份纸样。
```

在素材目录运行：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install reportlab==4.4.9
.venv/bin/python reproduce.py --output-dir ./output
```

Windows使用`.venv/Scripts/python.exe`替代`.venv/bin/python`。

## 尺寸与改版

| 文件 | 尺寸 | 使用方式 |
|---|---|---|
| [nameplate.svg](../../assets/examples/autumn-makers/printable-event-kit/nameplate.svg) | 210×148mm，中线74mm | 对折桌牌，两面文字朝外 |
| [stickers.svg](../../assets/examples/autumn-makers/printable-event-kit/stickers.svg) | A4竖向，每枚85×48mm | 自行裁切贴纸 |
| [trifold.svg](../../assets/examples/autumn-makers/printable-event-kit/trifold.svg) | A4横向，折线99/198mm | 等宽三折页 |

修改`event.json`后重新运行，SVG中的文字与形状仍可编辑。打印选择“实际大小／100%”，先用普通纸确认折法和阅读方向，再批量制作。可使用[纸样检查表](../../assets/examples/autumn-makers/printable-event-kit/print-checklist.md)。

PDF使用随包Noto Sans SC字体子集。输入新文字提示`Font lacks`时，用已授权的完整中文TTF：

```bash
.venv/bin/python reproduce.py --output-dir ./output --font /path/to/full-chinese.ttf
```

字体来源与OFL许可随包保存。长标题需要调整字号或换行；印刷厂出血与卷折尺寸按实际纸张另设。

## 常见问题

- 缺字：用`--font`指定包含所需字符的中文字体。
- 折线位置变化：关闭“适合页面”，量出100%打印后的纸张和折线。
- 中文裁切：缩短文字或调整字号，并查看PDF预览。
- 用Inkscape导出：`inkscape trifold.svg --export-type=pdf --export-filename=trifold.pdf`。

## 来源

- [Inkscape命令手册](https://inkscape.org/doc/inkscape-man.html)
- [ReportLab文档](https://docs.reportlab.com/reportlab/userguide/ch2_graphics/)

[回到龙虾造物工坊](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

---
title: "更新日志变成30秒发布片：保留可修改工程"
description: "把三条更新做成横竖版30秒MP4，换一份输入即可制作下一个版本。"
category: "创意与构建"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/changelog-to-release-video/index.html"
  artifactLabel: "播放横竖版30秒发布片"
  bundlePath: "assets/bundles/changelog-to-release-video-2026-10-30.zip"
  previewPath: "assets/examples/autumn-makers/changelog-to-release-video/preview.png"
---

# 更新日志变成30秒发布片：保留可修改工程

> 把三条更新做成横竖版30秒MP4，换一份输入即可制作下一个版本。

## 先播放，再换内容

[打开横竖版播放器](../../assets/examples/autumn-makers/changelog-to-release-video/index.html) · [下载材料包](../../assets/bundles/changelog-to-release-video-2026-10-30.zip) · [横版MP4](../../assets/examples/autumn-makers/changelog-to-release-video/landscape.mp4) · [竖版MP4](../../assets/examples/autumn-makers/changelog-to-release-video/portrait.mp4)

示例介绍阅读清单的三个变化：关键词搜索、Markdown导出与深色按钮。五个六秒章节分别讲开场、三个变化和下一步，使用示意界面，无配音。

适合制作开源更新、产品功能说明和教程短片。横版与竖版共用工程，替换输入即可保持同一套风格。

## 输入与工程

- [props.json](../../assets/examples/autumn-makers/changelog-to-release-video/props.json)：产品、受众、三条更新和结尾。
- [src.tsx](../../assets/examples/autumn-makers/changelog-to-release-video/src.tsx)：排版、动画和两个画幅，24fps、720帧。
- [package.json](../../assets/examples/autumn-makers/changelog-to-release-video/package.json)、[锁文件](../../assets/examples/autumn-makers/changelog-to-release-video/package-lock.json)与[render.mjs](../../assets/examples/autumn-makers/changelog-to-release-video/render.mjs)：依赖与渲染入口。
- [修改版输入](../../assets/examples/autumn-makers/changelog-to-release-video/variant-props.json)、[对照静帧](../../assets/examples/autumn-makers/changelog-to-release-video/variant-preview.png)与[章节字幕](../../assets/examples/autumn-makers/changelog-to-release-video/planned-subtitles.srt)。

使用Node.js与Chrome；工程固定Remotion / CLI 4.0.539、React 19.2.0。团队使用前查看[Remotion许可](https://www.remotion.dev/license)。

## 快速体验版（先跑一轮）

```text
读取 props.json、src.tsx 和 START-HERE.md，制作30秒发布片。
把产品名称、三条更新和结尾替换成我提供的内容。
按锁文件安装依赖，先渲染一张静帧检查中文、标题和画幅。
运行 node render.mjs，导出960×540横版和540×960竖版MP4。
逐段播放检查，保留工程、输入、视频与对照图。
```

在工程目录运行：

```bash
npm ci --ignore-scripts
node render.mjs
```

复用本机Chrome时设置`REMOTION_BROWSER_EXECUTABLE`，具体写法见[运行说明](../../assets/examples/autumn-makers/changelog-to-release-video/START-HERE.md)。

## 先做一帧，再做成片

```bash
npx --no-install remotion still src.tsx Landscape variant.png --frame=192 --props=variant-props.json
```

`--props`使用文件路径，便于处理Windows引号。确认改版的文字、颜色与布局后，再生成完整视频。输出为H.264，每版30秒。

## 常见问题

- Chrome找不到：环境变量应指向可执行文件，而不是`.app`目录；也可使用Remotion管理的浏览器。
- 依赖版本不一致：用`npm ci`安装锁文件中的版本。
- 长标题溢出：缩短标题或降低字号，横竖版分别检查。
- 中文字体变化：使用可分发的固定字体，重新渲染两种画幅。
- 添加旁白：放入授权音频，按音频节奏调整章节长度与字幕。

## 来源

- [Remotion render](https://www.remotion.dev/docs/cli/render)
- [Remotion still](https://www.remotion.dev/docs/cli/still)
- [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills)

[回到龙虾造物工坊](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

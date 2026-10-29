---
title: "让龙虾当3D设计师：做一座微缩工作台"
description: "用场景配置和Blender脚本搭建微缩桌面，自由修改配色、物件与镜头。"
category: "创意与构建"
published: "2026-10-30"
updated: "2026-10-30"
showcase:
  artifactPath: "assets/examples/autumn-makers/lobster-3d-workbench/index.html"
  artifactLabel: "查看设计图与场景脚本"
  bundlePath: "assets/bundles/lobster-3d-workbench-2026-10-30.zip"
  previewPath: "assets/examples/autumn-makers/lobster-3d-workbench/preview.svg"
---

# 让龙虾当3D设计师：做一座微缩工作台

> 用场景配置和Blender脚本搭建微缩桌面，自由修改配色、物件与镜头。

## 看设计，搭场景

[打开设计图](../../assets/examples/autumn-makers/lobster-3d-workbench/index.html) · [下载材料包](../../assets/bundles/lobster-3d-workbench-2026-10-30.zip)

深蓝圆角桌、薄荷色显示器、暖白台灯，再放上一只橙色几何龙虾。这个小场景可以改成自己的书桌、游戏角或工作室，继续换镜头、材质和物件。

## 输入与工具

- Blender 4.5 LTS，使用其内置Python执行脚本。
- [scene.json](../../assets/examples/autumn-makers/lobster-3d-workbench/scene.json)：配色、图片尺寸与镜头位置。
- [build_scene.py](../../assets/examples/autumn-makers/lobster-3d-workbench/build_scene.py)：建立物件、灯光和两个镜头。

## 快速体验版（先跑一轮）

将本例目录交给有本地执行工具的OpenClaw：

```text
读取 scene.json 与 build_scene.py，制作“龙虾工作台”。
使用 Blender 4.5 在新输出目录运行场景脚本，生成 front.png、side.png 和 scene.blend。
打开两张图片检查构图，再重新打开工程确认物件与材质可继续编辑。
把桌面改成我指定的颜色，重新渲染，保留原版与修改版。
```

自行运行：

```bash
blender --background --python build_scene.py -- --output-dir ./output
```

macOS可使用`/Applications/Blender.app/Contents/MacOS/Blender`。Windows在PowerShell用`&`加引号调用实际`blender.exe`路径。

## 改成自己的空间

1. 在`scene.json`修改`palette`中的颜色。
2. 调整`camera.front`与`camera.side`的位置，改变观察角度。
3. 在脚本中增减几何物件，重新运行到另一个输出目录。
4. 先用低分辨率检查构图，再提高`resolution`。

脚本输出两张960×720图片与一个可编辑工程。打开`scene.blend`后，可以继续加动画、调整灯光或制作相机环绕。

## 常见问题

- `No module named bpy`：用Blender的`--python`执行脚本，不使用系统`python3`。
- 渲染慢：先把`resolution`减半，或将`scene.cycles.samples`从24降到8。
- 物件被裁切：调整镜头位置或`ortho_scale`，检查正面和侧面两张图片。

## 来源

- [Blender 4.5命令参数](https://docs.blender.org/manual/en/4.5/advanced/command_line/arguments.html)
- [Blender 4.5 Python API](https://docs.blender.org/api/4.5/)
- [CLI-Anything](https://github.com/HKUDS/CLI-Anything/tree/34f519533bc175d2fe287ab8316b0dd99bb9cc43)：可用于后续Agent控制入口。

[回到龙虾造物工坊](../../resources/08-autumn-makers.md) · [分享自己的版本](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)

OPCBoost · by [Cogine](https://www.cogine.ai/)

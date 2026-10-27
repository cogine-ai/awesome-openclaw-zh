---
title: "数字人口播制作台：先完成26秒离线准备"
description: "实跑固定上游任务规划器，产出三段产品介绍、计划字幕和不可直接提交的任务草稿；未生成视频。"
category: "创意与构建"
published: "2026-10-27"
updated: "2026-10-27"
showcase:
  verification: script-reproduced
  verificationNote: "上游分段脚本已离线实跑；26秒为文字估时，未生成主播、配音或视频，未执行OpenClaw端到端流程。"
  platforms: [macos, windows, linux, browser]
  account: none
  cost: local-free
  artifactPath: assets/examples/digital-human-product-intro/index.html
  artifactLabel: 查看离线口播制作台
  previewPath: assets/examples/digital-human-product-intro/preview.svg
  bundlePath: assets/bundles/digital-human-product-intro-2026-10-27.zip
  testedAt: "2026-10-27"
  testedVersion: "Python 3.12 / 上游 5fa9b19"
  beginner: true
---

# 数字人口播制作台：先完成26秒离线准备

先把一句“介绍我们的项目”变成能审阅的口播制作包。本次为 OPCBoost 写了三段原创产品介绍，用固定上游 `build_tasks.py` 算出 **9、8、9秒，共26秒**的计划时长，再生成字幕和制作台。它们是实际文件，**没有生成数字人、声音或视频**。

## 先看成果，再决定是否生成

- [打开离线制作台](../../assets/examples/digital-human-product-intro/index.html)：逐段查看口播、分辨率和素材缺口。
- [原始口播](../../assets/examples/digital-human-product-intro/script.json)、[计划字幕](../../assets/examples/digital-human-product-intro/planned-subtitles.srt)、[任务草稿](../../assets/examples/digital-human-product-intro/draft-tasks.json)。
- [复现脚本](../../assets/examples/digital-human-product-intro/reproduce.py)和[上游固定信息](../../assets/examples/digital-human-product-intro/provenance.json)。

账号与费用标签对应当前可复现的**离线准备**。继续生成视频需要自己的 Renoise 账号、积分、可用模型和授权素材；目前这些条件不具备，因此报价为未知，任务 `readyToSubmit=false`，素材引用和模型名均为占位符。本包没有提交接口。

## 为什么值得试

上游把口播拆段、画中画、语音检查、字幕对齐与剪辑串成了技能流程。本例先取其中可离线复现的一步，适合把开源项目、教程或更新公告改成短视频脚本。先确定每句话的作用和素材去向，能在真正付费前发现长句、空镜和素材缺口。

本包三段分别承担“用户问题”“已有成果”“参与方式”。第二段计划画中画，画面应使用自己制作的实际网页录屏；目前没有录制这些素材。

## 复现现有结果

需要 Python 3.10+，无需额外依赖或网络。在仓库根目录运行：

```bash
python3 assets/examples/digital-human-product-intro/reproduce.py
```

脚本核对随包上游文件的 SHA-256，在临时目录放入原创演练 persona，再执行**未修改**的上游规划器。最后重新生成本包三个文件，临时目录自动清理。可用 `--output-dir /path/to/output` 输出到别处。

上游规划器要求价格字段才能计算任务。本包内部使用 `1` 个**算术测试单位**作为结构夹具，捕获而不发布其费用输出；它不是 Renoise 报价。公开任务的 `estimatedCredits=null`、`priceStatus=not-quoted` 始终保留。不要把测试单位替换为猜测的积分价格。

时长来自上游每秒5.4字的启发式，尚未与真实口音、停顿、模型输出或 Whisper 转录对齐。计划字幕不能当成最终视频字幕。超出单段15秒会退出，先拆句，再重跑。

## 交给 OpenClaw 改成自己的介绍

将本包完整目录交给具有本地文件与 Python 工具的 Agent，发送：

```text
读取 script.json 和 persona.offline.json，只做离线准备。
保留“问题、已有成果、下一步”三段结构，将介绍对象改为我提供的项目。
所有能力描述必须有项目内事实支持；不要虚构用户量、节省时间或生成结果。
每段不超过上游规划器的15秒估时。运行 reproduce.py，检查实际生成文件。
保留 readyToSubmit=false、未知报价、占位素材引用和模型ID。
输出实际文件路径与仍缺的素材。不要连接媒体服务或提交付费任务。
```

这段是复用入口，本次未在 OpenClaw 内执行。上游作者主要验证 Claude Code 流程，对 OpenClaw 的兼容描述不能代替本地端到端验证。

## 有账号后的最小下一步

1. 上传自己拥有权利的主播参考图与声音；本包没有复用作者的主播形象。
2. 在自己账号查询当前模型、分辨率价格、余额与有效素材引用；确认总预算后才提交一段。
3. 验收口播内容、嘴型、人物一致性与实际时长，再生成其余两段。
4. 用真实音频做对齐、检查画中画遮挡，再决定剪辑和发布。若使用上游 Remotion 模板，先核对其公司授权条件。

离线制作台和脚本可跨平台阅读、运行；上游完整流程的 Apple Vision 人物分割依赖 macOS，不能据此承诺全套跨平台。

## 来源与许可

- [上游固定版本](https://github.com/andyhuo520/digital-human-koubo/tree/5fa9b19f52fb8920c83567468fa30e8391b8c503)，本页于2026-10-27核查。
- [实际运行的任务规划器](https://github.com/andyhuo520/digital-human-koubo/blob/5fa9b19f52fb8920c83567468fa30e8391b8c503/skills/digital-human-koubo/scripts/build_tasks.py)。
- 代码与文档按[上游MIT许可](../../assets/examples/digital-human-product-intro/LICENSE.upstream.txt)保留；[形象限制](../../assets/examples/digital-human-product-intro/NOTICE.upstream.md)和[第三方说明](../../assets/examples/digital-human-product-intro/THIRD_PARTY.upstream.md)随包附上。本包没有复制其演示媒体或模板素材。

可触类旁通：把同一介绍分别做成“案例复现前后”“一分钟排错”“每周三个更新”脚本，再由真人或自己授权的数字人录制。先比较脚本和成片的实际完成成本，再决定长期形式。

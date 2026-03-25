# AI 视频编辑助手

> 用聊天方式完成粗剪、加字幕、转竖屏和批量导出，把重复视频后处理交给 OpenClaw。

## 这个案例能帮你做什么

- 直接用自然语言描述剪辑需求，不必每次都进时间线软件手动拖拽。
- 自动加字幕、裁掉不需要的片段、补背景音乐，并输出适合短视频平台的成片。
- 对多个素材批量执行同一种处理流程，节省重复劳动。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`video-editor-ai`](https://clawhub.ai/skills/video-editor-ai) | 聊天式视频编辑、加 BGM、导出成片 | ClawHub |
| 外部 | [`ai-subtitle-generator`](https://clawhub.ai/skills/ai-subtitle-generator) | 自动字幕、烧录字幕、导出 SRT | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的视频后期助理。
请先帮我预演一个最小剪辑任务：
1. 把这段视频裁到 0:15 到 1:30
2. 加一段偏轻快的背景音乐
3. 自动生成英文字幕并烧录到视频里
4. 导出为 mp4
```

## 稳定自动版（可长期运行）

### 1) 安装所需技能

```bash
clawhub install video-editor-ai
clawhub install ai-subtitle-generator
```

### 2) 单视频处理提示词

```text
Trim this video from 0:15 to 1:30, add background music (something upbeat),
and burn subtitles in English.
```

### 3) 批量处理提示词

```text
I have 5 clips in /videos/raw/. For each one:
- Crop to 9:16 vertical
- Add auto-generated captions at the bottom
- Export as mp4
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的视频编辑助手，请执行「AI 视频编辑助手」流程。
请使用 Skills：video-editor-ai、ai-subtitle-generator。

执行步骤：
1. 先确认输入文件路径和输出格式
2. 按我的自然语言要求做剪辑、裁切和字幕处理
3. 如果我要批量处理，就对整个目录执行同一套规则
4. 输出最终文件路径，并说明做了哪些改动
```

### 5) 输出模板（可选）

```markdown
# 视频处理结果

- 输入文件：
- 输出文件：
- 裁切范围：
- 是否加字幕：
- 是否加背景音乐：
- 输出比例：
```

## 成功标准

- [ ] 能通过自然语言完成一次完整视频后处理。
- [ ] 字幕、裁切和导出设置能按要求落地。
- [ ] 批量处理时，多份素材能复用同一套规则。

## 风险与边界

- 原始场景明确提醒不要把含有人脸、证件、保密屏幕的敏感素材随意上传给第三方处理服务。
- 字幕效果和颜色风格更适合用“结果描述”表达，例如“偏暖”“适合 Shorts”，而不是过度依赖技术参数。
- 时间戳和输出分辨率最好说清楚，否则批量处理时容易出现结果不一致。

## 使用建议

- 先从“剪一条视频”开始，再升级到“目录批量处理”。
- 字幕任务里尽量说明原始语言，尤其是非英语素材。
- 如果你做短视频分发，可以把“转 9:16 + 烧字幕 + 导出 mp4”固定成一条常用模版。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/ai-video-editing.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/ai-video-editing.md)

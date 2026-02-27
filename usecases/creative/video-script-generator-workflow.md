# 视频脚本生成工作流

> 覆盖短视频与长视频脚本，支持系列选题批量生成。

## 这个案例能帮你做什么

- 从“没灵感”到“可拍摄脚本”形成固定流程。
- 统一脚本结构和钩子逻辑，提高内容吸引力。
- 支持批量生成系列脚本，适合稳定更新账号。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `script` 配置能力 | 按平台生成脚本 | OpenClaw Built-in |
| 外部 | `video-agent` / `sora-video-gen` / `veo3-video-gen` / `tube-cog` / `video-cog` / `youtube-title-generator` | 视频相关扩展能力 | ClawHub |

## 快速体验版（先跑一轮）

先做 60 秒短视频脚本：

```text
你是我的 OpenClaw 助手。
请帮我做“视频脚本生成工作流”的预演版：
1. 主题：OpenClaw，平台：抖音，时长：60秒。
2. 按“开场-痛点-解决方案-效果展示-结尾”输出完整脚本。
3. 给出拍摄建议和BGM建议。
4. 本轮只生成脚本，不做批量系列。
```

## 稳定自动版（可长期运行）

### 1) OpenClaw 配置

```bash
# 1. 配置脚本生成
openclaw config set script.platform "douyin,bilibili"
openclaw config set script.style "professional"

# 2. 配置内容优化
openclaw config set script.optimize true
openclaw config set script.add-hooks true

# 3. 配置批量生成
openclaw config set script.batch-mode true
openclaw config set script.series-planning true
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“视频脚本生成工作流”。

执行流程：
1. 根据平台（抖音/B站）和时长生成脚本结构。
2. 短视频优先突出钩子、节奏和转化引导。
3. 长视频输出完整章节脚本和演示段落。
4. 批量模式下按系列主题一次生成多期脚本。
5. 输出脚本质量评分与拍摄建议。
```

## 成功标准

| 任务类型 | 使用前 | 使用后 | 节省时间 | 提升比例 |
|---|---:|---:|---:|---:|
| 短视频脚本 | 60分钟 | 5分钟 | 55分钟 | 91.7% |
| 长视频脚本 | 180分钟 | 15分钟 | 165分钟 | 91.7% |
| 系列规划 | 300分钟 | 20分钟 | 280分钟 | 93.3% |
| 平均 | 540分钟 | 40分钟 | 500分钟 | 92.6% |

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

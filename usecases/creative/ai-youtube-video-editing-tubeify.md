# AI YouTube 视频剪辑（Tubeify）

> 用 Tubeify API 自动删除视频里的停顿和口头禅，让 OpenClaw 接管重复剪辑动作。

## 这个案例能帮你做什么

- 把原始视频 URL 交给 OpenClaw，由 Tubeify 自动剪掉长停顿和口头禅。
- 不打开剪辑软件，也能完成一次短视频粗剪和导出。
- 适合 YouTuber、播客剪辑、课程录屏和短视频团队先做批处理。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`tubeify`](https://clawhub.ai/esokullu/tubeify) | AI 视频剪辑 API，处理停顿、语速和字幕等参数 | ClawHub |
| 外部 | Tubeify API | 提交视频处理任务并轮询结果 | Tubeify |

## 快速体验版（先跑一轮）

```text
你是我的视频剪辑助手。
请先为这个视频生成 Tubeify 处理计划：
视频 URL：[视频 URL]
目标：
1. 删除超过 0.5 秒的停顿
2. 保持原始语速
3. 不改变视频比例
4. 本轮只输出请求参数，不要提交任务或付款
```

## 稳定自动版（可长期运行）

### 1) OpenClaw 执行提示词（自动版）

```text
你是我的视频剪辑助手，请使用 Tubeify 处理以下视频：

视频 URL：[URL]
处理要求：
1. 删除长停顿
2. 保持 1.0x 语速
3. 如需字幕，先确认语言和字幕样式
4. 任务提交前展示费用、参数和风险
5. 任务完成后返回下载链接和处理摘要
```

### 2) 输出模板

```markdown
# Tubeify 处理结果

- 输入视频：
- 处理参数：
- 任务 ID：
- 状态：
- 下载链接：
- 注意事项：
```

## 成功标准

- [ ] 能生成明确的 Tubeify 请求参数。
- [ ] 真实提交前会确认费用和视频 URL。
- [ ] 完成后能返回下载链接或任务状态。

## 风险与边界

- 涉及付费处理，提交任务和付款前必须请求用户确认。
- 不要上传包含人脸、证件、客户资料、会议录屏等敏感素材。
- 视频长度、格式和费用限制以 Tubeify 当前 API 文档为准。

## 引用来源

- 来源 PR： [cogine-ai/awesome-openclaw-zh#7](https://github.com/cogine-ai/awesome-openclaw-zh/pull/7)
- 官网： [tubeify.xyz](https://tubeify.xyz)
- Skill 文档： [tubeify.xyz/skills.md](https://tubeify.xyz/skills.md)

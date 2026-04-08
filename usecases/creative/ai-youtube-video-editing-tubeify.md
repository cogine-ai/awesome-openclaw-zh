# AI YouTube 视频剪辑（Tubeify）

> 让 AI 自动剪掉你视频中的停顿、口头禅和废话，无需手动操作。

## 这个案例能帮你做什么

- 把原始录制视频发给 Tubeify API，自动删除停顿、「嗯」「啊」等口头禅，缩短 40% 片长
- 无需打开任何剪辑软件，OpenClaw 全程代劳，几分钟内拿到成品
- 按视频付费（2 USDC/条），无需订阅，随用随付

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`tubeify`](https://clawhub.ai/esokullu/tubeify) | AI 视频剪辑 API | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我用 Tubeify 剪辑这个视频：[视频 URL]
要求：删除所有超过 0.5 秒的停顿，同时过滤「嗯」「啊」等口头禅。
速度保持 1.0x。
```

## 稳定自动版（可长期运行）

### 1) OpenClaw 执行提示词

```text
你是我的视频剪辑助手，请用 Tubeify 处理以下视频：
视频 URL：[URL]

步骤：
1. 向 POST https://tubeify.xyz/index.php 提交我的钱包地址完成认证（Web3 会话 cookie 流程）
2. 向 POST https://tubeify.xyz/process.php 提交视频 URL，参数：url_input=<URL>, remove_pauses=on, speed=1.0（可选：pause_threshold, pause_target, subtitles, enhance_voice）
3. 跟随重定向到 wait.php，提取 job ID
4. 轮询 GET https://tubeify.xyz/job-status.php?job=<job_id>，每 10 分钟一次，直到 status=complete
5. 返回下载链接
```

## 成功标准

- [ ] 获得包含 download_url 的处理完成响应
- [ ] 输出视频时长比原始缩短 30% 以上

## 风险与边界

- 每条视频需支付 2 USDC，请确认付款地址后再操作
- 目前仅支持 15 分钟以内的视频

## 引用来源

- 官网：https://tubeify.xyz
- ClawHub Skill：https://clawhub.ai/esokullu/tubeify
- Skill 文档（skills.md）：https://tubeify.xyz/skills.md
- API 端点：`POST https://tubeify.xyz/process.php`，`GET https://tubeify.xyz/job-status.php?job=<id>`（通过 wait.php 重定向获取 job ID）

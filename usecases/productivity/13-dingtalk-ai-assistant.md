# 钉钉 AI 助手

> 把 OpenClaw 接进钉钉，让团队在原有办公群里直接触发 AI 任务。

## 这个案例能帮你做什么

- 在钉钉私聊或群聊中直接与 OpenClaw 对话，不要求团队成员切换新工具。
- 使用钉钉 Stream 模式接收消息，个人电脑或内网机器也可以先跑通。
- 支持群聊中 @ 机器人触发，避免普通讨论被 AI 频繁打断。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`@soimy/dingtalk`](https://github.com/soimy/openclaw-channel-dingtalk) | 钉钉通道插件，连接 OpenClaw 与钉钉机器人 | 社区插件 |
| 外部 | 钉钉开放平台应用 | 获取 Client ID / Client Secret 并开启机器人能力 | 钉钉开放平台 |

## 快速体验版（先跑一轮）

```text
你是我的钉钉 AI 助手。
请在这个钉钉会话中完成一次最小测试：
1. 用 3 条内容说明你已经收到消息
2. 总结你可以处理的办公任务类型
3. 不要执行任何外部写入动作
```

## 稳定自动版（可长期运行）

### 1) 创建钉钉应用

在钉钉开放平台创建企业内部应用，开启机器人能力，记录：

- Client ID / AppKey
- Client Secret / AppSecret
- 消息接收模式：优先选择 Stream 模式

### 2) 安装通道插件

```bash
openclaw plugins install @soimy/dingtalk
```

将插件加入 OpenClaw 插件 allowlist：

```json
{
  "plugins": {
    "enabled": true,
    "allow": ["@soimy/dingtalk"]
  }
}
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是公司钉钉 AI 助手。
当用户在群里 @ 你时，请按下面规则处理：
1. 先判断任务类型：信息查询、文档整理、会议纪要、待办拆解、技术排障
2. 如果任务需要访问外部系统，先说明需要的权限和数据范围
3. 对写入、删除、发送外部消息等动作，必须先请求确认
4. 输出要适合钉钉群阅读：结论先行，步骤清晰
```

## 成功标准

- [ ] 钉钉私聊能收到 OpenClaw 回复。
- [ ] 群聊中只有 @ 机器人时才触发。
- [ ] 高风险动作会先请求确认。

## 风险与边界

- 企业群里不要默认开放 shell、文件系统、账号后台等高权限工具。
- 群聊上下文可能包含敏感业务信息，建议配置 allowlist 和 pairing。
- 通道插件版本会影响多媒体消息支持范围，生产使用前要先验证图片、文件、语音等类型。

## 引用来源

- 来源仓库： [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)
- 原始条目： [usecases/cn-dingtalk-ai-assistant.md](https://github.com/AlexAnys/awesome-openclaw-usecases-zh/blob/main/usecases/cn-dingtalk-ai-assistant.md)
- 通道插件： [soimy/openclaw-channel-dingtalk](https://github.com/soimy/openclaw-channel-dingtalk)

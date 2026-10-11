---
published: 2026-10-11
updated: 2026-10-11
status: "文档组合，待实测"
source_date: 2026-10-11
---

# 让 Agent 进入会议：实时听、答与留下纪要

> 让 OpenClaw 加入一个受控会议，先验证字幕记录，再逐步启用语音参与。

## 来源与验证状态

| 项目 | 说明 |
|---|---|
| 内容性质 | 文档组合：官方 Meeting plugins 与 Google Meet 工具指南 |
| 文档基线 | OpenClaw `v2026.10.1` 的会议插件文档 |
| 查阅日期 | 2026-10-11 |
| 最近更新证据 | `v2026.9.5` 于 2026-09-19 发布，扩展 GPT Live 到会议；`v2026.9.6` 更新实时纪要路径 |
| 本仓库验证 | 已核对模式、安装与依赖；未加入实际会议，未验证远端可听性、字幕或费用 |

## 这个案例能帮你做什么

- 让 Agent 在 Meet、Teams、Zoom，或已开启的 Slack huddle 中参与讨论。
- 先用只观察的模式获取会议字幕，再选择普通 Agent 回答或低延迟实时语音。
- 会议结束后查看保存的字幕与纪要，而不是手动把录音上传给模型。

这里的“进入会议”覆盖会议参加与语音路径。Teams、Zoom 插件不因此获得创建会议、调用厂商 API 或录制音视频的能力。

## 三种模式先选一种

| 模式 | 行为 | 前置条件 |
|---|---|---|
| `transcribe` | 只观察，提供可用字幕的有限实时尾部 | 平台确实提供字幕；不需要虚拟音频桥 |
| `agent` | 转写交给普通 OpenClaw Agent，TTS 发声 | 转写提供者、TTS、受支持的虚拟音频桥 |
| `bidi` | 实时语音模型直接听和答，支持时委派 Agent | 实时语音授权与模型、受支持的音频桥 |

第一次推荐 `transcribe`。如果平台或主持人未提供字幕，这个模式不会凭空转写音频。

## 开始前需要什么

- 可以访问会议的 Chrome 环境，以及平台要求的登录、主持人准入或浏览器权限。
- 只安装自己使用的平台插件。消息渠道插件与会议参加插件是不同组件。
- 受控测试会议与第二位参与者，用来确认真实入会、字幕、远端听到的声音与打断效果。
- 启用说话时，Chrome 所在机器需要虚拟音频依赖；远程 Chrome node 还需允许对应平台命令与 `browser.proxy`。

只加入你有权添加 Agent 的会议，并按实际会议规则告知自动参加和转写行为。

## 最小设置：Google Meet 只观察

```bash
openclaw plugins install @openclaw/google-meet
```

将 Google Meet 的默认模式设置为只观察：

```json5
{
  plugins: {
    entries: {
      "google-meet": {
        config: { defaultMode: "transcribe" },
      },
    },
  },
}
```

运行官方 setup 检查：

```bash
openclaw googlemeet setup
```

任何失败都先按返回信息处理，不能把插件安装成功当作会议路径已经可用。

## 快速体验

创建一个只用于测试的会议，打开字幕，替换下面的链接：

```text
请加入这个测试会议：[Google Meet 链接]。
使用 transcribe 模式，显示名称清楚标明是 AI 助手。
先返回实际入会状态和 sessionId。
收到字幕后，只根据已收到的内容整理议题、决定、负责人和待办。
没有字幕时说明缺失，不补写会议内容。
我说“结束”时使用会议工具 leave，并报告结束状态。
```

也可用官方 CLI 加入，示例 URL 需要替换为自己的会议：

```bash
openclaw googlemeet join 'https://meet.google.com/abc-defg-hij'
```

入会 `status`、等待主持人准入、出现字幕和生成纪要是不同阶段，应分别核对。

## 再启用语音参加

先按官方 [会议音频指南](https://docs.openclaw.ai/plugins/meeting-plugins#prepare-chrome-and-audio) 配置 Chrome 所在主机。macOS 文档给出的依赖为：

```bash
brew install blackhole-2ch sox
```

官方还要求重启并检查音频设备；这是一次性主机设置，不应在正在使用的会议中临时执行。Linux 使用桌面用户的 PipeWire-Pulse 音频会话。

要走 `agent` 模式，配置转写和 TTS；要走 `bidi`，配置已有实时语音授权及模型。以下是官方 GPT Live 配置中的核心字段，需账户实际支持：

```json5
{
  plugins: {
    entries: {
      "google-meet": {
        config: {
          defaultMode: "bidi",
          realtime: {
            voiceProvider: "openai",
            model: "gpt-live-1-codex",
            providers: { openai: { voice: "cove" } },
          },
        },
      },
    },
  },
}
```

模型授权、音频桥和远端可听性都要验证。官方文档中的 `speechOutputVerified` 证明本地麦克风注入；仍需第二位参与者确认会议里实际听到，以及说话时能否打断。

## 输出与失败处理

- 三种模式都可保存已经完成的字幕行与会议纪要；有新语音时纪要约每五分钟更新，离会后写最终摘要。
- 可用 `openclaw transcripts` 查看、检查或导出保存记录；这不等于创建了音视频录像。
- `manualAction` 返回登录、验证码、准入或权限步骤时，在同一 Chrome profile 完成，不反复创建新标签页。
- 没有字幕、音频依赖缺失、提供者授权失败时，停止对应路径并记录原因。
- 用明确的 `leave` 结束会议；清理失败时继续检查该 session，而不是立即发起另一次入会。

## 引用来源

- [固定版本：Meeting plugins 的模式、音频与入会检查](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/plugins/meeting-plugins.md)
- [Google Meet 工具与状态](https://docs.openclaw.ai/plugins/google-meet/tool-and-modes)
- [Google Meet 配置：GPT Live with Cove](https://docs.openclaw.ai/plugins/google-meet/config#gpt-live-with-cove)
- [v2026.9.5 发布记录：2026-09-19](https://github.com/openclaw/openclaw/releases/tag/v2026.9.5)
- [2026.9.6 实时会议纪要更新](https://docs.openclaw.ai/releases/2026.9.6)

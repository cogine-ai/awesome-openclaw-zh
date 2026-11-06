---
title: "换 Agent 不重新讲一遍：共享记忆的纠正与接棒实验"
description: "用 Sno Station 探索共享记忆，让一个客户端纠正事实，另一个客户端读取新版本。"
category: "内存管理"
published: "2026-10-27"
updated: "2026-10-27"
showcase:
  verification: experimental
  platforms: [macos, linux]
  account: none
  cost: local-free
  artifactPath: "assets/examples/cross-agent-memory-handoff/index.html"
  artifactLabel: "查看记忆纠正流程"
  previewPath: "assets/examples/cross-agent-memory-handoff/preview.svg"
  bundlePath: "assets/bundles/cross-agent-memory-handoff-2026-10-27.zip"
  testedAt: "2026-10-27"
  testedVersion: "Sno Station v1.6.0 / 5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363"
  beginner: false
---

# 换 Agent 不重新讲一遍：共享记忆的纠正与接棒实验

> 把一份记忆写入、纠正并交给另一个客户端读取，让后续 Agent 接上当前事实。

## 先看记忆纠正流程

[打开共享记忆接入示例](../../assets/examples/cross-agent-memory-handoff/index.html)，查看两版输入、接口流程和本地运行入口。这是一条基于 Sno Station 的接入实验路线。

## 版本与选题依据

[Sno Station v1.6.0](https://github.com/sno-ai/sno-station/releases/tag/v1.6.0) 发布于 2026-10-23，固定提交 [`5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363`](https://github.com/sno-ai/sno-station/tree/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363)，Apache-2.0 许可。它是社区共享记忆方案，支持 Codex、Claude Code、OpenClaw 等宿主；不是 OpenClaw 官方内置能力。

Sno Station v1.6.0 支持写入、检索和保留历史的纠正，并将检索后的重排放在本地。

本例使用两个 API 客户端访问同一个新建 profile，依次完成写入、读取、纠正和当前事实召回。可以用它作为 Agent 共享记忆的起点。

## 前置条件与费用

| 路径 | 要求与边界 |
|---|---|
| 查看成果页、离线核对 | 浏览器；运行核对器需 Python 3.10+。不需要账号、模型或网络。 |
| 真正运行服务演练 | macOS 或 Linux，Node 22.22.3+、24.15.0+ 或上游支持的更新版本，npm；首次获取依赖及约 **639MB** 本地 embedding 模型需网络、磁盘空间和 CPU。 |
| 本例设置 | Local First；重排 `none`；全部 LLM 路由 `off`；REM、遥测和会话采集关闭。无需模型 API key 或 Sno 账号。 |
| 后续真实 Agent 接棒 | 需另行安装相应宿主插件、核对模式和数据去向，并用实际会话验收。本例没有修改任何真实 Agent 配置、Hook 或调度器。 |

上游的不同模式有不同数据边界：Local First 不把记忆文字送到 Sno；Agent Native 默认的夜间学习与 REM Enhanced 涉及其他处理路径。不能用本例的关闭设置，推断安装器或其他模式也会沿用相同设置。请阅读[固定版本安全说明](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/docs/security.md)。

## 打开示例页面

在本仓库根目录运行：

```bash
python3 assets/examples/cross-agent-memory-handoff/reproduce.py --verify
```

输出会明确写 `memory operations remain UNVERIFIED`。它核对输入 SHA-256、状态记录、HTML 和派生 SVG，不调用 Sno。复制到新目录再看：

```bash
python3 assets/examples/cross-agent-memory-handoff/reproduce.py --out /tmp/memory-handoff-preview
```

将结果输出到一个新目录。[receipt.json](../../assets/examples/cross-agent-memory-handoff/receipt.json)保存输入版本与运行记录。

## 最小公开输入

[fixture.json](../../assets/examples/cross-agent-memory-handoff/fixture.json)包含以下虚构演练事实。它们不是公司承诺或用户口述：

```json
{
  "original": "Public rehearsal: the OPCBoost demo handoff deadline is October 30, 2026.",
  "corrected": "Public rehearsal: the OPCBoost demo handoff deadline is October 31, 2026.",
  "query": "What is the OPCBoost demo handoff deadline in this public rehearsal?"
}
```

准备检查的顺序：`store → reader get → correct → reader get old/new → recall current → store/forget temporary`。目标是旧条目保留 `superseded_by` 关联、当前召回只出现修订文本、临时演练记忆删除后不可按原 ID 读取。这些是代码中的**待运行断言**，当前未通过运行证明。

固定 1.6.0 的 API 有两个需要分清的细节：`inspect(get)` 读取退役条目时，会在原文后追加 `\nretired; superseded by <新ID>`；检查器同时核对这个后缀、原文与 metadata 中的 `superseded_by`，而不是要求返回文本仍与原文完全相同。显式 `source:"manual"` 召回会保留退役历史，因此当前事实检查使用 `source:"auto", injectionPhase:"prompt"`，并验证新版 ID/文本出现、旧版 ID/文本均排除。未来成功回执只将已经验证一致的真实新版 ID 替换为 `memory-v2` 别名，明确保留这项归一说明。

## 在隔离目录实际运行

下面会安装临时依赖，并下载约 639 MB 的 embedding 模型。请使用新建 profile；已有 profile 的密钥与数据应按原设置保留。

```bash
mkdir /tmp/sno-public-runtime
cp assets/examples/cross-agent-memory-handoff/package.json /tmp/sno-public-runtime/package.json
npm install --prefix /tmp/sno-public-runtime --legacy-peer-deps --no-audit --no-fund
python3 assets/examples/cross-agent-memory-handoff/reproduce.py \
  --run --runtime /tmp/sno-public-runtime --out /tmp/memory-handoff-real-run
```

依赖版本为 `@snoai/memory@1.6.0`、`@snoai/embedder@1.2.1`。npm 12 需要按上游说明允许原生依赖的安装脚本。

[run-memory.mjs](../../assets/examples/cross-agent-memory-handoff/run-memory.mjs)沿用官方 `SNO_PROFILE_DIR` 隔离接口，在临时目录创建独立加密库和随机密钥。它手动启动只属于本次演练的前台 sidecar，使用两个明确叫 `public-fixture-writer/reader` 的 API 客户端，设置所有 LLM 路由关闭，并拒绝覆盖已有 profile 或结果。

只有六组真实断言全部成功，运行器才导出白名单结果；失败则退出，不写成功回执。Python 包装器为该 Node 运行器创建独立进程组，结束或超时后清理它，再删除临时 profile 和密钥；模型缓存与安装依赖留在你明确指定的 runtime，方便重试。它不运行 `sno setup`，不改变 `HOME`，不读取真实会话或宿主 Agent 配置。

## 交给 Agent 继续接入

可以把下面任务交给已配置的 Agent：

```text
先核对 Sno 1.6.0 的官方宿主接入方式与隔离 profile，
只使用公开演练目录，不读取或导入任何真实会话。
让第一个真实 Agent 写入演练事实，再由我纠正日期；
让第二个真实 Agent 取回当前事实，并给出引用的记忆 ID 与旧新关联。
分别记录 API 检查、真实宿主调用和用户确认，不能用两个脚本客户端冒充 Agent。
任何安装、模型下载或认证失败都如实停止；不补写模拟成功记录。
```

## 来源与许可

- [固定版本记忆服务设置](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/docs/memory-setup.md)
- [官方独立 profile 与 MemoryClient 接口](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/packages/memory/src/contract/client.ts)
- [store / correct / forget / inspect 请求类型](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/packages/memory/src/contract/inputs.ts)
- [固定 API 的退役条目显示与自动召回实现](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/packages/memory/src/engine/contract-runtime.ts)
- [上游纠正与历史回归](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/tests/packages/memory/integration/mem-update.test.ts)。
- [Apache-2.0 许可副本](../../assets/examples/cross-agent-memory-handoff/LICENSE-upstream.txt)与 [NOTICE](../../assets/examples/cross-agent-memory-handoff/NOTICE-upstream.txt)

由 Cogine 团队整理示例输入、本地运行入口与展示页。
---
title: "换 Agent 不重新讲一遍：共享记忆的纠正与接棒实验"
description: "用 Sno Station v1.6.0 准备可追溯的公开记忆演练；附隔离服务入口与真实未通过状态，不把两个API客户端冒充跨Agent实测。"
category: "内存管理"
published: "2026-10-27"
updated: "2026-10-27"
showcase:
  verification: experimental
  verificationNote: "已核固定源码、发布版本、隔离配置和API；临时依赖安装未在预算内完成，未启动服务、未跑CRUD/召回或真实Agent接棒。离线核对与Node语法检查通过。"
  platforms: [macos, linux]
  account: none
  cost: local-free
  artifactPath: "assets/examples/cross-agent-memory-handoff/index.html"
  artifactLabel: "查看演练输入与验证状态"
  previewPath: "assets/examples/cross-agent-memory-handoff/preview.svg"
  bundlePath: "assets/bundles/cross-agent-memory-handoff-2026-10-27.zip"
  testedAt: "2026-10-27"
  testedVersion: "Sno Station v1.6.0 / 5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363（源码与npm版本核对，服务未运行）"
  beginner: false
---

# 换 Agent 不重新讲一遍：共享记忆的纠正与接棒实验

> 第一个 Agent 记住了一件事，后来你纠正了它。换一个 Agent 时，能否拿到新版本，同时保留旧版本从何而来？这件事值得先独立验证。

## 先看交付与状态

[打开公开演练输入与状态页](../../assets/examples/cross-agent-memory-handoff/index.html)。这里展示两版原创输入、准备验证的接口流程、真实运行限制和可以继续执行的隔离入口。

**本例目前是实验，运行尚未通过。** 本轮已读取固定源码并核对 npm 包 `1.6.0`，在新建临时目录尝试安装依赖；必需的 ONNX 原生运行库取回未在约 11 分钟依赖预算内完成，主动中止。没有启动 Sno 服务、没有开始下载 embedding 模型，也没有执行记忆 CRUD、纠正召回或真实 Agent 接棒。没有用 mock 或预填的“成功结果”替代这些步骤。

离线重放器只能证明：公开输入与该未通过状态记录一致，HTML / SVG 可以从它们重建。它不会把实验状态升级为“服务已验证”。

## 版本与选题依据

[Sno Station v1.6.0](https://github.com/sno-ai/sno-station/releases/tag/v1.6.0) 发布于 2026-10-23，固定提交 [`5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363`](https://github.com/sno-ai/sno-station/tree/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363)，Apache-2.0 许可。它是社区共享记忆方案，支持 Codex、Claude Code、OpenClaw 等宿主；不是 OpenClaw 官方内置能力。

这次版本把检索后的重排保持在本地；本地模型尚未就绪或超时时，保留初始搜索结果。基础记忆能力包括写入、检索及保留历史的纠正。这个案例使用该稳定版本检验“接棒前的记忆底座”；不把既有共享记忆宣称为 1.6.0 首次新增。

本例目标是先把最小边界跑清楚：两个真实 API 客户端访问同一个**新建公开演练 profile**，检查纠正后的当前事实与历史。即使这段将来跑通，也只能证明服务接口共享，不等于 Codex / OpenClaw 自动接棒成功。

## 前置条件与费用

| 路径 | 要求与边界 |
|---|---|
| 查看成果页、离线核对 | 浏览器；运行核对器需 Python 3.10+。不需要账号、模型或网络。 |
| 真正运行服务演练 | macOS 或 Linux，Node 22.22.3+、24.15.0+ 或上游支持的更新版本，npm；首次获取依赖及约 **639MB** 本地 embedding 模型需网络、磁盘空间和 CPU。 |
| 本例设置 | Local First；重排 `none`；全部 LLM 路由 `off`；REM、遥测和会话采集关闭。无需模型 API key 或 Sno 账号。 |
| 后续真实 Agent 接棒 | 需另行安装相应宿主插件、核对模式和数据去向，并用实际会话验收。本例没有修改任何真实 Agent 配置、Hook 或调度器。 |

本轮只在 macOS arm64、Node `v24.22.1` 尝试依赖准备；Linux 没有本地运行验证。依赖较重，因此不标为新手起步案例。

上游的不同模式有不同数据边界：Local First 不把记忆文字送到 Sno；Agent Native 默认的夜间学习与 REM Enhanced 涉及其他处理路径。不能用本例的关闭设置，推断安装器或其他模式也会沿用相同设置。请阅读[固定版本安全说明](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/docs/security.md)。

## 离线核对这次交付

在本仓库根目录运行：

```bash
python3 assets/examples/cross-agent-memory-handoff/reproduce.py --verify
```

输出会明确写 `memory operations remain UNVERIFIED`。它核对输入 SHA-256、状态记录、HTML 和派生 SVG，不调用 Sno。复制到新目录再看：

```bash
python3 assets/examples/cross-agent-memory-handoff/reproduce.py --out /tmp/memory-handoff-preview
```

输出目录必须尚不存在，避免覆盖别人的文件。[receipt.json](../../assets/examples/cross-agent-memory-handoff/receipt.json)只保留版本、公开输入校验和与验证范围，不含安装日志、服务 token、密钥、用户名、邮箱或机器路径。

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

## 在隔离目录实际运行

这是开发者实验入口。以下步骤会安装临时依赖和下载公开模型；本轮依赖安装未完成，后续步骤仍待运行验收。不要对已有的真实 profile 重跑初始化：随机密钥会让原库无法读取。

```bash
mkdir /tmp/sno-public-runtime
cp assets/examples/cross-agent-memory-handoff/package.json /tmp/sno-public-runtime/package.json
npm install --prefix /tmp/sno-public-runtime --legacy-peer-deps --no-audit --no-fund
python3 assets/examples/cross-agent-memory-handoff/reproduce.py \
  --run --runtime /tmp/sno-public-runtime --out /tmp/memory-handoff-real-run
```

目录须为自己新建且未使用的目录。npm 主依赖固定为 `@snoai/memory@1.6.0`、`@snoai/embedder@1.2.1`；本轮未得到完整安装锁文件，**不声称全部传递依赖已固定或安装已验证**。npm 12 默认阻止安装脚本时，应按上游文档在**这个临时 runtime** 中处理原生依赖的脚本许可；不要直接把命令套到真实记忆目录。

[run-memory.mjs](../../assets/examples/cross-agent-memory-handoff/run-memory.mjs)沿用官方 `SNO_PROFILE_DIR` 隔离接口，在临时目录创建独立加密库和随机密钥。它手动启动只属于本次演练的前台 sidecar，使用两个明确叫 `public-fixture-writer/reader` 的 API 客户端，设置所有 LLM 路由关闭，并拒绝覆盖已有 profile 或结果。

只有六组真实断言全部成功，运行器才导出白名单结果；失败则退出，不写成功回执。Python 包装器为该 Node 运行器创建独立进程组，结束或超时后清理它，再删除临时 profile 和密钥；模型缓存与安装依赖留在你明确指定的 runtime，方便重试。它不运行 `sno setup`，不改变 `HOME`，不读取真实会话或宿主 Agent 配置。

## 给后续真实 Agent 验收的提示词

下面是待验证的接入任务，不是本轮已完成的记录：

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
- [上游纠正与历史回归](https://github.com/sno-ai/sno-station/blob/5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363/tests/packages/memory/integration/mem-update.test.ts)：本轮只审阅，没有运行该套测试。
- [Apache-2.0 许可副本](../../assets/examples/cross-agent-memory-handoff/LICENSE-upstream.txt)与 [NOTICE](../../assets/examples/cross-agent-memory-handoff/NOTICE-upstream.txt)

由 Cogine 团队编写公开输入、实验运行入口和展示页。对未执行的服务与 Agent 路径保留明确状态，后续只有实际验收后才升级验证等级。

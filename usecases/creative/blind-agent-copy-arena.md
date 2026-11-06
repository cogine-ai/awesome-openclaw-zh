---
title: "文案匿名擂台：先打分，再揭晓写法"
description: "围绕同一份 Brief 比较三种文案，先按统一标准评分，再揭晓写法。"
category: "创意与构建"
published: "2026-10-27"
updated: "2026-10-27"
showcase:
  verification: experimental
  platforms: [macos, windows, linux, browser]
  account: none
  cost: local-free
  artifactPath: assets/examples/blind-agent-copy-arena/index.html
  artifactLabel: 试玩文案匿名评分
  previewPath: assets/examples/blind-agent-copy-arena/preview.svg
  bundlePath: assets/bundles/blind-agent-copy-arena-2026-10-27.zip
  testedAt: "2026-10-27"
  testedVersion: "离线Python/Node；原生契约 main@43dc38e"
  beginner: false
---

# 文案匿名擂台：先打分，再揭晓写法

给三个候选同一份事实和评分表，先看文字，再看来源。这个玩法可以用来选开场白、标题、案例推荐语，也可以在具备原生能力的 OpenClaw 主机上研究“模型知道自己身份时，回答是否改变”。两种实验必须分开记录。

## 现在就能玩的成果

- [打开三选一评分台](../../assets/examples/blind-agent-copy-arena/index.html)：按具体、可信、行动三个维度各打0–5分，锁定后揭晓文案写法。
- [公开Brief与三句候选](../../assets/examples/blind-agent-copy-arena/brief.json)：明确受众、已知事实与禁止虚构的承诺。
- [复现脚本](../../assets/examples/blind-agent-copy-arena/reproduce.py)、[原生适配函数](../../assets/examples/blind-agent-copy-arena/native-trial.mjs)、[契约回归](../../assets/examples/blind-agent-copy-arena/test-native.mjs)。

页面内有三份示例文案：先匿名打分，再揭晓各自的写法。评分保存在当前页面，刷新后可以重新比较。

## 复现离线界面

Python 3.10+ 即可重建，浏览器可直接打开，无服务账号：

```bash
python3 assets/examples/blind-agent-copy-arena/reproduce.py
```

同一份输入固定到同一组A/B/C，方便复查。更换真实试验结果时应另存原始回答和分配表，再使用事先确定的随机分配；本包的固定顺序是演练回放，不是严谨试验随机化。

若有 Node.js 22+，可运行：

```bash
node assets/examples/blind-agent-copy-arena/test-native.mjs
```

这条命令用假主机检查适配函数：缺少能力时拒绝启动；启动参数必须 `context:"isolated"`、`blind:true`；真实失败状态保留。它**没有调用 OpenClaw 或模型服务**。

## 原生 blind 的适用边界

2026-10-27核查的 [OpenClaw main文档](https://github.com/openclaw/openclaw/blob/43dc38e6c1370e7682156b8a84ed6fc1abfaa0b7/docs/plugins/sdk-runtime/background-work.md)描述了 `native-subagent-blind-v1`。支持它的主机可从 OpenClaw 自己构造的子Agent提示中省去模型和部分运行身份字段；它要求隔离上下文，并限制运行形态。

接入原生 blind 能力前，先确认主机提供对应接口；否则使用本页的示例文案完成评分体验。

原生模式也不是安全边界：工具返回、模型自己的内置提示、供应商差异仍可能暴露线索。它不提高权限，不证明请求指定的模型一定实际执行。父级应保留主机的选择回执、完成状态和原始结果。

## 在兼容主机接入

本包 `native-trial.mjs` 是供已有插件调用的小函数，**不是可直接安装的插件**。需要在符合上游要求、已获当前请求者授权的 `reply_dispatch` 处理器中调用：

```javascript
import { runBlindTrial } from './native-trial.mjs';
// api 必须来自当前 OpenClaw 插件处理器，不能自行拼造。
const receipt = await runBlindTrial(api, reviewedTask, 'opcboost-copy-trial-a-v1');
// 审查 accepted 与 collected 的真实状态后再收录回答。
```

适配函数使用主机提供的 `spawn/collect` 方法。同一试验保持 `requestId` 一致，改任务后换一个 ID，再收集完整回答。

一轮真正的文案试验可这样做：

1. 冻结 Brief、事实、长度约束和评分表，选择一项要比较的因素；别同时改变模型、提示和输入。
2. 在符合条件的原生运行中收集回答及回执，失败和截断单独记录，不用空文本替补。
3. 在评分前隐藏候选来源、随机安排顺序，由不了解分配的人评分；候选里若自报身份，应标记污染。
4. 评分锁定后再揭晓。多轮、多人重复，再讨论具体任务上的差异；一次选择不能外推为“某模型更强”。

浏览器评分体验无需账号。原生运行需要配置文本模型，费用按自己的模型设置计算。

## 可继续创造的玩法

- **案例开场白挑战**：每周用同一Brief比较“成果先行”和“问题先行”，发布时附输入与选择理由。
- **错误答案找茬**：把夸大承诺混入人工练习，让读者先辨认哪一句超出证据；清楚标明教学用途。
- **标题与正文一致性**：候选必须引用真实案例材料，评分时增加“标题能否在正文兑现”一项。

选一个方向替换输入，再比较结果。[工具与来源](../../assets/examples/blind-agent-copy-arena/provenance.json)随包提供；界面与适配代码遵循仓库许可。
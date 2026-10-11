---
published: 2026-10-11
updated: 2026-10-11
status: "文档组合，待实测"
source_date: 2026-10-11
---

# Lobster 交互工作流：暂停、补充信息、从原处继续

> 让多步骤工作在需要人类反馈时保存进度，收到结构化回答后继续执行。

## 来源与验证状态

| 项目 | 说明 |
|---|---|
| 内容性质 | 文档组合：官方 Lobster 插件指南与 `ask`、`pick` 实现 |
| 版本基线 | OpenClaw `v2026.10.1`；该版本插件依赖 Lobster `2026.9.14` |
| 查阅日期 | 2026-10-11 |
| 最近更新证据 | 2026-10-11 台湾时间发布的 `v2026.10.1` 明确列出交互输入、修正回答与取消支持 |
| 本仓库验证 | 已核对固定版本的语法；未运行 Gateway 插件或验证跨会话恢复 |

## 这个案例能帮你做什么

- 稿件审阅、方案选择或资料补齐时，让执行流程在问题处暂停。
- 把用户回答按 JSON Schema 验证；不合格回答可以修正，不必从第一步重做。
- 在同一个流程里连续遇到多个问题或批准点，并在需要时取消剩余步骤。

适合步骤相对确定、但中途需要人类判断的工作。普通聊天中的“等我确认”不等于持久工作流检查点。

## 开始前需要什么

| 依赖 | 说明 |
|---|---|
| 可用的 OpenClaw Gateway | 执行插件工具 |
| 可选 `@openclaw/lobster` 插件 | 官方文档说明需单独安装 |
| 工具策略允许 `lobster` | 安装插件不自动放开工具 |
| 非 sandbox 工具上下文 | 官方插件在 sandbox 工具上下文中完全禁用 |
| 私下保留恢复令牌 | 插件不提供待处理检查点列表 |

官方 OpenClaw 插件使用内嵌 runtime，不需要另装独立 `lobster` CLI。独立 CLI 用于开发或外部流水线，是另一条执行路径。

## 最小设置

```bash
openclaw plugins install @openclaw/lobster
```

在现有工具策略上添加允许项：

```json5
{
  tools: {
    alsoAllow: ["lobster"],
  },
}
```

保留其他已有设置。`alsoAllow` 是补充工具权限；替换成严格 `allow` 列表会改变其他工具的可用性。

## 快速体验：一个无外部写入的选择题

下面的 `ask` 与 `pick` 语法来自插件实际依赖的 Lobster `v2026.9.14`。这是一段组合示例，不涉及邮箱、社交平台或文件写入。

让 Agent 调用 `lobster` 工具，参数为：

```json
{
  "action": "run",
  "pipeline": "ask --prompt '请选择测试稿件的处理方式' --schema '{\"type\":\"object\",\"properties\":{\"decision\":{\"type\":\"string\",\"enum\":[\"approve\",\"redraft\",\"reject\"]},\"feedback\":{\"type\":\"string\"}},\"required\":[\"decision\"]}' | pick decision,feedback",
  "timeoutMs": 30000
}
```

也可以直接复制下面的提示词，让 Agent 填写工具参数：

```text
请用 Lobster 做一次输入暂停测试。
流程是 ask -> pick decision,feedback。
ask 的 decision 只接受 approve、redraft、reject，feedback 为可选字符串。
出现 needs_input 后把问题展示给我，私下保留 resumeToken，不继续猜答案。
我回复后按返回 schema 用 responseJson 恢复；本轮不执行外部写入。
```

预期第一轮返回 `needs_input`，其中包含问题、回答 schema 与 `resumeToken`。没有检查点返回时，先检查实际 runtime 和工具结果。

## 回答后怎么继续

例如用户回复“修改开头，让它更简短”，Agent 将其转成允许的结构化回答：

```json
{
  "action": "resume",
  "token": "<本次返回的 resumeToken>",
  "responseJson": "{\"decision\":\"redraft\",\"feedback\":\"请缩短开头\"}"
}
```

`responseJson` 是包含 JSON 文本的字符串，不是任意自然语言，也不是直接嵌入的对象。工具根据检查点返回的 schema 验证它。

此最小示例只把选择与反馈作为结果返回；`redraft` 不是自动改稿命令。后续接入真实改稿或写入步骤，需要单独编写并检查流程。

如需取消这个暂停流程：

```json
{
  "action": "resume",
  "token": "<本次返回的 resumeToken>",
  "cancel": true
}
```

恢复参数只选一种：输入回答 `responseJson`、批准决定 `approve`，或者 `cancel: true`。

## 从演示扩展到审阅工作

1. 用已经可用的步骤生成候选稿件或列表。
2. `ask --subject-from-stdin` 可以把当前结果作为待审材料，并给出 schema。
3. 根据真实返回值决定继续、重写或停止；状态仍需要流程显式实现。
4. 有外部副作用时增加批准点，在审批前展示具体目标和待执行操作。

官方 `.lobster` 文件支持 `steps`、`stdin: $step.stdout` 与 `condition: $approve.approved`。不要把文档中的 `inbox` 示例命令误认为已经安装的工具。

## 输出与失败处理

- `ok`：流程完成；`needs_input`：等待结构化回答；`needs_approval`：等待批准；`cancelled`：已取消。
- 回答不是有效 JSON 或不符合 schema 时，检查点仍可用于纠正；按实际错误修正后再恢复。
- 恢复可能继续返回下一个问题或批准点，不能把第一次恢复当作全部完成。
- 令牌指向保存的运行状态，应保密；持有令牌且能调用工具的人可以恢复，它不绑定 OpenClaw 用户或会话。
- 只保存令牌不等于状态文件不会丢失；状态存储目录需要保留，停止或迁移实例前检查实际保存位置。
- 内嵌 runner 中，`openclaw.invoke` 不会自动继承 Gateway/auth；不要直接复制它来嵌套调用工具。
- 已派发调用超时后先检查实际结果；官方不会据此自动重试可能已经执行的动作。

## 引用来源

- [固定版本：OpenClaw Lobster 插件指南](https://github.com/openclaw/openclaw/blob/v2026.10.1/docs/tools/lobster.md)
- [固定版本：插件实际 runtime 依赖](https://github.com/openclaw/openclaw/blob/v2026.10.1/extensions/lobster/package.json)
- [Lobster v2026.9.14：ask 的参数与恢复实现](https://github.com/openclaw/lobster/blob/v2026.9.14/src/commands/stdlib/ask.ts)
- [Lobster v2026.9.14：pick 字段投影](https://github.com/openclaw/lobster/blob/v2026.9.14/src/commands/stdlib/pick.ts)
- [2026.10.1 交互工作流发布说明](https://github.com/openclaw/openclaw/blob/v2026.10.1/CHANGELOG/2026.10.1.md)

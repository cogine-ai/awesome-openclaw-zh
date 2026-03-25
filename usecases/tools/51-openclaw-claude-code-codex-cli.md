# OpenClaw 调度 Claude Code 与 Codex

> 让 OpenClaw 作为总控，把 Claude Code、Codex CLI 这类 coding harness 接进同一套工作流。

## 这个案例能帮你做什么

- 在聊天里直接把编码任务路由给 Claude Code 或 Codex CLI。
- 用 CLI backend 做文本级兜底，用 ACP session 做持续会话式编码。
- 让不同 Agent 固定使用不同 coding runtime，避免所有代码任务都挤在一个执行器里。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | CLI Backends | 把 `claude-cli/...`、`codex-cli/...` 接成 OpenClaw 模型后端 | OpenClaw Gateway |
| 内置 | ACP Agents | 让外部 coding harness 以持久会话方式运行 | OpenClaw Built-in |
| 外部（需安装） | `claude` CLI | 复杂多文件编码任务 | Claude Code CLI |
| 外部（需安装） | `codex` CLI | 常规实现、修复和代码解释 | Codex CLI |

## 快速体验版（先跑一轮）

```text
你是我的编码任务调度器。
请根据任务复杂度在 Claude Code 和 Codex CLI 之间选一个执行器，并说明原因：
1. 如果任务跨 3 个以上文件，优先 Claude Code
2. 如果任务是单点修复或明确功能实现，优先 Codex CLI
3. 输出推荐执行器、原因、预估改动范围、失败时回退策略

任务：修复一个 README 中的拼写错误，并顺手检查相关示例命令是否一致。
```

## 稳定自动版（可长期运行）

### 1) 先确认两个 CLI 后端可用

官方文档里最小验证命令是：

```bash
openclaw agent --message "hi" --model claude-cli/opus-4.6
openclaw agent --message "hi" --model codex-cli/gpt-5.4
```

### 2) CLI backend 配置（文本兜底）

```json5
{
  agents: {
    defaults: {
      cliBackends: {
        "claude-cli": {
          command: "/opt/homebrew/bin/claude"
        },
        "codex-cli": {
          command: "/opt/homebrew/bin/codex"
        }
      },
      model: {
        primary: "anthropic/claude-opus-4-6",
        fallbacks: [
          "claude-cli/opus-4.6",
          "codex-cli/gpt-5.4"
        ]
      },
      models: {
        "anthropic/claude-opus-4-6": { alias: "Opus" },
        "claude-cli/opus-4.6": {},
        "codex-cli/gpt-5.4": {}
      }
    }
  }
}
```

这一层适合“API provider 挂了也要有文本结果”的兜底模式。

### 3) ACP 持久会话配置（持续编码）

```json5
{
  agents: {
    list: [
      {
        id: "codex",
        runtime: {
          type: "acp",
          acp: {
            agent: "codex",
            backend: "acpx",
            mode: "persistent",
            cwd: "/workspace/repo-a"
          }
        }
      },
      {
        id: "claude",
        runtime: {
          type: "acp",
          acp: {
            agent: "claude",
            backend: "acpx",
            mode: "persistent",
            cwd: "/workspace/repo-a"
          }
        }
      }
    ]
  }
}
```

### 4) 典型操作命令

从聊天线程里拉起持久 Codex session：

```text
/acp spawn codex --mode persistent --thread auto
```

检查 ACP runtime 状态：

```text
/acp status
```

如果你希望 ACP client 直接连到 OpenClaw session：

```bash
acpx openclaw exec "Summarize the active OpenClaw session state."
acpx openclaw sessions ensure --name codex-bridge
```

### 5) OpenClaw 执行提示词（自动版）

```text
你是我的编码任务分发器。
请按下面规则使用 Claude Code 或 Codex CLI：
1. 多文件重构、架构决策、复杂上下文优先交给 Claude Code
2. 明确范围的功能实现、修复、代码解释优先交给 Codex CLI
3. 先判断是否需要 ACP 持久会话；需要多轮跟进时使用 ACP
4. 如果只是兜底文本响应，允许走 cliBackends fallback
5. 每次输出：选择的执行器、原因、预估文件数、是否需要持续线程
```

## 成功标准

- [ ] OpenClaw 能正确识别何时该用 Codex、何时该用 Claude Code。
- [ ] API provider 不可用时，CLI backend 仍能给出稳定文本结果。
- [ ] 需要多轮跟进的编码任务能固定在同一个 ACP 线程里继续执行。

## 风险与边界

- CLI backend 是文本兜底模式，官方文档明确说明这一路径下 OpenClaw tools 不可用。
- CLI backend 不支持流式输出；响应是收集完再返回。
- Codex CLI 的 resume 输出目前比初次 `--json` 运行更不结构化，长会话调试时要有心理预期。

## 使用建议

- 先把 CLI backend 当“保险丝”，再把 ACP 当“真正的持续编码线程”。
- 如果 gateway 跑在 launchd/systemd 下，优先给 `claude`、`codex` 配绝对路径，避免 PATH 问题。
- 给编码专用 Agent 单独 workspace，比在主助理里临时切后端更稳。

## 引用来源

- 来源仓库： [openclaw/openclaw](https://github.com/openclaw/openclaw)
- 原始条目：
  - [docs/gateway/cli-backends.md](https://github.com/openclaw/openclaw/blob/main/docs/gateway/cli-backends.md)
  - [docs/tools/acp-agents.md](https://github.com/openclaw/openclaw/blob/main/docs/tools/acp-agents.md)
  - [docs/cli/acp.md](https://github.com/openclaw/openclaw/blob/main/docs/cli/acp.md)

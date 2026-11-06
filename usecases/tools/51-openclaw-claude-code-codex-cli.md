---
updated: 2026-11-07
---

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

先区分两件事：**CLI backend 用于文本响应；ACP 用于让编码执行器持续处理项目。** 想实际修改文件，按下文配置 ACP，并先准备一个可丢弃的练习仓库。

配置好后，把下面任务交给 OpenClaw。优先使用你已经登录且配置完成的执行器：

```text
请使用已经配置好的 Codex 或 Claude Code ACP 执行器，处理当前练习仓库：
1. 读取 README，找一个明确的拼写错误；没有就报告未发现。
2. 找到后只修复这一个错误，不改动其他文件。
3. 返回修改前后对照和 git diff，说明用了哪个执行器。
4. 不提交、不推送。

如果 ACP 未配置或执行器未登录，先告诉我缺哪一步，不用文字建议冒充文件修改结果。
```

完成后，在练习仓库运行 `git diff`，应能看到与回复一致的单处改动。后续再换成实际项目中的小任务。

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
1. 优先使用我已登录、已配置的首选执行器；没有首选时先说明可用选项。
2. 实际修改项目、需要多轮跟进时使用 ACP 持久会话。
3. 如果只是文本响应，允许走 cliBackends fallback，并说明这次没有执行文件修改。
4. 每次输出：使用的执行器、实际改动、检查结果和需要我处理的事项。
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

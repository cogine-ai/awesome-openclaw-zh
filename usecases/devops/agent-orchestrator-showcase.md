# 编码任务编排中心（Agent Orchestrator）

> 让 OpenClaw 自动判断任务复杂度，把任务分配给最合适的编码工具链。

## 这个案例能帮你做什么

- 避免“小任务用重模型、大任务用轻工具”的错配。
- 在 Claude 配额不足时自动降级到 Codex / Opencode / Gemini，减少中断。
- 把路由理由显式输出，便于团队复盘“为什么这次选了这个工具”。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` | 启动被路由的子代理 | OpenClaw Built-in |
| 内置 | `exec` | 执行路由前检查（如配额脚本） | OpenClaw Built-in |
| 外部（需安装） | `@anthropics/claude-code` | 复杂多文件重构 | npm |
| 外部（需安装） | `openai-codex` | 常规功能开发与修复 | npm |
| 外部（需安装） | `opencode-ai` | 单文件快速修改 | npm |
| 外部（需安装） | `@google/gemini-cli` | 研究+实现混合任务 | npm |

## 快速体验版（先感受效果）

先跑最小路由，不改你现有流程：

```text
你是我的编码任务路由器。
请基于任务描述在 claude / codex / opencode / gemini 里选择一个，并输出：
1) 选择的工具
2) 选择原因
3) 预计影响文件数量
4) 如果首选不可用时的回退工具

任务：修复 README.md 里的一个拼写错误。
```

## 稳定自动版（可长期运行）

### 1) 安装 CLI 工具

```bash
npm install -g @anthropics/claude-code
npm install -g openai-codex
npm i -g opencode-ai
npm install -g @google/gemini-cli
```

在 `~/.openclaw/credentials/` 配置密钥：

```text
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
```

### 2) 编排代理配置（核心）

```yaml
agents:
  orchestrator:
    model: anthropic/claude-sonnet-4-5
    tools:
      - sessions_spawn
      - exec
    system: |
      You are a coding task router. Analyze each task and select the optimal CLI tool.

      AVAILABLE TOOLS:
      1. claude - Complex multi-file refactors, architecture
      2. codex - Standard features/fixes, structured tasks
      3. opencode - Quick single-file edits
      4. gemini - Research + code hybrid tasks

      Use claude if:
      - Changes span 3+ files
      - Requires architectural decisions
      - Complex refactoring
      - Needs deep context

      Use codex if:
      - Single feature or fix
      - Well-defined scope
      - 1-2 files affected
      - Standard patterns

      Use opencode if:
      - Quick edit to single file
      - Simple fix (typo, logic tweak)
      - Fast turnaround needed

      Use gemini if:
      - Needs research (API docs, examples)
      - Learning new technology
      - Research + implementation

      FALLBACK CHAIN:
      claude → codex → opencode → gemini

      PROCESS:
      1. Analyze task description
      2. Check quota if needed
      3. Select optimal tool
      4. Spawn agent with selected tool
      5. Report: tool selected, why, expected scope
```

### 3) 调用示例

```json
{
  "agentId": "orchestrator",
  "message": "Task: Refactor auth system to use JWT. Spans 5 files, needs architectural decisions."
}
```

```json
{
  "agentId": "orchestrator",
  "message": "Task: Fix typo in README.md"
}
```

## 成功标准

- [ ] 路由结果与任务复杂度匹配（简单任务不再走重工具）。
- [ ] 首选工具不可用时可自动回退，不阻塞任务。
- [ ] 每次路由都有可读理由，方便团队复盘。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/agent-orchestrator.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/agent-orchestrator.md)

# AI 编程协作模式

> 由 OpenClaw 负责规划与调度，让 Claude Code 负责编码、测试与修复。

## 这个案例能帮你做什么

- 把“需求分析 → 编码实现 → 自动测试 → Bug 修复”串成一条流水线。
- 适合先做可运行版本，再逐步加自动测试和自动修复。
- 对个人开发者最直接的收益是减少重复样板开发和基础排障时间。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `@anthropic-ai/claude-code` | Claude Code 执行编码任务 | npm |
| 外部（需安装） | `openclaw-code-agent` | 在 OpenClaw 中托管 Claude Code / Codex 后台会话 | ClawHub |
| 内置 | OpenClaw 调度能力 | 任务拆解、流程编排、结果汇总 | OpenClaw Built-in |

## 快速体验版（先感受效果）

先跑一个小任务（不直接改生产项目）：

```text
你是我的 OpenClaw 开发助手。
请调用 Claude Code 完成一个最小 React + TypeScript 待办应用，要求：
1. 支持添加、删除、完成任务。
2. 数据持久化到 localStorage。
3. 输出运行命令与项目结构。
4. 先给可运行版本，再给可选优化项。
```

## 稳定自动版（可长期运行）

### 1) 安装与配置

```bash
npm install -g @anthropic-ai/claude-code
export ANTHROPIC_API_KEY="your-api-key"
openclaw plugins install clawhub:openclaw-code-agent
openclaw plugins enable openclaw-code-agent
```

### 2) Code Agent 关键参数

在 `~/.openclaw/openclaw.json` 里给插件添加最小配置：

```json5
{
  "plugins": {
    "entries": {
      "openclaw-code-agent": {
        "config": {
          "defaultHarness": "claude-code",
          "defaultWorkdir": "~/projects"
        }
      }
    }
  }
}
```

### 3) 自动测试与修复提示词

```text
你是我的 OpenClaw 开发助手。
请用 Claude Code 开发“用户管理系统”，并按以下流程执行：
1. 后端开发。
2. 前端开发。
3. 自动测试并列出失败项。
4. 自动修复失败项。
5. 执行回归测试直到全部通过。

输出要求：
- 每个阶段都给出状态（进行中 / 完成）
- 对每个修复项写明“问题原因 + 修复动作”
- 最后输出通过/失败统计
```

## 成功标准

- [ ] 能稳定完成“生成代码 → 测试 → 修复 → 回归”闭环。
- [ ] 修复说明清晰，可人工复核。
- [ ] 关键配置（模型、工作目录、自动测试开关）可复用。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)
- 当前插件： [OpenClaw Code Agent](https://clawhub.ai/plugins/openclaw-code-agent)

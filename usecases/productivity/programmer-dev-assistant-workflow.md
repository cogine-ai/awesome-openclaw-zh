# 程序员开发助手工作流

> 由 OpenClaw 负责调度，Claude Code 负责编码、测试、修复，形成研发闭环。

## 这个案例能帮你做什么

- 将开发任务拆解成“实现-测试-修复-回归”流水线。
- 对中小任务可快速产出可运行版本。
- 帮助开发者把精力从重复实现转到架构与验收。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `@anthropic-ai/claude-code` | Claude Code 执行开发任务 | npm |
| 外部（需安装） | `openclaw-code-agent` | 在 OpenClaw 中托管 Claude Code / Codex 后台会话 | ClawHub |
| 内置 | OpenClaw 调度能力 | 任务分解与流程编排 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的开发助手。
请调用 Claude Code 生成一个 React + TypeScript 待办应用，
要求：增删改查 + localStorage。
先给可运行版本，再输出测试清单。
```

## 稳定自动版（可长期运行）

### 1) 安装与配置

```bash
npm install -g @anthropic-ai/claude-code
openclaw plugins install clawhub:openclaw-code-agent
openclaw plugins enable openclaw-code-agent
```

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

### 2) 进阶提示词（源案例方向）

```text
用 Claude Code 开发一个用户管理系统，要求自动测试并修复所有 Bug：
1. 后端开发
2. 前端开发
3. 自动测试
4. 自动修复
5. 回归测试
```

## 成功标准

- [ ] 可稳定执行“开发→测试→修复→回归”。
- [ ] 修复过程有明确记录。
- [ ] 人工审查和安全检查可顺利接管。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)
- 当前插件： [OpenClaw Code Agent](https://clawhub.ai/plugins/openclaw-code-agent)

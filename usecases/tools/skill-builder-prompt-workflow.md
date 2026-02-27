# 技能构建提示词工厂

> 用一份标准提示词，持续产出更短、更稳、更省 token 的 AgentSkill。

## 这个案例能帮你做什么

- 把“写技能”从一次性创作变成可复用流程。
- 强制 SKILL.md 聚焦核心流程，避免文件膨胀。
- 将细节分流到 `references/`，提升维护性和上下文效率。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 方法论 | AgentSkills 规范 | 统一技能结构与触发规则 | [agentskills.io](https://agentskills.io/) |
| 内置（可选） | 文件系统工具 | 创建/重构技能目录 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

直接复制原文模板，让 OpenClaw 生成一个新技能：

```text
I need help creating or optimizing an AgentSkill.

Skill name:
[your-skill-name]

Purpose:
What the skill does and when it should activate.

Triggers:
What kinds of tasks or questions should activate this skill.

Tools needed:
Any tools, commands, or APIs the skill will use.

Reference docs:
Docs or specs that should live in references/ for on-demand loading.

Existing skill (if applicable):
Path to the current SKILL.md if this is a refactor.

Please:
- Create or optimize the skill following AgentSkills best practices
- Keep the core workflow in SKILL.md and move details into references/
- Keep SKILL.md under ~500 lines
- Validate the structure using the AgentSkills validator
- Show the final file structure and contents
```

## 稳定自动版（可长期运行）

### 1) 新建技能（原文示例）

- 明确 `Skill name / Purpose / Triggers / Tools needed / Reference docs`
- 强制 `SKILL.md` 控制在 ~500 行以内

### 2) 重构现有技能（原文示例）

- 指定现有路径：`~/.openclaw/workspace/skills/.../SKILL.md`
- 目标：从 1800 行降到 ~500 行
- 细节迁移到 `references/`

### 3) 推荐目录（原文）

```text
skills/
└── your-skill-name/
    ├── SKILL.md
    ├── references/
    │   ├── api-docs.md
    │   └── examples.md
    └── scripts/
        └── helper.sh
```

## 成功标准

- [ ] SKILL.md 聚焦触发与核心流程，无冗余说明。
- [ ] 细节文档分离到 references，按需加载。
- [ ] 技能可维护、可复用、token 开销可控。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/skill-builder-prompt.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/skill-builder-prompt.md)

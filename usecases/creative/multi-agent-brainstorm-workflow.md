# 多Agent头脑风暴

> 用不同角色的 Agent 并行讨论同一问题，快速形成可执行方案。

## 这个案例能帮你做什么

- 用多视角讨论复杂决策，降低单一视角盲区。
- 自动沉淀讨论记录、行动计划和归档材料。
- 可按固定节奏重复执行（如每周策略会）。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `multi-agent` 能力 | 多角色并行讨论 | OpenClaw Built-in |
| 内置 | `schedule/cron` | 定时发起策略讨论 | OpenClaw Built-in |
| 外部 | `notion` / `feishu`（可选） | 归档讨论结果 | 第三方集成 |

## 快速体验版（先跑一轮）

先做 2 轮小讨论：

```text
你是我的 OpenClaw 助手。
请帮我组织一场头脑风暴，主题是“新产品命名”。
参与者：营销专家、品牌设计师、产品经理。
讨论轮次：2轮。
最后输出：
1. 最终推荐名称
2. 三个角色的核心理由
3. 可执行行动计划（3-5条）
```

## 稳定自动版（可长期运行）

### 1) 多 Agent 基础配置

```bash
# 1. 启用多Agent功能
openclaw config set multi-agent.enabled true

# 2. 配置Agent角色
openclaw config set multi-agent.roles '{
  "marketing": {
    "name": "营销专家",
    "expertise": "市场定位、品牌传播",
    "personality": "积极、创新"
  },
  "designer": {
    "name": "设计师",
    "expertise": "视觉设计、用户体验",
    "personality": "细致、追求完美"
  }
}'

# 3. 配置讨论规则
openclaw config set multi-agent.rules '{
  "rounds": 3,
  "time-per-round": 300,
  "max-participants": 10,
  "auto-summary": true
}'
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“多Agent头脑风暴”。

执行规则：
1. 根据议题匹配互补专家角色。
2. 控制讨论轮次（简单1-2轮，中等2-3轮，复杂3-5轮）。
3. 每轮聚焦不同维度（市场、设计、产品、风险）。
4. 最终输出：结论、分歧点、行动计划、风险提示。
5. 自动保存讨论纪要并归档。
```

### 3) 最佳实践（原文）

```bash
# 每周一次战略讨论
openclaw schedule add "weekly-strategy" \
  --time "Mon 10:00" \
  --prompt "组织战略讨论会，回顾上周，规划本周"

# 自动归档讨论结果
openclaw config set brainstorm.archive true
openclaw config set brainstorm.archive-path "~/knowledge/brainstorm"

# 自动生成思维导图
openclaw config set brainstorm.mindmap true

# 自动同步到知识库
openclaw config set brainstorm.sync-to "notion,feishu"
```

## 成功标准

| 任务类型 | 传统方式 | 多Agent | 节省时间 | 提升比例 |
|---|---:|---:|---:|---:|
| 战略规划 | 8小时 | 30分钟 | 450分钟 | 93.8% |
| 产品设计 | 4小时 | 20分钟 | 220分钟 | 91.7% |
| 问题解决 | 6小时 | 25分钟 | 335分钟 | 93.1% |
| 创意生成 | 3小时 | 15分钟 | 165分钟 | 91.7% |
| 技术决策 | 5小时 | 20分钟 | 280分钟 | 93.3% |
| 平均 | 26小时 | 110分钟 | 1450分钟 | 92.9% |

## 风险与边界

- AI 讨论不能替代关键决策的人类审核。
- 法律与合规类问题需专业人士二次确认。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

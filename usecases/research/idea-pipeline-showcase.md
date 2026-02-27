# 想法漏斗自动推进（Idea Pipeline）

> 把白天收集的想法，凌晨自动做调研、可行性评估，再写回任务系统。

## 这个案例能帮你做什么

- 不再让想法“只采集不研究”，每天早上直接看到可执行结论。
- 每条想法自动补齐：竞品/开源替代、技术复杂度、预估工期、主要阻塞。
- 默认限制每晚只处理优先级最高的 3 条，避免信息过载。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_search` | 研究市场与技术方案 | OpenClaw Built-in |
| 内置 | 子代理能力（`sessions_spawn`） | 多想法并行研究 | OpenClaw Built-in |
| 外部 | 任务系统 API（Todoist / Trello / Asana） | 写回研究结果 | 对应平台 |
| 渠道 | Telegram / Discord / Email / 文件目录 | 作为想法采集入口 | 用户自选 |

## 快速体验版（先跑一轮）

先手工触发一次，验证全链路：

```bash
openclaw cron run idea-pipeline
```

## 稳定自动版（可长期运行）

### 1) 放入 cron.jobs（原文配置）

```json
{
  "name": "idea-pipeline",
  "schedule": {
    "kind": "cron",
    "expr": "0 3 * * *",
    "tz": "UTC"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Process ideas from [YOUR_CAPTURE_METHOD]. For each idea: 1) Search web for existing solutions and market landscape. 2) Analyze technical feasibility (complexity 1-5, estimated time, blockers). 3) Write summary to [YOUR_TASK_SYSTEM] with findings, top 3 similar solutions, feasibility assessment, and next steps. Be concise."
  },
  "sessionTarget": "isolated"
}
```

把以下占位符换成你的真实入口：
- `[YOUR_CAPTURE_METHOD]`：例如 `Telegram bot` / `Discord #ideas`
- `[YOUR_TASK_SYSTEM]`：例如 `Todoist` / `Trello`

### 2) 工具最小配置（原文示例）

```yaml
tools:
  web_search: {}
  message: {}
  todoist: {}
```

### 3) 详细执行提示词（原文）

```text
Process the ideas captured from [YOUR_CAPTURE_METHOD].

For each idea:
1. SEARCH: Search web for
   - Existing products/services solving similar problem
   - Open source alternatives
   - Technical approaches others used
   - Market size or demand indicators

2. ANALYZE feasibility:
   - Technical complexity (1-5 scale)
   - Estimated build time
   - Key technical decisions needed
   - Potential blockers

3. WRITE summary to [YOUR_TASK_SYSTEM]:
   - Brief overview of findings
   - Top 3 similar solutions found with links
   - Feasibility assessment
   - Recommended next steps

Be concise. Focus on actionable insights, not exhaustive research.
Limit to top 3 ideas per night by priority.
```

### 4) 并行增强（可选）

```javascript
for (const idea of ideas) {
  sessions_spawn({
    task: `Research: "${idea.text}". Search web, analyze feasibility, return structured summary.`,
    agentId: "researcher",
    model: "gemini"
  });
}
```

## 成功标准

- [ ] 每天都有稳定的“研究后想法”输出，而不是只堆积原始灵感。
- [ ] 每条想法都包含复杂度、工期、阻塞与下一步。
- [ ] 晚间处理量受控（Top 3），信息密度高但不拥挤。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/idea-pipeline.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/idea-pipeline.md)

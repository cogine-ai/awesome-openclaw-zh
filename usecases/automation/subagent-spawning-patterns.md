# 子代理并发调度模式

> 把复杂任务拆成多个子代理并行执行，提升夜间自动化吞吐。

## 这个案例能帮你做什么

- 在 Skill、Agent、Cron、Chat 四种场景下稳定拉起子代理。
- 对重任务做并发拆分，减少主会话阻塞。
- 用统一参数和调试方法，降低“拉起失败/结果丢失”的排障成本。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` | 创建子代理并等待返回 | OpenClaw Built-in |
| 内置 | `cron` | 定时触发并发任务 | OpenClaw Built-in |
| 内置 | `filesystem` | 保存并汇总结果文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先跑 1 个 researcher 子代理，验证链路：

```text
你是我的 OpenClaw 助手。
请帮我做“子代理并发调度”的预演版：
1. 使用 sessions_spawn 拉起一个 researcher 子代理。
2. 任务内容：Research OpenClaw documentation。
3. timeoutSeconds 设为 60。
4. 返回结果后输出一段摘要。
5. 如果超时或失败，给出重试建议。
```

## 稳定自动版（可长期运行）

### 1) 四种常见拉起方式

| 场景 | 方式 | 适合场景 |
|---|---|---|
| Skill 内 | 在代码里调用 `sessions_spawn()` | 编排器、并行批处理 |
| Agent 内 | 在提示词中调用 `sessions_spawn` 工具 | 自主委派 |
| Cron 内 | 定时 payload 中触发 spawn | 夜间批任务 |
| Chat 内 | `/subagents spawn <agent-id> <task>` | 手工一次性触发 |

### 2) Chat 命令（OpenClaw 2026.2.17+）

```text
/subagents spawn <agent-id> <task>
```

示例：

```text
/subagents spawn researcher "Find recent papers on transformer architectures"
```

### 3) Skill 内并发示例

```javascript
async function researchTopics(topics) {
  const promises = topics.map(topic =>
    sessions_spawn({
      agentId: "researcher",
      task: `Research: ${topic}. Find pricing, features, and reviews.`,
      label: `research-${topic.replace(/\s+/g, '-')}`,
      cleanup: "delete"
    })
  );

  const results = await Promise.all(promises);
  return results.map((result, i) => ({
    topic: topics[i],
    findings: result
  }));
}
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“子代理并发调度模式”。
请使用 sessions_spawn。

执行规则：
1. 收到复杂任务后先拆分子任务。
2. 为每个子任务选择合适 agentId。
3. 使用 sessions_spawn 创建子代理，并设置 label 便于追踪。
4. 对所有子代理结果执行等待与汇总，不要 fire-and-forget。
5. 对超时任务给出重试或降级方案。

参数约定：
- agentId：必须存在于 agents.list
- task：明确、可执行
- label：可追踪（建议唯一）
- timeoutSeconds：按任务复杂度设置
- cleanup："delete" 或 "keep"
```

### 5) 调试命令

```bash
openclaw config get | jq '.agents.list[].id'
openclaw sessions list
tail -f ~/.openclaw/gateway.log | grep spawn
```

## 常见错误与修正

- 错误：spawn 后不等待结果。  
  修正：使用 `await sessions_spawn(...)` 等待返回。
- 错误：`agentId` 拼错或未配置。  
  修正：先用 `openclaw config get | jq '.agents.list[].id'` 校验。
- 错误：小任务也盲目 spawn。  
  修正：仅在任务耗时较长、需要并行或隔离时使用。

## 使用建议

- 任务预计 >2-3 分钟、且可并行时再启用 spawn。
- 需要保留会话排错时把 `cleanup` 设为 `keep`。
- 多子代理共用上下文时，优先在配置中显式指定 workspace。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/spawning-patterns.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/spawning-patterns.md)

# 7 子代理夜间并行

> 晚上 23:00 一次性拉起 7 个子代理并行处理任务，早上统一汇总结果。

## 这个案例能帮你做什么

- 把不同类型的任务并行处理，显著缩短总耗时。
- 每个子代理隔离运行，降低互相干扰。
- 早上直接拿到合并后的结果，不用逐个检查。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `sessions_spawn` | 生成并管理子代理会话 | OpenClaw Built-in |
| 内置 | `git` | 提交夜间产出 | OpenClaw Built-in |
| 内置 | `filesystem` | 分区存储子任务结果 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先把“7 个任务”降到“2 个任务”验证流程：

```text
你是我的 OpenClaw 助手。
请帮我做“子代理夜间并行”的预演版：
1. 先生成 2 个子代理，并给出各自独立任务。
2. 每个子代理设置 1 小时超时。
3. 每 10 分钟汇报一次进度。
4. 结束后合并输出一个晨报摘要。
5. 本轮只演示流程，不做大规模并发。
```

## 稳定自动版（可长期运行）

### 1) 子代理任务配置

```javascript
const subAgents = [
  { name: "memory-cleanup", task: "consolidate daily logs" },
  { name: "budget-prep", task: "analyze spending patterns" },
  { name: "tts-research", task: "evaluate new TTS models" },
  { name: "books", task: "find relevant reading" },
  { name: "self-improve", task: "research agent optimization" },
  { name: "neuroscience", task: "study AI memory papers" },
  { name: "advisor", task: "document advisor patterns" }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“7 子代理夜间并行”。
请使用内置 Skills：sessions_spawn、git、filesystem。

在 23:00 按顺序执行：
1. 创建 7 个隔离子代理，并分配明确任务。
2. 每个子代理超时设置为 1 小时。
3. 每 10 分钟巡检一次进度。
4. 子代理完成后立即回收结果。
5. 汇总全部输出并提交到 git。
6. 生成晨报，说明每个子代理完成状态和关键结论。

分区规则：
- 每个子代理有独立 memory/
- 不共享写权限
- 共享数据只读
```

## 成功标准

- [ ] All 7 agents complete within 6 hours
- [ ] Results committed to version control
- [ ] Morning briefing generated automatically

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/12-7-sub-agent-night-parallel.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/12-7-sub-agent-night-parallel.md)

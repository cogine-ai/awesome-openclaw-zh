# 网络延迟基准测试

> 持续测量多代理网络延迟，提前识别拓扑与扩容瓶颈。

## 这个案例能帮你做什么

- 监控 P50/P95/P99 延迟，判断当前规模是否接近上限。
- 跟踪节点数量与延迟关系，识别非线性劣化点。
- 提前发现拓扑变化和异常波动，避免线上才暴露问题。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 拉取 mesh 状态 | OpenClaw Built-in |
| 内置 | `system` | 记录与计算性能指标 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```javascript
async function benchmarkMesh() {
  const start = Date.now();
  const responses = await Promise.all(nodes.map(n => ping(n)));
  const latency = Date.now() - start;
  return { latency, responses };
}
```

先手工执行一次，确认可拿到基础延迟数据。

## 稳定自动版（可长期运行）

### 1) 每日 02:00 基准任务（原文流程）

```text
Daily at 02:00:
1. Query agent mesh status
2. Measure P50/P95/P99 latency
3. Track node count vs latency correlation
4. Detect topology shifts
5. Report anomalies
```

### 2) 指标建议（原文）

- Coordination latency
- Message throughput
- Node churn rate
- Regional cluster formation

## 成功标准

- [ ] 每日延迟数据稳定采集。
- [ ] 每周能产出趋势判断。
- [ ] 瓶颈与异常有明确记录。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/26-network-latency-benchmark.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/26-network-latency-benchmark.md)

# 分布式追踪基准测试

> 对比不同 tracing 方案在代理网络中的延迟与内存开销，避免盲目上线。

## 这个案例能帮你做什么

- 对比 OpenTelemetry / Jaeger / 自定义 tracer 的真实开销。
- 用统一采样率矩阵评估 P99 延迟和吞吐影响。
- 用“延迟、内存、成本”三维指标给出可落地选型建议。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `system` | 性能采样与统计 | OpenClaw Built-in |
| 内置 | `docker` | 隔离测试环境 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```javascript
const configs = [
  { tracer: 'otlp', sampling: 1.0 },
  { tracer: 'jaeger', sampling: 0.1 },
  { tracer: 'custom', sampling: 0.5 }
];
```

先小规模跑完 3 组配置，确认指标采集链路可用。

## 稳定自动版（可长期运行）

### 1) 周度基准流程（原文）

```text
Weekly benchmark:
1. Deploy test mesh with different tracers
2. Measure P99 latency at each sampling rate
3. Track memory overhead
4. Test throughput under load
5. Generate comparison report
```

### 2) 选型阈值（原文）

- Latency impact `<5ms` 优先
- Memory overhead `<10%`
- 成本与可观测价值匹配

## 成功标准

- [ ] 关键 tracer 方案都有统一基准数据。
- [ ] 延迟与内存开销数据可复现。
- [ ] 结果被落实为明确配置建议。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/28-distributed-tracing-benchmark.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/28-distributed-tracing-benchmark.md)

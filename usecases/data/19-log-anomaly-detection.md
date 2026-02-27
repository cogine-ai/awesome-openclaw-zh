# 日志异常检测

> 用统计方式持续盯日志，发现错误激增时快速告警。

## 这个案例能帮你做什么

- 自动比较当前错误率和历史基线，及早发现异常。
- 区分 warning 与 urgent，减少无效报警。
- 让夜间问题在影响用户前被提前捕获。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读取与分析日志文件 | OpenClaw Built-in |
| 内置 | `telegram` | 发送异常告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“日志异常检测”的预演版：
1. 读取最近30分钟日志。
2. 统计 ERROR 类型频率。
3. 与近24小时基线比较。
4. 输出 warning/critical 判定和样例错误。
```

## 稳定自动版（可长期运行）

### 1) 异常检测逻辑

```javascript
function detectAnomaly(lines) {
  const errorRate = lines.filter(l => l.includes('ERROR')).length / lines.length;
  const baseline = getBaseline(); // Historical average
  return errorRate > baseline * 2;
}
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Log Anomaly Detection”。

每 30 分钟执行：
1. 读取最近日志。
2. 按错误类型统计频率。
3. 对比滚动24小时基线。
4. 超过2倍基线：warning。
5. 超过5倍基线：立即告警。
6. 告警中附带样例错误消息。
```

## 成功标准

- [ ] Anomalies detected within 30 min
- [ ] False positive rate <10%
- [ ] Zero missed critical errors

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/19-log-anomaly-detection.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/19-log-anomaly-detection.md)

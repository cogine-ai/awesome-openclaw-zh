# 心跳状态监控器

> 专门监控“监控任务本身是否新鲜”，防止心跳任务静默失效。

## 这个案例能帮你做什么

- 一眼看出哪些检查任务已经过期（stale）。
- 发现超阈值任务后可立即触发补跑。
- 给自动化系统加一层“监控监控器”的保险。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读取 `heartbeat-state.json` | OpenClaw Built-in |
| 内置 | `system` | 时间差计算与阈值判断 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的心跳状态检查助手。
请读取 heartbeat-state.json，计算每个检查项距现在的分钟数，
按 OK / STALE 输出状态清单。
本轮只输出报告，不触发补跑。
```

## 稳定自动版（可长期运行）

### 1) 状态文件格式

```json
{
  "lastChecks": {
    "email": "2026-02-19T08:00:00Z",
    "calendar": "2026-02-19T08:30:00Z"
  }
}
```

### 2) 核心检查逻辑

```javascript
function checkFreshness() {
  const state = JSON.parse(fs.readFileSync('heartbeat-state.json'));
  const now = Date.now();

  Object.entries(state.lastChecks).forEach(([check, time]) => {
    const age = (now - new Date(time)) / 1000 / 60;
    const status = age > 60 ? 'STALE' : 'OK';
    console.log(`${status}: ${check} - ${age} min ago`);
  });
}
```

### 3) OpenClaw 执行提示词（自动版）

```markdown
## Heartbeat State Monitor

Every heartbeat:
1. Read heartbeat-state.json
2. Calculate staleness for each check
3. Display human-readable status
4. Alert if any check > threshold
5. Trigger overdue checks immediately
```

## 成功标准

- [ ] 所有检查项都有新鲜度状态。
- [ ] 过期项能被及时告警。
- [ ] 告警后可触发补跑，不长期积压。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/36-heartbeat-state-monitor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/36-heartbeat-state-monitor.md)

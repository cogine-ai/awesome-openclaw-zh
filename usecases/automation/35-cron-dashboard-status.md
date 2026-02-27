# 定时任务仪表板状态

> 把所有 cron 任务的“最近执行、成功失败、下次时间”集中可视化。

## 这个案例能帮你做什么

- 一眼看清所有 cron 任务状态，不再“失败了很久都没人发现”。
- 快速定位失败任务和最近输出，缩短排查时间。
- 识别连续漏跑任务，提前处理稳定性问题。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `system` | 读取 crontab 与系统执行信息 | OpenClaw Built-in |
| 内置 | `filesystem` | 读取任务日志与输出 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先做一次只读巡检：

```text
你是我的 OpenClaw 助手。
请帮我做“定时任务仪表板状态”的预演版：
1. 列出所有已配置 cron 任务。
2. 展示每个任务最近执行时间与成功/失败状态。
3. 展示最近输出（最后 10 行）。
4. 标记漏跑 2 次及以上的任务。
```

## 稳定自动版（可长期运行）

### 1) 仪表板脚本片段

```javascript
function showCronStatus() {
  const jobs = parseCrontab();
  jobs.forEach(job => {
    const lastRun = getLastRunLog(job);
    const status = lastRun.success ? '✓' : '✗';
    console.log(`${status} ${job.name} - Last: ${lastRun.time}`);
  });
}
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Cron Dashboard Status”。
请使用内置 Skills：system、filesystem。

按需执行（on demand）：
1. 列出全部 cron 任务。
2. 显示最近执行时间。
3. 显示成功/失败状态。
4. 显示最近输出（last 10 lines）。
5. 显示下次计划执行时间。
6. 若任务漏跑 2 次及以上，立即标记告警。
```

## 成功标准

- [ ] All jobs visible in dashboard
- [ ] Failures detected within 1 hour
- [ ] Historical logs accessible

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/35-cron-dashboard-status.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/35-cron-dashboard-status.md)

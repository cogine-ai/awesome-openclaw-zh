# 效率数据监控系统

> 持续量化你的时间与任务执行表现，并给出每天可执行改进建议。

## 这个案例能帮你做什么

- 把效率管理从“感觉”变成“有指标可看”。
- 自动产生日报/周报/月报，减少手工复盘时间。
- 跟踪自动化覆盖率，持续扩大可自动化任务比例。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `tracking/reporting` 配置能力 | 采集与输出效率指标 | OpenClaw Built-in |
| 外部 | 日历同步（可选） | 任务完成对齐日程 | 第三方集成 |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“效率数据监控系统”的预演版：
1. 统计我今天的时间分配和任务完成率。
2. 统计深度工作时长和番茄钟数据。
3. 输出一份今日效率报告。
4. 给出3条改进建议。
```

## 稳定自动版（可长期运行）

### 1) 数据采集配置

```json
{
  "tracking": {
    "time_tracking": {
      "enabled": true,
      "categories": ["工作", "学习", "休息", "娱乐"],
      "auto_detect": true
    },
    "task_tracking": {
      "enabled": true,
      "sync_calendar": true,
      "track_completion": true
    },
    "focus_tracking": {
      "enabled": true,
      "pomodoro": 25,
      "break": 5
    }
  },
  "reporting": {
    "daily_summary": "20:00",
    "weekly_review": "Sunday 18:00",
    "monthly_report": "Last day 18:00"
  }
}
```

### 2) 报告生成命令

```bash
# 每日总结
openclaw agent --message "生成今日效率报告"
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“效率数据监控系统”。

每日执行：
1. 统计时间分配（工作/学习/休息/娱乐）。
2. 统计计划任务与完成率。
3. 统计深度工作时长与专注度。
4. 统计自动化任务数量与节省时间。
5. 输出3条可执行改进建议。

报告节奏：
- Daily summary: 20:00
- Weekly review: Sunday 18:00
- Monthly report: Last day 18:00
```

## 成功标准

- [ ] 时间利用率提升约 35%
- [ ] 工作效率提升约 50%
- [ ] 压力水平降低约 40%
- [ ] 工作满意度提升约 60%

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

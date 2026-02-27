# 智能任务管理系统

> 从任务输入到优先级排序、时间分配、进度跟踪和复盘的自动化闭环。

## 这个案例能帮你做什么

- 自动识别任务优先级，不再靠临时直觉排程。
- 根据工作时段和专注窗口分配执行时间。
- 可持续输出效率报告，形成“计划-执行-复盘”循环。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `task-manager` | 任务管理 | ClawHub |
| 外部（需安装） | `calendar-sync` | 日历联动 | ClawHub |
| 外部（需安装） | `priority-analyzer` | 优先级分析 | ClawHub |
| 外部（需安装） | `time-estimator` | 任务时长估算 | ClawHub |
| 内置 | `openclaw agent` | 计划生成、进度跟踪、日报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的任务管理助手。
我给你今天任务清单后，请输出：
1) 优先级排序
2) 时间安排（含固定会议）
3) 今日提醒点
本轮先做计划，不写入日历。
```

## 稳定自动版（可长期运行）

### 1) 安装技能（源案例）

```bash
clawhub install task-manager
clawhub install calendar-sync
clawhub install priority-analyzer
clawhub install time-estimator
```

### 2) 任务规则配置

`~/.openclaw/task-rules.json`：

```json
{
  "priority_rules": {
    "urgent_keywords": ["紧急", "立即", "今天必须"],
    "important_keywords": ["重要", "关键", "核心"],
    "deadline_weight": 0.4,
    "impact_weight": 0.3,
    "effort_weight": 0.3
  },
  "time_rules": {
    "work_hours": "09:00-18:00",
    "focus_time": "09:00-11:00",
    "meeting_time": "14:00-16:00",
    "break_interval": 90
  },
  "automation": {
    "auto_schedule": true,
    "auto_reminder": true,
    "auto_followup": true
  }
}
```

### 3) 效率报告（源案例）

```bash
openclaw agent --message "生成今日效率报告"
```

## 成功标准

- [ ] 任务完成率和时间利用率可见提升。
- [ ] 优先级安排可解释、可复盘。
- [ ] 每日效率报告可稳定生成。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

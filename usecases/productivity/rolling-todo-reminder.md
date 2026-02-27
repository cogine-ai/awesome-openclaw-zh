# 滚动式待办提醒系统

> 每天生成待办清单，并在关键时段滚动提醒高优先级任务。

## 这个案例能帮你做什么

- 把“记任务”升级为“按时推动任务完成”。
- 将待办状态与日报联动，自动更新优先级。
- 在通讯工具里直接提醒，减少遗漏。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw schedule` | 每日生成与定时提醒 | OpenClaw Built-in |
| 内置 | 飞书/企微/钉钉等消息通道 | 下发待办和提醒 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的待办提醒助手。
请基于今天任务生成一份清单：高/中/低优先级。
并模拟下午 15:00 的提醒内容（仅高优先级）。
本轮不创建定时任务。
```

## 稳定自动版（可长期运行）

### 配置口令（源案例）

```text
每天生成日报时，顺便：
1. 检查今日待办完成情况
2. 生成明日待办清单
3. 标注优先级
4. 设置提醒时间
5. 推送到飞书

每天下午3点：
- 提醒未完成的高优先级任务
```

### 推荐节奏

- `09:00`：今日待办总览
- `15:00`：高优先级滚动提醒

## 成功标准

- [ ] 高优任务能被持续提醒直到完成。
- [ ] 待办和日报数据一致。
- [ ] 当日遗漏显著减少。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

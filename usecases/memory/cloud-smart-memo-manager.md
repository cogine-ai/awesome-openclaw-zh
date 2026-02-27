# 云端智能备忘录管理

> 每周自动整理备忘录，去重分类并提取待办，同时做每日滚动提醒。

## 这个案例能帮你做什么

- 解决备忘录“越记越乱、重要事项被淹没”的问题。
- 每周自动把碎片笔记整理为“工作/学习/生活”三类结构。
- 自动提取未完成事项并生成下周计划，减少遗漏。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw schedule` | 配置每周整理与每日提醒 | OpenClaw Built-in |
| 内置 | 消息推送通道（如飞书） | 发送整理结果与提醒 | OpenClaw Built-in |
| 内置 | 备忘录读写能力 | 读取本周备忘录并做去重分类 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的备忘录助手。
请先对我本周备忘录做一次试运行：
1. 合并重复主题
2. 按工作/学习/生活分类
3. 提取未完成待办
4. 生成下周计划
本轮只输出结果，不写入定时任务。
```

## 稳定自动版（可长期运行）

### 1) 每周整理提示词（源案例）

```text
你：每周日晚上8点：
1. 读取本周所有备忘录
2. 智能去重（相同主题合并）
3. 分类整理（工作/学习/生活）
4. 提取未完成待办
5. 生成下周计划
6. 推送到飞书
```

### 2) 调度命令（源案例）

```bash
openclaw schedule add "weekly-notes-cleanup" \
  --time "Sun 20:00" \
  --prompt "整理本周备忘录：去重、分类、提取待办、生成下周计划"

openclaw schedule add "daily-todo" \
  --time "09:00" \
  --prompt "生成今日待办清单"

openclaw schedule add "todo-reminder" \
  --time "15:00" \
  --prompt "提醒未完成的高优先级任务"
```

### 3) 输出参考

```text
【本周备忘录整理】
- 新增备忘录：45条
- 去重后：28条
- 重要事项：8条
- 已完成：20条
- 待处理：8条
```

## 成功标准

- [ ] 每周都能产出结构化整理结果。
- [ ] 待办项从备忘录中被稳定提取并跟进。
- [ ] 重要事项不再被时间轴淹没。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

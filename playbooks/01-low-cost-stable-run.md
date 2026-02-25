# 低成本稳定运行（Non-Hype 版）

这份实践来自 runbook 与多份 awesome 资料的共同结论。

## 核心原则

1. 默认模型用“平衡型”，别把最贵模型设为常驻。
2. 高级模型只在复杂任务时调用。
3. 后台高频任务（心跳、巡检）用便宜模型。
4. 所有自动化任务都要有频率上限和失败重试上限。

## 你最容易踩的坑

- 一个模型做所有事，费用飙升
- 一上来就开很多自动任务，排队和超额并发
- 没有任务状态可视化，最后不知道它做了什么

## 推荐做法（非技术用户版）

- 每周只新增 1-2 个自动化任务
- 先做“每天稳定可见收益”的任务
- 每天固定 1 次查看结果，减少无效调参

## 先上这 5 个省心场景

- [每日晨间简报](../usecases/everyday/52-morning-briefing-telegram.md)
- [收件箱整理](../usecases/productivity/inbox-declutter.md)
- [阅读清单管理](../usecases/everyday/61-reading-list-curator.md)
- [会议纪要生成](../usecases/everyday/68-meeting-notes-generator.md)
- [定制早间简报](../usecases/productivity/custom-morning-brief.md)

# LinkedIn 周更草稿助手

> 按你的口吻自动生成周更内容草稿，减少写作启动成本。

## 这个案例能帮你做什么

- 你可以先把「按你的口吻自动生成周更内容草稿，减少写作启动成本。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `cron.jobs`
- `VOICE.md`
- `Notion`
- `Todoist`
- `GitHub`
- `cron`
- `OpenClaw`

### 命令片段

```bash
openclaw cron run linkedin-drafter
```

### 调度信息

- 0 10 * * 2

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「LinkedIn 周更草稿助手」。

任务目标：按你的口吻自动生成周更内容草稿，减少写作启动成本。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：cron.jobs、VOICE.md、Notion、Todoist、GitHub、cron）。
5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 我需要补充的信息
## 风险提醒
```

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/linkedin-drafter.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/linkedin-drafter.md)

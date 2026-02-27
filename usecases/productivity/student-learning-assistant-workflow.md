# 学生学习助手工作流

> 课程管理、复习规划、作业辅助的一体化学习流程。

## 这个案例能帮你做什么

- 你可以先把「课程管理、复习规划、作业辅助的一体化学习流程。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `Notion`
- `GitHub`
- `OpenClaw`
- `RSS`

### 命令片段

```bash
openclaw schedule add "daily-report" \
openclaw config set report.sources \
openclaw config set report.channel "feishu"
openclaw config set notes.default "备忘录/行业研究"
openclaw template add "meeting-notes" \
openclaw config set sync.targets "notion,feishu"
openclaw config set reminder.action-items true
openclaw config set archive.rules '{
openclaw schedule add "daily-summary" \
openclaw config set knowledge.graph true
openclaw schedule add "morning-report" \
openclaw config set clipper.default "备忘录/行业研究"
```

### 调度信息

- 7:00
- 09:00
- 10:00
- 14:00
- 16:00
- 17:00
- 18:00
- 07:00
- 9:00
- 12:00

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「学生学习助手工作流」。

任务目标：课程管理、复习规划、作业辅助的一体化学习流程。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：Notion、GitHub、OpenClaw、RSS）。
5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 我需要补充的信息
## 风险提醒
```

## 风险与边界

- 先在测试环境验证，再应用到生产或长期任务。

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

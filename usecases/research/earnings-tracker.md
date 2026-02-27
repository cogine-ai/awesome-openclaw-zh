# AI 财报追踪器

> 追踪科技/AI 财报，带有自动化预览、警报和详细摘要。

## 这个案例能帮你做什么

- 你可以先把「追踪科技/AI 财报，带有自动化预览、警报和详细摘要。」做成一个可重复执行的小流程。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。
- 建议先跑最小闭环，再按实际反馈逐步扩展。

## 开始前准备

### 技能与工具

- `web_search`
- `Telegram`
- `cron`
- `OpenClaw`

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「AI 财报追踪器」。

任务目标：追踪科技/AI 财报，带有自动化预览、警报和详细摘要。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：web_search、Telegram、cron、OpenClaw）。
5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 我需要补充的信息
## 风险提醒
```

## 风险与边界

- 涉及删除、外发、改密等动作时，先确认再执行。
- 密钥与凭证不要放在公开文本或提示词中。

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/earnings-tracker.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/earnings-tracker.md)

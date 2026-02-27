# 邮件转播客技能

> 邮件音频转换的可重用技能

## 这个案例能帮你做什么

- 你可以先把「邮件音频转换的可重用技能」做成一个可重复执行的小流程。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `email`
- `elevenlabs`
- `ffmpeg`
- `Gmail`
- `OpenClaw`

### 命令片段

```bash
npx molthub@latest install email-podcast
```

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「邮件转播客技能」。

任务目标：邮件音频转换的可重用技能

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：email、elevenlabs、ffmpeg、Gmail、OpenClaw）。
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

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/38-email-to-podcast-skill.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/38-email-to-podcast-skill.md)

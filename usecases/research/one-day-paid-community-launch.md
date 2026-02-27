# 1天冷启动付费社群流程

> 从定位到执行的高密度冷启动运营打法。

## 这个案例能帮你做什么

- 你可以先把「从定位到执行的高密度冷启动运营打法。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `Telegram`
- `Notion`
- `cron`
- `OpenClaw`

### 命令片段

```bash
openclaw ask "搜索过去24小时AI编程领域的热点，生成5个选题"
openclaw ziliu publish "$draft_id" \
curl -fsSL https://openclaw.example/install.sh | bash  # 替换为实际安装地址
openclaw config set api.key "your-api-key"
openclaw config set model "claude-opus-4"
crontab -e
openclaw run daily-topic-push
openclaw ask "写一篇关于AI编程的文章"
openclaw run publish-all "article-id"
```

### 调度信息

- 0 8 * * 1
- 每天
- 定时
- 每周
- 每日

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「1天冷启动付费社群流程」。

任务目标：从定位到执行的高密度冷启动运营打法。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：Telegram、Notion、cron、OpenClaw）。
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

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/15-solo-entrepreneur-cases.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/15-solo-entrepreneur-cases.md)

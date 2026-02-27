# 可公开配置基线模板

> 通过脱敏配置建立团队基线，方便复制和协作。

## 这个案例能帮你做什么

- 你可以先把「通过脱敏配置建立团队基线，方便复制和协作。」做成一个可重复执行的小流程。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。
- 建议先跑最小闭环，再按实际反馈逐步扩展。

## 开始前准备

### 技能与工具

- `sanitized-config.json`
- `agents.defaults.model`
- `primary`
- `fallbacks`
- `memorySearch`
- `text-embedding-3-small`
- `contextPruning`
- `cache-ttl`
- `compaction.memoryFlush`
- `softThresholdTokens`
- `memory/YYYY-MM-DD.md`
- `NO_FLUSH`
- `heartbeat.model`
- `127.0.0.1`

### 命令片段

```bash
openclaw doctor --fix
openclaw security audit --deep
```

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「可公开配置基线模板」。

任务目标：通过脱敏配置建立团队基线，方便复制和协作。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：sanitized-config.json、agents.defaults.model、primary、fallbacks、memorySearch、text-embedding-3-small）。
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

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/config-example-guide.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/config-example-guide.md)

# 10分钟全平台内容发布

> 把“选题→写作→分发”压缩到 10 分钟级别，同时保留人工审核关口。

## 这个案例能帮你做什么

- 固定每天推送选题，降低“今天写什么”的决策成本。
- 快速生成初稿并进入发布链路，显著缩短单篇产出时间。
- 覆盖多平台分发流程，但保留人工审核避免自动误发。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron` | 定时推送选题与日志任务 | OpenClaw Built-in |
| 内置 | `search` 能力 | 搜索 24 小时热点选题 | OpenClaw Built-in |
| 内置 | `telegram` | 推送每日选题 | OpenClaw Built-in |
| 外部 | 飞书 API / 字流 API | 草稿承载与多平台分发 | 第三方工具链 |

## 快速体验版（先跑一轮）

先验证“选题→初稿”两步：

```text
你是我的 OpenClaw 助手。
请帮我做“10分钟全平台内容发布”的预演版：
1. 搜索过去24小时 AI 编程热点，生成 5 个选题。
2. 我选 1 个后，5 分钟内生成一版初稿。
3. 输出可发布版本与待核实点。
4. 本轮不要自动发布。
```

## 稳定自动版（可长期运行）

### 1) 定时任务

```bash
# 每天早上9点推送选题
0 9 * * * /usr/local/bin/openclaw run daily-topic-push

# 每天晚上11点生成工作日志
0 23 * * * /usr/local/bin/openclaw run daily-summary

# 每周一早上8点生成周报
0 8 * * 1 /usr/local/bin/openclaw run weekly-report
```

### 2) 选题推送脚本片段

```bash
# daily-topic-push.sh

# 1. 搜索热点
openclaw ask "搜索过去24小时AI编程领域的热点，生成5个选题"

# 2. 推送到Telegram
openclaw telegram send "今日选题推荐：\n\n[选题内容]"

# 3. 记录日志
echo "$(date): 选题推送完成" >> /var/log/openclaw/daily-push.log
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“10分钟全平台内容发布”。

每日流程：
1. 09:00 推送 5 个热点选题。
2. 我选择题目后，生成初稿。
3. 按固定风格规范优化标题、结构和结尾。
4. 推送到飞书文档待审核。
5. 审核通过后再进入多平台发布。

铁规则：
- 所有发布必须人工确认，禁止自动发布。
- 不确定事实必须标注“待核实”。
```

## 成功标准

| 指标 | 使用前 | 使用后 | 提升 |
|---|---:|---:|---:|
| 单篇耗时 | 3小时 | 10分钟 | 94.4% |
| 每周产出 | 2-3篇 | 7篇 | 200%+ |
| 平台覆盖 | 3-4个 | 14个 | 300%+ |

## 风险与边界

- 所有内容发布前必须人工确认。
- 涉及事实和数据时，若来源不确定必须标注待核实。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/15-solo-entrepreneur-cases.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/15-solo-entrepreneur-cases.md)

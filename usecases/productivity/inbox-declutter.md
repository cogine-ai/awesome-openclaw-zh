# 收件箱整理（Newsletter Digest）

> 每晚自动读取过去 24 小时订阅邮件，生成重点摘要并持续学习你的偏好。

## 这个案例能帮你做什么

- 把堆积 newsletter 转成一条可读摘要，减少“已读焦虑”。
- 按反馈迭代摘要风格，越用越贴近你的阅读偏好。
- 支持把 newsletter 与主工作邮箱分离，降低干扰。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | Gmail OAuth Setup | 读取邮件 | [clawhub.ai/kai-jar/gmail-oauth](https://clawhub.ai/kai-jar/gmail-oauth) |
| 内置 | `cron` | 每日定时摘要 | OpenClaw Built-in |
| 内置 | 记忆能力 | 根据反馈更新筛选偏好 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 newsletter 助手。
请读取过去 24 小时邮件，输出“最重要 5 条摘要 + 原文链接”。
最后问我这次筛选是否合适，并记录反馈。
本轮只执行一次，不设定时。
```

## 稳定自动版（可长期运行）

### 执行提示词（源案例）

```text
I want you to run a cron job everyday at 8 p.m. to read all the newsletter emails of the past 24 hours and give me a digest of the most important bits along with links to read more. Then ask for my feedback on whether you picked good bits, and update your memory based on my preferences for better digests in the future jobs.
```

## 成功标准

- [ ] 每晚稳定产出摘要。
- [ ] 摘要可读且附带原文链接。
- [ ] 反馈后下一轮筛选质量有提升。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/inbox-declutter.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/inbox-declutter.md)

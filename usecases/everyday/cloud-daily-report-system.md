# 云端智能日报系统

> 在云上定时抓取多源信息，自动生成并推送结构化日报。

## 这个案例能帮你做什么

- 每天固定时段自动产出“可直接阅读”的行业日报。
- 覆盖搜索、社区更新、博客、论文等多源信息，不依赖单一 RSS。
- 通过技能组合把“手工搜集+整理+推送”变成长期自动流程。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `find-skills` | 自动发现可用技能并按需安装 | [github.com/vercel-labs/skills/tree/main/skills/find-skills](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |
| 外部（需安装） | `proactive-agent` | 在可自动化场景下主动发起建议 | [github.com/leomariga/ProactiveAgent](https://github.com/leomariga/ProactiveAgent) |
| 内置 | 定时任务调度 | 固定时间生成日报 | OpenClaw Built-in |
| 内置 | 飞书推送能力 | 下发日报到团队渠道 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的云端日报助手。
请生成一份“AI 行业日报”样稿，来源包含：
1) 行业动态搜索
2) OpenClaw 社区更新（GitHub）
3) 技术博客精选
4) 学术论文速递
输出为 Markdown，按主题分组并附原文链接。
```

## 稳定自动版（可长期运行）

### 1) Skills 安装

```bash
npx clawhub@latest install find-skills
npx clawhub@latest install proactive-agent
```

### 2) 对话式安装（源案例给法）

```text
你：帮我安装这里面的Skills：
https://github.com/vercel-labs/skills/tree/main/skills/find-skills
https://github.com/leomariga/ProactiveAgent
```

### 3) 日报任务提示词

```text
你：每天早上9点，搜索以下内容并生成日报：
1. AI行业最新动态（百度搜索）
2. OpenClaw社区更新（GitHub）
3. 技术博客精选（自定义RSS源）
4. 学术论文速递（百度学术）

格式要求：
- Markdown格式
- 分类整理
- 附带原文链接
- 推送到飞书
```

### 4) 使用提醒

- `proactive-agent` 安装时可能出现 VirusTotal 警告提示（源文档已说明该现象）。
- 时区需要与云端环境一致，否则日报触发时间会偏移。
- 推送渠道（如飞书）需提前配置可用。

## 成功标准

- [ ] 每天 9:00 左右稳定收到日报。
- [ ] 日报包含多源信息并附可追溯链接。
- [ ] 结构清晰，可直接转发给团队使用。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

# 本地 CRM / DenchClaw 框架

> 用 DenchClaw 把 OpenClaw 变成一套本地优先的 CRM、销售自动化和业务运营工作台。

## 这个案例能帮你做什么

- 一条命令拉起本地 CRM，不再自己拼数据库、前端和浏览器自动化。
- 用自然语言管理线索、客户、跟进状态和看板视图。
- 把浏览器、数据表、文件系统和 OpenClaw agent 连成一个业务闭环。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | [`denchclaw`](https://github.com/DenchHQ/DenchClaw) | 本地 CRM / 业务运营框架 | DenchHQ |
| 内置 | OpenClaw profile `dench` | 独立运行 DenchClaw 对应的 OpenClaw 配置 | DenchClaw |
| 外部（框架内置） | CRM / App Builder / Browser Automation | 管表、建应用、接浏览器 | DenchClaw 内置能力 |

## 快速体验版（先跑一轮）

```text
你是我的 CRM 助手。
请先按 DenchClaw 的思路帮我设计一个最小 Leads 管理流程：
1. 字段包括 Name、Email、Company、Status、Notes
2. 给出 New / Contacted / Qualified / Won / Lost 五个状态
3. 说明适合表格视图还是 Kanban 视图
4. 本轮先不要连接外部数据源，只输出结构和使用方法
```

## 稳定自动版（可长期运行）

### 1) 一键安装

```bash
npx denchclaw@latest
```

安装完成后会在本地打开 `localhost:3100`，并创建专用 OpenClaw profile `dench`。

### 2) 常用命令

```bash
npx denchclaw@latest
npx denchclaw@latest update
npx denchclaw restart
npx denchclaw start
npx denchclaw stop
```

```bash
openclaw --profile dench gateway restart
openclaw --profile dench config set gateway.port 19001
openclaw --profile dench gateway install --force --port 19001
```

### 3) 初始操作提示词

```text
Hey, create a "Leads" object with fields: Name, Email, Company, Status (New/Contacted/Qualified/Won/Lost), and Notes. Import this CSV of leads I downloaded from Apollo.
```

```text
Show me all leads where Status is "Contacted" and sort by last updated. Switch to Kanban view grouped by Status.
```

```text
Draft a personalized outreach email to each lead in "New" status based on their company's recent news. Save the drafts in a new "Outreach Drafts" document.
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的本地 CRM 助手，请按 DenchClaw 工作方式运行：
1. 所有客户、线索和跟进动作都优先落在本地 CRM 里
2. 我可以用自然语言创建对象、字段、视图和筛选条件
3. 如果要做浏览器导入或外联动作，先说明将使用哪一类已有登录态
4. 输出每次变更涉及的对象、视图和下一步跟进建议
```

## 成功标准

- [ ] 本地能跑起 DenchClaw，并打开 `localhost:3100`。
- [ ] 至少能建立一个 Leads 对象并切换不同视图。
- [ ] OpenClaw 能围绕客户数据执行查询、筛选和草稿生成。

## 风险与边界

- DenchClaw 会把业务数据和自动化能力都收拢到本地环境，更适合个人或小团队自托管，不是即开即用的 SaaS。
- 浏览器自动化依赖你现有登录态时，要明确哪些网站和账号是允许被代理操作的。
- 这套方案偏“框架型案例”，适合把 CRM、外联和运营工作流一起落地，不只是单一联系人管理。

## 使用建议

- 先从一个对象开始，例如 Leads，再慢慢扩展到公司、联系人、外联草稿。
- 把“导入数据”“切换视图”“生成草稿”作为三条固定口令练熟，会很快感受到价值。
- 如果你是中文用户，后续最值得做的是把对象字段、状态枚举和常用视图完全中国化。

## 引用来源

- 来源仓库： [DenchHQ/DenchClaw](https://github.com/DenchHQ/DenchClaw)
- 原始条目：
  - [README.md](https://github.com/DenchHQ/DenchClaw/blob/main/README.md)
  - [hesamsheikh/awesome-openclaw-usecases/usecases/local-crm-framework.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/local-crm-framework.md)

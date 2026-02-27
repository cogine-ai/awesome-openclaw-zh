# 知识工作者全天工作流

> 以“晨报-资料整理-会议纪要-晚间复盘”构建可持续的一天效率闭环。

## 这个案例能帮你做什么

- 早上自动获取日程、待办和行业动态。
- 会议后快速沉淀纪要并同步协作工具。
- 晚上自动产出日报与知识归档，减少信息流失。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw schedule` | 晨报与晚报调度 | OpenClaw Built-in |
| 外部（按需） | `web-clipper` / `notes-sync` | 资料抓取和备忘录同步 | ClawHub |
| 内置 | 模板与同步能力 | 会议纪要模板、Notion/飞书同步 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的工作流助手。
请先演示今天的一日流程输出：
1) 早间简报（日程+待办+行业动态）
2) 一条会议纪要模板示例
3) 晚间日报示例
本轮只生成样稿，不添加定时任务。
```

## 稳定自动版（可长期运行）

### 1) 早间简报

```bash
openclaw schedule add "daily-report" \
  --time "07:00" \
  --prompt "生成今日日报，包括：日程、待办、行业动态、建议"

openclaw config set report.sources "calendar,todo,rss,notion"
openclaw config set report.channel "feishu"
```

### 2) 资料整理与会议纪要

```bash
clawhub install web-clipper
clawhub install notes-sync
openclaw config set notes.default "备忘录/行业研究"

openclaw template add "meeting-notes" \
  --format "时间、参会人员、讨论要点、行动项、下次会议"
openclaw config set sync.targets "notion,feishu"
openclaw config set reminder.action-items true
```

### 3) 晚间复盘与归档

```bash
openclaw config set archive.rules '{
  "会议纪要": "Notion/会议记录",
  "行业研究": "备忘录/行业研究",
  "项目文档": "Notion/项目管理",
  "个人笔记": "备忘录/个人成长"
}'

openclaw schedule add "daily-summary" \
  --time "19:00" \
  --prompt "生成今日工作日报"

openclaw config set knowledge.graph true
```

## 成功标准

- [ ] 早间信息准备时间显著下降。
- [ ] 会议纪要可在会后快速沉淀并可追踪行动项。
- [ ] 晚间复盘持续产出，知识资产不丢失。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

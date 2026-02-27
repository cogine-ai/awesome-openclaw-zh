# Notion 全自动运营工作流

> 让日志、选题、草稿、额度状态等运营信息自动写入 Notion 统一管理。

## 这个案例能帮你做什么

- 把分散在聊天和脚本里的运营数据沉淀到结构化数据库。
- 让“内容产出-记录-复盘”形成统一数据链路。
- 与多机器人矩阵配合，减少手工记录负担。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | Notion API / `notion_client` | 自动写入日志、选题、状态 | Notion |
| 内置 | OpenClaw 调度能力 | 定时触发写入任务 | OpenClaw Built-in |
| 外部（建议） | Python 环境 | 运行自动化脚本 | Python |

## 快速体验版（先跑一轮）

```text
你是我的 Notion 运营助手。
请先演示一次写入流程：
1) 创建一条每日日志
2) 新增一个选题及评分
3) 更新一个用户额度状态
本轮只输出将调用的字段和数据库，不执行真实写入。
```

## 稳定自动版（可长期运行）

### 1) 自动化范围（源案例）

- 每天工作日志
- 内容草稿与发布记录
- 选题库评分状态
- 群成员额度状态
- KOL 监控数据

### 2) Notion 脚本（源案例）

```python
from notion_client import Client

class NotionAutomation:
    def __init__(self, token):
        self.client = Client(auth=token)

    def create_daily_log(self, content):
        self.client.pages.create(
            parent={"database_id": "daily-log-db-id"},
            properties={
                "Date": {"date": {"start": datetime.now().isoformat()}},
                "Title": {"title": [{"text": {"content": f"日志 {datetime.now().date()}"}}]}
            },
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {"rich_text": [{"text": {"content": content}}]}
                }
            ]
        )

    def add_topic(self, topic, score, status="pending"):
        self.client.pages.create(
            parent={"database_id": "topics-db-id"},
            properties={
                "Topic": {"title": [{"text": {"content": topic}}]},
                "Score": {"number": score},
                "Status": {"select": {"name": status}}
            }
        )

    def update_credit_status(self, user_id, status):
        results = self.client.databases.query(
            database_id="credits-db-id",
            filter={"property": "UserID", "rich_text": {"equals": user_id}}
        )

        if results['results']:
            page_id = results['results'][0]['id']
            self.client.pages.update(
                page_id=page_id,
                properties={"Status": {"select": {"name": status}}}
            )
```

### 3) 运营红线（源案例）

- 不自动发布内容，发布动作必须人工确认。

## 成功标准

- [ ] Notion 数据库按分类持续更新。
- [ ] 运营关键数据可追溯。
- [ ] 自动化写入稳定且不越权发布。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/15-solo-entrepreneur-cases.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/15-solo-entrepreneur-cases.md)

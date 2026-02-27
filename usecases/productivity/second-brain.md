# 第二大脑

> 用“像发消息一样记录、像搜索一样找回”的方式构建低摩擦知识系统。

## 这个案例能帮你做什么

- 把随手想法、链接、提醒统一沉淀，降低遗忘成本。
- 通过消息入口实现零门槛采集，不依赖复杂分类。
- 可配合 Next.js 做统一检索面板。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | Telegram / iMessage / Discord | 日常输入入口 | OpenClaw Built-in |
| 内置 | OpenClaw Memory | 长期记忆存储 | OpenClaw Built-in |
| 外部（可选） | Next.js | 可视化检索界面 | Next.js |

## 快速体验版（先跑一轮）

```text
你是我的第二大脑助手。
请把我接下来发的 5 条信息全部记录，并支持我问：
“我刚才提到的书和链接是什么？”
本轮只验证采集和检索，不搭建前端。
```

## 稳定自动版（可长期运行）

### 1) 采集方式（源案例）

直接发消息给机器人：

```text
Hey, remind me to read "Designing Data-Intensive Applications"
Save this link: https://example.com/interesting-article
Remember: John recommended the restaurant on 5th street
```

### 2) 构建检索 UI 提示词（源案例）

```text
I want to build a second brain system where I can review all our notes,
conversations, and memories. Please build that out with Next.js.

Include:
- A searchable list of all memories and conversations
- Global search (Cmd+K) across everything
- Ability to filter by date and type
- Clean, minimal UI
```

## 成功标准

- [ ] 记录动作足够低摩擦，能长期坚持。
- [ ] 检索可快速找到历史信息。
- [ ] 前端面板可按时间和类型过滤。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/second-brain.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/second-brain.md)

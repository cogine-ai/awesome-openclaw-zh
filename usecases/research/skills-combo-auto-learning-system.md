# 全自动学习系统（Skills 组合）

> 把“找资源→提炼知识→复习强化”做成可重复执行的学习流水线。

## 这个案例能帮你做什么

- 自动发现高质量学习资源，不再每天手动刷信息源。
- 自动提取重点并整理成结构化笔记，减少“看了很多但记不住”。
- 自动生成闪卡与复习节奏，形成长期学习闭环。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `github-trending` / `course-finder` / `paper-search` | 发现学习资源 | ClawHub |
| 外部（需安装） | `pdf-reader` / `video-transcriber` / `note-taker` | 内容提取与笔记整理 | ClawHub |
| 外部（需安装） | `flashcard-generator` / `mind-map-creator` / `spaced-repetition` | 记忆强化 | ClawHub |
| 内置 | `openclaw workflow` / `openclaw agent` | 触发与执行工作流 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先用对话触发一次学习主题：

```bash
openclaw agent --message "我想学习Python异步编程，帮我制定学习计划"
```

原文期望流程：
- 搜索学习资源（项目、教程、文章）
- 提取核心知识点
- 生成学习笔记
- 生成复习卡片
- 推荐实践项目

## 稳定自动版（可长期运行）

### 1) 安装技能（原文命令）

```bash
clawhub install github-trending
clawhub install course-finder
clawhub install paper-search
clawhub install pdf-reader
clawhub install video-transcriber
clawhub install note-taker
clawhub install flashcard-generator
clawhub install mind-map-creator
clawhub install spaced-repetition
```

### 2) 创建学习工作流配置（原文）

保存为 `~/.openclaw/workflows/learning.json`：

```json
{
  "workflow": "自动化学习系统",
  "steps": [
    {
      "name": "发现学习资源",
      "skills": ["github-trending", "course-finder"],
      "config": {
        "topics": ["AI", "自动化", "效率工具"],
        "quality_threshold": 80
      }
    },
    {
      "name": "内容提取",
      "skills": ["pdf-reader", "video-transcriber"],
      "config": {
        "extract_key_points": true,
        "generate_summary": true
      }
    },
    {
      "name": "知识整理",
      "skills": ["note-taker", "mind-map-creator"],
      "config": {
        "format": "markdown",
        "auto_categorize": true
      }
    },
    {
      "name": "记忆强化",
      "skills": ["flashcard-generator", "spaced-repetition"],
      "config": {
        "review_schedule": "1,3,7,15,30"
      }
    }
  ]
}
```

### 3) 运行工作流

```bash
openclaw workflow run learning
```

## 成功标准

- [ ] 资源发现时间从小时级降到分钟级。
- [ ] 每轮学习都能沉淀结构化笔记和可复习卡片。
- [ ] 学习计划可重复执行，而不是一次性冲刺。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

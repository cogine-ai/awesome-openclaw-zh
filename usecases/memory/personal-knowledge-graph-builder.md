# 个人知识图谱构建

> 把碎片知识变成“节点 + 关系”的结构化图谱，支持检索、推荐和复盘。

## 这个案例能帮你做什么

- 把分散在笔记、浏览记录、对话里的知识统一进图谱。
- 自动抽取实体关系，建立“概念之间如何关联”的可追踪结构。
- 支持图谱可视化、每周更新、质量检查和导出复用。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `note-parser` | 从笔记中提取知识点 | ClawHub |
| 外部（需安装） | `browser-history-analyzer` | 从浏览历史提取主题 | ClawHub |
| 外部（需安装） | `knowledge-graph-visualizer` | 生成图谱可视化页面 | ClawHub |
| 外部（需安装） | `knowledge-exporter` | 导出图谱为 Markdown | ClawHub |
| 内置 | `openclaw agent` | 关系提取、推荐、复盘与维护 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的知识图谱助手。
我会用“#知识点 xxx”给你几条输入，
请为每条提取：实体、关系、分类，并输出一份关系网预览。
本轮不做可视化，只验证结构是否合理。
```

## 稳定自动版（可长期运行）

### 1) 知识收集

```bash
clawhub install note-parser
openclaw agent --message "请使用 note-parser skill 从 ~/.openclaw/notes 提取知识点，保存到 ~/.openclaw/knowledge/entities.json"

clawhub install browser-history-analyzer
openclaw agent --message "请使用 browser-history-analyzer skill 分析最近30天的浏览历史，保存到 ~/.openclaw/knowledge/topics.json"

openclaw agent --message "分析我最近的对话，提取关键知识点"
```

### 2) 关系提取

```bash
openclaw agent --message "分析我的知识库，提取知识点之间的关系"
```

关系定义示例：

```json
{
  "relationships": [
    {
      "from": "OpenClaw",
      "to": "Skills",
      "type": "包含",
      "weight": 1.0
    },
    {
      "from": "Skills",
      "to": "自动化",
      "type": "实现",
      "weight": 0.9
    },
    {
      "from": "find-skills",
      "to": "ProactiveAgent",
      "type": "配合使用",
      "weight": 0.8
    }
  ]
}
```

### 3) 可视化

```bash
clawhub install knowledge-graph-visualizer
openclaw skills run knowledge-graph-visualizer \
  --input ~/.openclaw/knowledge \
  --output ~/.openclaw/knowledge/graph.html \
  --style "force-directed"

open ~/.openclaw/knowledge/graph.html
```

### 4) 应用与维护

```bash
openclaw agent --message "搜索：如何使用Skills"
openclaw agent --message "根据我的知识图谱，推荐下一步学习内容"
openclaw agent --message "生成本周知识复盘报告"

# 每周更新
openclaw agent --message "更新知识图谱"

# 质量检查
openclaw agent --message "检查知识图谱质量"

# 导出
openclaw agent --message "请使用 knowledge-exporter skill 导出知识图谱为 markdown 格式，保存到 ~/knowledge-base.md"
```

## 成功标准

- [ ] 图谱能持续吸收新增知识点。
- [ ] 关系网络可支持检索与学习推荐。
- [ ] 每周更新与质量检查稳定执行。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

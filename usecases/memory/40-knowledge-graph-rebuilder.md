# 知识图谱重建器

> 每晚从当日日志提取实体和关系，重建可查询的知识图结构。

## 这个案例能帮你做什么

- 把零散日志转为“实体-关系”结构，检索更快更准。
- 每晚自动更新，避免知识图长期滞后。
- 为“谁和谁相关、什么依赖什么”这类问题提供直接查询能力。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `memory` | 图谱存取与索引更新 | [clawhub.ai/skills/mem](https://clawhub.ai/skills/mem) |
| 内置 | `filesystem` | 读取每日记忆文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的知识图谱助手。
请读取今天的 memory 文件，提取：
1) 实体（人/项目/概念）
2) 关系（依赖/关联/参与）
输出一份“新增节点 + 新增关系”预览，不做写入。
```

## 稳定自动版（可长期运行）

### 1) 图谱 Schema

```javascript
const schema = {
  entities: ['Person', 'Project', 'Concept'],
  relations: ['works_on', 'knows', 'depends_on']
};
```

### 2) 重建流程

```javascript
function rebuildGraph() {
  const logs = readDailyLogs();
  const entities = extractEntities(logs);
  const relations = extractRelations(logs);
  return { entities, relations };
}
```

### 3) OpenClaw 执行提示词（自动版）

```markdown
## Knowledge Graph Rebuilder

Every night:
1. Read today's memory files
2. Extract entities (people, projects, concepts)
3. Identify relationships
4. Merge into knowledge graph
5. Update semantic indices
6. Prune outdated connections

Query capabilities:
- "What projects depend on X?"
- "Who knows about Y?"
- "Related concepts to Z"
```

## 成功标准

- [ ] 每晚重建稳定执行。
- [ ] 新实体和新关系可持续增长。
- [ ] 典型图谱查询可快速返回有效结果。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/40-knowledge-graph-rebuilder.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/40-knowledge-graph-rebuilder.md)

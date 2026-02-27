# 语义记忆搜索

> 给 OpenClaw 的 Markdown 记忆层加一层向量检索，按“语义”找回历史决策。

## 这个案例能帮你做什么

- 不再只能靠关键词 grep；用“意思相近”也能命中相关记录。
- 结合向量 + BM25 混合检索，兼顾语义召回与精确命中。
- 基于内容哈希增量索引，重复执行不会重复花 embedding 成本。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `memsearch` | 索引与检索 OpenClaw memory | [zilliztech/memsearch](https://github.com/zilliztech/memsearch) |
| 外部（需安装） | Python 3.10+ | 运行 `memsearch` CLI | Python |
| 外部（可选） | 本地 embedding provider | 无 API Key 本地化检索 | `memsearch[local]` |

## 快速体验版（先跑一轮）

```bash
pip install memsearch
memsearch config init
memsearch index ~/path/to/your/memory/
memsearch search "what caching solution did we pick?"
```

## 稳定自动版（可长期运行）

### 1) 开启文件监听自动同步

```bash
memsearch watch ~/path/to/your/memory/
```

### 2) 本地 embedding（无外部 API）

```bash
pip install "memsearch[local]"
memsearch config set embedding.provider local
memsearch index ~/path/to/your/memory/
```

### 3) OpenClaw 执行提示词（检索增强版）

```text
你是我的记忆检索助手。
当我问历史决策时，先调用 memsearch 语义检索，再返回：
1. 最相关的 3 条记忆
2. 每条记忆的原始文件位置
3. 与问题的相关原因
4. 如果结果不足，明确告诉我缺什么信息
```

## 成功标准

- [ ] 用不同措辞提问，仍能稳定命中历史记录。
- [ ] 索引可持续增量更新，不重复重建全库。
- [ ] 记忆检索返回可追溯到具体文件片段。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/semantic-memory-search.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/semantic-memory-search.md)

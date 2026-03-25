# arXiv 论文阅读助手

> 直接按 arXiv ID 抓摘要、目录和全文，让 OpenClaw 变成可对话的论文阅读器。

## 这个案例能帮你做什么

- 不再手动下载 PDF 再到处切窗口，直接在 OpenClaw 里读论文。
- 先看摘要、再看目录、最后按需深读某一节，减少无效阅读。
- 一次比较多篇论文，快速决定先读哪篇、哪篇只做归档。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`arxiv-reader`](https://github.com/Prismer-AI/Prismer/tree/main/skills/arxiv-reader) | 获取 arXiv 摘要、目录与扁平化全文 | Prismer |
| 内置 | 记忆/笔记能力 | 记录已读论文与一句话结论 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的论文阅读助手。
请先按下面方式帮我预演：
1. 当我给出 arXiv ID 时，先只抓摘要
2. 如果这篇值得读，再列出目录
3. 最后用中文总结这篇论文的核心贡献
4. 本轮只做一篇，不做批量对比
```

## 稳定自动版（可长期运行）

### 1) 安装方式

原始用例建议直接把 `skills/arxiv-reader/` 放进 OpenClaw 的 skills 目录中使用。

### 2) OpenClaw 执行提示词（自动版）

```text
我正在做论文研究，请按这个阅读流程工作：

1. 当我给你一个 arXiv ID（例如 2301.00001）：
   - 先获取 abstract，帮我判断值不值得继续读
   - 如果我说“继续”，再获取全文，默认去掉 appendix
   - 最后总结核心贡献、方法和实验结果

2. 当我给你多个 arXiv ID：
   - 先取回全部摘要
   - 给我一个对比表，说明各自更适合解决什么问题

3. 当我问某个章节：
   - 先告诉我这篇论文有哪些 sections
   - 再抓指定章节并详细解释

4. 帮我维护一份已读论文清单，每篇保留一句 takeaway。
```

### 3) 示例参数（来自原技能）

全文抓取：

```json
{ "arxiv_id": "2301.00001", "remove_appendix": true }
```

目录提取：

```json
{ "arxiv_id": "2301.00001" }
```

摘要提取：

```json
{ "arxiv_id": "2301.00001" }
```

## 成功标准

- [ ] 能按 arXiv ID 拉到摘要、目录和全文。
- [ ] 多篇论文可以先做摘要级对比，再决定深读顺序。
- [ ] 已读论文能沉淀成可回看的研究清单。

## 风险与边界

- 首次抓取大论文时可能要等 10-30 秒，重复请求才会更快。
- 这类工具更适合 LaTeX 源可用的论文；如果源有缺失，解析效果会受影响。
- 摘要和全文都是研究辅助，不能替代你自己对实验和结论的判断。

## 使用建议

- 先用 `arxiv_abstract` 做初筛，再决定要不要走全文。
- 对比多篇论文时，最好给一个明确研究主题，否则相关性排序会偏散。
- 和 HF Papers 那篇组合使用效果最好：先追热点，再深读。

## 引用来源

- 来源仓库： [Prismer-AI/Prismer](https://github.com/Prismer-AI/Prismer)
- 原始条目：
  - [skills/arxiv-reader/SKILL.md](https://github.com/Prismer-AI/Prismer/blob/main/skills/arxiv-reader/SKILL.md)
  - [hesamsheikh/awesome-openclaw-usecases/usecases/arxiv-paper-reader.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/arxiv-paper-reader.md)

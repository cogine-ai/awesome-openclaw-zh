# HuggingFace Papers 研究发现流水线

> 每天自动抓 Hugging Face Papers 热门论文，再联动 arXiv 深读，形成一套持续研究雷达。

## 这个案例能帮你做什么

- 每天先看 Hugging Face Papers 热榜，快速知道大家在关注什么。
- 对某篇论文继续展开：看摘要、作者、GitHub 仓库、社区评论和更完整的 arXiv 原文。
- 把当天读过的论文沉淀成一份中文研究简报，方便团队同步和二次检索。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`hf-papers`](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/hf-papers-research-discovery.md) | 获取 Hugging Face Papers 热榜、搜索、详情与评论 | 社区场景说明 |
| 外部 | [`arxiv-source`](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/hf-papers-research-discovery.md) | 联动 arXiv 原文做深读 | 社区场景说明 |
| 内置 | 记忆/笔记能力 | 持续记录当日看过的论文与一句话结论 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 AI 研究助理。
请先做一个 Hugging Face Papers 今日热榜预演：
1. 列出今天最热门的 5 篇论文
2. 每篇给出标题、点赞数、GitHub 仓库（如果有）和一句中文摘要
3. 帮我挑出最值得深读的 2 篇
4. 本轮先不要做长期记忆写入，只输出今日榜单和推荐理由
```

## 稳定自动版（可长期运行）

### 1) 安装两个技能

```bash
clawhub install hf-papers
clawhub install arxiv-source
```

### 2) OpenClaw 执行提示词（自动版）

```text
我想长期追踪机器学习研究，请按下面工作流运行：

1. 每天早上先给我看 Hugging Face Papers 热榜前 10
   - 每篇输出：标题、点赞数、GitHub 仓库（如果有）、一句中文总结

2. 当我说“搜索 [topic]”时：
   - 在 HF Papers 里搜索相关论文
   - 优先标出高点赞或带 GitHub 仓库的条目

3. 当我选中某篇论文时：
   - 输出完整摘要、作者和相关资源
   - 如果有评论，提炼社区讨论焦点
   - 问我是否继续深读

4. 如果我要深读：
   - 用 arxiv-source 取回全文
   - 总结核心贡献、方法、实验结果和我应该看的代码仓库

5. 帮我维护一份“今日已读论文清单”，每篇保留一句 takeaway。
```

### 3) 输出模板（可选）

```markdown
# 今日 HF Papers 研究简报

## 热门论文
- 标题：
  - 点赞：
  - GitHub：
  - 一句话摘要：

## 深读候选
- 论文：
  - 为什么值得读：

## 今日已读
- 论文：
  - takeaway：
```

## 成功标准

- [ ] 能稳定拿到当日 Hugging Face Papers 热榜。
- [ ] 选中论文后能继续拉出详情、评论和 arXiv 原文。
- [ ] 最终能沉淀成一份当天可复用的研究简报。

## 风险与边界

- 这个流水线依赖公开数据源，榜单和评论区内容会随时间变化。
- 社区热度不等于论文质量，仍然需要你自己做筛选判断。
- 如果当天热门论文没有 arXiv 源或源信息不完整，深读环节会受限。

## 使用建议

- 适合每天固定一个时间跑，把“追热点”和“深读”拆成两步。
- 给不同研究方向设置不同检索口令，例如“搜索 agentic coding”“搜索 multimodal”。
- 如果你已经有飞书/邮件渠道，可以把最终研究简报推送出去，而不是只停留在聊天窗口里。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/hf-papers-research-discovery.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/hf-papers-research-discovery.md)

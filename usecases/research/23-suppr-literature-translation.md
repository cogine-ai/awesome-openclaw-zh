# Suppr 文献检索与文档翻译

> 用 Suppr MCP 或 Skills 把学术文献检索、论文元数据整理和 PDF 翻译接入 OpenClaw。

## 这个案例能帮你做什么

- 用自然语言检索 PubMed 方向的学术文献，并返回标题、摘要、DOI、PMID、作者和期刊信息。
- 创建、查询和管理文档翻译任务，支持 PDF、Word、PPT、Excel、TXT、HTML 等格式。
- 把论文检索、筛选、翻译和阅读笔记整理成一个研究工作流。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`suppr-mcp`](https://github.com/zjg678/suppr-mcp) | MCP 方式接入 Suppr 文献检索和翻译 API | 社区 MCP |
| 外部 | [`suppr-skills`](https://github.com/WildDataX/suppr-skills) | Claude Code / Skill 方式调用 Suppr 检索和翻译能力 | 社区 Skills |
| 外部 | `SUPPR_API_KEY` | 调用 Suppr API 的认证密钥 | Suppr |

## 快速体验版（先跑一轮）

```text
你是我的学术研究助手。
请搜索「CRISPR gene editing therapy」相关的最新论文：
1. 返回前 5 篇
2. 每篇给标题、年份、期刊、DOI、PMID 和 2 句摘要
3. 最后按研究方向归类
本轮只做检索，不翻译全文。
```

## 稳定自动版（可长期运行）

### 1) 安装 MCP Server

```bash
npm install -g suppr-mcp
export SUPPR_API_KEY="your_api_key_here"
```

也可以用 npx 方式启动：

```bash
npx suppr-mcp
```

### 2) MCP 配置示例

```json
{
  "mcpServers": {
    "suppr": {
      "command": "npx",
      "args": ["-y", "suppr-mcp"],
      "env": {
        "SUPPR_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的论文研究助手，请执行「Suppr 文献检索与翻译」流程。

执行步骤：
1. 根据我的研究问题检索相关论文
2. 按相关性筛选前 10 篇，列出 DOI、PMID、摘要和年份
3. 让我选择需要阅读全文或翻译的论文
4. 对确认的 PDF 创建翻译任务
5. 轮询任务状态，完成后返回译文链接和阅读笔记
```

## 成功标准

- [ ] 能返回结构化文献元数据。
- [ ] 能创建并查询翻译任务状态。
- [ ] 输出中明确区分“检索结果”和“AI 总结/归纳”。

## 风险与边界

- 需要 Suppr API Key，不应把密钥写入仓库。
- 上传或提交文档 URL 前，要确认版权、隐私和数据合规要求。
- 文献检索结果需要人工复核，尤其是医学和药物相关结论。

## 引用来源

- 来源 issue： [cogine-ai/awesome-openclaw-zh#11](https://github.com/cogine-ai/awesome-openclaw-zh/issues/11)
- MCP： [zjg678/suppr-mcp](https://github.com/zjg678/suppr-mcp)
- Skills： [WildDataX/suppr-skills](https://github.com/WildDataX/suppr-skills)

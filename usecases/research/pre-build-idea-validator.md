# 开工前想法验证闸门（Pre-Build Idea Validator）

> 在开始写代码之前先跑竞争度检查，避免投入后才发现赛道过度拥挤。

## 这个案例能帮你做什么

- 在 GitHub / HN / npm / PyPI / Product Hunt 五个来源先做竞争扫描。
- 输出 `reality_signal`（0-100）作为是否继续开发的前置信号。
- 用固定阈值规则决定“继续 / 转向 / 暂停讨论”。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `MCP server 接入（mcpServers）` | 在 OpenClaw 中注册并调用外部 MCP 服务 | hesamsheikh/awesome-openclaw-usecases |
| 外部（需安装） | [`idea-reality-mcp`](https://github.com/mnemox-ai/idea-reality-mcp) | 返回 `reality_signal` 与竞品结果 | hesamsheikh/awesome-openclaw-usecases |

## 快速体验版（先跑一轮）

1. 安装 `idea-reality-mcp`。
2. 在 OpenClaw 配置里添加 `mcpServers.idea-reality`。
3. 对 1 个新想法先跑检查，再决定是否编码。

```bash
uvx idea-reality-mcp
```

```json
{
  "mcpServers": {
    "idea-reality": {
      "command": "uvx",
      "args": ["idea-reality-mcp"]
    }
  }
}
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 把 `idea_check` 固化为新项目/新功能默认前置步骤。
2. `reality_signal > 70` 先停并报告前三竞品；`30-70` 给 pivot_hints；`< 30` 再继续。
3. 每次都先展示评分与竞品，再进入编码阶段。

## 成功标准

- [ ] 每个新想法在编码前都执行过 `idea_check`。
- [ ] 高竞争想法不会直接进入开发。
- [ ] 每次决策都有评分和竞品依据可追溯。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/pre-build-idea-validator.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/pre-build-idea-validator.md)

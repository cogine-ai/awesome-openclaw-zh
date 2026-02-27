# 数据分析工作流（Skills组合）

> 把数据收集、清洗、分析、可视化和报告写作串成自动化分析管线。

## 这个案例能帮你做什么

- 避免手工在多个工具之间反复切换。
- 把一次性分析流程沉淀为可复用模板。
- 显著缩短“拿到数据到拿到结论”的时间。

## 你需要的 Skills（按类型）

| 类型 | Skills 组合 | 用途 | 来源 |
|---|---|---|---|
| 外部 | `api-connector` + `web-scraper` + `database-query` | 数据收集 | Skills 组合 |
| 外部 | `data-cleaner` + `duplicate-remover` + `format-converter` | 数据清洗 | Skills 组合 |
| 外部 | `statistical-analyzer` + `trend-detector` + `anomaly-finder` | 数据分析 | Skills 组合 |
| 外部 | `chart-generator` + `dashboard-creator` | 可视化 | Skills 组合 |
| 外部 | `report-writer` + `insight-summarizer` | 报告生成 | Skills 组合 |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“数据分析工作流（Skills组合）”的预演版：
1. 以 OpenClaw 项目增长为样本收集数据。
2. 清洗并标准化数据。
3. 输出趋势分析 + 1张关键图表。
4. 生成一页分析结论。
```

## 稳定自动版（可长期运行）

### 1) 流程定义（原文）

```text
数据收集 → 数据清洗 → 数据分析 → 可视化 → 报告生成
```

### 2) Skills 组合方案

```bash
# 数据收集
api-connector + web-scraper + database-query
  ↓
# 数据清洗
data-cleaner + duplicate-remover + format-converter
  ↓
# 数据分析
statistical-analyzer + trend-detector + anomaly-finder
  ↓
# 可视化
chart-generator + dashboard-creator
  ↓
# 报告生成
report-writer + insight-summarizer
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“数据分析工作流（Skills组合）”。

请按流程执行：
1. 收集目标数据（示例：OpenClaw 增长趋势）。
2. 去重、补缺失、格式标准化。
3. 分析增长、活跃度、用户画像、功能偏好。
4. 生成趋势图和分类图。
5. 输出《数据分析报告》：核心指标、洞察、建议。
```

## 成功标准

- [ ] 分析时间：从4小时缩短到10分钟
- [ ] 数据准确性提升约40%
- [ ] 洞察深度提升约60%
- [ ] 决策效率提升约80%

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

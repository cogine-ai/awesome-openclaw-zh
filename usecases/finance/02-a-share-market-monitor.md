# A 股每日行情监控

> 让 OpenClaw 在交易日前后自动整理 A 股行情、板块轮动和自选股变化。

## 这个案例能帮你做什么

- 开盘前整理隔夜外盘、A50、今日重要事件和自选股提醒。
- 收盘后汇总指数涨跌、成交量、涨跌家数、板块排名和资金流向。
- 跟踪自选股表现，把每日复盘自动推送到飞书、钉钉或企业微信。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`AKShare`](https://github.com/akfamily/akshare) | 获取 A 股、港股、指数、板块和宏观数据 | 开源金融数据库 |
| 外部（可选） | [`mcp-cn-a-stock`](https://github.com/elsejj/mcp-cn-a-stock) | 用 MCP 方式查询 A 股个股信息 | 社区 MCP |
| 内置 | Cron / 定时任务 | 每个交易日自动推送简报 | OpenClaw |

## 快速体验版（先跑一轮）

```text
你是我的 A 股信息整理助手。
请用可获取的数据生成一份盘后复盘：
1. 上证、深成指、创业板指数涨跌
2. 涨幅前 5 的行业板块
3. 北向资金或主力资金摘要
4. 我的自选股：600519、300750、000858
只做信息整理，不给买卖建议。
```

## 稳定自动版（可长期运行）

### 1) 安装数据依赖

```bash
pip install akshare
```

如果使用 MCP 服务，则按 `mcp-cn-a-stock` 项目说明配置 MCP server。

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 A 股行情监控助手，请在每个交易日执行：

盘前 08:30：
1. 整理隔夜美股、A50、重要财经日历
2. 标出可能影响我自选股的事件

盘后 15:30：
1. 整理指数涨跌、成交量、涨跌家数
2. 输出板块涨跌 TOP5
3. 汇总自选股表现和异常波动
4. 明确声明：这不是投资建议
```

### 3) 输出模板

```markdown
# A 股每日复盘

- 日期：
- 市场概览：
- 热点板块：
- 资金流向：
- 自选股：
- 明日关注：
- 风险提示：仅供信息整理，不构成投资建议。
```

## 成功标准

- [ ] 能稳定生成盘前或盘后简报。
- [ ] 自选股代码能被正确识别。
- [ ] 输出只做信息整理，不直接生成买卖指令。

## 风险与边界

- AKShare 部分接口依赖公开网站数据，海外 IP 可能访问不稳定。
- 金融信息有延迟和缺失风险，重要决策要交叉验证。
- 本用例不构成投资建议，不应让 AI 自动下单。

## 引用来源

- 来源仓库： [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)
- 原始条目： [usecases/cn-a-share-monitor.md](https://github.com/AlexAnys/awesome-openclaw-usecases-zh/blob/main/usecases/cn-a-share-monitor.md)
- 数据库： [akfamily/akshare](https://github.com/akfamily/akshare)
- MCP： [elsejj/mcp-cn-a-stock](https://github.com/elsejj/mcp-cn-a-stock)

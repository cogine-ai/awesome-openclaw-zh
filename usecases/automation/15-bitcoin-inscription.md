# 比特币铭文网页

> 夜间自动生成并上链一个小网页，得到长期可访问的链上页面资产。

## 这个案例能帮你做什么

- 把个人介绍页/作品页做成链上铭文，不依赖传统服务器托管。
- 自动控制页面体积与上链流程，降低手工处理成本。
- 早上直接拿到交易哈希、成本和产出结果。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `bitcoin` | 发起 Ordinal inscription | OpenClaw Built-in |
| 内置 | `web` | 生成网页内容（HTML） | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只生成页面和成本估算，不发起上链：

```text
你是我的 OpenClaw 助手。
请帮我做“比特币铭文网页”的预演版：
1. 生成一个个人主页 HTML 初稿。
2. 控制页面体积 <50KB。
3. 给出上链步骤与成本估算（sats 和美元）。
4. 本轮不要提交 inscription，只输出可执行计划。
```

## 稳定自动版（可长期运行）

### 1) HTML 模板

```html
<!DOCTYPE html>
<html>
<head><title>{{name}}</title></head>
<body>
  <h1>{{name}}</h1>
  <p>{{description}}</p>
</body>
</html>
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Bitcoin Inscription”。
请使用内置 Skills：bitcoin、web。

在夜间任务中按顺序执行：
1. 生成 HTML 页面内容。
2. 优化页面大小（<50KB）。
3. 通过 clawdbot.ordnet.io 提交 inscription。
4. 认领 .web3 域名。
5. 记录交易哈希与成本。
6. 写入晨报。

基线信息：
- Cost: ~5800 sats (~$0.50)
- Time: ~10 minutes
- Result: Permanent on-chain presence
```

## 成功标准

- [ ] 1 page inscribed per week
- [ ] All pages <50KB
- [ ] Domains registered successfully

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/15-bitcoin-inscription.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/15-bitcoin-inscription.md)

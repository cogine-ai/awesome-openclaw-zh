# 电商多 Agent 运营助手

> 用多个 OpenClaw Agent 分别处理销售、库存、客服和商品分析，让电商运营从查后台变成问对话。

## 这个案例能帮你做什么

- 在飞书、钉钉或 Slack 群里直接查询销售、库存、商品和客户数据。
- 用不同 Agent 绑定不同群组：销售助手看销售，客服助手看售后，库存助手看补货。
- 通过定时任务主动推送库存预警、退货异常和每日运营简报。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 自建 | `sales-query` | 查询销售额、订单、退货和趋势 | 电商 API |
| 自建 | `inventory-alert` | 检查低库存、断货和补货建议 | 电商 API |
| 自建 | `customer-insight` | 汇总新客、复购、地域和客诉信号 | 电商 API |
| 内置 | 多 Agent / bindings | 将不同群聊路由到不同 Agent | OpenClaw |

## 快速体验版（先跑一轮）

```text
你是我的电商运营助手。
请先用模拟数据生成一份今日运营简报：
1. 今日销售额、订单数、客单价
2. 库存低于安全线的商品
3. 退款率异常的商品
4. 明天优先处理的 3 件事
本轮不要连接真实店铺后台。
```

## 稳定自动版（可长期运行）

### 1) 按角色拆分 Agent

```json
{
  "agents": {
    "list": [
      { "id": "sales", "name": "销售助手", "workspace": "/data/ws/sales" },
      { "id": "support", "name": "售后客服", "workspace": "/data/ws/support" },
      { "id": "inventory", "name": "库存助手", "workspace": "/data/ws/inventory" }
    ]
  }
}
```

### 2) 将群组绑定到 Agent

```json
{
  "bindings": [
    {
      "match": { "channel": "feishu", "peer": { "kind": "group", "id": "oc_sales" } },
      "agentId": "sales"
    },
    {
      "match": { "channel": "feishu", "peer": { "kind": "group", "id": "oc_support" } },
      "agentId": "support"
    }
  ]
}
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是电商运营多 Agent 系统里的销售助手。
请只处理销售和商品分析相关问题。
当用户询问今日销售、热销商品、滞销商品、退款异常时：
1. 调用对应 Skill 查询数据
2. 先给结论，再给表格
3. 标注异常数据和可能原因
4. 不执行退款、改价、下架等写操作
```

## 成功标准

- [ ] 不同群组消息能进入对应 Agent。
- [ ] 销售、客服、库存能力边界清晰。
- [ ] 写操作默认关闭，只有查数和告警自动执行。

## 风险与边界

- 淘宝、京东、拼多多等平台 API 通常需要商家认证和应用审核。
- Shopify 等跨境电商平台 API 更开放，适合作为第一版验证。
- 电商场景不要让 AI 默认执行退款、改价、下架、发券等动作。

## 引用来源

- 来源仓库： [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)
- 原始条目： [usecases/cn-ecommerce-multi-agent.md](https://github.com/AlexAnys/awesome-openclaw-usecases-zh/blob/main/usecases/cn-ecommerce-multi-agent.md)

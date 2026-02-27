# 比价购物助手

> 一条消息完成多平台比价、运费汇总、优惠码检查与购买建议。

## 这个案例能帮你做什么

- 把每次购买前 15-20 分钟的手工比价压缩到几分钟。
- 用统一表格比较“总价”而非只看标价。
- 自动提醒高价风险、同价位新款、近期促销窗口。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Web Search` | 搜索电商平台商品 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | `Web Fetch` | 抓取价格、运费、链接等页面信息 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的购物助手。
请帮我对“[Product Name]”做一次比价预览：
Amazon、Walmart、Best Buy、Target。
输出：标价、运费、总价、链接、最佳购买建议。
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are my shopping assistant. When I tell you something I want to buy:

1. Search across:
- Amazon
- Walmart
- Best Buy
- Target
- [Add local stores relevant to YOUR COUNTRY]

2. Compare:
| Store | Price | Shipping | Total | Link |

3. Report:
- Best Deal
- Coupon codes found
- Price history (if available)

Extras:
- Check if a newer model is available at similar price
- Flag unusually high prices
- Note upcoming sales (Black Friday, Prime Day) if within 2 weeks

Rules:
- Compare identical or equivalent products only
- Include total cost (shipping + tax estimate)
- Flag marketplace sellers with poor ratings
```

### 调度配置

- 按需触发：发送“我要买 xxx”时执行

## 成功标准

- [ ] 比价结果 2 分钟左右可返回。
- [ ] 购买前能看到总价维度最佳选项。
- [ ] 降低“买完才发现更便宜”的概率。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/67-price-comparison-shopper.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/67-price-comparison-shopper.md)

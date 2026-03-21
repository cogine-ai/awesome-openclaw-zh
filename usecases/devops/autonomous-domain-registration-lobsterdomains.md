# 用加密货币自动注册域名（LobsterDomains）

> 让 AI 自主完成域名查询、付款和注册全流程，无需人工干预。

## 这个案例能帮你做什么

- 通过 API 查询任意域名的可用性和实时价格（支持 .com/.xyz/.org 等 1000+ 后缀）
- 用 USDC/USDT/ETH/BTC 完成链上支付，收到 DNS 管理凭据
- 全程无需浏览器、无需验证码、无需信用卡，AI 完全自主操作

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`lobsterdomains`](https://clawhub.ai/esokullu/lobsterdomains) | 加密货币域名注册 API | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我查询 [你想要的域名].com 是否可用，以及当前价格。
不要执行付款，只需告诉我结果。
```

## 稳定自动版（可长期运行）

### 1) OpenClaw 执行提示词

```text
你是我的域名注册助手，请用 LobsterDomains 完成以下操作：
目标域名：[域名]

步骤：
1. GET https://lobsterdomains.xyz/api/v1/domains/check?domain=[域名] 查询可用性和价格
2. 确认价格后，告知用户需支付的 USDC 金额和收款地址
3. 收到链上交易 hash 后，POST https://lobsterdomains.xyz/api/v1/domains/register 完成注册
4. 返回 DNS 管理凭据
```

## 成功标准

- [ ] 域名查询返回 available: true
- [ ] 注册完成后收到 DNS 管理凭据

## 风险与边界

- 域名采用「到期不续费自动释放」策略，请在到期前手动续费
- 建议先查询价格再付款，ETH/BTC 汇率波动较大

## 引用来源

- 官网：https://lobsterdomains.xyz
- ClawHub Skill：https://clawhub.ai/esokullu/lobsterdomains
- Skill 文档（skills.md）：https://lobsterdomains.xyz/skills.md
- API 端点：`GET https://lobsterdomains.xyz/api/v1/domains/check`，`POST https://lobsterdomains.xyz/api/v1/domains/register`

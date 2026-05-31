# 加密货币自动注册域名（LobsterDomains）

> 让 OpenClaw 通过 API 完成域名查询、链上付款确认和注册流程。

## 这个案例能帮你做什么

- 查询目标域名是否可注册，以及当前价格和可用后缀。
- 用 USDC、USDT、ETH、BTC 等方式完成付款确认后继续注册。
- 获得 DNS 管理凭据，把域名购买流程纳入自动化项目启动链路。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`lobsterdomains`](https://clawhub.ai/esokullu/lobsterdomains) | 域名查询、注册和链上付款确认 | ClawHub |
| 外部 | LobsterDomains API Key | 调用域名注册 API | LobsterDomains |

## 快速体验版（先跑一轮）

```text
你是我的域名助手。
请帮我查询下面 5 个域名是否可注册，并按价格排序：
1. [domain-a].com
2. [domain-b].xyz
3. [domain-c].ai
4. [domain-d].org
5. [domain-e].dev
本轮只查询，不注册、不付款。
```

## 稳定自动版（可长期运行）

### 1) 获取 API Key

在 LobsterDomains 控制台生成 API Key，并通过环境变量或本地安全配置传给 OpenClaw。

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的域名注册助手，请使用 LobsterDomains 完成以下流程：

目标域名：[域名]
执行步骤：
1. 查询域名可用性和价格
2. 展示价格、币种、链、收款地址和到期/续费规则
3. 等我确认后再进入付款流程
4. 我提供交易 hash 后，再提交注册请求
5. 返回 DNS 管理凭据，并提醒我保存到密码管理器
```

## 成功标准

- [ ] 查询阶段不触发付款或注册。
- [ ] 注册前明确展示价格、链和币种。
- [ ] 注册成功后返回 DNS 管理入口或凭据保存建议。

## 风险与边界

- 域名注册和链上付款不可轻易回滚，必须显式确认。
- API Key、DNS 凭据和交易 hash 不应写入公开仓库。
- 建议先把域名注册流程用于测试域名，再接入正式业务域名。

## 引用来源

- 来源 PR： [cogine-ai/awesome-openclaw-zh#7](https://github.com/cogine-ai/awesome-openclaw-zh/pull/7)
- Skill 仓库： [esokullu/lobsterdomains-skills](https://github.com/esokullu/lobsterdomains-skills)
- Skill 文档：
  - [README.md](https://github.com/esokullu/lobsterdomains-skills/blob/main/README.md)
  - [SKILL.md](https://github.com/esokullu/lobsterdomains-skills/blob/main/SKILL.md)

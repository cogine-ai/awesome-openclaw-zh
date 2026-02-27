# 加密幸运饼干

> 生成“交易智慧短句”并做成可交互网页，再铭刻上链长期保存。

## 这个案例能帮你做什么

- 每周批量产出可分享的加密短句，用于社区互动和传播。
- 自动生成带随机展示逻辑的网页，提高内容可玩性。
- 上链后可形成长期可访问的 `.web3` 内容资产。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `bitcoin` | 提交链上铭文 | OpenClaw Built-in |
| 内置 | `filesystem` | 管理 fortune 文案和页面文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做文案和页面，不上链：

```text
你是我的 OpenClaw 助手。
请帮我做“加密幸运饼干”的预演版：
1. 生成 10 条加密主题短句（交易、安全、市场心理）。
2. 生成带随机展示逻辑的 HTML 页面。
3. 本轮不要执行铭文，只输出页面内容和预估流程。
```

## 稳定自动版（可长期运行）

### 1) 文案库示例

```javascript
const fortunes = [
  "HODL through the dip, profit comes to those who wait",
  "Fear and greed index whispers: check before you trade",
  "Your private keys are your true wallet, guard them well"
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Crypto Fortune Cookie”。
请使用内置 Skills：bitcoin、filesystem。

每周执行：
1. 生成 10 条新的 crypto fortunes。
2. 组合 fortune 选择逻辑。
3. 生成交互式 HTML 页面。
4. 铭刻到 Bitcoin。
5. 将域名分享到社区。

Fortune themes:
- Trading wisdom
- Security reminders
- Market psychology
- Technical analysis
```

## 成功标准

- [ ] 10 new fortunes weekly
- [ ] Page interaction tracked
- [ ] Community sharing

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/46-crypto-fortune-cookie.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/46-crypto-fortune-cookie.md)

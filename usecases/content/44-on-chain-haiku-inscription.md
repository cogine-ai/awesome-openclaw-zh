# 链上俳句铭文

> 夜间生成加密主题俳句并铭刻上链，形成可长期保留的创意页面。

## 这个案例能帮你做什么

- 把创意内容（俳句）和区块链永久存储结合，做成可分享作品。
- 用固定约束（5-7-5、主题限定、页面大小）保证输出稳定。
- 早上可直接查看铭文哈希和页面结果。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `bitcoin` | 发起铭文流程 | OpenClaw Built-in |
| 内置 | `filesystem` | 保存俳句与页面文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只生成内容，不上链：

```text
你是我的 OpenClaw 助手。
请帮我做“链上俳句铭文”的预演版：
1. 生成 3-5 条加密主题俳句。
2. 每条遵循 5-7-5 音节结构。
3. 组装成一个 HTML 页面（<10KB）。
4. 本轮只输出页面内容和上链计划，不执行 inscription。
```

## 稳定自动版（可长期运行）

### 1) 俳句素材示例

```javascript
const haikus = [
  "Private keys sleep deep",
  "Immutable blocks rise high",
  "Trustless code runs true"
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“On-Chain Haiku Inscription”。
请使用内置 Skills：bitcoin、filesystem。

夜间任务流程：
1. 生成 3-5 条 crypto-themed haikus。
2. 组装为 HTML 页面。
3. 通过 clawdbot 发起比特币铭文。
4. 认领 .web3 域名。
5. 记录 transaction hash。
6. 将结果写入晨报。

约束：
- Traditional 5-7-5 syllables
- Crypto/blockchain themes
- Page <10KB
```

## 成功标准

- [ ] 1 haiku set per week
- [ ] All inscribed successfully
- [ ] Domains registered

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/44-on-chain-haiku-inscription.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/44-on-chain-haiku-inscription.md)

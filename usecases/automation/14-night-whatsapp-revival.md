# 夜间 WhatsApp 关系维护

> 自动处理未读消息并维护长期沉默会话，降低“忘回消息”的社交损耗。

## 这个案例能帮你做什么

- 每 5 分钟扫描未读消息，按紧急/工作/朋友分层处理。
- 对长期未互动联系人自动发送轻量问候，维持联系温度。
- 关键敏感话题先交给人工确认，避免误回。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `whatsapp` | 读取并回复消息 | OpenClaw Built-in |
| 内置 | `memory` | 记录会话历史与已发送内容 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做分类与草稿，不实际发送：

```text
你是我的 OpenClaw 助手。
请帮我做“夜间 WhatsApp 关系维护”的预演版：
1. 扫描当前未读消息并按 urgent/work/friend 分类。
2. 为每条消息生成回复草稿，但先不要发送。
3. 对 7 天以上未互动联系人给出一条 check-in 草稿。
4. 标记需要人工确认的敏感话题。
```

## 稳定自动版（可长期运行）

### 1) 消息分类规则

```javascript
const categories = {
  urgent: { response: "I'll have my human reply ASAP", maxAge: 0 },
  work: { response: "Acknowledged, will follow up", maxAge: 2 },
  friend: { response: "Hey! How have you been?", maxAge: 7 }
};
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Night WhatsApp Revival”。
请使用内置 Skills：whatsapp、memory。

每 5 分钟执行：
1. 扫描 WhatsApp Web 未读消息。
2. 按发送者类型和紧急程度分类。
3. 工作消息：先发确认与预计跟进时间。
4. 朋友消息：超过 7 天未互动时发送轻量问候。
5. 所有已发送内容写入 memory/。
6. 家庭相关消息默认不自动回复，需人工批准。

安全规则：
- No financial transactions
- No personal/confidential info
- Flag sensitive topics for human review
```

## 成功标准

- [ ] Response time <1 hour for work
- [ ] No friendship stale >14 days
- [ ] Zero inappropriate auto-replies

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/14-night-whatsapp-revival.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/14-night-whatsapp-revival.md)

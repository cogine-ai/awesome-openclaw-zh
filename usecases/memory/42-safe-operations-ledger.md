# 安全操作台账

> 先定义“哪些动作可自动执行、哪些必须审批”，再放权给代理。

## 这个案例能帮你做什么

- 明确自动化边界，减少越权和误操作。
- 对未知请求、模糊请求、不可逆请求统一走审批。
- 让人和代理都能快速对齐“什么能做、什么不能做”。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 维护 `safe_ops.md` 台账文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的安全操作助手。
请先生成一版 safe_ops.md，分三栏：
1) Allowed Without Approval
2) Requires Approval
3) Escalation Rules
并用 5 个操作示例做分类演示。
```

## 稳定自动版（可长期运行）

### 1) 台账模板

```markdown
# Safe Operations

## Allowed Without Approval
- Heartbeat checks
- File organization
- Log rotation
- Memory maintenance

## Requires Approval
- Sending external emails
- Financial transactions
- Code deployment
- Data deletion

## Escalation Rules
1. Unknown request → Ask
2. Ambiguous scope → Ask
3. Irreversible action → Ask
```

### 2) OpenClaw 执行提示词（自动版）

```markdown
## Safe Operations Ledger

Before any autonomous action:
1. Check if operation is in allowed list
2. If yes: proceed with logging
3. If no: request approval
4. Document decision rationale

Update ledger weekly with new permissions earned through demonstrated reliability.
```

## 成功标准

- [ ] 所有自动动作都有类别归属。
- [ ] 无越权执行。
- [ ] 台账每周持续更新。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/42-safe-operations-ledger.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/42-safe-operations-ledger.md)

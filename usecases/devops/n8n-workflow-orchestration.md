# n8n 工作流编排

> 把外部 API 调用统一交给 n8n Webhook，OpenClaw 不直接持有业务密钥。

## 这个案例能帮你做什么

- 凭证集中在 n8n Credential Store，减少 `.env` 泄露风险。
- 流程可视化，可在 n8n UI 里直接审查和调试每一步。
- 稳定子任务走工作流，减少不必要的 LLM 推理开销。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `fetch` 或 `curl` | 调用 n8n Webhook | OpenClaw Built-in / 系统命令 |
| 外部（需安装） | `n8n` | 承载外部系统集成与凭证管理 | [n8n](https://n8n.io/) |
| 外部（可选） | Docker / Docker Compose | 一键拉起 OpenClaw+n8n 栈 | Docker |

## 快速体验版（先感受效果）

先用一个 webhook 跑通“代理不接触密钥”的最小闭环：

```text
你是我的 OpenClaw 助手。
目标：把“发送 Slack 消息”改成 n8n webhook 调用。
要求：
1. 不在 OpenClaw 环境中保存 Slack API Key。
2. 只调用 http://n8n:5678/webhook/my-workflow。
3. 输出最小 JSON payload 与调用命令。
```

## 稳定自动版（可长期运行）

### 1) 预置栈（可选）

```bash
git clone https://github.com/caprihan/openclaw-n8n-stack.git
cd openclaw-n8n-stack
cp .env.template .env
docker-compose up -d
```

### 2) 手动模式下的集成规则（放入 `AGENTS.md`）

```text
## n8n Integration Pattern

When I need to interact with external APIs:

1. NEVER store API keys in my environment or skill files
2. Check if an n8n workflow already exists for this integration
3. If not, create one via n8n API with a webhook trigger
4. Notify the user to add credentials and lock the workflow
5. For all future calls, use the webhook URL with a JSON payload

Workflow naming: openclaw-{service}-{action}
Example: openclaw-slack-send-message

Webhook call format:
curl -X POST http://n8n:5678/webhook/{workflow-name} \
  -H "Content-Type: application/json" \
  -d '{"channel": "#general", "message": "Hello from OpenClaw"}'
```

### 3) 运行规则

- 流程固定后执行“build → test → lock”。
- 变更 API 逻辑时先改 n8n workflow，再由 OpenClaw 调 webhook。
- 只把 webhook URL 暴露给代理，不传递真实密钥。

## 成功标准

- [ ] OpenClaw 侧不再持有第三方 API Key。
- [ ] 每个外部调用都有对应 n8n workflow 可视化记录。
- [ ] 关键 workflow 可锁定，避免被意外改写。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/n8n-workflow-orchestration.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/n8n-workflow-orchestration.md)

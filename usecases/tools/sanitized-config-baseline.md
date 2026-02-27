# 可公开配置基线模板

> 用脱敏后的 `openclaw.json` 建立团队统一基线，兼顾可复制、安全与成本可控。

## 这个案例能帮你做什么

- 快速拉起一套可共享配置，不暴露真实密钥。
- 通过默认模型、上下文裁剪、并发限制控制成本与稳定性。
- 在发布前跑完整安全检查，避免把高风险配置带到生产。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw doctor` | 配置校验与修复建议 | OpenClaw CLI |
| 内置 | `openclaw security audit` | 安全审计 | OpenClaw CLI |
| 外部（系统） | `chmod` / `netstat` / `grep` | 权限、监听、敏感信息检查 | 系统工具 |

## 快速体验版（先跑一轮）

### 1) 原文快速流程

1. 复制 `sanitized-config.json` 到 `~/.openclaw/openclaw.json`。
2. 替换所有 `YOUR_*` 占位符。
3. 执行：

```bash
openclaw doctor --fix
openclaw security audit --deep
```

## 稳定自动版（可长期运行）

### 1) 成本友好模型策略（原文重点）

- 不把高价模型放在 `primary`。
- `primary` 用高性价比模型，强模型放 `fallbacks` 或仅绑定特定 agent。

### 2) 记忆检索与上下文控制（原文示例）

```json
"memorySearch": {
  "sources": ["memory", "sessions"],
  "experimental": { "sessionMemory": true },
  "provider": "openai",
  "model": "text-embedding-3-small"
},
"contextPruning": {
  "mode": "cache-ttl",
  "ttl": "6h",
  "keepLastAssistants": 3
}
```

### 3) 自动压缩写入记忆（原文示例）

```json
"compaction": {
  "mode": "default",
  "memoryFlush": {
    "enabled": true,
    "softThresholdTokens": 40000,
    "prompt": "Distill this session to memory/YYYY-MM-DD.md. Focus on decisions, state changes, lessons, blockers. If nothing worth storing: NO_FLUSH",
    "systemPrompt": "Extract only what is worth remembering. No fluff."
  }
}
```

### 4) 安全基线（原文）

```json
"gateway": {
  "bind": "loopback"
},
"logging": {
  "redactSensitive": "tools"
}
```

```bash
chmod 700 ~/.openclaw
chmod 600 ~/.openclaw/openclaw.json
chmod 700 ~/.openclaw/credentials
netstat -an | grep 18789 | grep LISTEN
```

### 5) 上线前核查（原文）

```bash
openclaw doctor --fix
openclaw security audit --deep
grep -r "sk-" ~/.openclaw/
```

## 成功标准

- [ ] 配置可公开分享但不暴露密钥。
- [ ] 默认运行成本稳定可预测。
- [ ] 网关与权限安全基线检查通过。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/config-example-guide.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/config-example-guide.md)

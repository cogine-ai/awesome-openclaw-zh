# AWS 凭证扫描器

> 扫描本地文件与代码仓库中的 AWS Key 暴露风险，并即时告警。

## 这个案例能帮你做什么

- 发现明文 `AKIA...`、`aws_access_key_id`、`aws_secret_access_key`。
- 检查 `~/.aws/credentials` 等敏感文件权限是否过宽。
- 把高危发现第一时间推送，缩短从暴露到处理的时间。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 扫描文件内容 | OpenClaw Built-in |
| 内置 | `telegram` | 风险告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```javascript
const patterns = [
  /AKIA[0-9A-Z]{16}/,
  /aws_access_key_id/i,
  /aws_secret_access_key/i
];
```

先用上述模式对常用目录做一次人工扫描。

## 稳定自动版（可长期运行）

### 1) 周度扫描提示词（原文）

```text
Weekly scan:
1. Search home directory for AWS patterns
2. Check ~/.aws/credentials permissions
3. Search code repositories for hardcoded keys
4. Identify plaintext storage
5. Immediate alert for any findings

Remediation:
- Move to aws-vault or similar
- Rotate exposed keys
- Update .gitignore
- Enable CloudTrail
```

### 2) 建议补救顺序

1. 立刻停用并轮换暴露密钥
2. 清理仓库与历史记录
3. 引入安全存储（如 `aws-vault`）
4. 打开审计日志（CloudTrail）

## 成功标准

- [ ] 零明文 AWS 凭证暴露。
- [ ] 周扫描持续执行。
- [ ] 所有凭证使用受控存储方式。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/29-aws-credential-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/29-aws-credential-scanner.md)

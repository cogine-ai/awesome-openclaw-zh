# SSH 密钥扫描器

> 定期扫描文件系统，找出暴露的 SSH 私钥与 AWS 凭证。

## 这个案例能帮你做什么

- 自动发现错误位置、错误权限、误入 Git 仓库的私钥文件。
- 同时检查明文 AWS 凭证，提前拦截高风险泄露。
- 输出可执行修复动作（`chmod`、`git rm --cached`、密钥轮换）。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 递归扫描目录 | OpenClaw Built-in |
| 内置 | `git` | 检查是否已被版本控制追踪 | OpenClaw Built-in |
| 内置 | `telegram` | 高风险告警推送 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

### 1) 准备扫描配置（原文）

`config/security-scan.json`：

```json
{
  "scan_paths": ["~/.ssh", "~/Downloads", "~/projects", "~/workspace"],
  "exclusions": ["node_modules", ".git/objects", "*.pub"],
  "patterns": {
    "ssh_key": [
      "BEGIN OPENSSH PRIVATE KEY",
      "BEGIN RSA PRIVATE KEY",
      "BEGIN EC PRIVATE KEY"
    ],
    "aws_key": [
      "AKIA[0-9A-Z]{16}",
      "aws_access_key_id",
      "aws_secret_access_key"
    ]
  }
}
```

### 2) 先做一次手工修复演练

```bash
# 权限修复
chmod 600 ~/.ssh/*

# 若误提交到 git，先从索引移除
git rm --cached deploy_key
echo "deploy_key" >> .gitignore
```

## 稳定自动版（可长期运行）

### 1) 扫描脚本（原文逻辑）

- 递归扫描 `scan_paths`
- 命中私钥后检查：
  - 权限是否 `600`
  - 是否在 `~/.ssh/`
  - 是否处在 Git 仓库并被追踪
- 命中 AWS Key 模式时标记高危

### 2) 调度配置（原文）

```json
{
  "schedule": "0 2 * * 0",
  "task": "security_key_scan",
  "immediate_alert_threshold": "high"
}
```

### 3) OpenClaw 执行提示词（原文流程）

```text
Weekly security scan (Sundays 02:00):
1. Scan all configured paths for SSH private keys
2. Check file permissions (must be 600)
3. Check if keys are in git repositories
4. Check for AWS credentials in plain text
5. Look for keys in non-standard locations
6. Generate security report
7. Send critical alerts immediately
8. Save report to memory/security-scans/YYYY-MM-DD.md
```

## 成功标准

- [ ] SSH 私钥权限 100% 合规（`600`）。
- [ ] Git 仓库内零私钥文件。
- [ ] 明文 AWS 凭证能被及时告警并处理。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/09-ssh-key-scanner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/09-ssh-key-scanner.md)

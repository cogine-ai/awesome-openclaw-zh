# Git 历史清理器

> 发现密钥误提交后，清理历史并配套轮换凭证，避免“删文件但仍可回溯”。

## 这个案例能帮你做什么

- 定位历史提交中的密码、API key、`.env` 泄露痕迹。
- 用 BFG / 重写历史彻底清除敏感内容。
- 配套团队协同动作（通知、强推、凭证轮换），减少二次事故。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `git` | 检测与清理历史 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先做只读排查：

```bash
git log --all --full-history -- .env
git log --all -p | grep -i "password\|secret\|key"
```

## 稳定自动版（可长期运行）

### 1) 清理流程（原文）

```bash
bfg --delete-files .env
bfg --replace-text passwords.txt
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### 2) 执行提示词（原文）

```text
When secrets found in history:
1. Identify all affected commits
2. Notify team of upcoming history rewrite
3. Run BFG Repo-Cleaner
4. Force push to all remotes
5. Rotate exposed credentials
6. Update .gitignore
7. Verify cleanup with git log
```

## 成功标准

- [ ] Git 历史中零敏感信息残留。
- [ ] 暴露凭证全部轮换。
- [ ] `.gitignore` 与提交流程可阻断同类问题复发。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/33-git-history-cleaner.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/33-git-history-cleaner.md)

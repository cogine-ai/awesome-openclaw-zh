# Skill 预检检查器

> 技能安装前做 90 秒预检，先拦截风险，再决定是否安装。

## 这个案例能帮你做什么

- 安装前快速核验作者、安装脚本、可疑命令与权限边界。
- 在容器里先跑一遍，降低本机被污染风险。
- 把预检结果沉淀到 runbook，后续复用决策依据。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 分析包文件与脚本 | OpenClaw Built-in |
| 内置 | `docker` | 隔离安装测试 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```bash
npm view package-name author
jq '.scripts' package.json
grep -r "curl\|wget\|eval" node_modules/
docker run --rm -v $(pwd):/app node:alpine npm install package-name
```

## 稳定自动版（可长期运行）

### 1) 安装前标准流程（原文）

```text
Before installing any skill:
1. Check author reputation on npm/Moltbook
2. Read package.json scripts section
3. Search for network/file access patterns
4. Install in container first
5. Monitor what files it touches
6. Document in runbook
```

### 2) 红旗信号（原文）

- `postinstall` 脚本
- 安装阶段主动外联
- 读取 `~/.ssh`、`~/.env`
- 未知作者、来源不明

## 成功标准

- [ ] 所有技能在安装前都走预检。
- [ ] 主环境零恶意技能安装事件。
- [ ] 预检记录可复盘、可追责。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/34-skill-preflight-checker.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/34-skill-preflight-checker.md)

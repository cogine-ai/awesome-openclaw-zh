# 夜间 Shell 别名构建器

> 睡觉时自动分析高频命令，早上直接用更短 alias。

## 这个案例能帮你做什么

- 自动发现你常用但很长的命令，减少重复输入。
- 用低风险方式把 alias 写入 shell 配置，第二天即可生效。
- 把“命令优化”变成每晚可重复执行的日常流程。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `shell` | 写入 `~/.bashrc` / `~/.zshrc` | OpenClaw Built-in |
| 内置 | `filesystem` | 读取 shell 历史 | OpenClaw Built-in |
| 内置 | `git` | 提交 alias 变更 | OpenClaw Built-in |

## 快速体验版（先感受效果）

先不改任何配置文件，只输出候选建议：

```text
你是我的 OpenClaw 助手。
请帮我做“夜间 Shell 别名构建器”的预演版：
1. 分析我最近命令历史里高频且较长的命令（频次>=5）。
2. 给出 3 个候选 alias（每个 alias 2-4 个字符）。
3. 不要写入任何 rc 文件，只输出建议。
4. 对每个建议给出：原命令、alias 名称、避免冲突的检查点。
```

## 稳定自动版（可长期运行）

### 1) 本机脚本：`~/.openclaw/scripts/analyze-history.js`

```javascript
const fs = require('fs');

function analyzeHistory(historyFile) {
  const lines = fs.readFileSync(historyFile, 'utf8').split('\n');

  const counts = {};
  lines.forEach((cmd) => {
    const base = cmd.split(' ').slice(0, 3).join(' ');
    counts[base] = (counts[base] || 0) + 1;
  });

  return Object.entries(counts)
    .filter(([cmd, count]) => count >= 5 && cmd.length > 20)
    .map(([cmd, count]) => ({ cmd, count }));
}

function generateAlias(cmd) {
  const words = cmd.split(' ');
  if (words[0] === 'docker-compose') {
    return `dc${words[1]?.[0]}${words[2]?.[0] || ''}`;
  }
  if (words[0] === 'git') {
    return `g${words[1]?.slice(0, 2)}`;
  }
  return words.map((w) => w[0]).join('').slice(0, 4);
}

const historyFile = process.argv[2] || `${process.env.HOME}/.zsh_history`;
const candidates = analyzeHistory(historyFile)
  .slice(0, 10)
  .map((x) => ({ ...x, alias: generateAlias(x.cmd) }));

console.log(JSON.stringify(candidates, null, 2));
```

### 2) 本机脚本：`~/.openclaw/scripts/add-alias.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

RC_FILE="${1:-$HOME/.zshrc}"
ALIAS_NAME="${2:-}"
ALIAS_CMD="${3:-}"

if [ -z "$ALIAS_NAME" ] || [ -z "$ALIAS_CMD" ]; then
  echo "Usage: $0 <rc_file> <alias_name> <alias_command>"
  exit 1
fi

if grep -q "alias $ALIAS_NAME=" "$RC_FILE"; then
  echo "SKIP: alias already exists -> $ALIAS_NAME"
  exit 0
fi

if [[ "$ALIAS_CMD" =~ (^|[[:space:]])(rm|dd)([[:space:]]|$) ]]; then
  echo "SKIP: dangerous command -> $ALIAS_CMD"
  exit 0
fi

{
  echo ""
  echo "# Added by Night Shell Alias Builder"
  echo "alias $ALIAS_NAME='$ALIAS_CMD'"
} >> "$RC_FILE"

echo "ADDED: $ALIAS_NAME => $ALIAS_CMD"
```

### 3) 一次性准备命令

```bash
mkdir -p ~/.openclaw/scripts
# 把上面两个脚本分别保存为：
# ~/.openclaw/scripts/analyze-history.js
# ~/.openclaw/scripts/add-alias.sh
chmod +x ~/.openclaw/scripts/add-alias.sh
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“夜间 Shell 别名构建器”。
请使用内置 Skills：filesystem、shell、git。

在 03:00 夜间任务中按顺序执行：
1. 读取 ~/.zsh_history。
2. 识别最近一周执行 5 次以上、长度 > 20 字符的命令（按前 3 个词聚合）。
3. 过滤掉已有 alias 后，生成 2-4 字符 alias。
4. 检查 alias 是否与已有 alias 或系统命令冲突。
5. 每晚只新增 1 个 alias，执行：
   ~/.openclaw/scripts/add-alias.sh ~/.zshrc <alias_name> <original_command>
6. 执行 git add ~/.zshrc && git commit -m "nightly alias: <alias_name>"。
7. 输出晨报：新增 alias、原命令、最近频次、预计节省时间、回滚方式。

安全规则：
- 不覆盖已有 alias。
- 不为危险命令（rm、dd）创建 alias。
- 写入前必须做冲突检查。
- 每晚最多新增 1 个 alias。
```

### 5) 调度配置

```json
{
  "schedule": "0 3 * * *",
  "task": "alias_builder",
  "steps": [
    "analyze_history",
    "generate_candidates",
    "check_conflicts",
    "add_alias",
    "git_commit",
    "morning_briefing"
  ]
}
```

## 晨报输出参考

```markdown
🌙 Nightly Build Report

New alias added:
  gst = 'git status'

Usage: Replaces "git status" (typed 47x this week)
Savings: ~3 seconds per use × 47 uses = 2.3 min/week

To use: Type `gst` instead of `git status`
To remove: Delete line from ~/.zshrc
```

## 成功标准

- [ ] 1 new alias per week minimum
- [ ] Human uses alias within 48 hours
- [ ] Zero conflicts with existing commands
- [ ] Average command time reduced 20% over month

## 回滚方式

- 打开 `~/.zshrc` 或 `~/.bashrc`，删除新增 alias 行。
- 执行 `source ~/.zshrc`（或重开终端）使回滚生效。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/05-night-shell-alias-builder.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/05-night-shell-alias-builder.md)

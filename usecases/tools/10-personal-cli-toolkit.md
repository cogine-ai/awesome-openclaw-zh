# 个人 CLI 工具包

> 给代理做一套“自己就能调用”的本地命令，减少重复提示词输入。

## 这个案例能帮你做什么

- 把高频动作封装成短命令：状态看板、快速记录、网页抓取、日报回顾。
- 降低上下文切换成本，让代理执行更快更稳定。
- 通过模块化脚本持续扩展，形成你自己的 Agent CLI。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `nodejs` | 构建命令入口与子命令 | OpenClaw Built-in |
| 内置 | `filesystem` | 读写记忆与抓取文件 | OpenClaw Built-in |
| 内置 | `web_fetch` | 抓取目标页面 | OpenClaw Built-in |
| 内置 | `git` | 看提交状态与历史 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

### 1) 创建目录结构（原文）

```text
~/bin/
├── molty
├── molty-status.js
├── molty-remember.js
├── molty-scrape.js
└── molty-recap.js
```

### 2) 安装并测试（原文）

```bash
chmod +x ~/bin/molty*
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
molty status
```

## 稳定自动版（可长期运行）

### 1) 主入口（原文）

```bash
#!/usr/bin/env node

const [,, cmd, ...args] = process.argv;

const commands = {
  status: () => require('./molty-status'),
  remember: (note) => require('./molty-remember')(note.join(' ')),
  scrape: (target) => require('./molty-scrape')(target),
  recap: () => require('./molty-recap')
};

if (commands[cmd]) {
  commands[cmd](args);
} else {
  console.log(`Usage: molty <command>

Commands:
  status              Show dashboard
  remember "text"     Add timestamped note
  scrape @username    Scrape X profile
  recap               Show daily summary
  `);
}
```

### 2) 常用能力（原文）

- `molty status`：汇总 crontab、git、memory、磁盘状态
- `molty remember "..."`：追加时间戳笔记到当日 memory
- `molty scrape @username`：抓取并保存页面结果
- `molty recap`：输出当日记录摘要

### 3) 抓取命令关键调用（原文）

```bash
openclaw web_fetch https://nitter.net/${username}
```

## 成功标准

- [ ] 高频动作都有对应短命令，减少重复输入。
- [ ] 每日记录可快速写入与回看。
- [ ] 新需求可以通过新增 `molty-<name>.js` 平滑扩展。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/10-personal-cli-toolkit.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/10-personal-cli-toolkit.md)

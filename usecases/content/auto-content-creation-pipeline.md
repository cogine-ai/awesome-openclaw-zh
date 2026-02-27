# 自动化内容创作流水线

> 从热点收集到成稿排版再到多平台分发，形成可重复执行的内容生产闭环。

## 这个案例能帮你做什么

- 把“找选题、找资料、写大纲、写正文、排版发布”串成一个统一流程。
- 通过脚本化和定时任务，把内容生产从“想到才做”变成“自动触发”。
- 在保证质量前提下显著缩短单篇内容产出时间。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | `brave-search` | 检索热点与背景资料 | ClawHub |
| 外部 | `rss-reader` | 订阅并抓取 RSS 信息源 | ClawHub |
| 外部 | `github-trending` | 追踪 GitHub 热门项目 | ClawHub |
| 外部 | `content-analyzer` | 质量评分与内容分析 | ClawHub |
| 外部 | `text-summarizer` | 摘要提炼 | ClawHub |
| 外部 | `duplicate-checker` | 去重检查 | ClawHub |

## 快速体验版（先跑一轮）

先做“单篇主题”的最小闭环：

```text
你是我的 OpenClaw 助手。
请帮我做“自动化内容创作流水线”的预演版：
1. 围绕主题“OpenClaw自动化测试实战”搜索资料。
2. 生成 3-5 节文章大纲。
3. 生成一版完整草稿。
4. 输出排版优化建议。
5. 本轮只产出 final.md，不做自动发布。
```

## 稳定自动版（可长期运行）

### 1) 安装必需 Skills

```bash
# 安装信息收集Skills
clawhub install brave-search      # 网页搜索
clawhub install rss-reader        # RSS订阅
clawhub install github-trending   # GitHub热门

# 安装内容处理Skills
clawhub install content-analyzer  # 内容分析
clawhub install text-summarizer   # 文本摘要
clawhub install duplicate-checker # 去重检查
```

### 2) 创作脚本：`~/.openclaw/scripts/content-creation.sh`

```bash
#!/bin/bash

TOPIC=$1
OUTPUT_DIR="$HOME/.openclaw/content"
mkdir -p "$OUTPUT_DIR"

# 1. 搜索相关资料
openclaw skills run brave-search \
  --query "$TOPIC" \
  --max-results 10 \
  --output "$OUTPUT_DIR/research.json"

# 2. 生成大纲
openclaw agent --message "根据以下资料生成文章大纲：
主题：$TOPIC
资料：$(cat $OUTPUT_DIR/research.json)
要求：
- 结构清晰，3-5个章节
- 包含实战案例
- 字数2000-3000字" \
  --output "$OUTPUT_DIR/outline.md"

# 3. 创作内容
openclaw agent --message "根据大纲创作完整文章：
$(cat $OUTPUT_DIR/outline.md)
要求：
- 语言通俗易懂
- 包含代码示例
- 添加配图建议" \
  --output "$OUTPUT_DIR/draft.md"

# 4. 优化排版
openclaw agent --message "优化文章排版：
$(cat $OUTPUT_DIR/draft.md)
要求：
- 添加emoji
- 优化标题层级
- 添加引用和提示框" \
  --output "$OUTPUT_DIR/final.md"
```

### 3) 使用命令

```bash
# 创作一篇文章
bash ~/.openclaw/scripts/content-creation.sh "OpenClaw自动化测试实战"
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“自动化内容创作流水线”。
请使用 Skills：brave-search、rss-reader、github-trending、content-analyzer、text-summarizer、duplicate-checker。

执行流程：
1. 收集热点与资料（搜索 + RSS + GitHub 热门）。
2. 合并并去重信息。
3. 生成 3-5 节大纲。
4. 生成 2000-3000 字草稿。
5. 完成排版优化并输出 final.md。
6. 按需补充配图和多平台发布建议。
```

### 5) 定时任务

```bash
# 添加到crontab
crontab -e

# 每天早上8点执行
0 8 * * * /bin/bash ~/.openclaw/scripts/daily-digest.sh
```

## 成功标准

- [ ] 每天自动收集 50+ 条信息
- [ ] 过滤后保留 15-20 条高质量内容
- [ ] 节省时间约 2 小时/天
- [ ] 信息质量提升约 60%

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

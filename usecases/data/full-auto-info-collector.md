# 全自动信息收集系统

> 每天自动收集多源信息、去重评分并生成日报。

## 这个案例能帮你做什么

- 把 RSS、GitHub 热门、关键词搜索统一采集。
- 自动去重、评分和分类，只保留高质量信息。
- 每天固定生成日报并推送到飞书。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | `brave-search` | 网页搜索 | ClawHub |
| 外部 | `rss-reader` | RSS 抓取 | ClawHub |
| 外部 | `github-trending` | GitHub 热门采集 | ClawHub |
| 外部 | `content-analyzer` | 内容评分分析 | ClawHub |
| 外部 | `text-summarizer` | 摘要生成 | ClawHub |
| 外部 | `duplicate-checker` | 去重检查 | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“全自动信息收集系统”的预演版：
1. 从2个RSS源抓取最新内容。
2. 抓取今日GitHub热门项目。
3. 合并并去重。
4. 输出10条高质量候选和评分。
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

### 2) 信息源配置 `~/.openclaw/info-sources.json`

```json
{
  "sources": {
    "rss": [
      {
        "name": "阮一峰的网络日志",
        "url": "https://www.ruanyifeng.com/blog/atom.xml",
        "category": "技术"
      },
      {
        "name": "少数派",
        "url": "https://sspai.com/feed",
        "category": "效率"
      }
    ],
    "github": {
      "trending": {
        "language": "python",
        "since": "daily"
      },
      "repos": [
        "openclaw/openclaw",
        "microsoft/vscode"
      ]
    },
    "keywords": [
      "OpenClaw",
      "AI工具",
      "效率提升",
      "自动化"
    ]
  },
  "filter": {
    "keywords": ["AI", "自动化", "效率", "工具"],
    "exclude": ["广告", "营销", "推广"],
    "quality_threshold": 75,
    "max_items": 20
  },
  "schedule": {
    "time": "08:00",
    "timezone": "Asia/Shanghai"
  }
}
```

### 3) 自动化脚本 `~/.openclaw/scripts/daily-digest.sh`

```bash
#!/bin/bash

DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="$HOME/.openclaw/digests"
mkdir -p "$OUTPUT_DIR"

openclaw agent --message "请使用 rss-reader skill 收集 ~/.openclaw/info-sources.json 中配置的RSS源，保存到 $OUTPUT_DIR/rss-$DATE.json"
openclaw agent --message "请收集GitHub今日Python热门项目，保存到 $OUTPUT_DIR/github-$DATE.json"
openclaw agent --message "请搜索'OpenClaw AI工具'相关信息，最多10条结果，保存到 $OUTPUT_DIR/search-$DATE.json"
openclaw agent --message "请合并 $OUTPUT_DIR/*-$DATE.json 中的所有信息并去重，保存到 $OUTPUT_DIR/merged-$DATE.json"
openclaw agent --message "请分析 $OUTPUT_DIR/merged-$DATE.json 中的内容并评分，保存到 $OUTPUT_DIR/analyzed-$DATE.json"
openclaw agent --message "请根据以下信息生成今日日报，按技术、产品、行业分类，每条信息包含标题、摘要、链接和推荐理由：
$(cat $OUTPUT_DIR/analyzed-$DATE.json)" --output "$OUTPUT_DIR/digest-$DATE.md"
openclaw channels send feishu --message "$(cat $OUTPUT_DIR/digest-$DATE.md)" --title "📰 每日资讯 $DATE"
```

### 4) 定时任务

```bash
# 添加到crontab
crontab -e

# 每天早上8点执行
0 8 * * * /bin/bash ~/.openclaw/scripts/daily-digest.sh
```

## 成功标准

- [ ] 每天自动收集 50+ 条信息
- [ ] 智能过滤后保留 15-20 条高质量内容
- [ ] 节省时间：每天约 2 小时
- [ ] 信息质量提升约 60%

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

# 每日 AI 行业日报推送

> 每天定时生成并推送一份 AI 行业日报，减少手工整理成本。

## 这个案例能帮你做什么

- 固定时间自动产出日报，不用每天手动找新闻。
- 支持直接发到飞书、Telegram、企微、钉钉等渠道。
- 失败会写日志，便于排查任务稳定性。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw message send` | 发送日报消息 | OpenClaw CLI |
| 外部（系统） | `bash` + `crontab` | 定时调度与日志记录 | 系统工具 |
| 渠道 | `feishu` / `telegram` / `wecom` / `dingtalk` | 接收日报 | 消息渠道 |

## 快速体验版（先跑一轮）

把原文脚本保存为 `~/daily-report.sh`，然后手动执行一次：

```bash
bash ~/daily-report.sh
```

## 稳定自动版（可长期运行）

### 1) 原文脚本

```bash
#!/bin/bash
# OpenClaw 每日AI日报自动推送脚本
# 使用方法：添加到crontab: 0 9 * * * ~/daily-report.sh

# 配置
OPENCLAW_BIN="openclaw"
CHANNEL="feishu"  # 或 telegram, wecom, dingtalk
LOG_FILE="$HOME/.openclaw/logs/daily-report.log"

# 日志函数
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 开始执行
log "开始生成每日AI日报"

# 生成日报内容
PROMPT="请生成今天的AI行业日报，包括：
1. 最新的AI技术动态（3-5条）
2. 重要的产品发布或更新
3. 行业趋势分析
4. 值得关注的研究论文

请用简洁的格式呈现，每条新闻包含标题、简介和链接。"

# 发送消息
if $OPENCLAW_BIN message send --channel "$CHANNEL" --message "$PROMPT"; then
    log "✅ 日报推送成功"
else
    log "❌ 日报推送失败"
    exit 1
fi

log "完成"
```

### 2) 定时任务（原文）

```bash
0 9 * * * ~/daily-report.sh
```

## 成功标准

- [ ] 每天固定时段收到日报。
- [ ] 失败会记录到日志并可定位原因。
- [ ] 更换渠道后不影响日报生成逻辑。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [examples/automation/daily-report.sh](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/examples/automation/daily-report.sh)

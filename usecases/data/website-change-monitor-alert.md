# 网站更新监控通知

> 监控目标网站关键内容变化，有更新就即时推送提醒。

## 这个案例能帮你做什么

- 自动比较最新页面内容和上次缓存，快速发现更新。
- 首次运行自动初始化缓存，后续只在变化时提醒。
- 可用于官网新闻、公告页、文档更新页监控。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `openclaw message send` | 发送通知消息 | OpenClaw Built-in |
| 外部 | `curl` | 拉取目标页面内容 | Shell 工具 |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“网站更新监控通知”的预演版：
1. 监控 https://www.anthropic.com/news 的首条 h2 内容。
2. 若无缓存则初始化缓存。
3. 若内容变化则生成通知消息。
4. 本轮只输出消息内容，不实际发送。
```

## 稳定自动版（可长期运行）

### 1) 监控脚本

```bash
#!/bin/bash
# OpenClaw 网站监控脚本
# 监控指定网站的内容变化，发现更新时通知

# 配置
WEBSITE_URL="https://www.anthropic.com/news"
CACHE_FILE="$HOME/.openclaw/cache/website-monitor.txt"
OPENCLAW_BIN="openclaw"
CHANNEL="telegram"

# 创建缓存目录
mkdir -p "$(dirname "$CACHE_FILE")"

# 获取网站内容
CURRENT_CONTENT=$(curl -s "$WEBSITE_URL" | grep -oP '<h2.*?</h2>' | head -n 1)

# 检查是否有缓存
if [ -f "$CACHE_FILE" ]; then
    CACHED_CONTENT=$(cat "$CACHE_FILE")

    # 比较内容
    if [ "$CURRENT_CONTENT" != "$CACHED_CONTENT" ]; then
        echo "发现更新！"

        # 提取标题
        TITLE=$(echo "$CURRENT_CONTENT" | sed 's/<[^>]*>//g')

        # 发送通知
        MESSAGE="🔔 网站更新通知

网站：$WEBSITE_URL
最新内容：$TITLE

请访问网站查看详情。"

        $OPENCLAW_BIN message send --channel "$CHANNEL" --message "$MESSAGE"

        # 更新缓存
        echo "$CURRENT_CONTENT" > "$CACHE_FILE"
    else
        echo "无更新"
    fi
else
    # 首次运行，创建缓存
    echo "$CURRENT_CONTENT" > "$CACHE_FILE"
    echo "初始化缓存"
fi
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“网站更新监控通知”。

执行规则：
1. 拉取目标网站首条 h2。
2. 与缓存值比较。
3. 有变化则发送 Telegram 通知并更新缓存。
4. 无变化则仅记录“无更新”。
5. 首次运行时先初始化缓存，不发告警。
```

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [examples/automation/website-monitor.sh](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/examples/automation/website-monitor.sh)

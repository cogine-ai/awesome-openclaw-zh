# 配置自动备份与保留

> 定时打包 OpenClaw 配置并清理过期备份，降低误操作与故障损失。

## 这个案例能帮你做什么

- 自动备份 `~/.openclaw` 目录，避免配置丢失。
- 默认排除日志和缓存，减小备份体积。
- 自动删除超出保留天数的历史备份。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（系统） | `bash` / `tar` / `find` | 备份、压缩、清理 | 系统工具 |
| 内置（可选） | `cron` | 定时执行脚本 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

把原文脚本保存为 `backup-config.sh` 后执行：

```bash
bash backup-config.sh
```

## 稳定自动版（可长期运行）

### 1) 备份脚本（原文）

```bash
#!/bin/bash
OPENCLAW_DIR="$HOME/.openclaw"
BACKUP_DIR="$HOME/openclaw-backups"
RETENTION_DAYS=30

mkdir -p "$BACKUP_DIR"
BACKUP_FILE="$BACKUP_DIR/openclaw-$(date +%Y%m%d-%H%M%S).tar.gz"

echo "开始备份OpenClaw配置..."
tar -czf "$BACKUP_FILE" \
    --exclude="$OPENCLAW_DIR/logs" \
    --exclude="$OPENCLAW_DIR/cache" \
    "$OPENCLAW_DIR"

if [ $? -eq 0 ]; then
    echo "✅ 备份成功：$BACKUP_FILE"
    SIZE=$(du -h "$BACKUP_FILE" | cut -f1)
    echo "备份大小：$SIZE"
    echo "清理超过 $RETENTION_DAYS 天的旧备份..."
    find "$BACKUP_DIR" -name "openclaw-*.tar.gz" -mtime +$RETENTION_DAYS -delete
    echo "当前备份列表："
    ls -lh "$BACKUP_DIR"/openclaw-*.tar.gz
else
    echo "❌ 备份失败"
    exit 1
fi
```

### 2) 定时执行（可选）

```bash
# 每天凌晨 2 点
0 2 * * * /bin/bash /path/to/backup-config.sh
```

## 成功标准

- [ ] 每日备份产物可见且可读。
- [ ] 超期备份会自动清理。
- [ ] 恢复演练可以成功还原配置。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [examples/automation/backup-config.sh](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/examples/automation/backup-config.sh)

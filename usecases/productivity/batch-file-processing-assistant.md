# 批量文件处理助手

> 对目录中的文件逐个调用 OpenClaw 处理，并输出成功/失败统计。

## 这个案例能帮你做什么

- 把大量文件摘要、初筛、提取这类重复工作自动化。
- 一次运行处理整目录，避免手工逐条发送提示词。
- 自动产出处理统计，便于定位失败项重跑。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | OpenClaw 消息调用能力 | 逐文件执行处理提示词 | OpenClaw Built-in |
| 内置 | Shell + 文件系统 | 目录遍历与结果写入 | 系统命令 |

## 快速体验版（先跑一轮）

```text
你是我的文件处理助手。
请先对 ~/Documents/ToProcess 中前 3 个文件做摘要，
把输出写到 ~/Documents/Processed/，并返回成功/失败统计。
```

## 稳定自动版（可长期运行）

### 批处理脚本（源案例）

```bash
#!/bin/bash
# OpenClaw 批量文件处理脚本
# 批量处理指定目录下的文件

# 配置
SOURCE_DIR="$HOME/Documents/ToProcess"
OUTPUT_DIR="$HOME/Documents/Processed"
OPENCLAW_BIN="openclaw"

# 创建输出目录
mkdir -p "$OUTPUT_DIR"

# 统计
TOTAL=0
SUCCESS=0
FAILED=0

echo "开始批量处理文件..."
echo "源目录：$SOURCE_DIR"
echo "输出目录：$OUTPUT_DIR"
echo "---"

# 遍历文件
for file in "$SOURCE_DIR"/*; do
    if [ -f "$file" ]; then
        TOTAL=$((TOTAL + 1))
        filename=$(basename "$file")

        echo "处理文件 $TOTAL: $filename"

        # 使用OpenClaw处理文件
        # 示例：提取文件摘要
        PROMPT="请分析这个文件并生成摘要：$file"

        if $OPENCLAW_BIN message send --message "$PROMPT" > "$OUTPUT_DIR/${filename}.summary.txt"; then
            SUCCESS=$((SUCCESS + 1))
            echo "✅ 成功"
        else
            FAILED=$((FAILED + 1))
            echo "❌ 失败"
        fi
    fi
done

# 输出统计
echo "---"
echo "处理完成！"
echo "总计：$TOTAL 个文件"
echo "成功：$SUCCESS 个"
echo "失败：$FAILED 个"
```

## 成功标准

- [ ] 批量任务可稳定跑完并生成统计。
- [ ] 每个输入文件都产生可追溯输出文件。
- [ ] 失败项可单独定位并重跑。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [examples/automation/batch-process-files.sh](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/examples/automation/batch-process-files.sh)

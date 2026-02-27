# Todoist 任务管理器（Agent 可视化）

> 把代理执行计划和进度日志同步到 Todoist，实现任务过程透明化。

## 这个案例能帮你做什么

- 将复杂任务拆解状态可视化到 `In Progress/Waiting/Done`。
- 让计划、子步骤日志、完成状态都沉淀在任务系统中。
- 通过心跳巡检发现停滞任务并提醒处理。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需配置） | Todoist REST API | 创建/更新任务与评论 | [developer.todoist.com](https://developer.todoist.com/rest/v2/) |
| 内置 | Shell + 文件系统 | 运行本地脚本封装 API | OpenClaw Built-in |
| 内置 | `heartbeat` | 定期巡检 stalled 任务 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 Todoist 可视化助手。
请先模拟一次复杂任务执行：
1) 创建 In Progress 任务并写入 PLAN
2) 增加 3 条进度评论
3) 任务完成后移动 Done
本轮不调用真实 API。
```

## 稳定自动版（可长期运行）

### 1) `scripts/todoist_api.sh`

```bash
#!/bin/bash
# Usage: ./todoist_api.sh <endpoint> <method> [data_json]
ENDPOINT=$1
METHOD=$2
DATA=$3
TOKEN="YOUR_TODOIST_API_TOKEN"

if [ -z "$DATA" ]; then
  curl -s -X "$METHOD" "https://api.todoist.com/rest/v2/$ENDPOINT" \
    -H "Authorization: Bearer $TOKEN"
else
  curl -s -X "$METHOD" "https://api.todoist.com/rest/v2/$ENDPOINT" \
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-Type: application/json" \
    -d "$DATA"
fi
```

### 2) `scripts/sync_task.sh`

```bash
#!/bin/bash
# Usage: ./sync_task.sh <task_content> <status> [task_id] [description] [labels_json_array]
CONTENT=$1
STATUS=$2
TASK_ID=$3
DESCRIPTION=$4
LABELS=$5
PROJECT_ID="YOUR_PROJECT_ID"

case $STATUS in
  "In Progress") SECTION_ID="SECTION_ID_PROGRESS" ;;
  "Waiting")     SECTION_ID="SECTION_ID_WAITING" ;;
  "Done")        SECTION_ID="SECTION_ID_DONE" ;;
  *)             SECTION_ID="" ;;
esac

PAYLOAD="{\"content\": \"$CONTENT\""
[ -n "$SECTION_ID" ] && PAYLOAD="$PAYLOAD, \"section_id\": \"$SECTION_ID\""
[ -n "$PROJECT_ID" ] && [ -z "$TASK_ID" ] && PAYLOAD="$PAYLOAD, \"project_id\": \"$PROJECT_ID\""
if [ -n "$DESCRIPTION" ]; then
  ESC_DESC=$(echo "$DESCRIPTION" | sed ':a;N;$!ba;s/\n/\\n/g' | sed 's/"/\\"/g')
  PAYLOAD="$PAYLOAD, \"description\": \"$ESC_DESC\""
fi
[ -n "$LABELS" ] && PAYLOAD="$PAYLOAD, \"labels\": $LABELS"
PAYLOAD="$PAYLOAD}"

if [ -n "$TASK_ID" ]; then
  ./scripts/todoist_api.sh "tasks/$TASK_ID" POST "$PAYLOAD"
else
  ./scripts/todoist_api.sh "tasks" POST "$PAYLOAD"
fi
```

### 3) `scripts/add_comment.sh`

```bash
#!/bin/bash
# Usage: ./add_comment.sh <task_id> <comment_text>
TASK_ID=$1
TEXT=$2
ESC_TEXT=$(echo "$TEXT" | sed ':a;N;$!ba;s/\n/\\n/g' | sed 's/"/\\"/g')
PAYLOAD="{\"task_id\": \"$TASK_ID\", \"content\": \"$ESC_TEXT\"}"
./scripts/todoist_api.sh "comments" POST "$PAYLOAD"
```

## 成功标准

- [ ] 复杂任务过程在 Todoist 中可见。
- [ ] 子步骤评论持续更新。
- [ ] 停滞任务能被巡检发现并提醒。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/todoist-task-manager.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/todoist-task-manager.md)

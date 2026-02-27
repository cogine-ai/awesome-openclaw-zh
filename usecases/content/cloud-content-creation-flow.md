# 云端内容创作工作流

> 在云端自动完成“资料检索→PPT 生成→素材清理”，把内容生产和存储管理一起自动化。

## 这个案例能帮你做什么

- 在云端直接生成完整 PPT（含资料检索、配图、排版、导出）。
- 自动识别可删除素材并生成清理建议，避免输出目录膨胀。
- 云端处理内容生产，本地设备几乎无负担。

## 你需要的 Skills（按类型）

| 类型 | Skill / 能力 | 用途 | 来源 |
|---|---|---|---|
| 外部 | `find-skills` | 发现并安装合适技能 | ClawHub |
| 外部 | `proactive-agent` | 持续执行自动化流程 | ClawHub |
| 外部 | `banana-ai` | 支持云端内容创作能力 | ClawHub |
| 内置 | `schedule/cron` | 固定时间触发任务 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先做一次“生成 + 清理建议”演示：

```text
你是我的 OpenClaw 助手。
请帮我做“云端内容创作工作流”的预演版：
1. 生成一份“OpenClaw 原理介绍”PPT。
2. 输出素材目录和文件大小统计。
3. 对比 24 小时前备份，生成可删除清单。
4. 本轮只给清理建议，不执行删除。
```

## 稳定自动版（可长期运行）

### 1) 场景命令示例（PPT 生成）

```bash
你：通过百度搜索和百度学术，生成一份介绍OpenClaw原理的PPT
```

### 2) 场景命令示例（自动清理）

```bash
你：每天早上9点，检查我的输出目录：
- 对比24小时前的备份
- 识别可删除的多余文件
- 生成清理清单
- 在日报中确认
- 我确认后才能删除
```

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“云端内容创作工作流”。

目标流程：
1. 使用搜索与学术检索生成内容素材。
2. 自动生成 PPT（大纲、正文、配图、排版、导出）。
3. 将素材保存到输出目录。
4. 每天 09:00 生成清理建议（仅建议，不自动删除）。
5. 只有在我回复“确认”后才执行删除。
```

### 4) 配置脚本片段（来自云端完整配置）

```bash
# 1. 安装Skills双幻神
npx clawhub@latest install find-skills
npx clawhub@latest install proactive-agent

# 2. 配置云端内容创作
clawhub install banana-ai
openclaw config set content.auto-cleanup true

openclaw schedule add "file-cleanup" \
  --time "09:00" \
  --prompt "检查输出目录，生成清理建议"
```

## 使用建议

- 清理策略默认“建议优先”，确认后再删除，降低误删风险。
- 输出目录建议按项目分层保存，便于后续回溯复用。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

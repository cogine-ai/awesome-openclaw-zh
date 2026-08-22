# 零依赖认知记忆引擎（Mnemosyne）

> 用"纯本地 Markdown + 认知心理学检索"给 OpenClaw 助手装上永不丢失的持久记忆，零 API 成本、数据不出境。

## 这个案例能帮你做什么

- 解决会话间上下文断层——助手重启后还记得你是谁、聊过什么、喜欢什么。
- 把记忆按「短期 / 工作台 / 中期 / 长期」四层自动沉淀，重要的事自动记住、旧事自然淡出但不消失。
- 零 token 成本、零向量数据库、零 embedding 模型，普通电脑即可运行，数据 100% 留在本机。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | [`mnemosyne`](https://github.com/ElonAug7/Mnemosyne-agentmemory-engine-openclaw-hermes) | 四层记忆引擎 + 复合线索检索 + 用户画像自动提炼 | [GitHub](https://github.com/ElonAug7/Mnemosyne-agentmemory-engine-openclaw-hermes) |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我接入 Mnemosyne 记忆引擎：
1. git clone https://github.com/ElonAug7/Mnemosyne-agentmemory-engine-openclaw-hermes
2. cd Mnemosyne-agentmemory-engine-openclaw-hermes/Mnemosyne-v6.4 && bash install.sh
3. 打开 http://127.0.0.1:8765 查看记忆面板
4. 本轮只做安装和验证，不要改动我现有的 SOUL.md / AGENTS.md 之外的任何文件
```

## 稳定自动版（可长期运行）

### 1) 配置或脚本片段

```bash
# 安装（自动注入记忆协议到 SOUL.md / AGENTS.md）
cd Mnemosyne-v6.4 && bash install.sh

# 手动查询记忆 / 查看画像
node engine.js search --query "上次聊到的项目" --mode keyword
node engine.js profile
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，已接入 Mnemosyne 记忆引擎。

每条回复前，请先读取 memory/short/working/last-recall.json；
涉及历史/决策/偏好时，运行 node tools/memory-engine/engine.js recall --query "关键词"，
并在回复中引用记忆来源。

执行步骤：
1. 收到消息后自动记录（引擎 hook 已接管）
2. 高价值消息自动触发 recall
3. 每 30 分钟自动 consolidate 生成中期摘要
4. 每晚 22:30 自动提炼长期记忆为 proposals，待我确认
```

### 3) 调度配置（可选）

```json
{
  "schedule": "每 30 分钟 consolidate 一次；每晚 22:30 nightly distill"
}
```

### 4) 输出模板

```markdown
# 记忆状态
- 今天新记录：N 条
- 当前画像：技术栈 / 偏好 / 风格
- 待确认的长期记忆 proposals：N 条
```

## 实测数据

在 Memory-Native Evaluation 基准（80 查询、11 个系统）上，检索质量 nDCG@10 = 0.238，是上一版的 5.2 倍，反超裸 BM25 和所有嵌入系统——而它完全不需要任何 embedding 模型。搜索延迟约 7ms。

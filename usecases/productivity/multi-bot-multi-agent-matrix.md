# 多机器人多 Agent 矩阵

> 多 Gateway + 多机器人并行部署，不同角色直接私聊对应机器人。

## 这个案例能帮你做什么

- 避免单机器人里频繁切模型/切上下文。
- 每个机器人绑定一个独立 Gateway，互不干扰。
- 复杂任务可按角色拆分流转（主助理/内容/技术/资讯）。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | 多 Gateway 运行能力 | 独立代理实例 | OpenClaw Built-in |
| 外部（需配置） | 飞书机器人应用 | 多入口对话 | 飞书开放平台 |
| 内置 | 角色配置（SOUL/USER） | 定义每个 Agent 职责 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的部署助手。
请先给出 2 机器人版本（主助理+内容助手）的最小落地方案：
1) 端口分配
2) 角色职责
3) 私聊使用方式
本轮不启动全量 4 机器人。
```

## 稳定自动版（可长期运行）

### 1) 架构要点（源案例）

- 创建 4 个飞书机器人应用。
- 启动 4 个独立 Gateway（示例端口：`18789-18792`）。
- 每个 Gateway 对应一个 Agent 和模型配置。

### 2) 启动与检查

```bash
./start-all-gateways.sh
./check-gateways.sh
```

### 3) 使用方式（源案例）

- 私聊“主助理”处理复杂任务。
- 私聊“内容创作助手”处理写作任务。
- 私聊“技术开发助手”处理代码问题。
- 私聊“AI资讯助手”获取行业动态。

## 成功标准

- [ ] 各机器人职责稳定，不串上下文。
- [ ] 某个 Gateway 故障不影响其他机器人。
- [ ] 角色切换不再依赖手动命令。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/15-solo-entrepreneur-cases.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/15-solo-entrepreneur-cases.md)

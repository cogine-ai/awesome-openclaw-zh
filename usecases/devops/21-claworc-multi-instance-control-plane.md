# Claworc 多实例控制台

> 用一个 Web 控制台集中管理多个 OpenClaw 实例，把实例隔离、权限控制和运维入口统一起来。

## 这个案例能帮你做什么

- 给团队里不同人、不同任务、不同模型准备独立 OpenClaw 实例。
- 通过单一入口统一管理浏览器、终端、文件、日志和 API key。
- 在不直接暴露每个 OpenClaw 实例的前提下，做更稳的权限控制和运维监控。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | [`claworc`](https://github.com/gluk-w/claworc) | 多实例控制平面与管理界面 | gluk-w |
| 外部（系统） | Docker Compose 或 Helm | 部署 Claworc 控制台 | Docker / Kubernetes |
| 内置 | OpenClaw Gateway | 作为被管理的 Agent 实例运行入口 | OpenClaw |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 平台架构师。
请先帮我设计一个最小可用的 Claworc 方案：
1. 一个实例给日常助理
2. 一个实例给数据分析
3. 一个实例给 IT 支持
4. 说明每个实例为什么要独立，以及控制台应该统一看哪些信息
本轮先不要进入生产部署细节。
```

## 稳定自动版（可长期运行）

### 1) Docker Compose 方式启动

```bash
git clone https://github.com/gluk-w/claworc.git
cd claworc
mkdir -p ~/.claworc/data/configs
CLAWORC_DATA_DIR=~/.claworc/data docker compose up -d
```

启动后，Dashboard 默认在：

```text
http://localhost:8000
```

### 2) 常用运维命令

```bash
docker compose logs -f
docker compose down
docker compose up -d
docker compose down -v
```

### 3) 如果你要用安装脚本

```bash
curl -fsSL https://raw.githubusercontent.com/gluk-w/claworc/main/install.sh | bash
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 基础设施管理员。
请按 Claworc 的方式管理多个实例：
1. 给每个团队成员或任务类型分配独立实例
2. 每个实例都要有独立浏览器、终端和持久化存储
3. 控制台统一展示实例状态、日志、连接健康和访问权限
4. 如果我要新增实例，先给出用途、模型、权限和是否需要单独 API key
```

## 成功标准

- [ ] 可以从一个控制台看到多个 OpenClaw 实例。
- [ ] 每个实例都具备独立浏览器、终端和持久化存储。
- [ ] 默认通过控制平面代理访问，而不是把每个 Agent 端口直接暴露出去。

## 风险与边界

- 这更适合“团队多实例管理”而不是单机个人使用；如果你只有一个实例，复杂度可能过高。
- Claworc 强调 SSH 隧道、代理和角色控制，部署时需要同时考虑控制平面和实例侧的网络边界。
- 如果你希望不同实例共享同一套 API key 或模型策略，需要自己设计更细的权限边界。

## 使用建议

- 先用 2-3 个实例做试点，不要一上来就把所有角色都塞进去。
- 最适合放进去的实例通常是：日常助理、数据分析、IT/运维支持。
- 如果你已经在用多 Agent、多 Gateway，这篇可以看作进一步升级成“多实例控制平面”。

## 引用来源

- 来源仓库： [gluk-w/claworc](https://github.com/gluk-w/claworc)
- 原始条目：
  - [README.md](https://github.com/gluk-w/claworc/blob/main/README.md)
  - [docs/install.md](https://github.com/gluk-w/claworc/blob/main/docs/install.md)
  - [digitalknk/openclaw-runbook/showcases/claworc.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/claworc.md)

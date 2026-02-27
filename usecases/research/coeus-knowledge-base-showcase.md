# 自托管知识库助手（Coeus）

> 在本地把笔记、灵感、工作记录沉淀成可语义搜索的知识库。

## 这个案例能帮你做什么

- 把日常输入（`note:`、`idea:`、`standup:`）统一入库，不再散落在聊天和文件里。
- 先走零成本的全文检索，再在结果不足时自动补语义检索，速度和召回率都兼顾。
- 给每天/每周摘要提供缓存短摘要，减少上下文 token 消耗。

## 你需要的 Skills（按类型）

| 类型 | Skill / 依赖 | 用途 | 来源 |
|---|---|---|---|
| 内置 | 文件系统读写 | 保存 `schema.sql`、`state.json`、导出文件 | OpenClaw Built-in |
| 外部（需安装） | Python 3.11+ | 运行 `coeus.py` | Python |
| 外部（需安装） | SQLite 3.45.1+ + `vec0` 扩展 | FTS + 向量检索 | [asg017/sqlite-vec](https://github.com/asg017/sqlite-vec) |
| 外部（需安装） | `torch`、`transformers`、`sentence-transformers` | 本地 embedding 与摘要处理 | PyPI |

## 快速体验版（先跑一轮）

先确认本机向量扩展可用：

```bash
sqlite3 :memory: ".load /usr/local/lib/sqlite3/vec0.so" "SELECT 'vec0 OK';"
```

然后最小化初始化并写入一条测试记录：

```bash
mkdir -p ~/coeus && cd ~/coeus
python3 -m venv venv
source venv/bin/activate
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers sentence-transformers --no-deps

# 按原文准备 coeus.py 与 schema.sql 后执行
python3 coeus.py capture "note: Testing Coeus setup"
python3 coeus.py stats
```

## 稳定自动版（可长期运行）

### 1) 初始化目录与数据库

```bash
mkdir -p ~/coeus && cd ~/coeus

# 把原文里的完整 schema.sql 保存到当前目录
# 然后初始化数据库
sqlite3 coeus.db << 'INIT'
.load /usr/local/lib/sqlite3/vec0.so
.read schema.sql
INIT

echo '{"capture_mode": false, "current_session_id": null, "last_capture_block_id": null}' > state.json
mkdir -p exports
```

### 2) 约定采集触发词（与原文一致）

- 显式前缀：`note:`、`capture:`、`log:`、`remember:`、`kb:`
- 模板触发：`standup:`、`meeting [name]:`、`idea [project]:`
- 批量模式：`start capturing` → 多条 `note:` → `stop capturing`

### 3) 常用 CLI（每日可复用）

```bash
cd ~/coeus
source venv/bin/activate

python3 coeus.py capture "note: your content here"
python3 coeus.py search "find container scaling"
python3 coeus.py brief today
python3 coeus.py stats
```

### 4) OpenClaw 执行提示词（落地版）

```text
你是我的知识库助手。
请把我今天输入的 note:/idea:/standup: 内容按 Coeus 规范入库，并遵循以下规则：
1. 先做全文检索（FTS），只有结果不足时再做语义检索。
2. 输出优先使用 one-line summary，而不是整段原文。
3. 给出：命中内容、来源、建议下一步。
4. 不做删除操作；涉及覆盖写入时先让我确认。
```

## 成功标准

- [ ] 日常记录能通过语义问题快速找回（不依赖原词复现）。
- [ ] 每日/每周摘要优先走缓存摘要，token 消耗明显下降。
- [ ] 新增内容可稳定自动入库，不需要手工搬运。

## 引用来源

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [showcases/coeus-knowledge-base.md](https://github.com/digitalknk/openclaw-runbook/blob/main/showcases/coeus-knowledge-base.md)

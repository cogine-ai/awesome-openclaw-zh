# 安全 CTF 课程

> 每周自动产出 CTF 训练题、解题文档和学习进度跟踪。

## 这个案例能帮你做什么

- 自动跟踪最新漏洞和题型方向，保持训练内容不过时。
- 按类别批量生成挑战题与解法。
- 把训练过程沉淀成可复用课程目录。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`web_search`](https://clawhub.ai/skills/searching-assistant) | 检索最新 CVE 与资料 | ClawHub |
| 内置 | `filesystem` | 组织课程目录与解题文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“安全 CTF 课程”的预演版：
1. 研究最近安全漏洞主题。
2. 生成每个类别2道训练题（含解法）。
3. 输出 week-01 目录结构。
4. 本轮只做样例，不做完整周课发布。
```

## 稳定自动版（可长期运行）

### 1) 课程目录结构

```text
ctf/
├── week-01/
│   ├── web-security/
│   ├── crypto/
│   └── forensics/
└── solutions/
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Security CTF Curriculum”。

每周执行：
1. 研究最新 CVEs。
2. 每个类别设计 5 道挑战题。
3. 编写标准解法。
4. 对题目难度进行测试。
5. 发布到课程目录。

类别轮换：
- Web security
- Cryptography
- Forensics
- Reverse engineering
- Binary exploitation
```

## 成功标准

- [ ] Weekly curriculum published
- [ ] Challenges tested
- [ ] Progress tracked

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/43-security-ctf-curriculum.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/43-security-ctf-curriculum.md)

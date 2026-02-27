# 代理技能目录

> 维护一个可检索的 Agent 能力目录，让协作方快速知道“这个 Agent 能做什么”。

## 这个案例能帮你做什么

- 把技能能力集中展示，提升团队协作和能力发现效率。
- 定期补充“能力 + 用法 + 示例”，减少重复沟通。
- 通过链上版本留存，形成长期公开目录页面。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `bitcoin` | 发布目录链上版本 | OpenClaw Built-in |
| 内置 | `filesystem` | 维护目录内容结构 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先做目录原型页：

```text
你是我的 OpenClaw 助手。
请帮我做“代理技能目录”的预演版：
1. 建立 5 个能力分类（Browser/File/Shell/Blockchain/Communication）。
2. 每个分类先放 2 条能力示例。
3. 生成 HTML 原型页，不执行上链。
```

## 稳定自动版（可长期运行）

### 1) 目录结构示例

```html
<h1>Agent OS Skills</h1>
<section>
  <h2>Browser Automation</h2>
  <ul>
    <li>Web scraping</li>
    <li>Form filling</li>
  </ul>
</section>
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Agent Skills Directory”。
请使用内置 Skills：bitcoin、filesystem。

每月更新：
1. 记录新增能力。
2. 为每个能力补 usage example。
3. 补充 source skills 链接。
4. 生成更新版目录页面并执行 inscription。
5. 将新版本发布给社区。

目录分类：
- Browser automation
- File operations
- Shell execution
- Blockchain interaction
- Communication
```

## 成功标准

- [ ] Directory updated monthly
- [ ] 20+ skills documented
- [ ] Community references

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/47-agent-skills-directory.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/47-agent-skills-directory.md)

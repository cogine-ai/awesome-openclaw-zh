# 夜间文档修复器

> 夜间自动扫文档，修 typo、修坏链、统一格式，并生成可审阅 PR。

## 这个案例能帮你做什么

- 持续修复拼写和格式问题，避免文档质量长期下滑。
- 自动检查 README 链接有效性，提前发现失效链接。
- 每晚产出小步 PR，早会前就能完成文档维护。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `git` | 建分支、提交、发起 PR | OpenClaw Built-in |
| 内置 | `filesystem` | 扫描并修改文档文件 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先只做扫描与修复建议，不提交 PR：

```text
你是我的 OpenClaw 助手。
请帮我做“夜间文档修复器”的预演版：
1. 扫描 docs 与 README，找出常见 typo 和格式不一致。
2. 检查 README 链接可用性（识别 404）。
3. 输出修复清单和建议改动。
4. 本轮不要创建分支和 PR。
```

## 稳定自动版（可长期运行）

### 1) 拼写修复映射

```javascript
const typos = {
  "recieve": "receive",
  "seperate": "separate",
  "occured": "occurred"
};

// Scan and fix
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Night Documentation Fixer”。
请使用内置 Skills：git、filesystem。

每晚执行：
1. 扫描文档中的常见拼写错误。
2. 检查 README 链接（404 detection）。
3. 修复格式不一致项。
4. 创建分支：fix/docs-YYYYMMDD。
5. 提交 PR，并附变更摘要。
6. 记录到 memory/documentation-fixes.md。
```

## 成功标准

- [ ] 5+ typos fixed weekly
- [ ] Zero broken links
- [ ] Consistent formatting

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/18-night-documentation-fixer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/18-night-documentation-fixer.md)

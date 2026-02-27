# GitHub 陈旧问题清理

> 每周识别长期无人更新的 issue，先预警再清理，控制积压规模。

## 这个案例能帮你做什么

- 自动识别超过 30 天未活动的 issue。
- 输出“可关闭候选清单”供人工确认。
- 通过先评论再关闭，降低误关风险。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`github`](https://clawhub.ai/skills/git) | 拉取 issue 与执行评论/关闭 | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“GitHub 陈旧问题清理”的预演版：
1. 查找 open issues 中超过30天无活动的项。
2. 过滤掉已有 wontfix/duplicate 标签。
3. 输出候选清单与理由。
4. 本轮不执行关闭，仅生成报告。
```

## 稳定自动版（可长期运行）

### 1) stale 检测逻辑

```javascript
const staleDays = 30;
const issues = await github.listIssues({ state: 'open' });
const stale = issues.filter(i =>
  daysSince(i.updated_at) > staleDays &&
  i.comments === 0
);
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“GitHub Stale Issue Cleanup”。

每周日执行：
1. 查找超过30天无活动 issue。
2. 检查是否带 wontfix / duplicate 标签。
3. 输出 closure candidate list。
4. 人工审核后再执行关闭。
5. 关闭前先自动评论 stale warning。
```

## 成功标准

- [ ] Stale issues identified weekly
- [ ] Backlog reduced 10% per month
- [ ] Zero accidental closures

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/17-github-stale-issue-cleanup.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/17-github-stale-issue-cleanup.md)

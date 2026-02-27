# GitHub Issue 优先级排序器

> 自动扫描多个仓库 Issue，按紧急程度排序并输出晨间处理清单。

## 这个案例能帮你做什么

- 把“无序 issue 堆积”变成“按优先级处理队列”。
- 自动识别长期无人跟进的 stale issue。
- 每天固定推送前 10 条关键 issue 给团队快速决策。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`github`](https://clawhub.ai/skills/git) | 读取仓库 issue 数据 | ClawHub |
| 内置 | `web_fetch` | 获取 issue 详情 | OpenClaw Built-in |
| 内置 | `telegram` | 推送优先级日报 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先在单仓库演示排序：

```text
你是我的 OpenClaw 助手。
请帮我做“GitHub Issue 优先级排序器”的预演版：
1. 拉取一个仓库的 open issues。
2. 计算每个 issue 的优先级分数。
3. 输出 top 10 列表（含原因）。
4. 标记 7 天以上无活动且无人认领的 issue。
```

## 稳定自动版（可长期运行）

### 1) 仓库配置 `config/repos.json`

```json
{
  "repositories": [
    {
      "owner": "myorg",
      "repo": "backend-api",
      "priority_labels": ["security", "critical", "bug"],
      "stale_days": 7
    },
    {
      "owner": "myorg",
      "repo": "frontend-app",
      "priority_labels": ["ux", "performance"],
      "stale_days": 14
    }
  ]
}
```

### 2) 优先级评分算法

```javascript
function calculatePriority(issue) {
  let score = 0;

  const daysOld = (Date.now() - new Date(issue.created_at)) / 86400000;
  score += Math.min(daysOld * 2, 20);

  const weights = {
    "security": 50,
    "critical": 40,
    "bug": 20,
    "enhancement": 10,
    "documentation": 5
  };
  issue.labels.forEach(l => score += weights[l.name] || 0);

  score += issue.comments * 3;

  const urgent = ["crash", "broken", "urgent", "down", "error"];
  if (urgent.some(w => issue.title.toLowerCase().includes(w))) {
    score += 30;
  }

  return score;
}
```

### 3) stale issue 检测

```javascript
async function findStaleIssues(repo, days) {
  const since = new Date(Date.now() - days * 86400000).toISOString();

  const issues = await github.listIssues({
    owner: repo.owner,
    repo: repo.repo,
    state: "open",
    since: since
  });

  return issues.filter(i =>
    !i.assignee &&
    new Date(i.updated_at) < new Date(since)
  );
}
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“GitHub Issue Prioritizer”。
请使用 Skills：github、web_fetch、telegram。

每天 08:00：
1. 拉取配置仓库的 open issues。
2. 计算优先级分数。
3. 识别 stale issue（超过阈值无活动）。
4. 分类输出：Critical / High / Medium / Low。
5. 推送 top 10 到 Telegram。

每周日：
- 输出 stale issue 关闭建议。
- 统计平均响应时间趋势。
```

### 5) 调度配置

```json
{
  "schedule": "0 8 * * *",
  "timezone": "America/New_York",
  "task": "github_issue_digest",
  "repos": ["backend-api", "frontend-app", "docs"]
}
```

## 成功标准

- [ ] Critical issues flagged within 24h of creation
- [ ] Stale issues identified weekly
- [ ] Average response time tracked
- [ ] Human reviews digest within 2 hours

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/07-github-issue-prioritizer.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/07-github-issue-prioritizer.md)

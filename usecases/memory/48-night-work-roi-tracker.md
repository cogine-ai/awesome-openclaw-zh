# 夜间工作 ROI 跟踪器

> 记录每个夜间自动构建的“使用率/回滚率”，用数据决定后续自动化方向。

## 这个案例能帮你做什么

- 避免“看起来做了很多，实际价值不高”的夜间自动化。
- 每周量化命中率（hit rate），识别值得继续投入的类型。
- 通过回滚原因反推策略，减少低价值构建。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 记录构建日志与使用结果 | OpenClaw Built-in |
| 内置 | `memory` | 沉淀决策原因与策略调整记录 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 ROI 跟踪助手。
请对昨晚自动构建项做一次盘点，输出：
1) 做了什么
2) 是否被使用
3) 是否被回滚
4) 初步 ROI 结论
本轮只做统计，不做策略调整。
```

## 稳定自动版（可长期运行）

### 1) 记录结构

```javascript
const build = {
  timestamp: Date.now(),
  description: "Added shell alias",
  used: null,
  reverted: false,
  reason: null
};
```

### 2) OpenClaw 执行提示词（自动版）

```markdown
## Night Work ROI Tracker

For each autonomous build:
1. Log what was built
2. Track if human uses it
3. Note if reverted
4. Calculate hit rate weekly
5. Adjust strategy based on data

Metrics:
- Hit rate: used / total
- Time saved per successful build
- Revert reasons
```

## 成功标准

- [ ] 每个夜间构建都有记录。
- [ ] 每周稳定产出 hit rate。
- [ ] 月度策略调整有数据依据。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/48-night-work-roi-tracker.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/48-night-work-roi-tracker.md)

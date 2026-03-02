# 自主教育游戏开发流水线（Autonomous Educational Game Development Pipeline）

> 以“先修 Bug、再做新游戏”的规则持续推进教育游戏开发。

## 这个案例能帮你做什么

- 按开发队列自动推进教育游戏的实现、注册和交付。
- 强制执行 Bugs First，避免问题积压后继续堆新功能。
- 每轮自动更新版本记录与项目计划文件。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 内置 | `git` | 执行拉取、建分支、提交、推送与合并流程 | hesamsheikh/awesome-openclaw-usecases |

## 快速体验版（先跑一轮）

1. 准备好 `bugs/`、`development-queue.md`、`game-design-rules.md`、`games-list.json`。
2. 先跑一个最小周期，验证是否严格先修 bug。
3. 本轮先观察流程完整性，再扩大任务规模。

```text
Act as an Expert in Web Game Development and Child UX.
Your goal is to develop the next game in the production queue.

Please read and analyze the following context files before starting:

1.  BUG CONTEXT (Top Priority - CRITICAL):
    @[bugs/]
    (Check this folder. If there are files, YOUR TASK IS TO FIX **ONLY THE FIRST FILE** (in alphabetical order). Ignore the rest of the bugs and the game queue for now).

2.  QUEUE CONTEXT (Which game is next):
    @[development-queue.md]
    (Identify the game marked as [NEXT] in the "Next Games" section. ONLY if there are no bugs).

3.  DESIGN RULES (Technical Standards):
    @[game-design-rules.md]
    (Strictly follow these rules: Pure HTML/CSS/JS, folder structure, mobile responsiveness)

4.  GAME SPECIFICATIONS (Mechanics and Assets):
    (Identify the corresponding file in games-backlog/ based on the game ID)

5.  CENTRAL REGISTRY (Integration):
    @[public/js/games-list.json]
    (File where you MUST register the new game so it appears on the home page)
```

## 稳定自动版（可长期运行）

### 推荐流程

1. 每轮先检查 `bugs/`，只处理按字母序第一条 bug。
2. 无 bug 再按 `development-queue.md` 处理下一款游戏，并写入 `games-list.json`。
3. 每轮都更新 `CHANGELOG.md`、`master-game-plan.md`、`development-queue.md` 并走完整 git 交付。

## 成功标准

- [ ] 每轮都严格执行 Bugs First。
- [ ] 新游戏会被正确注册并可在主页可见。
- [ ] 每轮变更都有可追踪的 git 记录。

## 引用来源

- 来源仓库： [hesamsheikh/awesome-openclaw-usecases](https://github.com/hesamsheikh/awesome-openclaw-usecases)
- 原始条目： [usecases/autonomous-game-dev-pipeline.md](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/autonomous-game-dev-pipeline.md)

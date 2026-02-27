# 数据分析工作流（Skills组合）

> 通过多个技能协同完成数据处理和输出。

## 来源与对齐

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- 作为超级个体，你需要持续学习和获取信息，但手动收集信息太耗时。通过OpenClaw构建全自动信息收集系统，每天早上自动生成个性化日报。
- 多源信息收集 → 智能去重 → 质量评分 → 自动分类 → 生成日报 → 飞书推送
- 传统的待办清单只是记录任务，智能任务管理系统能够：
- 自动识别任务优先级

### 核心动作（来源提炼）
- **第一步：安装必需的Skills**
- **场景**：作为开发者，需要每天了解最新的技术动态。
- "sources": {
- "https://news.ycombinator.com/rss",
- "https://www.reddit.com/r/programming/.rss",
- "https://dev.to/feed"

### 技能/工具/渠道（来源提炼）
- > 💡 **本章目标**：学习高级自动化工作流、多Skills组合应用、个人知识图谱构建和效率优化策略，让你成为真正的超级个体。
- clawhub install brave-search      # 网页搜索
- clawhub install rss-reader        # RSS订阅
- clawhub install github-trending   # GitHub热门
- clawhub install content-analyzer  # 内容分析
- clawhub install text-summarizer   # 文本摘要
- clawhub install duplicate-checker # 去重检查
- **第二步：配置信息源**

### 风险与边界（来源提炼）
- 源头未明确列出风险条目，默认采用最小权限与二次确认。

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「数据分析工作流（Skills组合）」。

目标（来自来源案例）：通过多个技能协同完成数据处理和输出。
来源关键动作：**第一步：安装必需的Skills**；**场景**：作为开发者，需要每天了解最新的技术动态。；"sources": {
优先工具/渠道：Notion、GitHub、cron、OpenClaw
来源节奏信息：08:00；09:00；18:00；11:00；14:00

请按下面流程输出并执行：
1. 先给出“最小可运行版本（MVP）”执行计划（3-5条）
2. 立刻产出第一版结果（不要只讲思路）
3. 缺失的信息统一放到“待我补充信息”里，不要中断整体流程
4. 若涉及高风险操作（删除、外发、改密、生产写操作），先暂停并请求确认

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 待我补充信息
## 风险与边界
```

## 可选补充信息（提高效果）

- 你的常用渠道：[Telegram/飞书/微信/邮箱]
- 你的时区与执行时间：[例如 UTC+8，每天 09:00]
- 你最在意的结果指标：[例如 节省时间、回复率、发布频次]

## 效果检查（非技术版）

- **学习效率提升**：
- 资源发现时间：从2小时 → 10分钟
- 笔记整理时间：从1小时 → 5分钟

## 参考来源

- [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

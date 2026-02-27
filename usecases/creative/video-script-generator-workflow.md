# 视频脚本生成工作流

> 短视频与长视频脚本自动生成，支持系列化输出。

## 来源与对齐

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- **用户**：内容创作者、设计师、自媒体运营、教程作者
- **需求**：快速生成配图、白板图、Logo设计、批量处理
- **工具**：Gemini图像生成、Banana Pro、Midjourney、Stable Diffusion
- ❌ 手机无法使用：专业绘图工具只有网页版

### 核心动作（来源提炼）
- 这是一个真实的使用案例：为OpenClaw教程的每一章生成手写白板风格的总结图。
- 需求：为教程的16章内容生成配图
- 风格：手写白板风格，易于理解
- 要求：包含核心要点、框图、箭头等手绘元素
- 数量：每章1张，共16张
- 你：把这张照片转换成水彩画风格

### 技能/工具/渠道（来源提炼）
- 在开始使用之前，需要先安装绘图Skill。
- **方式1：从GitHub安装（推荐）**
- cp -r my-awesome-skills/.claude/skills/bananapro-image-gen ~/.openclaw/skills/
- ls ~/.openclaw/skills/bananapro-image-gen
- 根据ClawHub技能市场，以下是推荐的AI绘画相关Skills：
- **1. fal-ai - 多功能AI生成**
- clawhub install banana-pro
- openclaw config set banana.api-key "YOUR_API_KEY"

### 风险与边界（来源提炼）
- **1. AI的局限性**
- • AI不能替代真实专家
- • 复杂决策需要人工审核
- • 关键决策需要多方验证

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「视频脚本生成工作流」。

目标（来自来源案例）：短视频与长视频脚本自动生成，支持系列化输出。
来源关键动作：这是一个真实的使用案例：为OpenClaw教程的每一章生成手写白板风格的总结图。；需求：为教程的16章内容生成配图；风格：手写白板风格，易于理解
优先工具/渠道：WhatsApp、Discord、Notion、GitHub、heartbeat、OpenClaw
来源节奏信息：0:30；2:00；5:00；7:00；12:00

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

- > 💡 **本章目标**：探索OpenClaw在创意领域的应用，包括AI绘画工作流、视频脚本生成、多语言翻译和数据分析自动化。
- **使用前后对比**：
- **创作效率提升**：

## 参考来源

- [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

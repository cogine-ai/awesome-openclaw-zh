# 知识工作者全天工作流

> 覆盖日报、资料、会议、复盘的一整天效率流程。

## 来源与对齐

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
- **角色**：张明，管理咨询顾问
- 需要处理大量信息
- 频繁的会议和沟通
- 需要快速产出报告

### 核心动作（来源提炼）
- > 💡 **本章目标**：通过5个真实场景，学习如何用OpenClaw打造个人效率提升系统，涵盖知识工作者、程序员、内容创作者、学生和超级个体的完整工作流。
- openclaw schedule add "daily-report" \
- --time "07:00" \
- --prompt "生成今日日报，包括：日程、待办、行业动态、建议"
- openclaw config set report.sources \
- "calendar,todo,rss,notion"

### 技能/工具/渠道（来源提炼）
- clawhub install web-clipper
- **百度Skills库**：
- 官方文档：https://cloud.baidu.com/doc/qianfan/s/Mmlda41a2
- baidu-search：百度搜索（云端自带）
- baidu-scholar：百度学术
- baidu-baike：百度百科
- 其他百度生态Skills
- **YouSkill - Skills搜索引擎**：

### 风险与边界（来源提炼）
- 代码审查：AI生成的代码需要人工审查
- 测试验证：必须进行充分测试
- 安全检查：检查是否有安全漏洞
- 备份代码：定期备份重要代码

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

```text
你是我的 OpenClaw 助手，现在执行案例「知识工作者全天工作流」。

目标（来自来源案例）：覆盖日报、资料、会议、复盘的一整天效率流程。
来源关键动作：> 💡 **本章目标**：通过5个真实场景，学习如何用OpenClaw打造个人效率提升系统，涵盖知识工作者、程序员、内容创作者、学生和超级个体的完整工作流。；openclaw schedule add "daily-report" \；--time "07:00" \
优先工具/渠道：Notion、GitHub、OpenClaw
来源节奏信息：7:00；09:00；10:00；14:00；16:00

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

- > 💡 **本章目标**：通过5个真实场景，学习如何用OpenClaw打造个人效率提升系统，涵盖知识工作者、程序员、内容创作者、学生和超级个体的完整工作流。
- **使用前后对比**：
- **每月效率提升**：

## 参考来源

- [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

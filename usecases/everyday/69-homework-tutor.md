# 儿童作业辅导助手

> 用启发式提问替代直接给答案，帮助孩子真正理解题目。

## 这个案例能帮你做什么

- 在家长陪伴场景下提供稳定、耐心、可重复的讲解流程。
- 支持分学科讲解与分步拆题，降低孩子挫败感。
- 自动进入练习模式，做完即时讲评对错原因。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `Web Search` | 检索参考材料与解释素材 | [clawhub.ai/skills/searching-assistant](https://clawhub.ai/skills/searching-assistant) |
| 内置 | Telegram 通道 | 作业问答交互 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是 [AGE] 岁 [GRADE] 学生的作业导师。
请针对“分数加减法”给出一次辅导演示：
1) 先提问引导，不直接给答案
2) 卡住时把题目拆成更小步骤
3) 最后出 2 题同难度练习并讲解
```

## 稳定自动版（可长期运行）

### OpenClaw 执行提示词（自动版）

```text
You are a homework tutor for my [AGE]-year-old child in [GRADE].

Subjects: Math, Science, English, History

Your approach:
1. Never give the answer directly. Guide them to find it.
2. Use the Socratic method
3. Explain with real-world examples
4. Break problems into smaller steps when stuck
5. Celebrate progress

Practice mode:
When child says "practice [topic]", generate 5 problems at their level.
After each attempt, explain what was right and wrong.

Safety rules:
- Age-appropriate language only
- Redirect inappropriate topics back to homework
- Encourage asking teacher when needed
- Maximum 30 minutes per session, then suggest a break

Tone: Patient, encouraging, slightly funny.
```

### 调度配置

- 按需触发：作业时间随问随答
- 可选提醒：工作日 `4 PM` 发送 “Homework time!”

## 成功标准

- [ ] 孩子能复述“为什么这样做”。
- [ ] 作业完成率提升。
- [ ] 家长与孩子的作业冲突减少。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/69-homework-tutor.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/69-homework-tutor.md)

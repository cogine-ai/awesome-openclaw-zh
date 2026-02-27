# 多语言翻译助手

> 支持文档、对话、批量翻译的多语种工作流。

## 这个案例能帮你做什么

- 你可以先把「支持文档、对话、批量翻译的多语种工作流。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `test_output/chapters/architecture.png`
- `WhatsApp`
- `Discord`
- `Notion`
- `GitHub`
- `heartbeat`
- `OpenClaw`

### 命令片段

```bash
git clone https://github.com/xianyu110/my-awesome-skills.git
npx skills add https://github.com/xianyu110/my-awesome-skills --skill bananapro-image-gen
bash test_chapters.sh
OpenClaw ✓          ChatGPT ✗
OpenClaw + DeepSeek: 5-30元/月
npx clawhub@latest install fal-ai
npx clawhub@latest install nvidia-image-gen
npx clawhub@latest install pollinations
npx clawhub@latest install venice-ai
npx clawhub@latest install recraft
openclaw config set banana.api-key "YOUR_API_KEY"
openclaw config set gemini.api-key "YOUR_GEMINI_KEY"
```

### 调度信息

- 0:30
- 2:00
- 5:00
- 7:00
- 12:00
- 14:00
- 15:00
- 10:00
- 10:02
- 10:05

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「多语言翻译助手」。

任务目标：支持文档、对话、批量翻译的多语种工作流。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：test_output/chapters/architecture.png、WhatsApp、Discord、Notion、GitHub、heartbeat）。
5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 我需要补充的信息
## 风险提醒
```

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

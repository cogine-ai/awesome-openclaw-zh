# 个人知识图谱构建

> 把知识点和关系沉淀成图谱，提升检索与复盘效率。

## 这个案例能帮你做什么

- 你可以先把「把知识点和关系沉淀成图谱，提升检索与复盘效率。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `Telegram`
- `Discord`
- `Notion`
- `GitHub`
- `cron`
- `OpenClaw`
- `RSS`

### 命令片段

```bash
openclaw agent --message "请使用 rss-reader skill 收集 ~/.openclaw/info-sources.json 中配置的RSS源，保存到 $OUTPUT_DIR/rss-$DATE.json"
openclaw agent --message "请收集GitHub今日Python热门项目，保存到 $OUTPUT_DIR/github-$DATE.json"
openclaw agent --message "请搜索'OpenClaw AI工具'相关信息，最多10条结果，保存到 $OUTPUT_DIR/search-$DATE.json"
openclaw agent --message "请合并 $OUTPUT_DIR/*-$DATE.json 中的所有信息并去重，保存到 $OUTPUT_DIR/merged-$DATE.json"
openclaw agent --message "请分析 $OUTPUT_DIR/merged-$DATE.json 中的内容并评分，保存到 $OUTPUT_DIR/analyzed-$DATE.json"
openclaw channels send feishu \
crontab -e
openclaw skills run brave-search \
bash ~/.openclaw/scripts/content-creation.sh "OpenClaw自动化测试实战"
openclaw agent --message "分析最近的技术热点，生成3个博客选题"
bash ~/.openclaw/scripts/content-creation.sh "选题1"
openclaw agent --message "生成今日效率报告"
```

### 调度信息

- 08:00
- 09:00
- 18:00
- 11:00
- 14:00
- 16:00
- 15:00
- 12:00
- 13:00
- 17:00

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「个人知识图谱构建」。

任务目标：把知识点和关系沉淀成图谱，提升检索与复盘效率。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：Telegram、Discord、Notion、GitHub、cron、OpenClaw）。
5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 我需要补充的信息
## 风险提醒
```

## 风险与边界

- 密钥与凭证不要放在公开文本或提示词中。

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/13-advanced-automation.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/13-advanced-automation.md)

# 学生学习助手工作流

> 覆盖课程资料整理、作业辅助、复习规划和学习进度跟踪。

## 这个案例能帮你做什么

- 把课程资料、作业、论文笔记整理成统一学习库。
- 在编程作业场景下提供分析、代码和优化建议。
- 用固定提醒节奏推动复习计划执行。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部（需安装） | `file-organizer` | 课程资料自动归类 | ClawHub |
| 外部（需安装） | `paper-reader` | 论文阅读与笔记模板 | ClawHub |
| 外部（需安装） | `code-helper` | 编程作业辅助 | ClawHub |
| 外部（需安装） | `study-planner` / `flashcard-generator` | 复习计划与卡片生成 | ClawHub |
| 外部（需安装） | `project-manager` / `calendar-sync` | 科研进度与时间管理 | ClawHub |

## 快速体验版（先跑一轮）

```text
你是我的学习助手。
请先演示“机器学习课程”当天学习计划：
1) 今日课程资料清单
2) 一项作业拆解
3) 晚间复习任务
本轮不写配置。
```

## 稳定自动版（可长期运行）

### 学习助手配置脚本（源案例）

```bash
#!/bin/bash
# 学生学习助手完整配置

# 1. 课程资料管理
clawhub install file-organizer
openclaw config set courses.path "~/课程资料"
openclaw config set courses.auto-organize true

# 2. 论文阅读
clawhub install paper-reader
openclaw config set paper.language "中英文"
openclaw config set paper.notes-template "标准模板"

# 3. 作业辅助
clawhub install code-helper
openclaw config set homework.check true
openclaw config set homework.optimize true

# 4. 考试复习
clawhub install study-planner
clawhub install flashcard-generator
openclaw config set study.daily-reminder true

# 5. 科研项目
clawhub install project-manager
openclaw config set project.progress-tracking true
openclaw config set project.milestone-alert true

# 6. 时间管理
clawhub install calendar-sync
openclaw config set calendar.auto-create true

echo "✅ 学生学习助手配置完成！"
```

## 成功标准

- [ ] 课程资料和作业状态可视化。
- [ ] 学习计划可每日执行并追踪进度。
- [ ] 复习与作业提醒稳定触发。

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/12-personal-productivity.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/12-personal-productivity.md)

# 邮件自动分类器

> 自动把新邮件分到 urgent / routine / spam，并对紧急邮件即时提醒。

## 这个案例能帮你做什么

- 自动完成邮件初筛，减少人工清邮箱时间。
- 识别紧急邮件并在 15 分钟内提醒。
- 把“重要邮件被淹没”风险降到最低。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`email`](https://clawhub.ai/skills/agentmail-wrapper) | 读取与分类邮件 | ClawHub |
| 内置 | `telegram` | 紧急邮件告警 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的 OpenClaw 助手。
请帮我做“邮件自动分类器”的预演版：
1. 扫描最近30封邮件。
2. 按规则归类 urgent/routine/spam。
3. 输出分类统计与紧急项列表。
4. 本轮不移动邮件，仅做分类演示。
```

## 稳定自动版（可长期运行）

### 1) 分类规则

```javascript
const rules = [
  { pattern: /meeting|urgent|asap/i, folder: 'urgent' },
  { pattern: /unsubscribe|newsletter/i, folder: 'routine' },
  { pattern: /viagra|winner/i, folder: 'spam' }
];
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Email Auto-Classifier”。

每 15 分钟执行：
1. 检查新邮件。
2. 应用分类规则。
3. 移动到对应文件夹。
4. 如有 urgent，立即告警。
5. 输出统计：X urgent, Y routine, Z spam。

Urgent indicators:
- From boss/CEO
- Contains "urgent", "asap", "meeting changed"
- Reply-to within 2 hours requested
```

## 成功标准

- [ ] Urgent emails alerted within 15 min
- [ ] False positive rate <5%
- [ ] Zero missed urgent messages

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/21-email-auto-classifier.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/21-email-auto-classifier.md)

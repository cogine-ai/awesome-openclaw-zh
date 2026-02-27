# 每日自我改进定时任务

> 每天固定做 1 项能力升级，把“持续优化”变成系统行为。

## 这个案例能帮你做什么

- 通过稳定节奏让能力持续复利，而不是偶发优化。
- 从技能安装、MCP 接入、Bug 修复到流程优化都有可执行入口。
- 每天有记录、每周可复盘，不再“感觉在进步”。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `cron` | 每日 06:00 触发改进任务 | OpenClaw Built-in |
| 内置 | `filesystem` | 记录改进日志与 backlog | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```text
你是我的持续改进助手。
请从改进待办里选 1 项今天可完成的动作，输出：
1) 执行步骤
2) 验证方式
3) 记录模板
本轮只给方案，不落地改动。
```

## 稳定自动版（可长期运行）

### 1) 改进队列示例

```javascript
const improvements = [
  { type: 'skill', name: 'web_search' },
  { type: 'mcp', name: 'github-server' },
  { type: 'bugfix', issue: '#123' },
  { type: 'integration', service: 'notion' }
];
```

### 2) OpenClaw 执行提示词（自动版）

```markdown
## Daily Self-Improvement Cron

Every day at 06:00:
1. Review improvement backlog
2. Select 1 item for today
3. Execute improvement
4. Test thoroughly
5. Document in memory/improvements.md
6. Report to human

Categories:
- Install new skill
- Add MCP server
- Fix known bug
- Integrate new service
- Optimize existing workflow
```

## 成功标准

- [ ] 每天完成 1 项可验证改进。
- [ ] backlog 持续更新不堆积。
- [ ] 周复盘能看见稳定增长曲线。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/39-daily-self-improvement-cron.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/39-daily-self-improvement-cron.md)

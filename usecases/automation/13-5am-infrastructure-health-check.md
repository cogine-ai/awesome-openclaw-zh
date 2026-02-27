# 凌晨 5 点基础设施健康检查

> 在工作日开始前完成资源巡检，问题提前暴露，避免早高峰临时救火。

## 这个案例能帮你做什么

- 每天 05:00 自动检查磁盘、内存、负载和备份状态。
- 达到阈值时立刻告警，没问题就静默通过。
- 把“上班后才发现故障”改成“上班前已定位风险”。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `system` | 读取系统资源指标 | OpenClaw Built-in |
| 内置 | `telegram` | 异常即时通知 | OpenClaw Built-in |
| 内置 | `cron` | 固定时间触发巡检 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先执行一次“白天演练”：

```text
你是我的 OpenClaw 助手。
请帮我做“5AM 基础设施健康检查”的预演版：
1. 现在立刻检查一次磁盘、内存、负载、备份状态、外网连通性。
2. 不要做系统改动，只输出检查结果和告警级别。
3. 按阈值标记 Warning / Critical。
4. 最后给出明天 05:00 的自动执行计划。
```

## 稳定自动版（可长期运行）

### 1) 健康检查脚本：`check-health.sh`

```bash
#!/bin/bash
# check-health.sh

df -h | grep -E "(9[0-9]|100)%" && alert "Disk critical"
free -m | awk '/Mem:/ {if ($3/$2 > 0.9) print "Memory high"}'
uptime | awk '{if ($3 > 7) print "Reboot suggested"}'
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“5AM Infrastructure Check”。
请使用内置 Skills：system、telegram、cron。

每天 05:00 执行：
1. 检查所有卷磁盘使用率。
2. 检查内存利用率。
3. 检查 load average。
4. 验证备份是否完成。
5. 测试外部网络连通性。
6. 如任一检查失败，立即告警。
7. 全部通过则静默成功。

阈值：
- Disk >90%: Warning
- Disk >95%: Critical
- Memory >90%: Warning
- Load >4: Investigate
```

## 成功标准

- [ ] 100% uptime for critical services
- [ ] Issues detected before 8 AM
- [ ] False positive rate <5%

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/13-5am-infrastructure-health-check.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/13-5am-infrastructure-health-check.md)

# VPS部署与加固流程

> 从部署到安全收口的一体化流程，适合长期在线运行。

## 这个案例能帮你做什么

- 你可以先把「从部署到安全收口的一体化流程，适合长期在线运行。」做成一个可重复执行的小流程。
- 这个场景适合加上定时执行，减少手动重复操作。
- 可结合现有技能与渠道，把结果直接推送到你常用入口。

## 开始前准备

### 技能与工具

- `gateway.trusted_proxies_missing`
- `fs.credentials_dir.perms_readable`
- `0.0.0.0`
- `minimal`
- `session_status`
- `coding`
- `messaging`
- `full`
- `heartbeat-example.md`
- `agent-prompts.md`
- `cron`
- `heartbeat`
- `OpenClaw`
- `Tailscale`

### 命令片段

```bash
ssh user@your-vps-ip
curl -fsSL https://tailscale.com/install.sh | sh
tailscale ip -4
ssh user@100.64.1.2
ssh user@your-public-vps-ip
openclaw doctor --fix
openclaw security audit --deep
openclaw gateway restart
git add .gitignore openclaw.json
git commit -m "config: baseline"
git commit -am "config: before model update"
git commit -am "config: switched to Gemini 3 Flash"
```

### 调度信息

- 0 2 * * 0

## 可复制提示词

```text
你是我的 OpenClaw 助手，请帮我完成「VPS部署与加固流程」。

任务目标：从部署到安全收口的一体化流程，适合长期在线运行。

请按这个顺序执行：
1. 先给出今天可落地的最小版本（3-5步）。
2. 直接产出第一版结果，不要只讲思路。
3. 如果缺少信息，把问题集中放在最后让我一次补全。
4. 使用我已启用的技能（优先：gateway.trusted_proxies_missing、fs.credentials_dir.perms_readable、0.0.0.0、minimal、session_status、coding）。
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
- 远程访问和权限建议按最小授权配置。
- 关键变更前先备份，确保可回滚。

## 使用建议

- 先手动跑通一次，再设置自动化。
- 先用一个渠道验证结果，再扩到更多渠道。
- 关键动作建议保留确认步骤。

## CITATION

- 来源仓库： [digitalknk/openclaw-runbook](https://github.com/digitalknk/openclaw-runbook)
- 原始条目： [examples/vps-setup.md](https://github.com/digitalknk/openclaw-runbook/blob/main/examples/vps-setup.md)

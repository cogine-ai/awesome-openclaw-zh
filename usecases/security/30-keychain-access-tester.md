# 钥匙串访问测试器

> 通过可控测试验证“人是否会在未核验来源时输入密码”。

## 这个案例能帮你做什么

- 定期演练人机协作中的社会工程学风险。
- 记录响应时间、核验动作、是否误输密码。
- 把测试结果沉淀为家庭/团队安全规则。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `system` | 触发测试命令 | OpenClaw Built-in |
| 内置 | `memory` | 记录测试结果与规则更新 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```bash
security find-generic-password -s "test" -w
```

该命令会触发 Keychain 弹窗，用于观察是否进行来源核验。

## 稳定自动版（可长期运行）

### 1) 月度测试流程（原文）

```text
Monthly security test:
1. Run command that triggers keychain dialog
2. Observe if human types password
3. Document response time and verification
4. If password entered: security briefing
5. Update household security rules
```

### 2) 安全教育要点（原文）

- 输入密码前先确认弹窗来源进程
- 不确定时优先点击 Cancel
- 把“先核验再输入”写成固定规则

## 成功标准

- [ ] 每月测试有记录。
- [ ] 人工核验率可跟踪。
- [ ] 安全规则会根据测试结果更新。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/30-keychain-access-tester.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/30-keychain-access-tester.md)

# 安全与权限边界（非技术版）

## 3 条红线

1. 不把 API Key、密码、私钥写在提示词里。
2. 不给 OpenClaw 超出需求的系统权限。
3. 不执行来源不明的第三方技能。

## 做对这 4 件事

- 使用独立账号和最小权限
- 高风险操作必须要求二次确认
- 记录“自动任务都能访问什么”
- 每周回看一次权限和日志

## 你可以先用这些安全类案例

- [技能预检检查器](../usecases/security/34-skill-preflight-checker.md)
- [技能供应链审计](../usecases/security/31-skill-supply-chain-audit.md)
- [API 安全测试器](../usecases/security/32-api-security-tester.md)
- [令牌使用优化器](../usecases/security/27-token-usage-optimizer.md)

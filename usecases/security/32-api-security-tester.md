# API 安全测试器

> 对接口做定期安全探测，优先发现重定向、鉴权与输入校验类漏洞。

## 这个案例能帮你做什么

- 发现“307 跳转丢 Authorization”等隐蔽问题。
- 固定频率验证鉴权绕过、限流缺失、输入校验薄弱点。
- 形成可复现的测试记录，支持负责任披露。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 发送 HTTP 测试请求 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

```javascript
const tests = [
  {
    name: "Redirect header preservation",
    url: "https://example.com/redirect",
    header: "Authorization: Bearer test",
    check: (response) => response.request.headers.authorization
  }
];
```

## 稳定自动版（可长期运行）

### 1) 月度安全测试（原文）

```text
Monthly tests:
1. Test redirect header handling
2. Check for authentication bypasses
3. Verify rate limiting
4. Test input validation
5. Document findings with reproduction steps

Responsible disclosure:
- Report privately first
- Allow 30 days for fix
- Publish after resolution
```

## 成功标准

- [ ] 月度测试稳定执行。
- [ ] 每个发现都带复现步骤。
- [ ] 披露流程符合“先私下、后公开”。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/32-api-security-tester.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/32-api-security-tester.md)

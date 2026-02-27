# Skills 供应链审计

> 对已安装 Skills 做周期性安全扫描，拦截恶意脚本与凭证窃取行为。

## 这个案例能帮你做什么

- 扫描技能包中的可疑网络外联与敏感文件读取行为。
- 用 YARA 规则快速定位高风险模式（如读取 `.env` 并回传）。
- 降低“装了一个 Skill，泄露整套权限”的系统性风险。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `filesystem` | 读取技能文件 | OpenClaw Built-in |
| 内置 | `yara` | 恶意模式匹配 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先建一条最小 YARA 规则：

```yara
rule CredentialStealer {
  strings:
    $env = /\.env/
    $webhook = /webhook\.site/
    $curl = "curl" nocase
  condition:
    all of them
}
```

## 稳定自动版（可长期运行）

### 1) 周度审计流程（原文）

```text
Weekly scan:
1. List all installed skills
2. Run YARA rules against each
3. Check for network calls to unknown domains
4. Verify file system access patterns
5. Flag suspicious behavior
6. Report findings to community
```

### 2) 运营侧实践（原文）

- 版本固定，不直接跟 `latest`
- 安装前先读 `SKILL.md`
- 先在沙箱验证，再进主环境

## 成功标准

- [ ] 每周完成全量技能扫描。
- [ ] 主环境零恶意技能驻留。
- [ ] 异常样本有记录并可追踪。

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/31-skill-supply-chain-audit.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/31-skill-supply-chain-audit.md)

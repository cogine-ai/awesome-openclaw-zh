# 微信公众号自动发布

> 用 OpenClaw 串起选题、写稿、排版和草稿箱推送，减少公众号运营的重复劳动。

## 这个案例能帮你做什么

- 从热点、资料或旧文章中生成公众号选题和长文初稿。
- 将 Markdown 转成公众号编辑器友好的排版，并上传封面图和正文图片。
- 把文章推送到公众号草稿箱，让人工只负责最终审核和发布。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`md2wechat-skill`](https://github.com/geekjourneyx/md2wechat-skill) | Markdown 转公众号排版并推送草稿箱 | 社区项目 |
| 外部（可选） | [`wechat-publisher`](https://github.com/0731coderlee-sudo/wechat-publisher) | 一键将 Markdown 推送到公众号草稿箱 | 社区项目 |
| 外部（可选） | [`china-hot-ranks`](https://github.com/LucianaiB2004/China-Hot-Ranks) | 聚合微博、抖音、B 站等热点 | 社区项目 |

## 快速体验版（先跑一轮）

```text
你是我的公众号运营助手。
请把下面这篇 Markdown 转成适合微信公众号阅读的版本：
1. 保留一级标题和小标题层级
2. 自动生成 2 个备选标题和 1 段摘要
3. 只输出排版后的内容，不要发布

[粘贴 Markdown]
```

## 稳定自动版（可长期运行）

### 1) 准备微信公众号凭证

在微信公众平台获取：

- AppID
- AppSecret
- IP 白名单配置权限

个人订阅号通常可以写入草稿箱，但最终发布往往仍需人工在后台或公众号助手 App 里确认。

### 2) 安装排版与发布工具

```bash
brew install geekjourneyx/tap/md2wechat
md2wechat config init
```

如果使用 Skill 方式，也可以按对应项目说明安装 `wechat-publisher`。

### 3) OpenClaw 执行提示词（自动版）

```text
你是我的公众号内容运营助手，请执行「公众号草稿生产」流程。

执行步骤：
1. 根据今天的热点和我的账号定位，给出 3 个选题
2. 让我确认选题后，写一篇 1500-2500 字公众号长文
3. 生成标题、摘要、封面图建议和正文图片建议
4. 转换为公众号友好的 Markdown 排版
5. 推送到草稿箱；如果当前账号不能 API 发布，只返回草稿信息并提醒人工审核
```

## 成功标准

- [ ] 能从 Markdown 生成适合公众号的排版内容。
- [ ] 能成功创建公众号草稿或输出可复制到编辑器的版本。
- [ ] 发布前保留人工审核环节。

## 风险与边界

- AppSecret 泄露等同于账号被接管，必须通过环境变量或本地配置管理。
- AI 生成内容需要人工检查事实、版权和合规风险。
- 个人订阅号和未认证账号的发布接口权限可能受限，不要假设可以全自动群发。

## 引用来源

- 来源仓库： [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)
- 原始条目： [usecases/cn-wechat-mp-automation.md](https://github.com/AlexAnys/awesome-openclaw-usecases-zh/blob/main/usecases/cn-wechat-mp-automation.md)
- 相关项目： [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill)

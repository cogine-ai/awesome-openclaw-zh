# 贡献指南

欢迎你把真实可用的 OpenClaw 用法补充进来。

## 投稿标准（简单版）

- 提供一手来源支持的能力，或明确标记为原创实验；只有实际跑通才标记为实测
- 非技术用户看得懂
- 提供可直接复制的提示词
- 明确写清楚“能干什么”
- 给出最小输入、预期产物和可检查的成功标准

## 提交流程

### 不会提交 PR？

直接[分享一个跑通的案例](https://github.com/cogine-ai/awesome-openclaw-zh/issues/new/choose)，或报告失效的步骤。提供脱敏结果、版本与来源即可，维护者可以帮助整理。

### 提交文档

1. 复制 [usecases/TEMPLATE.md](./usecases/TEMPLATE.md)
2. 放到对应分类目录（`usecases/*`）
3. 在 [resources/usecases-index.json](./resources/usecases-index.json) 增加条目（标题、描述、分类、本地路径、来源）
4. 执行 `python3 scripts/generate-index.py`，自动更新 Markdown 索引与 README 数量
5. 执行 `python3 scripts/generate-index.py --check`，确认没有漏索引、重复路径或错误分类
6. 发起 PR

## 来源与验证状态

- 上游案例：链接作者的原始展示、文档或仓库，描述其真实支持的能力。
- 文档组合：明确说明这是基于官方工具的工作流设计，不冒充作者实战。
- 原创实验：写清楚自己的组合思路、输入、预期产物和可检查的成功标准。
- 实测：只有实际跑通后才使用此标签，并记录版本、日期、平台和产物。提示词审阅、链接核对与网站构建通过分别说明。
- 新文章 frontmatter 使用 `published` / `updated` 日期，供网站发现最新内容；日期不代表实测通过。

## 命名建议

- 文件名统一英文短横线：`xxx-xxx.md`
- 尽量用动作导向命名：`daily-brief`、`inbox-cleanup`、`meeting-notes`

## 不建议内容

- 纯广告内容
- 无法复现的截图贴
- 明显违规或高风险自动化（如未授权数据抓取）

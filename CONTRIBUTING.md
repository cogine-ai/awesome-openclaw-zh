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

## 案例写法与来源

- 正文以任务、输入、工具、步骤和产物为主；描述现有文件时直接使用“设计图”“示例数据”“脚本”“视频”等准确名称。
- 给出来源链接和必要工具版本。只有实际跑通后才使用“实测”等结论，不把工具文档中的能力写成自己的运行成果。
- 运行日志、检查过程与维护记录放在 `docs/research/`，不在案例、提示词、预览和卡片里重复“未验证”“本轮未执行”等审计说明。
- 账号、费用、软件安装、字体与输入格式等影响操作的条件，直接写进对应步骤；避免“未知／未记录”占位和泛泛免责声明。
- 示例数据说明一次即可；不要在每个段落、标签和产物里重复标注。
- 新文章 frontmatter 使用 `published` / `updated` 日期，供网站发现最新内容。

## 命名建议

- 文件名统一英文短横线：`xxx-xxx.md`
- 尽量用动作导向命名：`daily-brief`、`inbox-cleanup`、`meeting-notes`

## 不建议内容

- 纯广告内容
- 无法复现的截图贴
- 明显违规或高风险自动化（如未授权数据抓取）

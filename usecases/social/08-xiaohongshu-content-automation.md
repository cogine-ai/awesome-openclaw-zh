# 小红书内容自动化

> 让 OpenClaw 辅助完成小红书选题、文案、封面和排期发布。

## 这个案例能帮你做什么

- 根据热点和账号定位生成小红书标题、正文、标签和封面建议。
- 用浏览器自动化流程辅助登录、排期和发布，减少重复操作。
- 追踪笔记表现，把高赞主题和文案风格沉淀为后续创作参考。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | [`XiaohongshuSkills`](https://github.com/white0dew/XiaohongshuSkills) | 小红书内容生成、登录与发布自动化 | 社区项目 |
| 外部 | Chrome 浏览器 | 账号登录和页面自动化 | 本地运行环境 |
| 外部 | Python 3.10+ | 运行自动化脚本依赖 | 本地运行环境 |

## 快速体验版（先跑一轮）

```text
你是我的小红书内容助理。
请围绕「居家收纳」生成一篇小红书图文笔记草稿：
1. 给 5 个标题
2. 写正文，不超过 600 字
3. 给 8 个标签
4. 给封面图构图建议
本轮只生成内容，不登录、不发布。
```

## 稳定自动版（可长期运行）

### 1) 安装社区技能

```bash
git clone https://github.com/white0dew/XiaohongshuSkills.git
cd XiaohongshuSkills
pip install -r requirements.txt
```

首次使用建议只做登录验证：

```bash
python scripts/cdp_publish.py login
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的小红书运营助手，请执行「小红书内容自动化」流程。

执行步骤：
1. 根据账号定位和最近表现，挑 3 个选题
2. 让我确认后生成标题、正文、标签和封面建议
3. 如果需要发布，先确认发布时间、账号和内容最终版
4. 通过 XiaohongshuSkills 执行发布或排期
5. 发布后记录 URL、发布时间和后续要追踪的数据
```

## 成功标准

- [ ] 能生成符合小红书语境的标题、正文和标签。
- [ ] 自动发布前会先确认账号、内容和发布时间。
- [ ] 发布结果能被记录，方便后续复盘。

## 风险与边界

- 小红书对自动化登录和发布有风控，建议先用测试账号验证。
- 不建议批量灌水式发布，容易影响账号权重。
- RPA 浏览器自动化不是官方 API，平台页面改版后可能需要调整脚本。

## 引用来源

- 来源仓库： [AlexAnys/awesome-openclaw-usecases-zh](https://github.com/AlexAnys/awesome-openclaw-usecases-zh)
- 原始条目： [usecases/cn-xiaohongshu-automation.md](https://github.com/AlexAnys/awesome-openclaw-usecases-zh/blob/main/usecases/cn-xiaohongshu-automation.md)
- 相关项目： [white0dew/XiaohongshuSkills](https://github.com/white0dew/XiaohongshuSkills)

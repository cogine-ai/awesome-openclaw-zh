# 六个新玩法：分发素材草稿

尚未对外发布或联系上游作者。使用前确认两份PR已合并、正式网站专题/成果/ZIP可打开，并核对目标渠道是否已有相同内容。以下是可直接调整的正文，不包含虚构增长数据。

## 社区首发

标题：给龙虾找点新玩法：桌面教学卡、文案匿名擂台、本地决策小游戏

我们维护的OPCBoost中文案例库又补了六个玩法。这次先打开成果，再决定是否动手：

- 让桌面教学卡分三步带你选路线，不把勾选当成已运行。
- 用同一份Brief做三句匿名文案，先评分再看写法。
- 看本地小模型如何排序动作，再检查路径规划与保护规则的作用。
- 把产品介绍拆成26秒口播计划，先审脚本和素材缺口，再考虑生成视频。
- 从B站公开评论检查选题证据；样本不足时明确停止推断。
- 准备共享记忆纠正与接棒实验，服务尚未跑通的部分也公开写明。

每个案例带输入、固定来源、复现入口与验证范围。九份ZIP还包含原有经验卡、手绘仓库战报和喜剧文字分镜；没有把预置演练写成模型实测，也没有把文字看板当视频。

专题：[先看六个新玩法](https://www.opcboost.com/resources/07-new-playbooks-lab/?utm_source=developer-community&utm_medium=post&utm_campaign=playbooks-20261027)

仓库：[awesome-openclaw-zh](https://github.com/cogine-ai/awesome-openclaw-zh)

你更想复刻哪一个？欢迎分享实际输入和成果。OPCBoost · by Cogine。

## 两条适合单独发的短稿

### 桌面教学卡 × 经验卡

教程一定要一次读完吗？我们用三张桌面教学卡，把“看成果、选路线、查条件”拆开；卡片输入可下载，真实CLI解析已检查。桌面启动成功，真人回答回传仍待验收；网页预览不会冒充桌面截图。

[看公开输入与教程](https://www.opcboost.com/usecases/tools/interactive-desktop-coach/?utm_source=desktop-coach&utm_medium=social&utm_campaign=playbooks-20261027)

配图可用：`assets/examples/interactive-desktop-coach/preview.svg`，保留“输入派生、非截图”的说明。

### 文案匿名擂台

如果先不看作者，你会选哪句开场白？我们把同一份事实写成三种开场方式，做成可以先评分再揭晓的离线页面。三句是预置演练，目的是体验固定评分表；原生Agent盲测需要另一套真实运行条件，没有拿演练做模型榜单。

[试玩文案匿名评分](https://www.opcboost.com/usecases/creative/blind-agent-copy-arena/?utm_source=copy-arena&utm_medium=social&utm_campaign=playbooks-20261027)

配图可用：`assets/examples/blind-agent-copy-arena/preview.svg`，保留预置候选和未原生执行的标记。

## 演示顺序与归因

1. 首屏展示一个实际成果，点击教程起步卡与ZIP；不要从206/212条数量开始讲。
2. 试玩一次文案评分，解释原始输入与验证范围，再展示一个有真实运行记录的案例。
3. 回到专题，邀请读者复刻一个小结果、提交版本或Star收藏；保持上游署名。
4. 每个渠道使用固定来源参数。先观察来源访问、成果打开、下载点击、仓库出站与真实跑通反馈的绝对数量。

`artifact_open`、`download`只表示点击意向；仓库出站不等于Star，Cogine出站不等于产品激活。此次没有新的站内分析后台数据，不能宣称改版已提高转化或带来增长。发布后使用实际数据决定下一篇，不在小样本上宣称A/B显著。

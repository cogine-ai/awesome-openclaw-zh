---
title: "帽子连纸袋一起跑：15秒无伤害喜剧追逐"
description: "用固定站位、道具受力链和两版Seedance投喂稿，制作实际通过离线检查的15秒喜剧分镜包。"
category: "创意与构建"
published: "2026-10-23"
updated: "2026-10-23"
validation: "M0制作包已离线校验并编译HTML；OpenClaw执行、图片与视频生成未验证"
---

# 帽子连纸袋一起跑：15秒无伤害喜剧追逐

> 两位咖啡店员追一顶软帽，终于用纸袋接住，风却把连帽的纸袋一起吹走。先让动作、站位与道具去向说得通，再决定是否生成视频。

## 先看已经做出的制作包

- [打开15秒离线分镜看板](../../assets/examples/comedy-chase/board.html)：一组、四个时间片，含角色文字档案、动作原文与可选资产出图提示词。
- [导演制作稿](../../assets/examples/comedy-chase/project.md)：故事、空间坐标系、站位路径、11环道具动力链、九字段分镜与连续性台账。
- 独立投喂稿：[Seedance 2.5](../../assets/examples/comedy-chase/seedance-2.5.txt)、[Seedance 2.0](../../assets/examples/comedy-chase/seedance-2.0.txt)。只选择一版，不把两版拼接成30秒。
- [六格预演故事板提示词](../../assets/examples/comedy-chase/帽子比人跑得快-预演故事板.md)：给人检查空间与道具关系，尚未出图。
- [复现脚本](../../assets/examples/comedy-chase/reproduce.py)：实际运行固定上游的检查器并重新编译看板。

**看板是已经编译的HTML制作文件，不是已生成的视频。** 本包采用上游允许的 **M0纯文字模式**：没有参考图，没有虚构图号，也没有宣称人物图、分镜图或成片已经核验。

## 来源与验证说明

| 项目 | 范围 |
|---|---|
| 内容类型 | 原创实验；借用上游动作设计、调度、文本检查与看板工具 |
| 固定来源 | 漫剧老李 V7.4.26，提交 `6f16955c57053d77ea0ffbdbbf3a7985a3e0080a` |
| 来源日期 | 该提交为2026-10-21；本页2026-10-23核查 |
| 使用规则 | `sd-real-engine` 的R1动作动力、空间/镜头方法；M0素材形态；P4.5预演附件 |
| 已完成 | 两版文本检查、两版六道闸门、六格预演附件检查、HTML编译与15秒/4时间片断言 |
| 尚未完成 | 未在OpenClaw内生成本包；未生成图片、视频或配音，未验证成片运动与模型费用 |

这次与[旧短剧看板案例](https://github.com/cogine-ai/awesome-openclaw-zh/blob/506f4291003e0ea3468d894b1fccb950f7d3e0b8/usecases/creative/short-drama-consistent-storyboard-board.md)的区别是：从固定角色与连续镜头，推进到**追逐路径、手掌接触、软帽入袋、风推动纸袋**的动作因果检查。故事、人物与道具均为新写，未使用旧红伞故事。

## 最小故事与固定条件

```text
片名：帽子比人跑得快。
人物：阿禾，28岁，矮个短卷发，蓝色短袖围裙制服；
      小满，30岁，瘦高短直发，绿色围裙。
场景：2026年现代咖啡店空院，干燥平地；北墙、东门、长凳固定。
道具：一顶黄色棉布软帽、一个棕色宽口轻纸袋。
风向：始终从东向西。摄影机：始终在南侧。
故事：风吹帽→阿禾捞空→小满用袋接帽→松手后袋连帽滑走。
时长：15秒，4/3/5/3秒四个连续时间片；16:9；原创明亮三维喜剧。
素材：M0纯文字。交付：导演稿、两版文本、预演提示词、HTML看板。
不生成图片或视频，不发布，不加入摔倒、撞人或道路追车。
```

四个“镜头”是上游解析器使用的时间片标签，**不代表视频模型已经实现四次硬切**。本包要求连续运镜与连续运动；若改成真正剪辑切镜，需要重新拆分生成段与校验。

## 前置条件与成本

| 要做什么 | 条件 |
|---|---|
| 浏览现有看板 | 浏览器即可；CSS与脚本内嵌，无地图服务或模型账号 |
| 重跑离线制作检查 | Python 3.10+、Git；首次获取固定上游需要网络 |
| 在OpenClaw改编 | 已可用的文本模型、文件读写/运行脚本能力；按作者说明部署总控与子技能 |
| 真正生成视频 | 自己的平台确实提供所选Seedance版本、对应时长/音频能力及额度 |

离线检查不调用模型或媒体API；不据此承诺视频免费。上游把多技能套装按13个同级目录部署，入口为 `short-drama-director`，`sd-real-engine` 是子技能；本页没有把子技能伪装成独立的一键出片工具。

## 先复现已经交付的结果

在本仓库根目录运行：

```bash
python3 assets/examples/comedy-chase/reproduce.py
```

脚本临时克隆上游、校验固定SHA，依次执行 `validate_prompt.py`、`gate_check.py`、`check_p45.py`、`build_board_lite.py`，完成后清理临时克隆。默认只更新本包的 `board.html`，不读取OpenClaw配置、密钥或云账号。

如果已经有该SHA的未修改上游副本，可省去下载；把路径替换为自己的真实路径：

```bash
python3 assets/examples/comedy-chase/reproduce.py --upstream-dir /path/to/manju-laoli-skill
```

需要把编译结果写到其他位置，可加 `--output-dir /path/to/output`。工具输出直接留在终端，不额外生成检查报告、日志或截图。

## 本次实际检查结果

| 检查 | 结果 |
|---|---|
| 2.5文本结构、版本、画幅、动作与风格检查 | 15秒、4时间片，0 FAIL，保留2 WARN |
| 2.0同范围检查 | 15秒、4时间片，0 FAIL，保留2 WARN；声音改为文字描述 |
| 两版六道闸门 | 各1个投喂单元，M0、引用图号为空，均0 FAIL / 0 WARN |
| 六格预演提示词 | 1段、6格，0 FAIL / 0 WARN |
| HTML看板编译 | 1组、4时间片、5项文字资产、5条可选资产提示词；15秒、0 WARN |

两版都显式开启 `--combat on --plugin real --c23 on`，没有修改或关闭上游检查器。文本文件以 `--delivery feed-only --contract` 核查其承诺的投喂范围，不宣称上游完整剧集生产契约全部通过。

**保留的两项告警及处理：**

- `C21b`：缺少格斗实体接触。本故事是儿童向无伤害追物；有掌心与软帽的道具接触，没有拳脚命中或兵器交击。按上游R1儿童向范围作人工放行，不为消除告警硬加撞人动作。
- `C22c`：每个时间片不具备“起、爆、顿、收”的打击节拍。本故事采用追赶、捞空、接帽、追袋的整段节拍；不添加命中顿帧，尤其不把2.5顿帧语法带进2.0。告警完整保留在终端。

复现脚本会拒绝新增的未审阅告警，也会拒绝“编译退出成功、实际却丢到0秒”的空看板。这里的人工放行只说明文字方案合理，不能证明视频模型理解了动作。

## 再交给OpenClaw做一次小改编

先给Agent提供整个 `assets/examples/comedy-chase/` 目录，以及固定版本的上游技能目录，再发送：

```text
请读取 comedy-chase 的 project.md、两版原稿和预演附件。
这是M0文字制作包，所有图像和视频都未生成；不要虚构图号或成片。
先复述阿禾、小满、帽子与纸袋在四个时间片的起点和落点。
保留15秒、16:9、单院落、东来风、南侧摄影机和现有道具数量。
只改最后一句吐槽，最多六个中文字，其他动作不重写。
把同一句台词同步改到两版原稿与制作稿，保留各自版本语法；制作稿仍展示2.5副本。
运行复现脚本，再明确选择2.5或2.0的一版投喂，不把两版拼接。
输出改动位置、实际检查结果与真实HTML路径；不要调用媒体或发布服务。
```

这段是待实际OpenClaw执行的复用入口，不是本次已经跑过的Agent轨迹。若模型权限、文件或上游工具不可用，应报告失败阶段，不用聊天中的“已检查”替代真实脚本结果。

## 人工验收与常见卡点

- **帽子回到头上：**制作稿要求软帽离头后先在地上、再入袋；图像/视频生成后必须逐帧检查，文字检查器无法保证。
- **袋子突然出现：**第一个时间片就有小满右手持折扁袋，随后双手展开；不能直接从地上变出袋。
- **人物交换通道：**阿禾走内侧，小满走外侧；摄影机不跨到北侧，两个路径错开半步。
- **看板显示0秒或少镜：**先查项目中的围栏与标题。固定编译器会把围栏内的Markdown标题也当分段；本包的看板副本只去掉包装标题，脚本会核对其余投喂原文一致。
- **准备上传参考图：**这是从M0切换到其他素材模式的变更，须补真实素材、接线单与对应检查；不能把可选出图文字当成已存在的图片。
- **平台不支持15秒或该版本：**停止投喂，按实际支持重排时间片并重跑检查，不只替换模型名字。

## 引用来源与许可

- [固定版本：套装说明与部署范围](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/README.md)
- [sd-real-engine：R1范围与儿童向例外](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/sd-real-engine/SKILL.md)
- [11环动作动力链](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/sd-real-engine/references/kinetic-chain-11.md)
- [M0 / M1 / M2素材形态](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/short-drama-director/references/asset-delivery-modes.md)
- [P4.5预演附件与验收边界](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/sd-storyboard-engine/references/p45-previs-storyboard.md)
- [固定版本的文本检查器](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/short-drama-director/scripts/validate_prompt.py)
- [固定版本的HTML编译器](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/6f16955c57053d77ea0ffbdbbf3a7985a3e0080a/short-drama-director/scripts/build_board_lite.py)

故事与复现胶水代码为本仓库原创；看板由上游MIT许可编译器生成，其许可随包保留为 [LICENSE.upstream.txt](../../assets/examples/comedy-chase/LICENSE.upstream.txt)。

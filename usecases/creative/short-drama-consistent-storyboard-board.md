---
title: "龙虾短剧导演：一致角色与离线分镜看板"
description: "把一个小故事整理为角色资产板、连续镜头提示词和可打开的 HTML 看板，减少短剧制作中的换脸与穿帮。"
category: "创意与构建"
published: "2026-10-11"
updated: "2026-10-11"
validation: "原创样例离线检查与看板渲染通过；图像与视频未生成"
---

# 龙虾短剧导演：一致角色与离线分镜看板

> 先把角色、道具和镜头衔接固定下来，让 OpenClaw 交付能检查的分镜包，再进入视频生成。

## 有趣在哪里

同一个人物前后不像、上一镜拿着道具下一镜消失，是 AI 短剧里很容易被看出的失误。[漫剧老李](https://github.com/lixiaoxiao9888-create/manju-laoli-skill)把资产、空间关系、分镜和提示词校验整理成一套 Skill，并提供单文件 HTML 看板。

本案例先做一个 16 秒的原创小故事，交付「固定资产 → 两段连续镜头 → 看板」；这个成果可以直接展示，也可以交给自己的视频模型继续制作。

**来源状态：**项目创建于 2026-08-15；2026-10-11 GitHub API 快照为 1,137 Stars、118 Forks，创建约 57 天累计千级 Star。未取得最近七天净增长数据。本轮脚本固定在提交 `edebc10e4b2aed5e259deff673d58d2080fe5c29`：作者 README 顶部仍标 V6.9.8，SKILL.md 已声明 V6.9.9／2026-10-02 修订，两个标记不完全同步。

**验证状态：**本仓库原创样例已通过包检查、两段分别的提示词检查和离线看板编译，并在浏览器确认时间轴、镜头卡、资产表与按段筛选。未安装到 OpenClaw，未出图，未调用视频模型；作者提及的实拍复盘属于作者证据。

**先看成果：**[打开原创 16 秒分镜看板](../../assets/examples/short-drama-board.html)，或下载 [项目原稿](../../assets/examples/short-drama-project.md)、[段 1 投喂稿](../../assets/examples/short-drama-segment-1.txt)、[段 2 投喂稿](../../assets/examples/short-drama-segment-2.txt)。图像资产全部标为待生成，图号仅是计划槽位。[完整离线验证记录](../../docs/research/short-drama-offline-validation-2026-10-11.md)保留检查结果与失败输入。

## 准备条件

| 项目 | 用途 |
|---|---|
| 已能运行的 OpenClaw 与文本模型 | 阅读 Skill、拆故事、保存项目 Markdown |
| `short-drama-director/` 完整目录 | 包含规则、参考文件与脚本；只复制 SKILL.md 不够 |
| Python 3 | 运行包检查、提示词校验与看板编译器 |
| 视频服务账号 | 后续可选；本轮 HTML 看板无需视频服务 |

作者当前支持 Seedance 2.5／2.0 和 MiniMax H3 的提示格式；可灵在 V6.8 起属于历史兼容。Skill 主要交付资产方案、分镜与模型提示词，**不承诺自动渲染出最终视频**。

## 安装与自检

```bash
git clone https://github.com/lixiaoxiao9888-create/manju-laoli-skill.git
cd manju-laoli-skill
openclaw skills install ./short-drama-director --as short-drama-director
python3 short-drama-director/scripts/check_package.py
openclaw skills check
```

本地目录安装方式同时见于作者 README 与 [OpenClaw Skills CLI](https://docs.openclaw.ai/cli/skills)。使用多个 Agent 时确认安装目标是本次会话的 Agent；安装后开启新会话，确保读到新技能。

## 最小故事：深夜失物招领

以下是本案例的原创故事输入，不是作者已拍摄的成片。

```text
片名：深夜失物招领
故事：便利店店员发现一把湿漉漉的红伞，以为客人遗忘了。
      店员追到门口，才发现客人故意把伞留下，给还没下班的她。
人物：店员小林，短发、黄色围裙；客人阿雨，蓝色雨衣。
场景：同一家便利店门口；暖色室内灯、门外夜雨。
道具：一把红伞，前后只出现这一把；不开新场景。
目标：16 秒，两段各 8 秒；无对白，靠动作讲清楚。
画幅：9:16。模型：Seedance 2.5。
段落衔接：末态衔接；第二段承接第一段结束时的站位和持伞手。
本轮：只做资产与分镜文档、提示词和离线看板，不生成视频。
```

把故事与下面的要求一起发给 OpenClaw：

```text
请读取 short-drama-director 的 SKILL.md 与所需参考文件，
为上面的《深夜失物招领》建立 examples/night-umbrella/project.md。

先固定模型 2.5、9:16 画幅、末态衔接，再创建角色四视图资产方案、
场景与红伞资产；给每个资产独立编码，两个镜头复用相同资产。
角色图尚未生成时，把参考图状态明确写为待生成，不伪造图片路径。
人物站位、镜头方向、拿伞的手和段末状态必须前后连续。

项目文档包含创作基准、剧本、视听圣经、资产清单、资产出图提示词、
两段完整的模型投喂提示词及逐镜时间码。按看板文档的输入契约组织。
每段从 00:00 开始，两段合计 16 秒；不要靠慢放凑时长。
将两段实际投喂文本分别导出为 segment-1.txt、segment-2.txt，
逐段调用 validate_prompt.py 校验，失败则修稿后复查。
调用 build_board_lite.py，输出 examples/night-umbrella/board.html。
返回文件路径、校验结果和仍缺的素材；不要调用生图、视频或发布服务。
```

这里约定的 `examples/night-umbrella/` 由 Agent 创建；它不是上游已经提供的示范工程。

## 可单独运行的交付检查

Agent 写好项目后，在仓库根目录执行：

```bash
python3 short-drama-director/scripts/validate_prompt.py examples/night-umbrella/segment-1.txt --model 2.5
python3 short-drama-director/scripts/validate_prompt.py examples/night-umbrella/segment-2.txt --model 2.5
python3 short-drama-director/scripts/build_board_lite.py examples/night-umbrella/project.md --out examples/night-umbrella/board.html
```

`validate_prompt.py` 按单段处理时间码和字符预算。本轮实测：把完整项目交给它，会把第二段从零开始误判为时间重叠，并触发镜数与字符预算错误；不要把两段拼在一个检查文件中。只把每段实际投喂文本分别交给它，原始项目仍保留完整内容，并记录实际检查文件。

本轮结果为：包检查通过；段 1、段 2 各 8 秒／2 镜头，均通过且无 WARN；看板编译识别 2 段／4 镜头、5 项资产、5 组资产出图提示词，总时长 16 秒，0 WARN。浏览器中的按段筛选也已核对。看板统计和提示词通过属于离线验证，不代表模型渲染或实际成片通过。

看板编译器默认输出 `<项目名>_分镜看板.html`，`--out` 可以指定文件。它会容忍缺字段并输出 WARN，**生成 HTML 不等于分镜质量检查通过**。

双击 `board.html`，核对：

| 检查点 | 应看到什么 |
|---|---|
| 顶部统计 | 已锁定模型与画幅，两段总时长 16 秒 |
| 时间轴与镜头卡 | 逐段顺序完整，每段内部时间码连续 |
| 资产表 | 两位角色与一把红伞的固定编码、复用关系 |
| 两类提示词 | 资产出图与视频投喂文本都在同一看板 |
| 告警 | 每项 WARN 有解释；缺素材如实标记 |

HTML 看板是只读产物。修改 `project.md` 后重新编译，避免原稿与看板各改一套。

## 继续做成视频

先生成并确认角色、场景和道具的参考图，再把同一组参考图送入已选模型。两段分别生成，核对段末与下一段首镜之后合并。换模型时重新适配提示格式并校验，不能只替换模型名字。

本轮即使没有视频账号，也应该交付可读的故事、资产方案与真实可打开的看板。生成最终成片后，再记录使用的模型、日期、成本与失败次数；未完成之前不标为实测通过。

## 常见卡点

- **角色或伞不一致：**先修资产编号和参考图复用，减掉不必要的机位；别只在提示词里重复「保持一致」。
- **质检 FAIL：**按具体规则修正后再次运行，保留失败记录与实际检查文件。
- **看板能打开但没有镜头：**检查章节、段标题与时间码，查看 WARN；不要把空看板当成成功。
- **未出图却写了图片引用：**改为待生成状态；资产方案和实际参考图必须区分。
- **视频平台不支持选择的模型：**停留在看板交付，换为自己可用的受支持模型后重新校验。

## 来源

- [本轮固定提交的 README（顶部 V6.9.8）](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/edebc10e4b2aed5e259deff673d58d2080fe5c29/README.md)
- [本轮总控 Skill（V6.9.9）](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/edebc10e4b2aed5e259deff673d58d2080fe5c29/short-drama-director/SKILL.md)
- [离线看板的输入契约与输出规则](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/edebc10e4b2aed5e259deff673d58d2080fe5c29/short-drama-director/references/storyboard-board-lite.md)
- [本轮提示词校验脚本](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/blob/edebc10e4b2aed5e259deff673d58d2080fe5c29/short-drama-director/scripts/validate_prompt.py)

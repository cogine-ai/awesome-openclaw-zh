# 原创短剧样例离线验证 · 2026-10-11

本轮只运行本地 Python 脚本和浏览器预览，无额外依赖安装、模型调用、图像／视频素材下载或发布。样例《深夜失物招领》由本仓库原创，全部角色与场景虚构。

## 固定来源

- 仓库：[manju-laoli-skill](https://github.com/lixiaoxiao9888-create/manju-laoli-skill)
- 本轮提交：[`edebc10e4b2aed5e259deff673d58d2080fe5c29`](https://github.com/lixiaoxiao9888-create/manju-laoli-skill/tree/edebc10e4b2aed5e259deff673d58d2080fe5c29)
- README 顶部标记 V6.9.8，SKILL.md 标记 V6.9.9／2026-10-02；包检查只核对 V6.9 家族，不能证明这两个细版本一致。
- 环境：Python 3；作者三个脚本均使用标准库。上游克隆在临时目录，未安装到 OpenClaw。
- HTML 模板来自作者 MIT 许可编译器；完整版权与 MIT 许可已嵌入看板头部注释。未使用任何第三方图片、视频、真人肖像或品牌素材。

## 产物

- [原创项目 Markdown](../../assets/examples/short-drama-project.md)：故事、基准、角色与场景规则、5 项待生成资产、5 组出图提示词、两段视频提示词。
- [段 1 投喂稿](../../assets/examples/short-drama-segment-1.txt)、[段 2 投喂稿](../../assets/examples/short-drama-segment-2.txt)：从项目围栏原文提取，每段独立时间码。
- [单文件 HTML 看板](../../assets/examples/short-drama-board.html)：CSS／JS 全内嵌，无外部脚本。

## 三项检查分别记录

| 检查 | 退出码 | 实际结果 |
|---|---|---|
| `check_package.py` | 0 | 全部检查通过，41 份 references 完整，脚本 C／H 系列 self-test 通过 |
| `validate_prompt.py segment-1.txt --model 2.5` | 0 | 8 秒、2 镜头、685 字符；PASSED；0 WARN |
| `validate_prompt.py segment-2.txt --model 2.5` | 0 | 8 秒、2 镜头、764 字符；PASSED；0 WARN |
| `build_board_lite.py project.md --out board.html` | 0 | 2 段、4 镜头、5 项资产、5 组出图提示词；16 秒；0 WARN |

浏览器预览确认：标题为「深夜失物招领」，顶部显示模型 2.5／9:16／2 段／4 镜／16 秒；时间轴偏移为段 1 从 0 秒起、段 2 从 8 秒起。资产表显示两位角色、场景、红伞、段缝站位参考及复用段，素材状态均为待生成。点击段 2 筛选后，只显示段 2 的泳道、两张镜头卡和投喂原文。

## 保留的失败输入

曾运行 `validate_prompt.py short-drama-project.md --model 2.5`，退出码为 1：

```text
[+] 时长8.0s 镜头4 字符4686 | model=2.5 mode=new
[!] WARN: C3 第105->122行 重叠(8.0 vs 0.0)
[!] WARN: C19c 首镜主体优先：镜1第一个分句以环境开头、人物名/身体局部出现在其后
[-] FAIL: C2 镜头数 4 > 段长÷3s 上限 3
[-] FAIL: C4 共 4686 字符 > 预算 4500
[-] 2 error(s)
```

该校验器把整个输入当成一个单段：它取最大时间码 8 秒，将两段从零开始的时间码误判为重叠；还将项目说明、资产出图词计入投喂预算与首镜规则。因此实际投喂稿改为两个独立检查文件，完整项目用于看板编译。未修改上游校验器，也没有隐藏这次失败。

## 最小复现

在本仓库根目录执行；`manju_script_dir` 替换为自己的上游克隆位置。固定提交避免上游变化影响结果：

```bash
git clone https://github.com/lixiaoxiao9888-create/manju-laoli-skill.git /tmp/manju-offline-example
git -C /tmp/manju-offline-example checkout edebc10e4b2aed5e259deff673d58d2080fe5c29
manju_script_dir="/tmp/manju-offline-example/short-drama-director/scripts"
python3 "$manju_script_dir/check_package.py"
python3 "$manju_script_dir/validate_prompt.py" assets/examples/short-drama-segment-1.txt --model 2.5
python3 "$manju_script_dir/validate_prompt.py" assets/examples/short-drama-segment-2.txt --model 2.5
python3 "$manju_script_dir/build_board_lite.py" assets/examples/short-drama-project.md --out /tmp/short-drama-board.html
```

重新编译得到的模板也来自 MIT 软件；分发时保留作者版权与许可。仓库现成 HTML 头部已包含许可，重编译文件不会自动继承额外的许可注释。

## 实际边界

16 秒是文字分镜计划。所有 @图片编号仅是未来图像的计划槽位，当前没有图像文件。没有进行视频渲染、成片质量、模型真实支持、角色一致性或成本验证。上游看板的「0 ERROR」表示编译器轻量告警层；不能替代逐段校验或最终成片检查。生成器在基准与视听圣经区保留了 Markdown 表格分隔行作为文字，属于当前模板展示细节，本轮没有修改生成器。

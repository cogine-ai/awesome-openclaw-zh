# 六案例专题补齐与验证记录

日期：2026-10-30（Asia/Taipei）。本记录承接[展示审查](./2026-10-30-autumn-makers-site-review.md)。

> 后续按用户要求，公开案例与网站已删除重复审计说明，执行记录集中至 `docs/research/autumn-makers/`。本页保留此前的补齐过程；最新清理见[内容精简记录](./2026-10-30-autumn-makers-copy-cleanup.md)。

## 本轮交付

六篇案例补齐独立输入、具体工具路线、针对性排错、材料预览和六份ZIP。专题采用同一份collectionCasePaths配置，在GitHub保留列表导航，在网站展示响应式卡片。目录维持218条。

| 案例 | 已有材料／实际运行 | 尚未验证 |
|---|---|---|
| 3D工作台 | 原创SVG设计稿、scene.json、Blender4.5脚本；JSON/XML/语法检查 | Blender实际运行、.blend、渲染、旋转视频 |
| 发布短片 | Remotion4.0.539真实生成横版960×540和竖版540×960，各30秒H.264 MP4；修改输入后静帧；锁文件与渲染脚本 | OpenClaw会话、配音、对外发布 |
| 学习包 | 原创Python生成三份资料、10题、12卡、依据定位和交互页 | NotebookLM服务、音频、OpenClaw |
| 模拟大会 | 原创Python生成五角色、两情境、十条明确手写预置发言及切换页 | MiroFish、模型讨论、真实用户研究、OpenClaw |
| 播客地图 | 三段虚构访谈、四条有引用的关系、筛选与定位页 | 真实节目获取、OpenCLI、模型、OpenClaw |
| 打印物料 | 三份SVG及三页PDF；嵌入OFL NotoSansSC子集；缺字预检与替代字体入口 | 纸样打印、Inkscape、OpenClaw |

五篇script-reproduced只对应各页列明的脚本范围；3D保留experimental与reviewedAt。没有将离线生成写成上游服务或Agent通过。

## 网站补齐

- 首页、更新页、资料组、内容专题加入新一期入口；更新页传递showcase状态。
- 专题1—12个安全案例路径解析、重复与缺失检查；桌面双列、手机单列，有状态、范围、条件、预览与下载入口。
- 实验方案可记录reviewedAt而不虚构testedAt；未知平台可明确记录，脚本／Agent复现仍需实际日期。
- 全部材料预览使用中性措辞；恢复顶部复制体验入口，修摘要误打渠道标签，收窄模拟讨论相关推荐。
- prompt_open仅识别本期六份明确提示词路径，许可TXT不误计；ZIP下载与打开提示词不混用。
- 本地dirty预览不声称固定提交来源；研究文档仍使用明确的动态仓库链接，干净版本保持固定commit链接。
- typecheck排除作为静态下载文件的vendor/public样例TSX，避免把独立Remotion工程当成网站依赖。
- OG字体更新为783个实际所需及转义检查字形，202424bytes，覆盖验证通过；原先请求无关ASCII集合会使当前上游回退全字体，现只请求实际渲染字符和转义检查字符，保留1MB预算及完整性校验。

## 已执行的检查

- 内容：218条索引与生成文件检查；64项unittest通过；六篇相对链接、代码围栏和Python语法检查。
- 离线材料：学习／播客／大会重建与--check通过；引用和结构检查，生成JS语法检查；这些检查不能证明答案语义或上游服务正确。
- ZIP：六份显式文件清单构建和--check；固定ZIP元数据与文件哈希；排除未列文件及拒绝路径穿越/符号链接的测试。包不声称对应某个Git提交，字节由BUNDLE-SOURCE.json标识。
- 视频：ffprobe两种画幅时长均30秒；抽帧和修改输入静帧检查；浏览器两视频readyState=4、无error，横版实际播放进度前进。
- PDF：三页尺寸为210×148、210×297、297×210毫米；Poppler渲染检查；pdffonts中文emb/sub/uni均yes；脚本重复输出PDF字节一致。
- 网站：完整bun run check通过，218条用例/241篇Markdown校验、类型检查、31个测试文件共163项通过、296页构建、Pagefind240页/10个筛选/2个排序。
- 浏览器：测验判分与闪卡翻面，观点筛选与依据跳转，预置讨论A/B切换，顶部复制成功，材料包实际下载与ZIP校验。
- 响应式：专题六张卡片存在；390×844视口下scrollWidth=390，无横向溢出。
- 搜索：正式dist产物上以“微缩”+experimental筛选得到1条3D结果，状态、预览与下载正确。

## 证据与发布状态

网站完整检查日志：`/tmp/opcboost-makers-site-check.log`。

桌面截图：`/Users/kiedis/.codex/visualizations/2026/10/29/01a18847-949d-70b0-b2c1-04a5aa1b08b5/autumn-makers-desktop.jpg`。

卡片截图：`/Users/kiedis/.codex/visualizations/2026/10/29/01a18847-949d-70b0-b2c1-04a5aa1b08b5/autumn-makers-cards.jpg`。

手机截图：`/Users/kiedis/.codex/visualizations/2026/10/29/01a18847-949d-70b0-b2c1-04a5aa1b08b5/autumn-makers-mobile.jpg`。

更改保留在内容与网站两个工作区，尚未git提交、推送、部署或对外发布。网站同步为dirty本地预览；正式发布应提交内容并同步包含内容的版本，然后构建部署。未调用任何付费模型或新增账号服务。

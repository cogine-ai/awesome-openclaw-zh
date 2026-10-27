---
published: 2026-10-27
updated: 2026-10-27
showcase:
  verification: script-reproduced
  verificationNote: "固定Laya 0.4.15与官方英文权重已真实CPU推理；回放区分BFS、模型排序与保护规则。官方MCP仅工具发现/状态检查，非OpenClaw端到端。"
  platforms: [macos, windows, linux, browser]
  account: none
  cost: local-free
  artifactPath: assets/examples/local-decision-snake/index.html
  artifactLabel: 回放每一步模型建议与保护规则
  previewPath: assets/examples/local-decision-snake/preview.svg
  bundlePath: assets/bundles/local-decision-snake-2026-10-27.zip
  testedAt: '2026-10-27'
  testedVersion: 'Laya 0.4.15 / torch 2.14.1 / Python 3.12.10 / CPU'
  beginner: false
---

# 本地决策蛇：把模型建议与保护规则摊开看

> 给Agent配一个本地“反射脑”之前，先看清：哪一步来自规划器，哪一步来自真实模型，哪一步又被保护规则拦了下来。

## 已经做出的成果

[打开可解释的蛇游戏回放](../../assets/examples/local-decision-snake/index.html)。页面可切换真实Laya分支与纯规划器基线，播放、暂停、拖动步骤，并逐步显示四方向概率、模型建议、实际执行及保护规则是否改写建议。

- [scenario.json](../../assets/examples/local-decision-snake/scenario.json)：8×8棋盘、固定种子7、64步预算。
- [run.json](../../assets/examples/local-decision-snake/run.json)：实际状态、特征、问题、概率、耗时与版本记录。
- [reproduce.py](../../assets/examples/local-decision-snake/reproduce.py)：离线重建、显式权重获取、真实推理与官方MCP检查入口。

**浏览器播放的是已记录的真实数据，不是在浏览器中实时运行模型。** 本例与已有“让多个Agent开发游戏”的案例不同：这里研究决策过程，不把生成一份游戏代码当作模型已经玩过游戏。

## 三个角色，分别做了什么

| 组件 | 实际任务 | 不能归给它的能力 |
|---|---|---|
| BFS规划器 | 计算碰撞、尾部可达、空间与靠近食物的特征，先给出路线偏好 | 它已做了重要规划，不能隐去后声称模型独立理解棋盘 |
| Laya英文checkpoint | 对描述过的四个有限方向给出概率与第一选择 | 不生成解释，不做开放问答，不保证概率就是游戏成功率 |
| 保护规则 | 在安全候选中执行概率最高的方向；无安全候选就停止 | 改写必须留下记录，不得把拦截后成绩全归给Laya |

“安全”是本例基于尾部可达与剩余空间的启发式，不是任意局面的长期生存证明。页面同时展示不调用模型的BFS基线；单种子、单次小样本不是公平的模型能力排行榜，也不足以证明模型比基线更好。

## 来源、固定版本与验证范围

Laya固定为 [v0.4.15](https://github.com/NandhaKishorM/laya/tree/v0.4.15)，标签对应提交 `7a77439b0923d6efe00052d50a7f787840bfce98`。使用官方英文模型 [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya/tree/7b928d828b7b0e022f929d9bd2e44165aa270148)，固定模型提交 `7b928d828b7b0e022f929d9bd2e44165aa270148`。

单份权重为 **842,609,210字节**，已核对SHA256 `891102d372688fc2a094dac56a384bc537b87c63f21f9f3dac0be2b7cbc8d86c`。本轮没有下载多语言或typed-decisions副本，没有把缺失权重替换成随机模型。首次完整HTTP流提前结束时大小检查拒绝了它，随后只续传缺失范围并核完整哈希。

路线特征与保护规则参考 [omp-laya-judge的特征辅助Snake](https://github.com/F0Rextasy/omp-laya-judge/blob/1a7c7c06c478ca78f63b67bd702ae2251777136b/demo/snake.py)。本例改为8×8、64步，保留单个move问题，记录前后状态并增加可验证的HTML回放；没有复制作者的分数或把作者演示当成本次结果。

本轮实际使用macOS arm64、Python 3.12.10、torch 2.14.1、transformers 5.21.0、CPU四线程。Laya加载时保留了上游告警：`choice:11+`温度值被限制到0.5。当前实验是四选一，未使用11个以上选项的桶；仍不据此宣称游戏置信度经过校准。告警原文保存在 `run.json` 的runtime字段中。

验证分开记录：**SDK确实执行模型推理；官方MCP确实完成初始化、工具发现与 `laya_status`；没有通过MCP运行游戏推理，也没有在OpenClaw会话中端到端执行。** MCP检查使用懒加载，避免默认预载两份权重。

2026-10-27这次实际记录为：Laya组合分支64步、得分4、保护规则改写0次；纯BFS分支64步、得分11。两者都到步数上限停止，本次没有证明加模型带来收益。模型SDK调用平均约56.51毫秒，仅代表本机这64次调用，不含下载、加载、BFS、MCP或OpenClaw开销。MCP发现10个工具，协议为 `2025-11-25`。这些数字来自随包记录，重新运行后应以新记录为准。

## 先复现已经记录的回放

默认只需Python 3.10+，不安装PyTorch，不联网，不加载权重：

```bash
python3 assets/examples/local-decision-snake/reproduce.py
python3 -m http.server 8765 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8765/assets/examples/local-decision-snake/`。可以在当前分支与BFS基线间切换；按Ctrl+C停止服务器。默认重建会检查数据连续性、合法动作、概率分布、得分和拦截记录，不把基线补成模型结果。

## 可选：真实重新推理

需要Python 3.12、网络、可安装PyTorch的机器，以及模型和运行时所需的数GB磁盘/内存余量；本例没有测量内存峰值。只有查看回放不需要这些条件。以下为macOS/Linux命令，Windows需替换虚拟环境的可执行文件路径。

```bash
uv venv /tmp/snake-lab-venv --python 3.12
UV_CACHE_DIR=/tmp/snake-lab-cache uv pip install --python /tmp/snake-lab-venv/bin/python "laya[mcp] @ git+https://github.com/NandhaKishorM/laya.git@7a77439b0923d6efe00052d50a7f787840bfce98" "torch==2.14.1" "transformers==5.21.0" "mcp==2.3.0"
/tmp/snake-lab-venv/bin/python assets/examples/local-decision-snake/reproduce.py --download-model --model-dir /tmp/snake-lab-checkpoint
HF_HUB_OFFLINE=1 /tmp/snake-lab-venv/bin/python assets/examples/local-decision-snake/reproduce.py --run-model --model-dir /tmp/snake-lab-checkpoint --check-mcp
```

权重获取需要显式参数，固定到一份英文模型；下载采用有限范围请求，发现短流、范围不符或哈希错误就停止。显式重试可接续已校验的完整范围，不自动改模型、镜像、账号或绕过TLS。已有完整且匹配的权重可省去下载步骤。

模型或MCP检查失败时不发布新回放，不用模拟概率补齐。要只检查官方MCP工具，可在已装依赖的虚拟环境中运行 `reproduce.py --check-mcp`；它使用临时HF目录、`LAYA_PRELOAD=0`与离线模式，只检查工具和状态，不下载模型或改任何Agent配置。

本次本地推理未调用付费API或账户；这不代表接入OpenClaw后的文本模型调用免费。不要把模型头没有生成文本Token，等同于整条Agent工作流零成本。

## 可以交给OpenClaw继续的实验

```text
先读取local-decision-snake的scenario、run和reproduce.py。
区分真实SDK推理、仅规划器基线、MCP工具检查和未运行的OpenClaw环节。
先复现已有回放，逐步解释一次模型第一选择与实际执行的差别。
不把规划器或保护规则成绩全部归给Laya，不凭一局给模型排名。
未经明确要求不下载新权重，不安装全局插件，不修改Agent配置。
如果要改实验，只调整一个参数并保留版本、种子、输入和失败结果。
```

这是下一轮实验入口，本轮未在OpenClaw中执行。真正做模型比较需要多种子、相同任务预算、独立的成功标准及失败样本，不能把这个小回放扩大成通用效果结论。

## 许可与一手文档

- [官方MCP能力与配置说明](https://github.com/NandhaKishorM/laya/blob/v0.4.15/README.md#mcp-server-optional)、[固定官方MCP服务源码](https://github.com/NandhaKishorM/laya/blob/v0.4.15/laya/mcp/server.py)。
- Laya代码和官方权重采用Apache-2.0，许可保留于 [LICENSE.laya.txt](../../assets/examples/local-decision-snake/LICENSE.laya.txt)；权重不随本包分发。
- 相邻Snake参考采用MIT，许可保留于 [LICENSE.snake-reference.txt](../../assets/examples/local-decision-snake/LICENSE.snake-reference.txt)。规划特征的适配与本地交付边界见复现脚本注释；页面、数据检查与胶水代码为本仓库新增。

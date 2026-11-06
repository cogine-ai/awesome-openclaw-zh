---
published: 2026-10-27
updated: 2026-10-27
showcase:
  verification: script-reproduced
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

> 给 Agent 配一个本地“反射脑”：用一局蛇游戏，逐步对照模型建议、路线规划和实际动作。

## 已经做出的成果

[打开可解释的蛇游戏回放](../../assets/examples/local-decision-snake/index.html)。页面可切换真实Laya分支与纯规划器基线，播放、暂停、拖动步骤，并逐步显示四方向概率、模型建议、实际执行及保护规则是否改写建议。

- [scenario.json](../../assets/examples/local-decision-snake/scenario.json)：8×8棋盘、固定种子7、64步预算。
- [run.json](../../assets/examples/local-decision-snake/run.json)：实际状态、特征、问题、概率、耗时与版本记录。
- [reproduce.py](../../assets/examples/local-decision-snake/reproduce.py)：离线重建、显式权重获取、真实推理与官方MCP检查入口。

浏览器播放已记录的决策轨迹。想换一个棋盘或种子，可以按下方的本地推理步骤生成新回放。

## 三个角色，分别做了什么

| 组件 | 实际任务 | 回放中看什么 |
|---|---|---|
| BFS规划器 | 计算碰撞、尾部可达、空间与靠近食物的特征，先给出路线偏好 | 棋盘特征与候选方向 |
| Laya英文checkpoint | 对描述过的四个有限方向给出概率与第一选择 | 四方向概率与模型建议 |
| 保护规则 | 在安全候选中执行概率最高的方向；无安全候选就停止 | 实际动作、停止原因与建议改写记录 |

保护规则按尾部可达与剩余空间筛选候选方向。页面同时提供纯 BFS 基线，方便在相同棋盘、种子与步数预算下比较两条决策轨迹。

## 工具与版本

Laya固定为 [v0.4.15](https://github.com/NandhaKishorM/laya/tree/v0.4.15)，标签对应提交 `7a77439b0923d6efe00052d50a7f787840bfce98`。使用官方英文模型 [`convaiinnovations/laya`](https://huggingface.co/convaiinnovations/laya/tree/7b928d828b7b0e022f929d9bd2e44165aa270148)，固定模型提交 `7b928d828b7b0e022f929d9bd2e44165aa270148`。

权重约 843 MB，SHA-256 为 `891102d372688fc2a094dac56a384bc537b87c63f21f9f3dac0be2b7cbc8d86c`。

路线特征与保护规则参考 [omp-laya-judge 的 Snake 示例](https://github.com/F0Rextasy/omp-laya-judge/blob/1a7c7c06c478ca78f63b67bd702ae2251777136b/demo/snake.py)。本例使用 8×8 棋盘和 64 步预算，记录模型建议、实际动作与前后状态。

示例环境：macOS arm64、Python 3.12.10、torch 2.14.1、transformers 5.21.0，CPU 四线程。

随包 2026-10-27 回放中，Laya 组合分支 64 步得分 4，纯 BFS 分支 64 步得分 11；保护规则改写 0 次。可以沿着轨迹比较每一步选择，再修改棋盘、种子或步数预算重跑。

## 先复现已经记录的回放

默认只需Python 3.10+，不安装PyTorch，不联网，不加载权重：

```bash
python3 assets/examples/local-decision-snake/reproduce.py
python3 -m http.server 8765 --bind 127.0.0.1
```

打开 `http://127.0.0.1:8765/assets/examples/local-decision-snake/`。可以在当前分支与 BFS 基线间切换；按 Ctrl+C 停止服务器。默认重建会检查数据连续性、合法动作、概率分布、得分和拦截记录。

## 可选：真实重新推理

需要 Python 3.12、网络、可安装 PyTorch 的机器，并为模型和运行时预留数 GB 磁盘与内存。查看已有回放只需浏览器。以下为 macOS/Linux 命令，Windows 需替换虚拟环境的可执行文件路径。

```bash
uv venv /tmp/snake-lab-venv --python 3.12
UV_CACHE_DIR=/tmp/snake-lab-cache uv pip install --python /tmp/snake-lab-venv/bin/python "laya[mcp] @ git+https://github.com/NandhaKishorM/laya.git@7a77439b0923d6efe00052d50a7f787840bfce98" "torch==2.14.1" "transformers==5.21.0" "mcp==2.3.0"
/tmp/snake-lab-venv/bin/python assets/examples/local-decision-snake/reproduce.py --download-model --model-dir /tmp/snake-lab-checkpoint
HF_HUB_OFFLINE=1 /tmp/snake-lab-venv/bin/python assets/examples/local-decision-snake/reproduce.py --run-model --model-dir /tmp/snake-lab-checkpoint --check-mcp --output-dir /tmp/snake-lab-run-1
```

新回放写入尚不存在的 `/tmp/snake-lab-run-1`，打开其中的 `index.html` 查看。比较参数时，先备份 `scenario.json` 再修改；每轮用 `--run-model` 重跑并换一个输出目录，即可保留前后的场景与轨迹。

`--download-model` 下载上面固定版本的英文模型，并检查文件哈希。已有完整且匹配的权重可省去下载步骤。

要单独检查官方 MCP 工具，在已装依赖的虚拟环境中运行 `reproduce.py --check-mcp`；它使用临时 HF 目录和离线模式，列出工具与服务状态。

本地推理使用下载的权重；接入 OpenClaw 后，文本模型费用按自己的配置计算。

## 可以交给OpenClaw继续的实验

```text
读取 local-decision-snake 的 scenario、run 和 reproduce.py，先重建已有回放。
选一步，解释棋盘特征、模型建议、保护规则和实际动作之间的关系。
对照同一条件下的 BFS 基线，找出两条轨迹从哪一步开始不同。
再建议一个值得调整的参数，说明预期变化。
本轮使用已有数据；重新下载权重或修改 Agent 配置前先与我确认。
重跑时保留版本、种子、输入和运行记录，方便前后比较。
```

## 许可与一手文档

- [官方MCP能力与配置说明](https://github.com/NandhaKishorM/laya/blob/v0.4.15/README.md#mcp-server-optional)、[固定官方MCP服务源码](https://github.com/NandhaKishorM/laya/blob/v0.4.15/laya/mcp/server.py)。
- Laya代码和官方权重采用Apache-2.0，许可保留于 [LICENSE.laya.txt](../../assets/examples/local-decision-snake/LICENSE.laya.txt)；权重不随本包分发。
- 相邻Snake参考采用MIT，许可保留于 [LICENSE.snake-reference.txt](../../assets/examples/local-decision-snake/LICENSE.snake-reference.txt)。规划特征的适配与本地交付边界见复现脚本注释；页面、数据检查与胶水代码为本仓库新增。

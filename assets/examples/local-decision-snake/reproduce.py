#!/usr/bin/env python3
"""Replay recorded decisions, or explicitly run one pinned local Laya checkpoint.

Default mode is stdlib-only and offline. No model is simulated as Laya.
--download-model needs an explicit --model-dir and downloads less than 900MB.
--run-model needs laya 0.4.15; --check-mcp probes the real official stdio server.
"""
from __future__ import annotations

import argparse
import asyncio
from collections import deque
import datetime as dt
import hashlib
import html
import importlib.metadata
import json
import math
import os
from pathlib import Path
import random
import shutil
import sys
import tempfile
import time
import urllib.request
import warnings

ROOT = Path(__file__).resolve().parent
VERSION = "0.4.15"
SOURCE_REVISION = "7a77439b0923d6efe00052d50a7f787840bfce98"
MODEL_REVISION = "7b928d828b7b0e022f929d9bd2e44165aa270148"
MODEL_REPO = "convaiinnovations/laya"
WEIGHT_BYTES = 842609210
WEIGHT_SHA256 = "891102d372688fc2a094dac56a384bc537b87c63f21f9f3dac0be2b7cbc8d86c"
DIRS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
MODEL_FILES = ("rl_agent_config.json", "encoder/config.json", "tokenizer/tokenizer.json",
               "tokenizer/tokenizer_config.json", "model.safetensors")


def validate_scenario(scenario):
    if not isinstance(scenario.get("width"), int) or not 4 <= scenario["width"] <= 16:
        raise ValueError("Grid width must be 4–16")
    if not isinstance(scenario.get("height"), int) or not 4 <= scenario["height"] <= 16:
        raise ValueError("Grid height must be 4–16")
    if not isinstance(scenario.get("steps"), int) or not 1 <= scenario["steps"] <= 300:
        raise ValueError("Step budget must be 1–300")
    if not isinstance(scenario.get("seed"), int):
        raise ValueError("An integer seed is required")
    return scenario


def distances(start, blocked, width, height):
    found, queue = {start: 0}, deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRS.values():
            cell = x + dx, y + dy
            if cell not in found and cell not in blocked and 0 <= cell[0] < width and 0 <= cell[1] < height:
                found[cell] = found[(x, y)] + 1
                queue.append(cell)
    return found


def plan(snake, food, width, height):
    """Adapted from omp-laya-judge's feature-assisted Snake (MIT).

    Deterministic BFS supplies reachability features; it already does substantial
    work. Tail reachability and room are heuristics, not a general survival proof.
    """
    body, moves = set(snake), {}
    before = distances(snake[0], body - {snake[0]}, width, height)
    for name, (dx, dy) in DIRS.items():
        head = snake[0][0] + dx, snake[0][1] + dy
        eats = head == food
        blocked = body if eats else body - {snake[-1]}
        if not (0 <= head[0] < width and 0 <= head[1] < height) or head in blocked:
            moves[name] = {"legal": False, "safe": False, "reason": "wall-or-body"}
            continue
        after_snake = [head] + (snake if eats else snake[:-1])
        occupied = set(after_snake)
        tail_ok = head in distances(after_snake[-1], occupied - {head, after_snake[-1]}, width, height)
        room = len(distances(head, occupied - {head}, width, height)) >= len(after_snake)
        after = distances(head, occupied - {head}, width, height)
        moves[name] = {"legal": True, "safe": bool(tail_ok and room), "eats": eats,
                       "advance": before.get(food, 999) - after.get(food, 999),
                       "tailReachable": tail_ok, "room": room}
    return moves


def decision_input(moves):
    safe = [name for name in DIRS if moves[name]["safe"]]
    preferred = max(safe, key=lambda name: (moves[name]["eats"], moves[name]["advance"])) if safe else None
    criteria = {}
    for name, move in moves.items():
        criteria[name] = ("Blocked. Collision." if not move["legal"] else
                          "Unsafe. May trap the snake." if not move["safe"] else
                          "Safe. Eat food now. Best." if move["eats"] else
                          "Safe. Best route to food." if name == preferred else "Safe. Slower route.")
    return preferred, f"Safe route available: {'yes' if safe else 'no'}.", {
        "move": {"type": "choice", "instructions": "Choose the best safe move toward food.", "criteria": criteria}}


def check_probabilities(probabilities):
    if set(probabilities) != set(DIRS):
        raise ValueError("A model decision must contain all four direction probabilities")
    if any(not isinstance(x, (int, float)) or not math.isfinite(x) or not 0 <= x <= 1
           for x in probabilities.values()) or abs(sum(probabilities.values()) - 1) > 0.001:
        raise ValueError("Invalid direction probability distribution")


def select_moves(moves, probabilities=None):
    """Use the same deterministic selection/tie rules for play and replay checks."""
    safe = [name for name in DIRS if moves[name]["safe"]]
    if not safe:
        raise ValueError("No safe move can be executed")
    if probabilities is None:
        preferred, _, _ = decision_input(moves)
        return preferred, preferred
    proposed = max(DIRS, key=probabilities.__getitem__)
    executed = proposed if proposed in safe else max(safe, key=probabilities.__getitem__)
    return proposed, executed


def play(scenario, predictor=None):
    validate_scenario(scenario)
    width, height = scenario["width"], scenario["height"]
    snake = [(width // 2, height // 2 + 1), (width // 2, height // 2), (width // 2 - 1, height // 2)]
    rng = random.Random(scenario["seed"])
    food = rng.choice([(x, y) for x in range(width) for y in range(height) if (x, y) not in snake])
    frames, score, interventions = [], 0, 0
    stopped = "step-limit"
    for step in range(scenario["steps"]):
        moves = plan(snake, food, width, height)
        _, state, questions = decision_input(moves)
        safe = [name for name in DIRS if moves[name]["safe"]]
        if not safe:
            stopped = "no-safe-move"  # Stop without executing a collision.
            break
        probabilities, confidence, answer_confidence, elapsed = None, None, None, None
        if predictor:
            start = time.perf_counter()
            answer = predictor(state, questions)["answers"]["move"]
            elapsed = round((time.perf_counter() - start) * 1000, 3)
            probabilities = answer["probabilities"]
            check_probabilities(probabilities)
            confidence = answer.get("confidence")
            answer_confidence = answer.get("answer_confidence")
        proposed, executed = select_moves(moves, probabilities)
        shield = proposed != executed
        interventions += int(shield)
        before, before_food = [list(p) for p in snake], list(food)
        dx, dy = DIRS[executed]
        head = snake[0][0] + dx, snake[0][1] + dy
        snake = [head] + snake
        ate = head == food
        if ate:
            score += 1
            free = [(x, y) for x in range(width) for y in range(height) if (x, y) not in snake]
            food = rng.choice(free) if free else None
        else:
            snake.pop()
        frames.append({"step": step + 1, "before": before, "beforeFood": before_food,
                       "snake": [list(p) for p in snake], "food": list(food) if food else None,
                       "features": moves, "state": state, "questions": questions, "proposed": proposed,
                       "executed": executed, "shield": shield, "probabilities": probabilities,
                       "confidence": confidence, "answerConfidence": answer_confidence,
                       "latencyMs": elapsed, "score": score})
        if not food:
            stopped = "board-filled"
            break
    return {"mode": "laya-local-sdk" if predictor else "planner-baseline", "frames": frames,
            "score": score, "steps": len(frames), "shieldInterventions": interventions, "stopped": stopped}


def validate_trace(trace):
    scenario = validate_scenario(trace["scenario"])
    if trace.get("model", {}).get("weightSha256") != WEIGHT_SHA256:
        raise ValueError("Unexpected checkpoint provenance")
    for arm in trace["runs"]:
        if arm["mode"] not in {"laya-local-sdk", "planner-baseline"}:
            raise ValueError("Unknown run provenance; do not label simulations as Laya")
        previous, previous_food, score, shields = None, None, 0, 0
        for frame in arm["frames"]:
            snake = [tuple(p) for p in frame["before"]]
            food = tuple(frame["beforeFood"])
            if previous is not None and frame["before"] != previous:
                raise ValueError("Broken trace continuity")
            if previous_food is not None and frame["beforeFood"] != previous_food:
                raise ValueError("Broken food continuity")
            moves = plan(snake, food, scenario["width"], scenario["height"])
            if frame["features"] != moves or not moves[frame["executed"]]["safe"]:
                raise ValueError("Unsafe or falsified executed move")
            if arm["mode"] == "laya-local-sdk":
                check_probabilities(frame["probabilities"])
            elif frame["probabilities"] is not None:
                raise ValueError("Planner baseline must not invent model probabilities")
            expected_proposed, expected_executed = select_moves(moves, frame["probabilities"])
            if frame["proposed"] != expected_proposed:
                raise ValueError("Proposed move differs from the model distribution or BFS preference")
            if frame["executed"] != expected_executed:
                raise ValueError("Executed move differs from the recorded selection rule")
            dx, dy = DIRS[frame["executed"]]
            head = snake[0][0] + dx, snake[0][1] + dy
            expected = [head] + (snake if head == food else snake[:-1])
            if frame["snake"] != [list(p) for p in expected] or len(set(expected)) != len(expected):
                raise ValueError("Falsified move or collision in trace")
            score += int(head == food)
            shields += int(frame["proposed"] != frame["executed"])
            if frame["score"] != score or frame["shield"] != (frame["proposed"] != frame["executed"]):
                raise ValueError("Falsified score or hidden guard intervention")
            previous, previous_food = frame["snake"], frame["food"]
        if arm["steps"] != len(arm["frames"]) or not arm["frames"]:
            raise ValueError("Empty or truncated run")
        if arm["score"] != score or arm["shieldInterventions"] != shields:
            raise ValueError("Run summary differs from the actual frames")
    return trace


def download_model(directory):
    directory.mkdir(parents=True, exist_ok=True)
    total = 0
    for name in MODEL_FILES:
        target = directory / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            total += target.stat().st_size
            continue
        url = f"https://huggingface.co/{MODEL_REPO}/resolve/{MODEL_REVISION}/{name}"
        part = target.with_suffix(target.suffix + ".part")
        if name == "model.safetensors":
            # Bounded ranges avoid the short full-file HTTP stream observed in
            # this run. Keep only verified complete range bytes for an explicit retry.
            offset = part.stat().st_size if part.exists() else 0
            if offset > WEIGHT_BYTES:
                raise ValueError("Oversized partial checkpoint; review/delete that explicit cache file")
            with part.open("ab") as output:
                while offset < WEIGHT_BYTES:
                    end = min(offset + 8 * 1024 * 1024, WEIGHT_BYTES) - 1
                    request = urllib.request.Request(url, headers={"User-Agent": "Cogine-local-decision-snake",
                                                                 "Range": f"bytes={offset}-{end}"})
                    with urllib.request.urlopen(request, timeout=60) as response:
                        if response.status != 206 or response.headers.get("Content-Range") != f"bytes {offset}-{end}/{WEIGHT_BYTES}":
                            raise ValueError("Checkpoint server did not honor the bounded range")
                        block = response.read(end - offset + 2)
                    if len(block) != end - offset + 1:
                        raise ValueError("Short checkpoint range; explicit retry keeps verified prefix")
                    output.write(block)
                    output.flush()
                    offset = end + 1
            digest = hashlib.sha256()
            with part.open("rb") as source:
                while block := source.read(1024 * 1024):
                    digest.update(block)
            if digest.hexdigest() != WEIGHT_SHA256:
                raise ValueError("Downloaded checkpoint hash mismatch; no model run was started")
            total += WEIGHT_BYTES
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Cogine-local-decision-snake"})
            with urllib.request.urlopen(request, timeout=45) as response:
                body = response.read(4 * 1024 * 1024 + 1)
            if len(body) > 4 * 1024 * 1024:
                raise ValueError("Unexpectedly large checkpoint metadata")
            total += len(body)
            part.write_bytes(body)
        if total > 900_000_000:
            raise ValueError("Single-checkpoint 900MB download budget exceeded")
        os.replace(part, target)
    verify_weights(directory)


def verify_weights(directory):
    weights = directory / "model.safetensors"
    if not weights.is_file() or weights.stat().st_size != WEIGHT_BYTES:
        raise ValueError("Expected the single 842,609,210-byte official English checkpoint")
    digest = hashlib.sha256()
    with weights.open("rb") as source:
        while chunk := source.read(1024 * 1024):
            digest.update(chunk)
    if digest.hexdigest() != WEIGHT_SHA256:
        raise ValueError("Checkpoint SHA256 mismatch")


async def mcp_probe():
    if importlib.metadata.version("laya") != VERSION:
        raise ValueError("The MCP probe requires pinned laya 0.4.15")
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
    # No registration in OpenClaw or other global agent settings. Lazy status only:
    # the default server otherwise preloads TWO checkpoints, exceeding this pack's scope.
    with tempfile.TemporaryDirectory(prefix="snake-mcp-") as directory:
        environment = {**os.environ, "HF_HOME": directory, "HF_HUB_OFFLINE": "1", "LAYA_PRELOAD": "0",
                       "LAYA_MODELS": "english", "LAYA_DEFAULT_MODEL": "english", "LAYA_DEVICE": "cpu",
                       "PYTHONDONTWRITEBYTECODE": "1", "PYTHONIOENCODING": "utf-8"}
        environment.pop("LAYA_BASE_URL", None)
        parameters = StdioServerParameters(command=sys.executable, args=["-m", "laya.mcp.server"], env=environment)
        async with stdio_client(parameters) as (read, write):
            async with ClientSession(read, write) as session:
                initialized = await session.initialize()
                if initialized.server_info.version != VERSION:
                    raise ValueError("The official MCP server reported an unexpected Laya version")
                tools = await session.list_tools()
                status = await session.call_tool("laya_status", {})
                if status.is_error:
                    raise ValueError("Official MCP laya_status returned a tool error")
                names = sorted(tool.name for tool in tools.tools)
                if "laya_predict" not in names or "laya_status" not in names:
                    raise ValueError("Official MCP decision tools were not discovered")
                return {"mode": "official-stdio-tools-and-status", "protocol": initialized.protocol_version,
                        "serverVersion": initialized.server_info.version,
                        "checkedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
                        "tools": names, "statusSucceeded": True, "modelInferenceThroughMcp": False,
                        "openclawEndToEnd": False}


def render(trace):
    validate_trace(trace)
    payload = json.dumps(trace, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    recorded_day = html.escape(trace["createdAt"][:10])
    real = any(run["mode"] == "laya-local-sdk" for run in trace["runs"])
    status = "真实本地模型 + 规划器 + 保护规则" if real else "仅规划器基线 · 未运行Laya"
    return '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>本地决策蛇：谁决定了下一步？</title><style>
*{box-sizing:border-box}body{margin:0;background:#111d29;color:#e4eef2;font:15px/1.6 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:32px 20px}header{max-width:900px}h1{font-size:clamp(30px,5vw,49px);line-height:1.2}.badge{display:inline-block;border:1px solid #558d7e;border-radius:8px;padding:5px 12px;color:#96e6c7}.muted{color:#9eafbf}.layout{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:22px;margin-top:24px}.panel{background:#1a2b3b;border:1px solid #32495b;border-radius:17px;padding:20px;min-width:0}canvas{width:100%;height:auto;display:block;border-radius:10px;background:#0b1520}button,select{font:inherit;background:#274356;border:1px solid #52708a;border-radius:8px;color:#fff;padding:9px 13px;cursor:pointer}label{display:inline-block;margin:5px 5px 5px 0}input[type=range]{width:100%}.controls{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.stat{padding:13px;border-radius:10px;background:#132432}.stat b{display:block;font-size:25px;color:#90e4c3}.barrow{display:grid;grid-template-columns:60px minmax(0,1fr) 52px;gap:10px;align-items:center;margin:11px 0}.track{height:9px;background:#0e1c28;border-radius:10px;overflow:hidden}.bar{height:100%;background:#68b7d1}.shield{color:#ffd282}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px;color:#b9d3e2;max-height:260px;overflow:auto}a{color:#8cddd4}summary{cursor:pointer}footer{padding:25px 0;color:#9eafbf;font-size:13px}#rangeLabel{display:block}#reason{min-height:50px}code{overflow-wrap:anywhere}@media(max-width:780px){.layout{grid-template-columns:1fr}main{padding:24px 15px}.panel{padding:15px}}
</style><main><header><p class="muted">COGINE / LOCAL DECISION LAB</p><span class="badge">''' + html.escape(status) + '''</span><h1>下一步向哪走？<br>把每一次建议和拦截摊开看。</h1><p class="muted">这是已记录数据的可交互回放，浏览器不运行模型。BFS先计算特征，Laya给四个方向排序，保护规则只执行安全候选。不能把整条流水线的成绩归给Laya。</p></header><div class="controls"><label>实验分支 <select id="arm"></select></label><label>速度 <select id="speed"><option value="650">慢速</option><option value="220" selected>标准</option><option value="70">快速</option></select></label><button id="play" type="button">播放</button><button id="restart" type="button">回到起点</button></div><div class="layout"><section class="panel"><canvas id="board" width="512" height="512" aria-label="蛇的位置与食物回放"></canvas><label id="rangeLabel" for="step">步骤</label><input id="step" type="range" min="0" value="0"><div class="stats"><div class="stat">本次得分<b id="score"></b></div><div class="stat">已发生拦截<b id="shields"></b></div><div class="stat">单次推理<b id="latency"></b></div></div></section><section class="panel"><h2 id="mode"></h2><p id="reason"></p><div id="probabilities"></div><p class="muted" id="confidence"></p><details open><summary>这一步的规划特征与模型输入</summary><pre id="features"></pre></details><details><summary>实验范围与版本</summary><pre id="metadata"></pre></details></section></div><section class="panel" style="margin-top:22px"><h2>怎样读这场实验</h2><p>概率来自已记录的模型回复；基线不显示虚构概率。保护规则可能改写模型的第一选择。单种子、单次小样本不能证明长期成绩、校准精度、相对其他模型的优势或速度收益。</p><p>真实SDK推理、官方MCP工具发现/状态调用、OpenClaw会话分别标记。工具检查不会下载第二份模型，也不能当作OpenClaw端到端运行。</p><p><a href="run.json">原始回放数据</a> · <a href="scenario.json">实验输入</a> · <a href="reproduce.py">复现脚本</a></p></section><footer>实验日期：''' + recorded_day + '''。模型权重不随包分发；默认复现只读本地记录，不联网、不启动后台服务。<p><a href="https://www.opcboost.com/usecases/creative/local-decision-snake-lab/">返回完整教程</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">Star / 参与共建</a> · <a href="https://www.cogine.ai/">Cogine</a></p></footer></main><script>
const DATA = ''' + payload + ''';
const $=id=>document.getElementById(id), arm=$('arm'), slider=$('step'), canvas=$('board'), ctx=canvas.getContext('2d');
let timer=null,index=0;
DATA.runs.forEach((run,i)=>{const option=document.createElement('option');option.value=i;option.textContent=run.mode==='laya-local-sdk'?'真实Laya SDK + 保护规则':'仅BFS规划器基线';arm.append(option)});
function stop(){clearTimeout(timer);timer=null;$('play').textContent='播放'}
function draw(){const run=DATA.runs[Number(arm.value)], frame=run.frames[index];slider.max=run.frames.length-1;slider.value=index;$('rangeLabel').textContent=`步骤 ${index+1} / ${run.frames.length} · 结束原因 ${run.stopped}`;
const w=DATA.scenario.width,h=DATA.scenario.height,cw=canvas.width/w,ch=canvas.height/h;ctx.fillStyle='#0b1520';ctx.fillRect(0,0,512,512);ctx.strokeStyle='#203544';for(let x=0;x<=w;x++){ctx.beginPath();ctx.moveTo(x*cw,0);ctx.lineTo(x*cw,512);ctx.stroke()}for(let y=0;y<=h;y++){ctx.beginPath();ctx.moveTo(0,y*ch);ctx.lineTo(512,y*ch);ctx.stroke()}
frame.snake.forEach(([x,y],i)=>{ctx.fillStyle=i?'#54a68d':'#a4f0c9';ctx.fillRect(x*cw+3,y*ch+3,cw-6,ch-6)});if(frame.food){ctx.fillStyle='#ffb36d';ctx.beginPath();ctx.arc((frame.food[0]+.5)*cw,(frame.food[1]+.5)*ch,cw*.23,0,Math.PI*2);ctx.fill()}
$('score').textContent=frame.score;$('shields').textContent=run.frames.slice(0,index+1).filter(x=>x.shield).length;$('latency').textContent=frame.latencyMs===null?'无模型':Math.round(frame.latencyMs)+'ms';$('mode').textContent=run.mode==='laya-local-sdk'?'模型建议 '+frame.proposed:'规划器建议 '+frame.proposed;$('reason').textContent=frame.shield?'保护规则拦截了第一选择，实际执行 '+frame.executed:'实际执行 '+frame.executed+'；本步没有改写建议';$('reason').className=frame.shield?'shield':'';
$('probabilities').replaceChildren();for(const name of ['UP','DOWN','LEFT','RIGHT']){const row=document.createElement('div');row.className='barrow';const label=document.createElement('span');label.textContent=name;const track=document.createElement('div');track.className='track';const bar=document.createElement('div');bar.className='bar';bar.style.width=frame.probabilities?(frame.probabilities[name]*100)+'%':'0%';track.append(bar);const number=document.createElement('span');number.textContent=frame.probabilities?(frame.probabilities[name]*100).toFixed(1)+'%':'—';row.append(label,track,number);$('probabilities').append(row)}
$('confidence').textContent=frame.probabilities?'模型confidence与answerConfidence保留在原始JSON；不把它们解释为本游戏的成功率。':'此分支未调用模型，不生成模型概率、置信度或延迟。';$('features').textContent=JSON.stringify({features:frame.features,state:frame.state,questions:frame.questions},null,2);$('metadata').textContent=JSON.stringify({createdAt:DATA.createdAt,model:DATA.model,runtime:DATA.runtime,mcp:DATA.mcp,scenario:DATA.scenario,runSummary:{score:run.score,steps:run.steps,shieldInterventions:run.shieldInterventions,stopped:run.stopped}},null,2)}
function tick(){const run=DATA.runs[Number(arm.value)];if(index>=run.frames.length-1){stop();return}index++;draw();timer=setTimeout(tick,Number($('speed').value))}
$('play').addEventListener('click',()=>{if(timer){stop();return}if(index>=DATA.runs[Number(arm.value)].frames.length-1)index=0;$('play').textContent='暂停';timer=setTimeout(tick,Number($('speed').value))});$('restart').addEventListener('click',()=>{stop();index=0;draw()});slider.addEventListener('input',()=>{stop();index=Number(slider.value);draw()});arm.addEventListener('change',()=>{stop();index=0;draw()});draw();
</script></html>'''


def preview(trace):
    validate_trace(trace)
    run = trace["runs"][0]
    frame = run["frames"][-1]
    real = run["mode"] == "laya-local-sdk"
    label = "真实Laya本地SDK + BFS + 保护规则" if real else "仅规划器基线 · Laya未运行"
    width, height = trace["scenario"]["width"], trace["scenario"]["height"]
    cells = []
    for i, (x, y) in enumerate(frame["snake"]):
        cells.append(f'<rect x="{814+x*30}" y="{190+y*30}" width="26" height="26" rx="3" fill="{"#a4f0c9" if i == 0 else "#54a68d"}"/>')
    if frame["food"]:
        x, y = frame["food"]
        cells.append(f'<circle cx="{827+x*30}" cy="{203+y*30}" r="9" fill="#ffb36d"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" role="img" aria-label="本地决策蛇实验预览"><rect width="1200" height="630" fill="#111d29"/><g fill="#e4eef2" font-family="system-ui,sans-serif"><text x="70" y="105" font-size="25" fill="#90cbb9">COGINE / LOCAL DECISION LAB</text><text x="70" y="180" font-size="48" font-weight="700">谁决定了下一步？</text><text x="70" y="235" font-size="23">{label}</text><text x="70" y="330" font-size="42">{run["steps"]} 步 · 得分 {run["score"]} · 拦截 {run["shieldInterventions"]} 次</text><text x="70" y="400" font-size="23" fill="#ffce91">只代表一次小样本，不是模型能力排名。</text><text x="70" y="510" font-size="21">可解释回放 / {html.escape(trace["createdAt"][:10])} / OpenClaw未端到端运行</text></g><rect x="802" y="178" width="{width*30+22}" height="{height*30+22}" rx="14" fill="#0b1520" stroke="#3d5b70"/>{''.join(cells)}</svg>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-model", action="store_true")
    parser.add_argument("--download-model", action="store_true")
    parser.add_argument("--model-dir", type=Path)
    parser.add_argument("--check-mcp", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    args = parser.parse_args()
    standalone = args.output_dir.resolve() != ROOT.resolve()
    if standalone and args.output_dir.exists():
        parser.error("--output-dir must name a new directory")
    if (args.run_model or args.download_model) and not args.model_dir:
        parser.error("Use an explicit --model-dir; no global model cache is selected")
    if args.download_model:
        download_model(args.model_dir)
    if args.run_model:
        if importlib.metadata.version("laya") != VERSION:
            raise ValueError("Install the pinned laya 0.4.15 in a temporary virtual environment")
        verify_weights(args.model_dir)
        import platform
        import torch
        import laya
        torch.set_num_threads(4)
        scenario = json.loads((ROOT / "scenario.json").read_text(encoding="utf-8"))
        with warnings.catch_warnings(record=True) as observed:
            warnings.simplefilter("always")
            agent = laya.load(str(args.model_dir.resolve()), device="cpu", fast=False, compile=False)
        runtime_warnings = [str(item.message) for item in observed]
        for message in runtime_warnings:
            print("Upstream warning: " + message, file=sys.stderr, flush=True)
        print("Running real local inference; planner and shield remain explicit.", flush=True)
        model_run = play(scenario, agent.predict)
        trace = {"createdAt": dt.datetime.now(dt.timezone.utc).isoformat(), "scenario": scenario,
                 "model": {"package": VERSION, "sourceRevision": SOURCE_REVISION, "repository": MODEL_REPO,
                           "revision": MODEL_REVISION, "weightBytes": WEIGHT_BYTES, "weightSha256": WEIGHT_SHA256},
                 "runtime": {"python": platform.python_version(), "platform": sys.platform,
                             "machine": platform.machine(), "device": "cpu", "threads": 4,
                             "torch": torch.__version__, "transformers": importlib.metadata.version("transformers"),
                             "warnings": runtime_warnings},
                 "mcp": {"mode": "not-run", "openclawEndToEnd": False},
                 "runs": [model_run, play(scenario)]}
    else:
        trace = json.loads((ROOT / "run.json").read_text(encoding="utf-8"))
    if args.check_mcp:
        trace["mcp"] = asyncio.run(asyncio.wait_for(mcp_probe(), timeout=90))
    document = render(trace)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if standalone:
        for name in ("scenario.json", "LICENSE.laya.txt", "LICENSE.snake-reference.txt", "reproduce.py"):
            shutil.copyfile(ROOT / name, args.output_dir / name)
    outputs = {"index.html": document, "preview.svg": preview(trace)}
    if args.run_model or args.check_mcp or standalone:
        outputs["run.json"] = json.dumps(trace, ensure_ascii=False, indent=2) + "\n"
    for name, text in outputs.items():
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.output_dir, delete=False) as handle:
            handle.write(text)
            temporary = handle.name
        os.replace(temporary, args.output_dir / name)
    for run in trace["runs"]:
        print(f'{run["mode"]}: steps={run["steps"]}, score={run["score"]}, shield={run["shieldInterventions"]}; {run["stopped"]}')
    print("Replay ready; browser playback is not live model inference or an OpenClaw run.")


if __name__ == "__main__":
    main()

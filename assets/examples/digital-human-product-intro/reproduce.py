#!/usr/bin/env python3
"""Run the pinned upstream planner offline. Never submit tasks or quote live prices."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
UPSTREAM_SHA = "5fa9b19f52fb8920c83567468fa30e8391b8c503"


def planned_tasks(script, persona):
    source = HERE / "upstream/scripts/build_tasks.py"
    expected = json.loads((HERE / "provenance.json").read_text())["builderSha256"]
    if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
        raise ValueError("Pinned upstream builder changed")
    if not isinstance(script, list) or not script or len(script) > 10:
        raise ValueError("Use 1–10 reviewed script segments")
    ids = set()
    for item in script:
        if (not isinstance(item, dict) or not isinstance(item.get("id"), str)
                or not item["id"].isalnum() or item["id"] in ids
                or not isinstance(item.get("t"), str) or not item["t"].strip()
                or item.get("shot") not in {"full", "pip"}):
            raise ValueError("Invalid or duplicate segment")
        ids.add(item["id"])
    with tempfile.TemporaryDirectory(prefix="opcboost-intro-") as temporary:
        root = Path(temporary)
        (root / "scripts").mkdir()
        shutil.copyfile(source, root / "scripts/build_tasks.py")
        (root / "persona.json").write_text(json.dumps(persona, ensure_ascii=False))
        (root / "script.json").write_text(json.dumps(script, ensure_ascii=False))
        result = subprocess.run([sys.executable, str(root / "scripts/build_tasks.py"),
                                 str(root / "script.json"), str(root / "tasks.json"),
                                 "--purpose", "introducing the OPCBoost reproducible case library"],
                                text=True, capture_output=True, timeout=15)
        if result.returncode:
            raise ValueError(result.stderr.strip() or "Upstream planning failed")
        tasks = json.loads((root / "tasks.json").read_text())
    if len(tasks) != len(script) or any(not 4 <= task["duration"] <= 15 for task in tasks):
        raise ValueError("Unexpected upstream task structure")
    # Its internal fixture-unit cost is deliberately not published as a service quote.
    return {"status": "offline-preparation", "readyToSubmit": False,
            "estimatedCredits": None, "priceStatus": "not-quoted",
            "generatedVideo": False, "upstreamCommit": UPSTREAM_SHA,
            "durationBasis": "upstream text heuristic, not recorded audio",
            "tasks": tasks}


def timestamp(seconds):
    return f"{seconds//3600:02}:{seconds//60%60:02}:{seconds%60:02},000"


def outputs(plan, script):
    seconds, subtitles, rows = 0, [], []
    for index, (task, item) in enumerate(zip(plan["tasks"], script), 1):
        end = seconds + task["duration"]
        subtitles.append(f"{index}\n{timestamp(seconds)} --> {timestamp(end)}\n{item['t']}\n")
        rows.append(f'<article><span>{seconds:02}–{end:02}s · {html.escape(item["shot"])}</span>'
                    f'<h2>{html.escape(task["label"])}</h2><p>{html.escape(item["t"])}</p>'
                    f'<small>{html.escape(task["resolution"])} · 计划 {task["duration"]} 秒</small></article>')
        seconds = end
    body = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OPCBoost 数字人口播 · 离线制作台</title><style>body{font:17px/1.75 system-ui;background:#f5f7f3;color:#17392c;max-width:1080px;margin:auto;padding:32px}a{color:#176c4e}header{border-bottom:3px solid #176c4e;padding-bottom:20px}.label{font-size:14px;letter-spacing:.1em}h1{font-size:clamp(30px,6vw,54px);line-height:1.2}section{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px}article{background:white;border:1px solid #b9c8b9;border-radius:16px;padding:22px}article span,small{color:#4c6355}h2{font-size:22px}.notice{background:#fff5d9;padding:20px;border-radius:12px}nav,footer{margin:24px 0}nav a{display:inline-block;margin:6px 20px 6px 0}li{margin:8px 0}</style>
<header><p class="label">OPCBOOST / 制作准备</p><h1>先把口播分好段，<br>再决定是否生成。</h1><p>COUNT段产品介绍 · TOTAL秒计划字幕 · 尚未生成视频</p></header>
<nav><a href="script.json">原始口播</a><a href="planned-subtitles.srt" download>计划字幕</a><a href="draft-tasks.json" download>未提交任务草稿</a><a href="reproduce.py">复现脚本</a></nav>
<p class="notice">离线准备包：使用固定上游脚本实算分段；人物、配音、视频和费用均未核验。字幕来自文字估时，尚未与音频对齐。任务含占位引用，不能直接提交。</p><section>ROWS</section>
<h2>生成前还缺什么</h2><ol><li>准备自己拥有使用权的主播形象与声音；本包没有复用上游作者形象。</li><li>连接自己的 Renoise 账号，查当前模型、额度和报价。不同分辨率价格需分别核对。</li><li>替换模型和上传后的素材引用，先核报总价并确认预算，再生成一小段验嘴型。</li><li>获得真实视频后再做 Whisper 对齐、画中画与剪辑验收；使用 Remotion 模板前核对公司授权条件。</li></ol>
<footer><a href="https://www.opcboost.com/usecases/creative/digital-human-product-intro/">阅读完整案例</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">Star / 参与共建</a> · <a href="https://cogine.ai">Cogine</a><p>未调用媒体服务 · 非成片展示 · OPCBoost by Cogine</p></footer></html>'''.replace("TOTAL", str(seconds)).replace("COUNT", str(len(script))).replace("ROWS", "".join(rows))
    strips=[]
    offset=0
    for i,(task,item) in enumerate(zip(plan['tasks'][:3],script[:3])):
        y=220+i*100
        strips.append(f'<rect x="50" y="{y-40}" width="1100" height="84" rx="14" fill="#fff" stroke="#bdcebf"/><text x="76" y="{y-5}" font-size="25" fill="#173f30">{offset:02}–{offset+task["duration"]:02}s · {task["resolution"]} · {html.escape(task["label"])}</text><text x="76" y="{y+28}" font-size="19" fill="#526655">{html.escape(item["t"])}</text>')
        offset+=task['duration']
    preview='<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="口播离线规划"><rect width="1200" height="630" fill="#f1f5ee"/><g font-family="system-ui,sans-serif"><text x="50" y="68" font-size="22" fill="#376b50">OPCBOOST / 离线制作准备</text><text x="50" y="135" font-size="46" font-weight="700" fill="#173f30">'+str(len(script))+'段口播，'+str(seconds)+'秒文字估时。</text>'+''.join(strips)+'<text x="50" y="555" font-size="23" fill="#526655">实际脚本产物 · 计划字幕 · 任务草稿</text><text x="50" y="596" font-size="21" fill="#8b4f14">未生成主播、声音或视频 · 价格未知</text></g></svg>\n'
    return {"draft-tasks.json": json.dumps(plan, ensure_ascii=False, indent=2) + "\n",
            "planned-subtitles.srt": "\n".join(subtitles), "index.html": body, "preview.svg":preview}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=HERE)
    args = parser.parse_args()
    standalone = args.output_dir.resolve() != HERE.resolve()
    if standalone and args.output_dir.exists():
        parser.error("--output-dir must name a new directory")
    script = json.loads((HERE / "script.json").read_text())
    persona = json.loads((HERE / "persona.offline.json").read_text())
    try:
        plan = planned_tasks(script, persona)
        rendered = outputs(plan, script)
    except (ValueError, subprocess.TimeoutExpired) as error:
        parser.error(str(error))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if standalone:
        # Explicit public dependencies keep every local link and the replay runnable.
        for name in ("script.json", "persona.offline.json", "provenance.json", "reproduce.py",
                     "LICENSE.upstream.txt", "NOTICE.upstream.md", "THIRD_PARTY.upstream.md",
                     "upstream/scripts/build_tasks.py"):
            target = args.output_dir / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(HERE / name, target)
    for name, content in rendered.items():
        (args.output_dir / name).write_text(content, encoding="utf-8")
    print(f"Offline preparation: {len(plan['tasks'])} segments / {sum(t['duration'] for t in plan['tasks'])} planned seconds; price unknown; video not generated.")


if __name__ == "__main__":
    main()

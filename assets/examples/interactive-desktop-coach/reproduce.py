#!/usr/bin/env python3
"""Replay recorded Bigarrow parsing, or explicitly validate with the real pinned CLI.

The default/--verify path is offline and opens no windows. --desktop is an explicit
opt-in that shows ONE real card; it never clicks, changes permissions or installs skills.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
COMMIT = "4ad1ce1d82368139b2ceec7b2e29ade837acc722"
UPSTREAM = "https://github.com/franzenzenhofer/big-arrow-on-the-screen"
NAMES = ("01-open", "02-choose", "03-check")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def inputs() -> list[dict]:
    return [load(ROOT / "cards" / (name + ".json")) for name in NAMES]


def check_recording() -> dict:
    result = load(ROOT / "dry-run-results.json")
    if result["version"] != "0.5.1" or result["commit"] != COMMIT:
        raise ValueError("unexpected recorded upstream version")
    for name, card, item in zip(NAMES, inputs(), result["cards"], strict=True):
        raw = (ROOT / "cards" / (name + ".json")).read_bytes()
        if item["name"] != name or item["inputSha256"] != hashlib.sha256(raw).hexdigest():
            raise ValueError("input differs from real CLI recording: " + name)
        if item["exitCode"] != 0 or item["output"] != card:
            raise ValueError("recorded card does not match input: " + name)
    if result["invalidInput"]["exitCode"] != 2:
        raise ValueError("missing real CLI bad-input check")
    return result


def run_cli(binary: Path) -> dict:
    version = subprocess.run([str(binary), "--version"], text=True, capture_output=True, check=True, timeout=20).stdout.strip().removeprefix("bigarrow ")
    if version != "0.5.1":
        raise ValueError("this example requires bigarrow --version = 0.5.1")
    rows = []
    for name in NAMES:
        path = ROOT / "cards" / (name + ".json")
        run = subprocess.run([str(binary), "card", str(path), "--dry-run", "--json"], text=True, capture_output=True, timeout=20)
        if run.returncode != 0:
            raise RuntimeError("CLI dry-run failed: " + run.stderr)
        output = json.loads(run.stdout)
        if output != load(path):
            raise ValueError("CLI normalized output differs from the public input: " + name)
        rows.append({"name": name, "inputSha256": hashlib.sha256(path.read_bytes()).hexdigest(), "exitCode": run.returncode, "output": output})
    invalid = '{"title":"invalid fixture","rows":[{"type":"text","value":"public input","colour":"green"}]}'
    bad = subprocess.run([str(binary), "card", "-", "--dry-run", "--json"], input=invalid, text=True, capture_output=True, timeout=20)
    if bad.returncode != 2 or "unknown key 'colour'" not in bad.stderr:
        raise ValueError("CLI did not reject an unknown row key before drawing")
    return {"version": version, "commit": COMMIT, "testedAt": datetime.now(timezone.utc).date().isoformat(), "mode": "real CLI --dry-run; no desktop UI or human reply", "cards": rows, "invalidInput": {"description": "unknown row key colour", "exitCode": bad.returncode, "error": json.loads(bad.stderr)}}


def render(recording: dict) -> str:
    cards = inputs()
    esc = lambda value: html.escape(str(value), quote=True)
    sections = []
    for index, (name, card) in enumerate(zip(NAMES, cards, strict=True), 1):
        blocks = []
        for row in card["rows"]:
            kind = row["type"]
            if kind == "text":
                blocks.append("<p>" + esc(row["value"]) + "</p>")
            elif kind == "link":
                blocks.append('<p><a href="' + esc(row["url"]) + '">' + esc(row["label"]) + " ↗</a></p>")
            elif kind == "code":
                blocks.append("<pre><code>" + esc(row["value"]) + "</code></pre>")
            else:
                label = "勾选项" if kind == "checklist" else "可选回答"
                blocks.append("<h3>" + label + "</h3><ul>" + "".join("<li>" + esc(item["label"]) + ("<small>" + esc(item["detail"]) + "</small>" if item.get("detail") else "") + "</li>" for item in row["items"]) + "</ul>")
        sections.append('<section id="step-' + str(index) + '"><div class="tag">步骤 ' + str(index) + ' · CLI 输入已解析</div><h2>' + esc(card["title"]) + '</h2>' + "".join(blocks) + '<p><a href="cards/' + name + '.json" download>下载原始卡片 JSON</a></p></section>')
    return '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>交互桌面教练 · 三步公开教程</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f7f5;color:#142b25;font:16px/1.7 system-ui,sans-serif}main{max-width:980px;margin:auto;padding:32px 18px 64px}h1{font-size:clamp(29px,6vw,48px);line-height:1.2}h2{font-size:23px;line-height:1.4}a{color:#12684c;overflow-wrap:anywhere}section,.notice{border:1px solid #cddbd3;border-radius:20px;background:white;padding:24px;margin-top:24px;min-width:0}section{box-shadow:0 8px 32px #163d2710}.notice{background:#e6f2eb}.tag{color:#146447;font-size:14px;font-weight:700}small{display:block;color:#5e716a}li{margin:10px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;border-radius:9px;background:#102e25;color:#d3f7e6;padding:14px}nav{display:flex;gap:16px;flex-wrap:wrap}footer{margin-top:36px;color:#50665d}a:focus-visible{outline:3px solid #da8c1c;outline-offset:4px}</style><main>
<p class="tag">COGINE · HUMAN IN THE LOOP</p><h1>把一段操作说明，变成三张桌面教学卡</h1>
<div class="notice"><strong>这是自含 HTML 预览，不是 macOS 截图或真实问答回放。</strong><p>已在 Bigarrow v0.5.1 运行三张卡片的真实 CLI dry-run，以及一个坏输入拒绝检查。主任务还实际启动第 1 张桌面卡，CLI 返回 ok:true 和控件矩形；真人回答到 wait 回传及 OpenClaw 接入待验证。此页只呈现公开输入，没有模拟用户点击、勾选或 Agent 完成。</p></div>
<nav aria-label="教学步骤"><a href="#step-1">1 看成果</a><a href="#step-2">2 选路线</a><a href="#step-3">3 查条件</a></nav>''' + "".join(sections) + '''<section><h2>在自己的 Mac 真正弹出一张卡</h2><p>从固定源码构建后，先只检查输入：</p><pre><code>python3 reproduce.py --cli /path/to/bigarrow --verify
python3 reproduce.py --cli /path/to/bigarrow --desktop --step 1
/path/to/bigarrow wait PID --timeout 30
/path/to/bigarrow stop --pid PID</code></pre><p>先把所有 <code>/path/to/bigarrow</code> 换成同一个已构建二进制的实际路径；例如按完整教程构建时为 <code>/tmp/bigarrow-coach-source/.build/release/bigarrow</code>。第二条会启动真实桌面卡并打印 PID，再把 <code>PID</code> 换成刚返回的数字，用第三条读取真实回答；超时只代表 pending，不代表完成。点击卡片 X 是取消；需要清理时只用第四条关闭自己的卡。不要全局清除其他人的卡。</p><p><a href="reproduce.py" download>复现脚本</a> · <a href="dry-run-results.json">真实解析产物</a> · <a href="LICENSE-upstream.txt">上游 MIT 许可</a></p></section>
<footer>由 Cogine 整理原创公开教学输入；卡片能力来自 <a href="''' + UPSTREAM + '/tree/' + COMMIT + '''">Franz Enzenhofer 的 Bigarrow v0.5.1</a>。<a href="verification.json">构建与验证范围</a>。<p><a href="https://www.opcboost.com/usecases/tools/interactive-desktop-coach/">返回完整教程</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">案例仓库</a> · <a href="https://www.cogine.ai/">Cogine</a></p></footer></main></html>'''


def render_preview() -> str:
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="#eff5ef"/><g font-family="system-ui,sans-serif"><text x="64" y="68" font-size="20" fill="#267051">COGINE · BIGARROW v0.5.1</text><text x="64" y="135" font-size="43" font-weight="700" fill="#12372b">把说明变成三张桌面教学卡</text><text x="64" y="178" font-size="22" fill="#526c60">原创输入派生预览 · 非 macOS 截图 · 未模拟真人回答</text>']
    panels = [('1 看成果', ['打开公开经验卡', '对照 v1 / v2', '你来点击与确认']), ('2 选路线', ['离线重放', '真实访谈', '说明模型与账号门槛']), ('3 查条件', ['使用公开输入', '检查 Python 3.10+', '勾选 ≠ 脚本完成'])]
    for index, (title, rows) in enumerate(panels):
        x = 64 + index * 390
        parts.append(f'<rect x="{x}" y="222" width="366" height="348" rx="22" fill="white" stroke="#c2d8ca"/><text x="{x+24}" y="275" font-size="29" font-weight="700" fill="#146447">{html.escape(title)}</text>')
        for row, text in enumerate(rows):
            parts.append(f'<rect x="{x+22}" y="{309+row*68}" width="322" height="48" rx="10" fill="#edf5ef"/><text x="{x+37}" y="{341+row*68}" font-size="23" fill="#224d3a">{html.escape(text)}</text>')
    parts.append('<text x="64" y="627" font-size="23" fill="#146447">实际验证：构建 PASS · 8 项上游测试 · 3 卡 CLI 解析</text><text x="64" y="669" font-size="20" fill="#526c60">第 1 卡启动返回 ok:true；真人问答 → wait 与 Agent 集成待验收</text></g></svg>')
    return ''.join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="check immutable input against the recorded real CLI output; no windows")
    parser.add_argument("--cli", type=Path, help="explicit locally built bigarrow v0.5.1 binary; runs real --dry-run")
    parser.add_argument("--out", type=Path, help="write a standalone copy to a NEW directory")
    parser.add_argument("--record", action="store_true", help="with --cli, refresh this example's real parsing outputs and preview")
    parser.add_argument("--desktop", action="store_true", help="explicitly show one real macOS card; never answers or clicks")
    parser.add_argument("--step", type=int, choices=(1, 2, 3), default=1)
    args = parser.parse_args()
    if args.out and args.out.exists():
        parser.error("--out must be a new directory; existing files are never overwritten")
    if (args.record or args.desktop) and not args.cli:
        parser.error("--record and --desktop require an explicit --cli")
    if args.desktop and (args.record or args.out):
        parser.error("--desktop cannot be combined with --record or --out")
    recording = run_cli(args.cli.resolve()) if args.cli else check_recording()
    if args.desktop:
        return subprocess.run([str(args.cli.resolve()), "card", str(ROOT / "cards" / (NAMES[args.step - 1] + ".json")), "--json"], check=False).returncode
    page = render(recording)
    preview = render_preview()
    if args.record:
        (ROOT / "dry-run-results.json").write_text(json.dumps(recording, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (ROOT / "index.html").write_text(page, encoding="utf-8")
        (ROOT / "preview.svg").write_text(preview, encoding="utf-8")
    elif args.out:
        import shutil
        args.out.mkdir(parents=True)
        shutil.copytree(ROOT / "cards", args.out / "cards")
        for name in ("reproduce.py", "LICENSE-upstream.txt", "dry-run-results.json", "verification.json"):
            shutil.copyfile(ROOT / name, args.out / name)
        (args.out / "index.html").write_text(page, encoding="utf-8")
        (args.out / "preview.svg").write_text(preview, encoding="utf-8")
    elif page != (ROOT / "index.html").read_text(encoding="utf-8"):
        raise ValueError("index.html differs from the reproducible preview")
    elif preview != (ROOT / "preview.svg").read_text(encoding="utf-8"):
        raise ValueError("preview.svg differs from its public card-derived preview")
    print("PASS: " + ("real CLI parsed 3 cards and rejected an unknown key; desktop not exercised" if args.cli else "offline input hashes, recorded real CLI output and preview match; CLI was not rerun"))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        print("FAIL:", error, file=sys.stderr)
        raise SystemExit(1)

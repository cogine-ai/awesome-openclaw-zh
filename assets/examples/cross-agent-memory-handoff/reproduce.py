#!/usr/bin/env python3
"""Offline replay of a public Sno receipt; --run explicitly calls the real local service."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import textwrap

ROOT = Path(__file__).resolve().parent
COMMIT = "5c4ee17f3ef4f12dc6514e2bd78ec6e580b9c363"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(receipt):
    if receipt["sourceCommit"] != COMMIT or receipt["version"] != "1.6.0":
        raise ValueError("unexpected Sno source version")
    if receipt["fixtureSha256"] != hashlib.sha256((ROOT / "fixture.json").read_bytes()).hexdigest():
        raise ValueError("public input differs from the real service recording")
    if receipt["realAgentsInvoked"] is not False or receipt["telemetry"] is not False:
        raise ValueError("recording boundary changed")
    if receipt["mode"] != "local-first" or receipt["rerank"] != "none" or receipt["llmCallsConfigured"] != "off":
        raise ValueError("this replay requires isolated Local First with model calls disabled")
    if receipt.get("status") == "blocked":
        if receipt["steps"] or not receipt.get("reason") or receipt.get("memoryOperationsVerified") is not False:
            raise ValueError("a blocked receipt must not claim successful memory operations")
        return
    if receipt.get("status") != "passed":
        raise ValueError("unknown validation status")
    expected = ["store", "get", "correct", "get-history", "recall-current", "store-and-forget"]
    if [step["operation"] for step in receipt["steps"]] != expected or not all(step["passed"] is True for step in receipt["steps"]):
        raise ValueError("missing successful real service operations")
    fixture = read_json(ROOT / "fixture.json")
    steps = receipt["steps"]
    if steps[0]["text"] != fixture["original"] or steps[1]["text"] != fixture["original"] or steps[2]["text"] != fixture["corrected"]:
        raise ValueError("recorded memory text does not match the public fixture")
    if (steps[3]["text"] != fixture["original"] + "\nretired; superseded by memory-v2"
            or steps[3]["supersededBy"] != "memory-v2"
            or steps[3].get("normalization") != "Verified runtime successor ID in annotated text and metadata is replaced with alias memory-v2."):
        raise ValueError("missing correction history")
    if (steps[4]["currentText"] != fixture["corrected"] or steps[4]["oldTextExcluded"] is not True
            or steps[4].get("source") != "auto" or steps[4].get("injectionPhase") != "prompt"):
        raise ValueError("missing current-only recall check")
    if steps[5]["readerGet"] is not None:
        raise ValueError("forgotten temporary memory remains readable")


def render(receipt):
    esc = lambda value: html.escape(str(value), quote=True)
    if receipt.get("status") == "blocked":
        fixture = read_json(ROOT / "fixture.json")
        return '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>共享记忆接棒 · 实验输入与真实验证状态</title><style>*{box-sizing:border-box}body{margin:0;background:#0a1721;color:#e0ebee;font:16px/1.75 system-ui,sans-serif}main{max-width:920px;margin:auto;padding:30px 18px 64px}h1{font-size:clamp(30px,5vw,46px);line-height:1.25}h2{font-size:23px}a{color:#6fe4bd;overflow-wrap:anywhere}section,.notice{margin-top:23px;border:1px solid #294352;border-radius:17px;padding:23px;background:#11232f;min-width:0}.notice{border-color:#a77a35;background:#382c19}.tag{color:#e9bd72;font-weight:700}.fact{overflow-wrap:anywhere;border-left:3px solid #739ba9;padding-left:14px}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#071019;padding:15px;border-radius:9px}footer{margin-top:34px}a:focus-visible{outline:3px solid #dca84a;outline-offset:4px}</style><main><p class="tag">COGINE · EXPERIMENTAL · 2026-10-27</p><h1>为下一位 Agent 准备可纠正、可追溯的共享记忆</h1><div class="notice"><strong>运行尚未通过；本页不是成功演示。</strong><p>''' + esc(receipt["reason"]) + '''</p><p>已完成固定源码与接口审阅、公开输入制作和真实服务入口的 Node 语法检查。尚未验证 Sno 服务启动、记忆 CRUD、纠正取回或真实 Agent 接棒；没有使用 mock 冒充这些结果。</p></div><section><h2>一份可检查的原创公开输入</h2><p>下面的日期完全是演练素材，不是公司真实交付承诺，也不是用户原话。</p><p class="fact">v1：''' + esc(fixture["original"]) + '''</p><p class="fact">修订目标：''' + esc(fixture["corrected"]) + '''</p><p>计划检查：writer 写入 → reader 读取 → writer 纠正 → reader 检查旧版关联与当前召回 → 删除一条临时演练记忆。writer / reader 是两个 API 客户端，不能作为 Codex / OpenClaw 已接棒的证据。</p></section><section><h2>离线核对与真实运行分开</h2><pre><code>python3 reproduce.py --verify
python3 reproduce.py --run --runtime /path/to/isolated-runtime --out /tmp/memory-replay</code></pre><p>第一条只核对公开输入、未通过的真实状态记录和 HTML；不会运行 Sno，也不会声称 CRUD 成功。第二条才启动真实隔离服务。先按完整教程准备临时依赖；首次还需下载约 639MB 的公开 embedding 模型。失败会退出，不把预期结果写成成功。</p><p>Local First；模型路由、重排、REM 和遥测关闭；运行器只使用新建 profile，不安装 Agent，不读取真实会话。仅在全部实际断言成功时才导出六步结果。</p><p><a href="fixture.json">下载公开输入</a> · <a href="receipt.json">实际验证状态</a> · <a href="reproduce.py" download>离线重放器</a> · <a href="run-memory.mjs" download>真实服务入口</a> · <a href="package.json">固定主依赖</a> · <a href="LICENSE-upstream.txt">Apache-2.0</a></p></section><footer>由 Cogine 整理实验。来源：<a href="https://github.com/sno-ai/sno-station/tree/''' + COMMIT + '''">Sno Station v1.6.0</a>。<p><a href="https://www.opcboost.com/usecases/memory/cross-agent-memory-handoff/">完整教程与前置条件</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">案例仓库</a> · <a href="https://www.cogine.ai/">Cogine</a></p></footer></main></html>'''
    labels = ["写入第一版", "另一 API 客户端读取", "纠正并创建新版", "保留旧版历史", "取回当前事实", "删除临时演练记忆"]
    sections = []
    for index, (label, step) in enumerate(zip(labels, receipt["steps"], strict=True), 1):
        detail = step.get("text", step.get("currentText", ""))
        extra = "<p>inspect 的旧版文本保留原文并追加 retired 标记，metadata 的 superseded_by 指向同一新版；本页将实际新版 ID 归一为 memory-v2。</p>" if step["operation"] == "get-history" else ""
        if step["operation"] == "recall-current":
            extra = "<p>查询：" + esc(step["query"]) + "</p><p>使用 source=auto、injectionPhase=prompt；已检查：当前召回包含新版 ID 与文本，不包含旧版 ID 或文本。</p>"
        if step["operation"] == "store-and-forget":
            extra = "<p>第二客户端按同一 ID 读取结果：null。这里只删除自己新建的公开演练记录。</p>"
        sections.append('<section><div class="tag">' + str(index) + ' · PASS · ' + esc(step["client"]) + '</div><h2>' + esc(label) + '</h2><p class="fact">' + esc(detail) + '</p>' + extra + '</section>')
    return '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>记忆纠正与接棒准备 · 真实 Sno 服务演练</title><style>
*{box-sizing:border-box}body{margin:0;background:#0a1721;color:#e0ebee;font:16px/1.75 system-ui,sans-serif}main{max-width:960px;margin:auto;padding:30px 18px 64px}h1{font-size:clamp(30px,5vw,47px);line-height:1.25}h2{font-size:23px;line-height:1.4}a{color:#6fe4bd;overflow-wrap:anywhere}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:18px}section,.notice{border:1px solid #294352;border-radius:17px;padding:23px;background:#11232f;min-width:0}.notice{margin:24px 0;background:#18352f;border-color:#397b61}.tag{color:#73dcaf;font-size:14px;font-weight:700}.fact{border-left:3px solid #6fe4bd;padding-left:14px;overflow-wrap:anywhere}code{overflow-wrap:anywhere}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#071019;padding:15px;border-radius:9px}footer{margin-top:36px;color:#a9bec6}a:focus-visible{outline:3px solid #dca84a;outline-offset:4px}</style><main>
<p class="tag">COGINE · LOCAL MEMORY REHEARSAL</p><h1>旧事实保留历史，新客户端取回修订后的版本</h1><div class="notice"><strong>真实 Sno 1.6.0 内存服务演练，未调用真实 Agent。</strong><p>数据是原创公开练习：将虚构交接日期从 10 月 30 日改为 10 月 31 日。writer / reader 是两个 API 客户端，不是 Codex、OpenClaw 或人的实际会话。没有读取真实记忆、自动接棒或夜间学习。</p></div>
<p>已运行：Local First · 加密 SQLite · 本地 embedding · store / get / correct / history / recall / forget。重排关闭；全部模型调用关闭；遥测关闭。记录日期：''' + esc(receipt["testedAt"]) + '''。</p><div class="grid">''' + "".join(sections) + '''</div><section style="margin-top:24px"><h2>两种重放，边界不同</h2><pre><code>python3 reproduce.py --verify
python3 reproduce.py --run --runtime /path/to/isolated-runtime --out /tmp/memory-replay</code></pre><p>第一条离线核对公开输入、已记录结果与 HTML，不重新运行 Sno。第二条实际启动新的隔离 profile，在本机重跑服务与内存操作；首次会下载约 639MB embedding 模型。不会安装 Agent 或修改全局配置。运行完成后删除临时 profile 和随机密钥，只导出白名单公开字段。</p><p><a href="fixture.json">公开输入</a> · <a href="receipt.json">实际运行结果</a> · <a href="reproduce.py" download>重放脚本</a> · <a href="run-memory.mjs" download>真实服务入口</a> · <a href="LICENSE-upstream.txt">Apache-2.0 许可</a></p></section>
<footer>由 Cogine 编写公开演练与展示适配，基础服务来自 <a href="https://github.com/sno-ai/sno-station/tree/''' + COMMIT + '''">Sno Station v1.6.0</a>。<p><a href="https://www.opcboost.com/usecases/memory/cross-agent-memory-handoff/">返回完整教程</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">案例仓库</a> · <a href="https://www.cogine.ai/">Cogine</a></p></footer></main></html>'''


def render_preview(receipt):
    passed = receipt["status"] == "passed"
    fixture = read_json(ROOT / "fixture.json")
    accent = "#71d5ae" if passed else "#e6bb75"
    status = "真实服务操作已复现 · 真实 Agent 未测试" if passed else "实验：依赖安装未完成 · 运行未通过"
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720"><rect width="1280" height="720" fill="#0a1721"/><g font-family="system-ui,sans-serif"><text x="64" y="65" font-size="20" fill="' + accent + '">COGINE · SNO STATION v1.6.0</text><text x="64" y="132" font-size="42" font-weight="700" fill="#e0ebee">共享记忆接棒，先检查纠正与取回</text><text x="64" y="176" font-size="22" fill="#a7bbc5">公开输入派生预览 · 非截图 · 演练日期不是公司承诺</text>']
    for index, (title, value) in enumerate([( "v1 原创演练记忆", fixture["original"]), ("v2 修订" + ("结果" if passed else "目标，尚未运行"), fixture["corrected"]) ]):
        x = 64 + index * 590
        parts.append(f'<rect x="{x}" y="226" width="564" height="300" rx="22" fill="#112936" stroke="#345467"/><text x="{x+25}" y="280" font-size="25" font-weight="700" fill="{accent}">{html.escape(title)}</text>')
        for line, text in enumerate(textwrap.wrap(value, width=35)):
            parts.append(f'<text x="{x+25}" y="{335+line*42}" font-size="24" fill="#e0ebee">{html.escape(text)}</text>')
    parts.append('<text x="64" y="593" font-size="27" font-weight="700" fill="' + accent + '">' + html.escape(status) + '</text><text x="64" y="643" font-size="22" fill="#a7bbc5">Local First 隔离入口 · 无模型生成 · 不读取真实会话</text><text x="64" y="682" font-size="20" fill="#a7bbc5">writer / reader 是 API 客户端；不冒充 Codex / OpenClaw 自动接棒</text></g></svg>')
    return ''.join(parts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--run", action="store_true", help="actually run Sno with an already prepared isolated dependency prefix")
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--node", default="node")
    parser.add_argument("--out", type=Path, help="write a new standalone delivery directory")
    parser.add_argument("--record", action="store_true", help="authoring: replace receipt and preview with a new real service run")
    args = parser.parse_args()
    if args.out and args.out.exists():
        parser.error("--out must not exist; refusing to overwrite unrelated work")
    if args.run and not args.runtime:
        parser.error("--run requires --runtime; no implicit installation or global configuration")
    if args.record and not args.run:
        parser.error("--record requires --run; cannot manufacture a successful receipt")
    if args.run:
        with tempfile.TemporaryDirectory(prefix="sno-public-rehearsal-") as temporary:
            scratch = Path(temporary)
            result = scratch / "result.json"
            command = [args.node, str(ROOT / "run-memory.mjs"), str(args.runtime.resolve()), str(scratch / "profile"), str(result)]
            child = subprocess.Popen(command, start_new_session=True)
            try:
                code = child.wait(timeout=600)
                if code:
                    raise subprocess.CalledProcessError(code, command)
            finally:
                # This group was created only for our Node runner and its foreground sidecar.
                # Stop it before TemporaryDirectory removes the profile and its random key.
                try:
                    os.killpg(child.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
                try:
                    child.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid, signal.SIGKILL)
                    child.wait()
            receipt = read_json(result)
        receipt["fixtureSha256"] = hashlib.sha256((ROOT / "fixture.json").read_bytes()).hexdigest()
    else:
        receipt = read_json(ROOT / "receipt.json")
    validate(receipt)
    page = render(receipt)
    preview = render_preview(receipt)
    if args.record:
        (ROOT / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (ROOT / "index.html").write_text(page, encoding="utf-8")
        (ROOT / "preview.svg").write_text(preview, encoding="utf-8")
    elif args.out:
        args.out.mkdir(parents=True)
        for name in ("fixture.json", "reproduce.py", "run-memory.mjs", "package.json", "LICENSE-upstream.txt", "NOTICE-upstream.txt"):
            shutil.copyfile(ROOT / name, args.out / name)
        if (ROOT / "package-lock.json").exists():
            shutil.copyfile(ROOT / "package-lock.json", args.out / "package-lock.json")
        (args.out / "receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (args.out / "index.html").write_text(page, encoding="utf-8")
        (args.out / "preview.svg").write_text(preview, encoding="utf-8")
    elif not args.run and page != (ROOT / "index.html").read_text(encoding="utf-8"):
        raise ValueError("generated preview differs from the committed artifact")
    elif not args.run and preview != (ROOT / "preview.svg").read_text(encoding="utf-8"):
        raise ValueError("derived SVG differs from the public fixture preview")
    print("PASS: " + ("real isolated Sno service rehearsal; no actual Agent called" if args.run else "offline public input / recorded status / preview match; Sno was not rerun") + ("; memory operations remain UNVERIFIED" if receipt.get("status") == "blocked" else ""))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print("FAIL:", error, file=sys.stderr)
        raise SystemExit(1)

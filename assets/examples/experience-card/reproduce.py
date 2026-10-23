#!/usr/bin/env python3
"""Replay Easel's unchanged new/revise CLI with public-page rehearsal inputs.

Python standard library only. No network, model, OpenClaw, or interview is used.
Default: verify the checked-in artifacts. --out: create a new artifact folder.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
UPSTREAM_SHA = "a097ddfbb704c9d1eeb1db49a056fdbca9c2351a"
TOPIC = "网站研究文档404修复演练"
ARTIFACTS = ("card-v1.md", "card-v2.md", "gallery.html")


def read_json(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def make_gallery(versions, provenance):
    payload = json.dumps({"versions": versions, "provenance": provenance}, ensure_ascii=False)
    payload = payload.replace("<", "\\u003c")
    return GALLERY.replace("__CARD_DATA__", payload)


def replay():
    provenance = read_json("provenance.json")
    assert provenance["upstream_commit"] == UPSTREAM_SHA, "Unexpected upstream revision"
    for name, digest in provenance["upstream_files_unmodified"].items():
        actual = hashlib.sha256((HERE / "upstream" / name).read_bytes()).hexdigest()
        assert actual == digest, f"Vendored upstream file changed: {name}"
    initial, revision = read_json("input-v1.json"), read_json("input-v2.json")
    card_cli = HERE / "upstream/skills/builtin/skill-record-card/scripts/card.py"
    with tempfile.TemporaryDirectory(prefix="easel-card-replay-") as directory:
        scratch = Path(directory)
        env = {**os.environ, "EASEL_ROOT": str(scratch), "PYTHONDONTWRITEBYTECODE": "1"}

        def call(*args):
            result = subprocess.run([sys.executable, str(card_cli), *args], cwd=scratch,
                                    env=env, text=True, capture_output=True)
            if result.returncode:
                raise RuntimeError(f"card.py {args[0]} failed: {result.stderr or result.stdout}")
            return result.stdout

        call("selftest")
        created = json.loads(call("new", "--topic", TOPIC, "--data", str(HERE / "input-v1.json"),
                                  "--date", provenance["fixture_date"]))
        assert created["card"] == "card-001" and created["version"] == 1
        card_path = Path(created["path"])
        assert card_path.resolve().is_relative_to(scratch.resolve())
        v1 = card_path.read_text(encoding="utf-8")
        args = ["revise", "--topic", TOPIC, "--card", "001", "--date", provenance["fixture_date"],
                "--change", revision["change"]]
        for field, value in revision["fields"].items():
            args.extend(["--" + field.replace("_", "-"), value])
        if revision["replace_ai_notes"]:
            args.append("--replace-ai-notes")
        for note in revision["ai_notes"]:
            args.extend(["--ai-note", note])
        revised = json.loads(call(*args))
        assert revised["card"] == "card-001" and revised["version"] == 2
        v2 = card_path.read_text(encoding="utf-8")
        assert call("show", "--topic", TOPIC, "--card", "001").strip() == v2.strip()
        listing = call("list", "--topic", TOPIC)
        assert "card-001" in listing and "v2" in listing and "card-002" not in listing

        # Read the actual outputs through the pinned upstream parser, not a second renderer.
        previous_root = os.environ.get("EASEL_ROOT")
        previous_bytecode = sys.dont_write_bytecode
        os.environ["EASEL_ROOT"] = str(scratch)
        sys.dont_write_bytecode = True
        try:
            upstream = runpy.run_path(str(card_cli))
            first = upstream["parse_versions"](v1)
            versions = upstream["parse_versions"](v2)
        finally:
            sys.dont_write_bytecode = previous_bytecode
            if previous_root is None:
                os.environ.pop("EASEL_ROOT", None)
            else:
                os.environ["EASEL_ROOT"] = previous_root
        assert [version["num"] for version in versions] == [1, 2]
        assert versions[0] == first[0], "Revision changed historical v1"
        assert versions[0]["quotes"] == versions[1]["quotes"] == [], "No user interview quotes exist"
        for field in upstream["FIELDS"]:
            assert versions[0]["fields"][field] == initial[field]
            assert versions[1]["fields"][field] == revision["fields"].get(field, initial[field])
        assert versions[1]["ai_notes"] == revision["ai_notes"]
        assert versions[0]["ai_notes"] == initial["ai_notes"]
        # Normalize only trailing blank lines in the published Markdown copies.
        return {"card-v1.md": v1.rstrip("\n") + "\n", "card-v2.md": v2.rstrip("\n") + "\n",
                "gallery.html": make_gallery(versions, provenance)}


GALLERY = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>一次404修复，怎样变成两版经验卡</title>
<style>
:root{color-scheme:light;font-family:system-ui,-apple-system,"PingFang SC",sans-serif;color:#172820;background:#f5f4ef}
*{box-sizing:border-box}body{margin:0}main{max-width:1120px;margin:auto;padding:48px 24px 72px}
header{border-bottom:1px solid #bcc8bd;padding-bottom:28px}h1{font-size:clamp(28px,5vw,48px);letter-spacing:-.04em;line-height:1.15;margin:14px 0}
.eyebrow{font-size:12px;letter-spacing:.1em;color:#456450}.lead{max-width:750px;line-height:1.8;color:#45604f}
.boundary{background:#fff0d8;border-left:4px solid #996b29;padding:14px 18px;font-size:14px;line-height:1.8}
nav{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:28px 0 20px}button{cursor:pointer;padding:11px 18px;border:1px solid #a4b9aa;border-radius:6px;background:transparent;font:inherit;color:inherit}
button[aria-pressed="true"]{background:#173e2b;color:#fff;border-color:#173e2b}.hint{font-size:13px;color:#536b5b}
.columns{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;align-items:start}.columns>*{min-width:0}.card{background:white;border:1px solid #d4ded3;border-radius:10px;padding:24px;margin-bottom:16px}
h2{font-size:19px;margin:0 0 16px}h3{font-size:14px;color:#456450;margin:24px 0 8px}.text{white-space:pre-wrap;line-height:1.85;margin:0;overflow-wrap:anywhere}
.tag{display:inline-block;background:#e4efe6;color:#244f35;padding:4px 8px;font-size:12px;border-radius:4px;margin-bottom:8px}
.source{padding-bottom:15px;margin-bottom:15px;border-bottom:1px solid #e0e7de;font-size:13px;line-height:1.8;overflow-wrap:anywhere}.source a,a{color:#145a40;text-underline-offset:3px}
.notes{background:#f1f5ef}.notes li{line-height:1.85;margin:10px 0}.change{font-size:13px;line-height:1.7;color:#685832}.meta{font-size:12px;color:#5d7061;line-height:1.8}
footer{border-top:1px solid #bcc8bd;padding-top:20px;margin-top:30px;font-size:12px;line-height:1.9;color:#536b5b}
@media(max-width:780px){main{padding:28px 16px 48px}.columns{grid-template-columns:1fr}.card{padding:20px}}
</style></head><body><main>
<header><div class="eyebrow">COGINE · OPENCLAW 维护者演练</div><h1>一次 404 修复，<br>怎样变成两版经验卡</h1>
<p class="lead">维护者用本项目已完成的链接修复作演练：把公开观察整理成 v1，再用同一张卡的 revise 加入证据边界，保留完整历史。页面内容来自实际运行 Easel card.py 后的文件。</p>
<div class="boundary">这是公开资料的维护者演练，未进行用户口述访谈。所有结构化正文与编辑建议均由助手整理；没有受访者采纳确认，不能当作本人经验终稿。</div></header>
<nav aria-label="卡片版本"><button type="button" data-version="1" aria-pressed="false">v1 · 整理修复事实</button><button type="button" data-version="2" aria-pressed="true">v2 · 补上证据边界</button><span class="hint">同一卡片升级；v1 原文保留</span></nav>
<div class="columns"><section><article class="card"><span class="tag" id="version-label"></span><h2 id="card-heading"></h2><p class="change" id="change"></p><div id="fields"></div></article>
<article class="card notes"><h2>AI 补充与提炼 · 未经受访者确认</h2><ul id="notes"></ul><h3>用户原话</h3><p class="text">无。没有用模拟回答冒充用户口述；脚本 Markdown 的空摘录占位不表示发生过访谈。</p></article></section>
<aside><article class="card"><h2>公开事实与出处</h2><div id="sources"></div><p class="meta">F4 是本轮直接访问旧路径的 404，只作文字记录；页面当前实际链接使用 F2 的 GitHub 目标。单个链接观察不代表全站审计。</p></article>
<article class="card"><h2>下载与复现</h2><p class="text"><a href="card-v1.md">v1 Markdown</a><br><a href="card-v2.md">v2 Markdown（含完整 v1）</a><br><a href="input-v1.json">v1 输入</a> · <a href="input-v2.json">v2 修订输入</a><br><a href="reproduce.py">离线复现脚本</a> · <a href="provenance.json">固定版本与来源</a></p></article></aside></div>
<footer>Easel skill-record-card · 固定提交 a097ddfbb704c9d1eeb1db49a056fdbca9c2351a。上游两份 Python 脚本未修改，按 Apache-2.0 保留；本页面与演练输入由本仓库制作。<br>页面自含，无外链加载资源；建卡与修订不调用模型。<a href="LICENSE.apache-2.0.txt">上游许可</a></footer>
</main><script type="application/json" id="card-data">__CARD_DATA__</script><script>
const data=JSON.parse(document.getElementById('card-data').textContent);
const labels={point:'核心要点',mechanism:'机理',method:'具体方法',scope_use:'使用范围 · 适用',scope_nouse:'使用范围 · 不适用'};
function render(number){const version=data.versions.find(item=>item.num===number);
 document.getElementById('version-label').textContent='v'+version.num+' · '+version.day+' · 脚本真实产物';
 document.getElementById('card-heading').textContent=number===1?'把修复经过写清楚':'区分文件、链接与版本证据';
 document.getElementById('change').textContent=version.change||'初版：公开事实的结构化整理，适用边界为助手编辑建议。';
 const fields=document.getElementById('fields');fields.replaceChildren();
 for(const [key,label] of Object.entries(labels)){const heading=document.createElement('h3');heading.textContent=label;const p=document.createElement('p');p.className='text';p.textContent=version.fields[key];fields.append(heading,p);}
 const notes=document.getElementById('notes');notes.replaceChildren();for(const text of version.ai_notes){const li=document.createElement('li');li.textContent=text;notes.append(li);}
 for(const button of document.querySelectorAll('[data-version]'))button.setAttribute('aria-pressed',String(Number(button.dataset.version)===number));}
for(const button of document.querySelectorAll('[data-version]'))button.addEventListener('click',()=>render(Number(button.dataset.version)));
const sources=document.getElementById('sources');for(const fact of data.provenance.facts){const item=document.createElement('div');item.className='source';const p=document.createElement('p');p.textContent=fact.id+' · '+fact.text;item.append(p);if(fact.source){const a=document.createElement('a');a.href=fact.source;a.textContent='查看公开来源';a.target='_blank';a.rel='noopener noreferrer';item.append(a);}else if(fact.observed_path){const code=document.createElement('code');code.textContent='观察到的旧路径：'+fact.observed_path;item.append(code);}sources.append(item);}
render(2);
</script></body></html>
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--out", type=Path, help="Create a new output directory; never overwrite")
    group.add_argument("--verify", action="store_true", help="Verify checked-in outputs (default)")
    args = parser.parse_args()
    if args.out and args.out.exists():
        parser.error("--out must name a new directory")
    artifacts = replay()
    if args.out:
        args.out.mkdir(parents=True, exist_ok=False)
        for name, text in artifacts.items():
            (args.out / name).write_text(text, encoding="utf-8")
        # Keep gallery downloads functional in a standalone replay folder.
        for name in ("input-v1.json", "input-v2.json", "provenance.json", "LICENSE.apache-2.0.txt", "reproduce.py"):
            shutil.copyfile(HERE / name, args.out / name)
        shutil.copytree(HERE / "upstream", args.out / "upstream", ignore=shutil.ignore_patterns("__pycache__"))
        print("PASS: upstream selftest/new/revise/list/show; v1 history and attribution retained; artifacts written.")
    else:
        for name, text in artifacts.items():
            assert (HERE / name).read_text(encoding="utf-8") == text, f"Artifact differs: {name}"
        print("PASS: upstream hashes, CLI replay, five fields, inherited v1, replaced v2 notes, and all 3 artifacts match.")


if __name__ == "__main__":
    main()

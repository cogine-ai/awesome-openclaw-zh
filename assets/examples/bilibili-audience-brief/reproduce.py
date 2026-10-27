#!/usr/bin/env python3
"""Build a source-labelled audience-to-topic brief. Default: committed input only.

--refresh uses only anonymous `video info` and first-page `comment list` reads.
It neither installs a skill nor opens the user's Bilibili credentials/configuration.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
REPOSITORY = "kukemc/bili-cli"
REVISION = "e17ab4da33a5b32a5fb4706e0a6dbb9ed994085a"
VERSION = "1.2.1"
INPUT = ROOT / "audience-input.json"
TOPICS = (
    ("setup", "安装失败时，先判断是哪一层", ("安装", "报错", "错误", "windows", "npm", "网络"),
     "用三个真实失败入口演示环境、依赖与Gateway的区别，逐项给出成功回执。", "诊断清单 + 一次失败到恢复的演示"),
    ("connect", "接入聊天渠道以后，怎样确认真的通了", ("飞书", "微信", "钉钉", "接入", "回调"),
     "把创建应用、接入、收消息与回消息分开验收，使用测试群与虚构消息。", "最小测试群回执 + 接入检查表"),
    ("cost", "先算清一次任务的模型与媒体成本", ("费用", "收费", "免费", "token", "额度", "api"),
     "区分聊天订阅、API额度和视频服务费用；展示自己的计费记录，不猜测观众预算。", "一次任务的带范围成本表"),
    ("use", "安装完成后，交付第一份能保存的成果", ("怎么用", "用途", "工作", "用处", "做什么"),
     "用公开测试素材完成一份可下载成果，给出输入、操作、输出与人工验收。", "可复现输入 + 实际成果文件"),
)


def qualified_question(text):
    # A topic word in a giveaway/advertisement is not an audience pain point.
    if len(text.strip()) < 5 or re.search(r"抱走|商单|学习咨询|点击获取|http|敲.{0,6}666", text, re.I):
        return False
    return bool(re.search(r"[？?]|怎么|为什么|报错|错误|无法|不能|不支持|多少|费用|怎样", text))


def validate_snapshot(data):
    if data.get("mode") not in {"live-public", "fixture"}:
        raise ValueError("Input mode must explicitly be live-public or fixture")
    if data.get("upstream", {}).get("revision") != REVISION:
        raise ValueError("Unexpected upstream revision")
    video = data.get("video", {})
    comments = data.get("comments", [])
    if not isinstance(comments, list) or not comments or len(comments) > 20:
        raise ValueError("Expected 1–20 bounded comment inputs")
    if data["mode"] == "live-public":
        bvid = video.get("bvid", "")
        if not re.fullmatch(r"BV[0-9A-Za-z]{10}", bvid):
            raise ValueError("Public snapshot needs a valid BV id")
        if video.get("url") != f"https://www.bilibili.com/video/{bvid}":
            raise ValueError("Unexpected public video URL")
        if data.get("collection", {}).get("anonymous") is not True:
            raise ValueError("Public collection must explicitly be anonymous")
    elif video.get("url") or video.get("bvid") or video.get("stat"):
        raise ValueError("A fixture must not impersonate a real video or its metrics")
    ids = set()
    for row in comments:
        ident, text = row.get("id"), row.get("text")
        if not isinstance(ident, str) or ident in ids or not isinstance(text, str) or not text.strip():
            raise ValueError("Missing/duplicate comment id or empty text")
        if len(text) > 180:
            raise ValueError("Comment excerpts must be bounded")
        if data["mode"] == "live-public" and not ident.isdigit():
            raise ValueError("Public comment id must be an actual rpid")
        if "user" in row or "mid" in row or "name" in row:
            raise ValueError("This brief does not publish audience identities")
        ids.add(ident)
    return data


def build_topics(snapshot):
    validate_snapshot(snapshot)
    topics = []
    for ident, title, words, angle, artifact in TOPICS:
        matches = [row for row in snapshot["comments"] if qualified_question(row["text"])
                   and any(word in row["text"].lower() for word in words)]
        if matches:
            topics.append({"id": ident, "title": title, "angle": angle, "artifact": artifact,
                           "evidence": [row["id"] for row in matches], "count": len(matches)})
    return sorted(topics, key=lambda row: (-row["count"], row["id"]))[:3]


def read_cli(binary, arguments, state_dir):
    # Each argv is constructed by this file. No user-supplied shell or write command.
    env = {**os.environ, "BILI_CLI_HOME": str(state_dir), "BILI_CLI_TIMEOUT": "25",
           "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1"}
    result = subprocess.run([str(binary), "--compact", *arguments], env=env, capture_output=True,
                            text=True, encoding="utf-8", timeout=35, check=False)
    try:
        payload = json.loads(result.stdout)
    except ValueError as error:
        raise ValueError("Bili CLI did not return JSON; existing snapshot is preserved") from error
    if result.returncode or payload.get("ok") is not True:
        error = payload.get("error", {})
        raise ValueError(f"Anonymous read failed ({error.get('code', 'unknown')}): {error.get('message', '')}")
    return payload["data"]


def collect(binary, bvid):
    if not re.fullmatch(r"BV[0-9A-Za-z]{10}", bvid):
        raise ValueError("Pass a BV id, not a command or arbitrary URL")
    with tempfile.TemporaryDirectory(prefix="bili-anonymous-") as directory:
        state = Path(directory)
        version = read_cli(binary, ["--version"], state)
        if version.get("version") != VERSION:
            raise ValueError(f"Expected bili-agent {VERSION}; use the pinned source")
        video = read_cli(binary, ["video", "info", bvid], state)
        comments = read_cli(binary, ["comment", "list", bvid, "--page", "1", "--sort", "hot"], state)
        if video.get("bvid") != bvid:
            raise ValueError("Video id mismatch")
        if (state / "credential.json").exists():
            raise ValueError("Anonymous read unexpectedly wrote a credential")
    rows = [{"id": str(row["rpid"]), "text": " ".join(str(row["content"]).split()[:20])[:40]}
            for row in comments.get("items", [])[:12] if row.get("content")]
    snapshot = {"mode": "live-public", "fetchedAt": dt.datetime.now(dt.timezone.utc).isoformat(),
                "upstream": {"repository": REPOSITORY, "revision": REVISION, "version": VERSION},
                "video": {key: video.get(key) for key in ("bvid", "url", "title", "duration", "pubdate", "stat")},
                "comments": rows, "collection": {"anonymous": True, "page": 1, "sort": "hot",
                    "scope": "公开热门评论第一页中的至多12条节选；省略用户身份和楼中楼，不是完整观众调查"}}
    return validate_snapshot(snapshot)


def render(snapshot):
    topics = build_topics(snapshot)
    esc = lambda value: html.escape(str(value), quote=True)
    fixture = snapshot["mode"] == "fixture"
    badge = "虚构观众提问 · fixture演练" if fixture else "真实公开数据 · 匿名读取快照"
    scope = "本页输入为明确虚构的课堂素材，不是实抓评论，不代表真实受众或平台趋势。" if fixture else snapshot["collection"]["scope"]
    qualified = sum(qualified_question(row["text"]) for row in snapshot["comments"])
    by_id = {row["id"]: row for row in snapshot["comments"]}
    cards, markdown = [], ["# 观众提问 → 下期选题简报", "", badge, "", scope, "",
                            f'输入{len(snapshot["comments"])}条，合格提问{qualified}条，形成{len(topics)}条选题提案。', ""]
    for index, topic in enumerate(topics, 1):
        quotes = "".join(f'<li><code>{esc(ident)}</code> {esc(by_id[ident]["text"])}</li>' for ident in topic["evidence"][:2])
        cards.append(f'<article><span class="num">0{index}</span><p class="eyebrow">样本内 {topic["count"]} 条相关输入 · 可重复归类</p><h2>{esc(topic["title"])}</h2><p>{esc(topic["angle"])}</p><p class="deliver"><b>最小成果</b><br>{esc(topic["artifact"])}</p><details><summary>查看选题依据</summary><ul>{quotes}</ul></details></article>')
        markdown += [f'## {index}. {topic["title"]}', "", topic["angle"], f'最小成果：{topic["artifact"]}',
                     '依据ID：' + '、'.join(topic["evidence"]), ""]
    if not cards:
        markdown += ["样本不足，暂不生成选题；资料推广、口令和没有明确问题的回复不作为需求依据。", ""]
        cards.append('<article><h2>样本不足，暂不生成选题</h2><p>本次未发现可归类的观众问题。资料推广、口令和无具体问题的回复不会被当成需求；不从视频播放量推断选题有市场。</p><p><a href="fixture.html">切换到明确虚构的提问演练 →</a></p></article>')
    source = ('无真实视频链接；输入完全虚构。' if fixture else
              f'<a href="{esc(snapshot["video"]["url"])}" rel="noreferrer">{esc(snapshot["video"]["title"])}</a>')
    refs = "".join(f'<li id="evidence-{esc(row["id"])}"><code>{esc(row["id"])}</code> {esc(row["text"])} <small>— {"纳入问题归类" if qualified_question(row["text"]) else "未纳入：没有明确问题或属于推广/口令"}</small></li>' for row in snapshot["comments"])
    document = f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>观众提问 → 下期选题简报</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#f3f4ef;color:#172e2b;font:16px/1.7 system-ui,sans-serif}}main{{max-width:1160px;margin:auto;padding:44px 22px}}header{{max-width:860px}}h1{{font-size:clamp(30px,5vw,55px);line-height:1.2;margin:18px 0}}.eyebrow{{font-size:12px;letter-spacing:.07em;color:#526c65}}.badge{{display:inline-block;background:#ffe1a6;border:1px solid #a77216;border-radius:8px;padding:5px 12px;font-weight:700}}.scope{{border-left:4px solid #b57b25;padding:8px 16px;background:#fff7e8}}.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:30px 0}}article{{min-width:0;background:white;border:1px solid #d5ded7;border-radius:18px;padding:24px;box-shadow:0 6px 22px #153d3010}}h2{{font-size:23px;line-height:1.4}}.num{{font-size:30px;color:#558b73;font-weight:800}}.deliver{{padding:13px;background:#edf5ef;border-radius:10px}}a{{color:#006e61}}li{{overflow-wrap:anywhere;margin:10px 0}}details{{margin-top:18px}}summary{{cursor:pointer}}.notes{{padding:22px;background:#e6ede7;border-radius:16px}}code{{font-size:12px}}footer{{font-size:13px;margin-top:30px;color:#526c65}}@media(max-width:850px){{.grid{{grid-template-columns:1fr}}main{{padding:26px 16px}}}}</style>
<main><header><p class="eyebrow">COGINE / OPENCLAW CONTENT LAB</p><span class="badge">{badge}</span><h1>先听见问题，<br>再决定下一期拍什么。</h1><p class="scope">{esc(scope)}</p><p>样本：{len(snapshot["comments"])}条 · 合格提问：{qualified}条 · 主题：{len(topics)}个 · 采样／制作日期：{esc(snapshot["fetchedAt"])}</p><p><a href="index.html">真实公开样本</a> · <a href="fixture.html">虚构提问演练</a></p></header><section class="grid">{''.join(cards)}</section><section class="notes"><h2>这是编辑简报，不是受众画像</h2><p>关键词归类可复现，一条留言可属于多个主题。条数是本样本内的留言数，不是独立人数、需求比例、增长率或转化预测。选题角度由本案例编辑规则提出，尚未发布或验证流量。</p><p>来源：{source}</p><details><summary>全部输入与出处</summary><ol>{refs}</ol></details><p><a href="{'fixture-input.json' if fixture else 'audience-input.json'}">输入JSON</a> · <a href="{'fixture-brief.md' if fixture else 'topic-brief.md'}">Markdown简报</a> · <a href="reproduce.py">复现脚本</a></p></section><footer>固定上游：{REPOSITORY}@{REVISION[:12]} / bili-agent {VERSION}。脚本只读本地输入或匿名公开页面；未运行OpenClaw会话，也没有登录、私信、互动或投稿。</footer></main></html>'''
    markdown += ["## 来源与边界", "", scope, snapshot["video"].get("url") or "无真实视频链接（fixture）",
                 "", "归类为规则输出，选题角度为编辑提案；未发布、未验证增长。"]
    return document, "\n".join(markdown) + "\n"


def preview(snapshot):
    count = len(snapshot["comments"])
    questions = sum(qualified_question(row["text"]) for row in snapshot["comments"])
    topics = len(build_topics(snapshot))
    label = "真实公开样本" if snapshot["mode"] == "live-public" else "明确虚构的fixture"
    outcome = "样本不足，不硬造需求" if not topics else "规则归类，编辑提案待验证"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" role="img" aria-label="观众提问选题简报预览"><rect width="1200" height="630" fill="#edf2ec"/><rect x="56" y="48" width="1088" height="534" rx="25" fill="#fff" stroke="#bfd1c4"/><g font-family="system-ui,sans-serif" fill="#173f36"><text x="94" y="110" font-size="24">COGINE / BILIBILI CONTENT LAB</text><text x="94" y="190" font-size="48" font-weight="700">先听见问题，再决定拍什么</text><text x="94" y="240" font-size="23">{label} · 2026-10-27 · 匿名读取</text><text x="94" y="350" font-size="62" font-weight="700">{count} 条输入 → {questions} 条提问 → {topics} 条选题</text><text x="94" y="420" font-size="31" fill="#9c651a">{outcome}</text><text x="94" y="500" font-size="21">另附独立标记的虚构提问演练；未发布、未验证转化。</text></g></svg>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--bili", type=Path, help="Pinned temporary venv's bili executable")
    parser.add_argument("--video", default="BV1dCEX64EyY")
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    args = parser.parse_args()
    if args.refresh and not args.bili:
        parser.error("--refresh requires --bili; no global executable is selected implicitly")
    snapshot = collect(args.bili, args.video) if args.refresh else json.loads(INPUT.read_text(encoding="utf-8"))
    document, brief = render(snapshot)  # Validate everything before changing existing outputs.
    args.output_dir.mkdir(parents=True, exist_ok=True)
    fixture = json.loads((ROOT / "fixture-input.json").read_text(encoding="utf-8"))
    if fixture.get("mode") != "fixture":
        raise ValueError("The separate demonstration must remain labelled fixture")
    fixture_document, fixture_brief = render(fixture)
    outputs = {"index.html": document, "topic-brief.md": brief, "preview.svg": preview(snapshot),
               "fixture.html": fixture_document, "fixture-brief.md": fixture_brief}
    if args.refresh:
        outputs["audience-input.json"] = json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"
    for name, text in outputs.items():
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=args.output_dir, delete=False) as handle:
            handle.write(text)
            temporary = handle.name
        os.replace(temporary, args.output_dir / name)
    print(f'Built {len(build_topics(snapshot))} topic proposals from {snapshot["mode"]}; no publishing.')


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Render selected public project data with pinned upstream profile-card renderers.

Default: reuse public-repositories.json. --refresh: read the named public repo via gh.
No token is read by this script. gh handles its own authentication.
"""
import argparse
import datetime as dt
import html
import importlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import xml.etree.ElementTree as ET

UPSTREAM = "mgkvibez/openclaw-profile-cards"
REVISION = "bc589498e4cb72dbe29de5121f5009eb95b5a22c"
REPOSITORIES = ("awesome-openclaw-zh",)
ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "public-repositories.json"
FIELDS = """
  nameWithOwner url isPrivate createdAt pushedAt isArchived diskUsage
  stargazerCount forkCount primaryLanguage { name }
  languages(first: 20, orderBy: {field: SIZE, direction: DESC}) {
    totalCount edges { size node { name } }
  }
  defaultBranchRef { name target { ... on Commit {
    history { totalCount }
    recent: history(first: 100) { nodes { committedDate } }
  } } }
"""


def refresh():
    query = "query {" + "\n".join(
        f'r{i}: repository(owner: "cogine-ai", name: "{name}") {{ {FIELDS} }}'
        for i, name in enumerate(REPOSITORIES)
    ) + "}"
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", "query=" + query],
        text=True, capture_output=True, check=False,
    )
    if result.returncode:
        raise SystemExit("GitHub read failed; check gh auth status and API connectivity.")
    payload = json.loads(result.stdout)
    if payload.get("errors"):
        raise SystemExit("GitHub returned GraphQL errors; snapshot was not changed.")
    repos = [payload["data"][f"r{i}"] for i in range(len(REPOSITORIES))]
    for repo, name in zip(repos, REPOSITORIES):
        if not repo or repo["isPrivate"] or repo["nameWithOwner"] != f"cogine-ai/{name}":
            raise SystemExit("Expected only the named public repository.")
        if repo["languages"]["totalCount"] != len(repo["languages"]["edges"]):
            raise SystemExit("Language results were truncated; snapshot was not changed.")
    snapshot = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scope": "Only cogine-ai/awesome-openclaw-zh; not an organization or personal profile total. Non-public repositories are excluded.",
        "api": "https://api.github.com/graphql",
        "commit_sample": "At most 100 latest default-branch commits per repository; committedDate in UTC. Includes merge commits, not unique authors or work hours.",
        "disk_usage": "GitHub diskUsage in KiB; repository storage, not source-code byte count.",
        "language_bytes": "GitHub languages edges.size; tracked language bytes, not prose/case counts.",
        "repositories": repos,
    }
    return snapshot


def data_for_renderers(snapshot):
    now = dt.datetime.fromisoformat(snapshot["fetched_at"].replace("Z", "+00:00"))
    repos, languages, commits = [], {}, []
    for repo in snapshot["repositories"]:
        if repo["isPrivate"] or repo["nameWithOwner"] not in {
            f"cogine-ai/{name}" for name in REPOSITORIES
        }:
            raise ValueError("Snapshot must contain only the selected public repositories.")
        name = repo["nameWithOwner"].split("/", 1)[1]
        branch = repo.get("defaultBranchRef") or {}
        target = branch.get("target") or {}
        pushed = dt.datetime.fromisoformat(repo["pushedAt"].replace("Z", "+00:00"))
        repos.append({
            "name": name, "private": False, "stars": repo["stargazerCount"],
            "language": (repo["primaryLanguage"] or {}).get("name", "unknown"),
            "pushed_at": repo["pushedAt"], "pushed_days_ago": (now - pushed).days,
            "size_kb": repo["diskUsage"], "commits": target.get("history", {}).get("totalCount", 0),
            "archived": repo["isArchived"],
        })
        languages[name] = {e["node"]["name"]: e["size"] for e in repo["languages"]["edges"]}
        commits.extend({"date": c["committedDate"], "repo": name}
                       for c in target.get("recent", {}).get("nodes", []))
    return {"login": "cogine-ai", "fetched_at": snapshot["fetched_at"],
            "repos": repos, "repo_langs": languages, "commit_sample": commits}


def download_renderers(directory):
    url = f"https://api.github.com/repos/{UPSTREAM}/tarball/{REVISION}"
    request = urllib.request.Request(url, headers={"User-Agent": "Cogine-public-project-cards"})
    with urllib.request.urlopen(request, timeout=45) as response:
        archive_bytes = response.read(20 * 1024 * 1024 + 1)
    if len(archive_bytes) > 20 * 1024 * 1024:
        raise ValueError("Unexpectedly large upstream archive.")
    # Extract only Python modules and the license; no archive paths are trusted.
    with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as archive:
        for member in archive.getmembers():
            parts = Path(member.name).parts[1:]
            if not member.isfile() or not parts or any(p in {".", ".."} for p in parts):
                continue
            relative = Path(*parts)
            if str(relative) != "LICENSE" and not (
                len(parts) == 2 and parts[0] == "cards" and relative.suffix == ".py"
            ):
                continue
            target = directory / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            source = archive.extractfile(member)
            if source is None:
                raise ValueError("Missing upstream archive member.")
            target.write_bytes(source.read())


def render(snapshot, source):
    sys.path.insert(0, str(source))
    theme = importlib.import_module("cards.theme")
    theme.apply("phosphor")
    data = data_for_renderers(snapshot)
    outputs = {}
    for name in ("city", "languages", "rhythm"):
        module = importlib.import_module("cards.card_" + name)
        svg = module.render(data)
        # Only scope/cadence captions change; upstream geometry and metrics are untouched.
        if name == "city":
            svg = svg.replace("rendered hourly in WAT", "one snapshot; sky clock WAT")
        elif name == "languages":
            svg = svg.replace("across every owned non-fork repository", "across the one selected public project repository")
        svg = svg.replace("</svg>", "<metadata>" + html.escape(
            f"Cogine project sample; only cogine-ai/awesome-openclaw-zh; fetched {snapshot['fetched_at']}. "
            f"Generated by {UPSTREAM}@{REVISION}. Scope/cadence captions adapted by Cogine; see LICENSE-upstream.txt."
        ) + "</metadata>\n</svg>")
        xml = ET.fromstring(svg)
        if any(e.tag.rsplit("}", 1)[-1] in {"script", "image", "foreignObject"} for e in xml.iter()):
            raise ValueError("Unexpected active or external SVG content.")
        if any(k.rsplit("}", 1)[-1] in {"href", "src"} for e in xml.iter() for k in e.attrib):
            raise ValueError("Unexpected external SVG reference.")
        outputs[f"{name}.svg"] = svg
    return data, outputs


def gallery(snapshot, data):
    cards = [
        ("city", "一座仓库，一栋开源小楼", "楼高是上游对提交数、Git 存储量、Star 与推送时间的组合排序，不能解释成收入、效率或增长率。本例只有一个公开仓库，因而不作项目间排名。天空沿用作者 WAT（UTC+1）时钟；本页只是一张固定快照。"),
        ("languages", "实际代码语言配比", "仅取这个仓库的 GitHub 语言字节数，不包含 Markdown 正文占比，也不是案例的类型分布。"),
        ("rhythm", "最近提交的时间节奏", "每个仓库最多取默认分支最近 100 条提交，包含合并提交；按 UTC 分组，不是组织贡献日历、人数、工时或过去一年的完整活跃度。"),
    ]
    sections = "".join(f'<section><h2>{title}</h2><p>{note}</p><a href="{name}.svg"><img src="{name}.svg" alt="{title}" loading="lazy"></a><p><a href="{name}.svg" download>下载 SVG</a></p></section>' for name, title, note in cards)
    rows = "".join(f'<tr><td><a href="{r["url"]}">{html.escape(r["nameWithOwner"])}</a></td><td>{r["stargazerCount"]}</td><td>{r["forkCount"]}</td><td>{r["defaultBranchRef"]["target"]["history"]["totalCount"]}</td></tr>' for r in snapshot["repositories"])
    page = f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cogine 开源项目手绘战报</title>
<style>body{{margin:0;background:#071019;color:#dde7ee;font:16px/1.7 system-ui,sans-serif}}main{{max-width:1000px;margin:auto;padding:30px 18px 64px}}h1{{font-size:clamp(28px,5vw,48px);line-height:1.2}}h2{{font-size:23px}}a{{color:#73e7a8}}p{{color:#b6c7d4}}section{{margin:32px 0;padding:20px;background:#0d1924;border:1px solid #223646;border-radius:18px}}img{{display:block;max-width:100%;height:auto;margin:24px auto}}table{{width:100%;border-collapse:collapse;font-size:14px}}th,td{{padding:10px 8px;border-bottom:1px solid #31414f;text-align:left;overflow-wrap:anywhere}}.scroll{{overflow:auto}}code{{overflow-wrap:anywhere}}footer{{margin-top:36px;color:#9aafbf}}a:focus-visible{{outline:3px solid #73e7a8;outline-offset:4px}}@media(prefers-reduced-motion:reduce){{*{{scroll-behavior:auto}}}}</style>
<main><p>COGINE · OPEN SOURCE SNAPSHOT</p><h1>一座公开仓库，三张真实数据卡</h1><p>awesome-openclaw-zh 内容库。采集：<time>{snapshot['fetched_at']}</time>（UTC，台湾时间为 UTC+8）。这是一张固定公开数据快照，没有自动刷新。</p>
<div class="scroll"><table><thead><tr><th>公开仓库</th><th>Stars</th><th>Forks</th><th>默认分支累计提交</th></tr></thead><tbody>{rows}</tbody></table></div><p>统计范围仅限上表一个仓库，不代表 Cogine 组织或任何个人的全部活动；不可公开的仓库未纳入。没有相同口径旧快照，因此不计算 Star 增速。</p>{sections}
<p><a href="public-repositories.json">查看公开 API 数据</a> · <a href="reproduce.py">复现脚本</a> · <a href="LICENSE-upstream.txt">上游 MIT 许可</a></p><footer>由 <a href="https://www.cogine.ai/">Cogine</a> 采集公开数据并组装。SVG 由 <a href="https://github.com/{UPSTREAM}/tree/{REVISION}">Michael Oogwu 的 openclaw-profile-cards</a> 原始渲染器生成；仅修正统计范围、刷新频率说明并添加来源元数据。本页不请求 API、不使用第三方字体或分析脚本。</footer></main></html>'''
    return page


def publish_artifacts(artifacts, snapshot=None):
    """Prepare every file before replacing outputs; commit a refreshed snapshot last."""
    targets = [(ROOT / name, text) for name, text in artifacts.items()]
    if snapshot is not None:
        targets.append((SNAPSHOT, json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n"))
    # The staging directory shares the destination filesystem for atomic replaces.
    with tempfile.TemporaryDirectory(prefix=".render-stage-", dir=ROOT) as directory:
        staged = []
        for index, (target, text) in enumerate(targets):
            source = Path(directory) / str(index)
            source.write_text(text, encoding="utf-8")
            staged.append((source, target))
        for source, target in staged:
            os.replace(source, target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Read and replace the named public repository snapshot through gh.")
    parser.add_argument("--upstream-dir", type=Path, help="Use an existing checkout at the pinned upstream SHA, without downloading code.")
    args = parser.parse_args()
    snapshot = refresh() if args.refresh else json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory(prefix="cogine-cards-render-") as temporary:
        source = args.upstream_dir.resolve() if args.upstream_dir else Path(temporary)
        if args.upstream_dir:
            revision = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip()
            if revision != REVISION:
                raise SystemExit("Upstream checkout must be at " + REVISION)
        else:
            download_renderers(source)
        data, outputs = render(snapshot, source)
        artifacts = {
            **outputs,
            "index.html": gallery(snapshot, data),
            "LICENSE-upstream.txt": (source / "LICENSE").read_text(encoding="utf-8"),
        }
        publish_artifacts(artifacts, snapshot if args.refresh else None)
    print(f"Generated {len(outputs)} SVGs and gallery from {len(data['repos'])} public repositories; {len(data['commit_sample'])} commit timestamps; snapshot {snapshot['fetched_at']}.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Prepare deterministic public source-and-output ZIPs; never publish."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-10-27"
PACKS = {
    "experience-card": "usecases/productivity/experience-interview-record-card.md",
    "github-cards": "usecases/creative/github-handdrawn-project-cards.md",
    "comedy-chase": "usecases/creative/comedy-chase-action-continuity.md",
    "interactive-desktop-coach": "usecases/tools/interactive-desktop-coach.md",
    "cross-agent-memory-handoff": "usecases/memory/cross-agent-memory-handoff.md",
    "digital-human-product-intro": "usecases/creative/digital-human-product-intro.md",
    "bilibili-audience-brief": "usecases/social/bilibili-audience-to-topic-brief.md",
    "blind-agent-copy-arena": "usecases/creative/blind-agent-copy-arena.md",
    "local-decision-snake": "usecases/creative/local-decision-snake-lab.md",
}
PACK_ASSETS = {
    "experience-card": (
        "LICENSE.apache-2.0.txt", "card-v1.md", "card-v2.md", "gallery.html",
        "input-v1.json", "input-v2.json", "provenance.json", "reproduce.py", "preview.svg",
        "upstream/skills/builtin/skill-record-card/scripts/card.py",
        "upstream/skills/shared/scripts/output_paths.py",
    ),
    "github-cards": (
        "LICENSE-upstream.txt", "city.svg", "languages.svg", "rhythm.svg",
        "index.html", "public-repositories.json", "reproduce.py",
    ),
    "comedy-chase": (
        "LICENSE.upstream.txt", "board.html", "project.md", "reproduce.py",
        "seedance-2.0.txt", "seedance-2.5.txt", "帽子比人跑得快-预演故事板.md", "preview.svg",
    ),
    "interactive-desktop-coach": (
        "LICENSE-upstream.txt", "cards/01-open.json", "cards/02-choose.json", "cards/03-check.json",
        "dry-run-results.json", "verification.json", "index.html", "preview.svg", "reproduce.py",
    ),
    "cross-agent-memory-handoff": (
        "LICENSE-upstream.txt", "NOTICE-upstream.txt", "fixture.json", "receipt.json", "package.json",
        "run-memory.mjs", "reproduce.py", "index.html", "preview.svg",
    ),
    "digital-human-product-intro": (
        "LICENSE.upstream.txt", "NOTICE.upstream.md", "THIRD_PARTY.upstream.md", "script.json",
        "persona.offline.json", "draft-tasks.json", "planned-subtitles.srt", "provenance.json",
        "reproduce.py", "upstream/scripts/build_tasks.py", "index.html", "preview.svg",
    ),
    "bilibili-audience-brief": (
        "LICENSE.upstream.txt", "audience-input.json", "fixture-input.json", "topic-brief.md",
        "fixture-brief.md", "index.html", "fixture.html", "preview.svg", "reproduce.py",
    ),
    "blind-agent-copy-arena": (
        "brief.json", "provenance.json", "native-trial.mjs", "test-native.mjs", "reproduce.py",
        "index.html", "preview.svg",
    ),
    "local-decision-snake": (
        "LICENSE.laya.txt", "LICENSE.snake-reference.txt", "scenario.json", "reproduce.py",
        "run.json", "index.html", "preview.svg",
    ),
}
PACK_SHARED = {name: ("scripts/generate-showcase-previews.py",)
               for name in ("experience-card", "comedy-chase")}


def reviewed_files(root):
    """Read an explicit manifest from one clean, committed Git revision."""
    paths = {
        name: sorted(["LICENSE", case, *PACK_SHARED.get(name, ()), *[
            f"assets/examples/{name}/{asset}" for asset in PACK_ASSETS[name]
        ]]) for name, case in PACKS.items()
    }
    selected = sorted({path for pack in paths.values() for path in pack})
    for relative in selected:
        source = root / relative
        path = Path(relative)
        if not source.is_file() or any((root / part).is_symlink() for part in [path, *path.parents]):
            raise ValueError(f"Missing or symlinked release input: {relative}")
    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True, stderr=subprocess.DEVNULL,
        ).strip()
        subprocess.run(["git", "ls-files", "--error-unmatch", "--", *selected],
                       cwd=root, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "diff", "--no-ext-diff", "--quiet", revision, "--", *selected],
                       cwd=root, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Read committed blobs, so a concurrent local edit cannot enter the ZIP.
        content = {path: subprocess.check_output(["git", "show", f"{revision}:{path}"],
                   cwd=root, stderr=subprocess.DEVNULL) for path in selected}
    except subprocess.CalledProcessError as error:
        raise ValueError("Release inputs must be tracked and unchanged from HEAD; commit reviewed changes first") from error
    return {name: {path: content[path] for path in pack} for name, pack in paths.items()}


def write_member(archive, name, content):
    """Stable timestamps, permissions, ordering and compression for a given revision."""
    info = zipfile.ZipInfo(name, date_time=(2026, 10, 27, 0, 0, 0))
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    archive.writestr(info, content, compresslevel=9)


def prepare_assets(root, output):
    if output.exists():
        raise ValueError("--out must name a new directory")
    files = reviewed_files(root)
    output.mkdir(parents=True, exist_ok=False)
    for name, selected in files.items():
        path = output / f"{name}-{DATE}.zip"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for relative, content in selected.items():
                write_member(archive, relative, content)
            write_member(archive, "BUNDLE-SOURCE.json", json.dumps({
                "files": {relative: hashlib.sha256(content).hexdigest() for relative, content in selected.items()},
                "scope": "Reviewed committed public inputs; verification limits are in the case and artifact.",
            }, ensure_ascii=False, indent=2) + "\n")
            preview_command = (f"\n文字预览重建：`python3 scripts/generate-showcase-previews.py --pack {name}`。\n"
                               if name in PACK_SHARED else "")
            case_url = "https://www.opcboost.com/" + PACKS[name].removesuffix(".md") + "/"
            write_member(archive, "START-HERE.md", (
                f"# {name}\n\n解压后从本目录阅读 `{PACKS[name]}`。\n"
                f"输入、实际产物、复现脚本和上游许可在 `assets/examples/{name}/`。\n"
                "先阅读案例的前置条件和验证范围，再执行命令。此包不含模型凭证或已生成视频。\n"
                + preview_command + f"\n[完整教程与更新]({case_url}) · "
                "[案例仓库与共建](https://github.com/cogine-ai/awesome-openclaw-zh) · "
                "[Cogine](https://www.cogine.ai/)\n"
            ))
        print(f"Prepared {path.name}: {len(selected)} source files plus start guide and public file hashes")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="New directory for ZIPs; refuses an existing path")
    args = parser.parse_args()
    try:
        prepare_assets(ROOT, args.out)
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()

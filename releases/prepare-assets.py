#!/usr/bin/env python3
"""Prepare three source-and-output ZIPs for a reviewed release; never publish."""
import argparse
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    "experience-card": "usecases/productivity/experience-interview-record-card.md",
    "github-cards": "usecases/creative/github-handdrawn-project-cards.md",
    "comedy-chase": "usecases/creative/comedy-chase-action-continuity.md",
}
PACK_ASSETS = {
    "experience-card": (
        "LICENSE.apache-2.0.txt", "card-v1.md", "card-v2.md", "gallery.html",
        "input-v1.json", "input-v2.json", "provenance.json", "reproduce.py",
        "upstream/skills/builtin/skill-record-card/scripts/card.py",
        "upstream/skills/shared/scripts/output_paths.py",
    ),
    "github-cards": (
        "LICENSE-upstream.txt", "city.svg", "languages.svg", "rhythm.svg",
        "index.html", "public-repositories.json", "reproduce.py",
    ),
    "comedy-chase": (
        "LICENSE.upstream.txt", "board.html", "project.md", "reproduce.py",
        "seedance-2.0.txt", "seedance-2.5.txt", "帽子比人跑得快-预演故事板.md",
    ),
}


def reviewed_files(root):
    """Read an explicit manifest from one clean, committed Git revision."""
    paths = {
        name: sorted(["LICENSE", case, *[
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


def prepare_assets(root, output):
    if output.exists():
        raise ValueError("--out must name a new directory")
    files = reviewed_files(root)
    output.mkdir(parents=True, exist_ok=False)
    for name, selected in files.items():
        path = output / f"{name}-2026-10-23.zip"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for relative, content in selected.items():
                archive.writestr(relative, content)
            archive.writestr("START-HERE.md", (
                f"# {name}\n\n解压后从本目录阅读 `{PACKS[name]}`。\n"
                f"输入、实际产物、复现脚本和上游许可在 `assets/examples/{name}/`。\n"
                "先阅读案例的前置条件和验证范围，再执行命令。此包不含模型凭证或已生成视频。\n"
                "OPCBoost · by Cogine\n"
            ))
        print(f"Prepared {path.name}: {len(selected)} source files plus START-HERE.md")


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

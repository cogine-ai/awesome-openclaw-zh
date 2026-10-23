#!/usr/bin/env python3
"""Prepare three source-and-output ZIPs for a reviewed release; never publish."""
import argparse
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    "experience-card": "usecases/productivity/experience-interview-record-card.md",
    "github-cards": "usecases/creative/github-handdrawn-project-cards.md",
    "comedy-chase": "usecases/creative/comedy-chase-action-continuity.md",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="New directory for ZIPs; refuses an existing path")
    args = parser.parse_args()
    if args.out.exists():
        parser.error("--out must name a new directory")
    files = {}
    for name, case in PACKS.items():
        folder = ROOT / "assets/examples" / name
        if not (ROOT / case).is_file() or not folder.is_dir():
            parser.error(f"Missing showcase inputs for {name}")
        selected = [p for p in folder.rglob("*") if p.is_file()
                    and not p.is_symlink() and "__pycache__" not in p.parts
                    and p.suffix in {".py", ".md", ".html", ".txt", ".json", ".svg"}]
        if not selected:
            parser.error(f"Empty showcase: {name}")
        files[name] = sorted([ROOT / case, ROOT / "LICENSE", *selected])
    args.out.mkdir(parents=True, exist_ok=False)
    for name, selected in files.items():
        path = args.out / f"{name}-2026-10-23.zip"
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for source in selected:
                archive.write(source, source.relative_to(ROOT).as_posix())
            archive.writestr("START-HERE.md", (
                f"# {name}\n\n解压后从本目录阅读 `{PACKS[name]}`。\n"
                f"输入、实际产物、复现脚本和上游许可在 `assets/examples/{name}/`。\n"
                "先阅读案例的前置条件和验证范围，再执行命令。此包不含模型凭证或已生成视频。\n"
                "OPCBoost · by Cogine\n"
            ))
        print(f"Prepared {path.name}: {len(selected)} source files plus START-HERE.md")


if __name__ == "__main__":
    main()

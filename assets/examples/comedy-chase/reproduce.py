#!/usr/bin/env python3
"""Verify the M0 production pack with pinned upstream tools; compile its HTML board.

Python 3.10+ and Git are required. No API keys, image service or video service is used.
The default output is board.html beside this script. Upstream clones are temporary.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

REVISION = "6f16955c57053d77ea0ffbdbbf3a7985a3e0080a"
REPOSITORY = "https://github.com/lixiaoxiao9888-create/manju-laoli-skill.git"
ROOT = Path(__file__).resolve().parent


def run(command: list[str], cwd: Path | None = None, show: bool = True) -> str:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1",
           "GIT_TERMINAL_PROMPT": "0"}
    result = subprocess.run(command, cwd=cwd, env=env, text=True, encoding="utf-8",
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if show:
        print(result.stdout, end="", flush=True)
    if result.returncode:
        if not show:
            print(result.stdout, end="", flush=True)
        raise RuntimeError(f"Command failed ({result.returncode}): {command[0:3]}")
    return result.stdout


def verify_and_compile(upstream: Path, output_dir: Path) -> None:
    head = run(["git", "rev-parse", "HEAD"], cwd=upstream, show=False).strip()
    if head != REVISION:
        raise RuntimeError(f"Expected upstream {REVISION}; found {head}")
    run(["git", "diff", "--exit-code", "HEAD", "--", "short-drama-director/scripts",
         "sd-feed-engine/scripts", "sd-storyboard-engine/scripts"], cwd=upstream, show=False)

    project = (ROOT / "project.md").read_text(encoding="utf-8")
    feed25 = (ROOT / "seedance-2.5.txt").read_text(encoding="utf-8")
    # The board parser splits Markdown headings even inside a fence. Its display
    # copy therefore omits only this wrapper; all production instructions must match.
    board_copy = re.sub(r"^## 【投喂单元[^\n]+】\n\n", "", feed25, flags=re.M)
    if board_copy not in project:
        raise RuntimeError("project.md and seedance-2.5.txt have drifted")

    for model in ("2.5", "2.0"):
        feed = ROOT / f"seedance-{model}.txt"
        text = run([sys.executable, str(upstream / "short-drama-director/scripts/validate_prompt.py"),
                    str(feed), "--model", model, "--aspect", "16:9", "--combat", "on",
                    "--plugin", "real", "--c23", "on", "--delivery", "feed-only", "--contract", "--json"])
        report = json.loads(text)
        if report["issues"] or report["stats"]["duration_s"] != 15 or report["stats"]["shots"] != 4:
            raise RuntimeError(f"Unexpected {model} validation result")
        # These two diagnostics are retained and displayed, not hidden. R1's
        # child-friendly exception is documented in the case and project text.
        codes = {warning.split()[0] for warning in report["warnings"]}
        if not codes.issubset({"C21b", "C22c"}):
            raise RuntimeError(f"New warnings require review: {sorted(codes)}")
        if not report["combat_checked"] or not report["c23_checked"]:
            raise RuntimeError("Required validator checks were not enabled")
        print(f"{model}: 15 seconds / 4 time slices / 0 FAIL; retained WARN: {sorted(codes)}")
        gates = run([sys.executable, str(upstream / "sd-feed-engine/scripts/gate_check.py"),
                     str(feed), "--model", model, "--mode", "M0", "--assets", "0"])
        if "FAIL=0  WARN=0" not in gates:
            raise RuntimeError(f"Unexpected {model} gate result")

    previs = run([sys.executable, str(upstream / "sd-storyboard-engine/scripts/check_p45.py"),
                  str(ROOT / "帽子比人跑得快-预演故事板.md"), "--segments", "1", "--json"])
    if "FAIL 0 · WARN 0" not in previs:
        raise RuntimeError("The previs attachment needs review")

    compiler_path = upstream / "short-drama-director/scripts/build_board_lite.py"
    spec = importlib.util.spec_from_file_location("pinned_board_compiler", compiler_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the pinned board compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = module.parse_md(project)
    if (len(data["segments"]) != 1 or sum(len(item["shots"]) for item in data["segments"]) != 4
            or module.total_duration(data) != 15 or data["warnings"]):
        raise RuntimeError(f"Board compilation lost content or reported warnings: {data['warnings']}")
    if len(data["assets"]) != 5 or len(data["asset_prompts"]) != 5:
        raise RuntimeError("The board lost a text asset or optional asset prompt")

    output_dir.mkdir(parents=True, exist_ok=True)
    board = output_dir / "board.html"
    run([sys.executable, str(compiler_path), str(ROOT / "project.md"), "--out", str(board)])
    if not board.is_file() or board.stat().st_size < 1000:
        raise RuntimeError("HTML board was not produced")
    print(f"Completed: {board.resolve()}")
    print("Text checks and HTML compilation only; no images or videos were generated.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream-dir", type=Path, help="Use an unchanged checkout of the pinned revision")
    parser.add_argument("--output-dir", type=Path, default=ROOT, help="Directory for the compiled board.html")
    args = parser.parse_args()
    sys.dont_write_bytecode = True
    try:
        if args.upstream_dir:
            verify_and_compile(args.upstream_dir.resolve(), args.output_dir.resolve())
        else:
            with tempfile.TemporaryDirectory(prefix="comedy-chase-tools-") as directory:
                upstream = Path(directory) / "manju"
                run(["git", "clone", "--filter=blob:none", "--no-checkout", REPOSITORY, str(upstream)])
                run(["git", "checkout", "--detach", REVISION], cwd=upstream)
                verify_and_compile(upstream, args.output_dir.resolve())
        return 0
    except (OSError, RuntimeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

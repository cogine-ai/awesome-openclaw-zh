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
SRT_ADAPTER_MARKER = "COMEDY_CHASE_SRT_ADAPTER_V1"


def load_tool(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load the pinned tool: {path.name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dialogue_field(shot_text: str) -> tuple[str, str, str] | None:
    """Read this pack's last dialogue field without changing either model's syntax.

    The pinned upstream gate and SRT exporter only accept square-bracket dialogue.
    Unknown/multiple fields are errors rather than silently becoming no dialogue.
    """
    fields = re.findall(r"台词：([^\n]*)", shot_text)
    if len(fields) != 1:
        raise RuntimeError("Expected exactly one dialogue field per time slice")
    field = fields[0].strip().removesuffix("。").strip()
    if field == "无":
        return None
    if field.startswith("{") and field.endswith("}"):
        field = field[1:-1]
    match = re.fullmatch(r'([^（：{}【】]+?)(?:（([^）]*)）)?：“([^”\n]+)”', field)
    if match is None:
        raise RuntimeError(f"Unsupported dialogue field: {fields[0]}")
    return match[1].strip(), (match[2] or "").strip(), match[3]


def adapt_gate_copy(source: str, gate) -> tuple[str, list[dict]]:
    """Adapt only a temporary inspection copy; the actual feed remains untouched."""
    units = gate.parse_units(source)
    if len(units) != 1:
        raise RuntimeError("Expected one feed unit before dialogue adaptation")
    shots = gate.parse_shots(units[0][1])
    if len(shots) != 4:
        raise RuntimeError("Expected four time slices before dialogue adaptation")
    adapted, captions = source, []
    for no, start, end, shot_text in shots:
        dialogue = dialogue_field(shot_text)
        if dialogue is None:
            continue
        role, tone, words = dialogue
        tone_slot = f"（{tone}）" if tone else ""
        canonical = f'台词：【{role}{tone_slot}：“{words}”】。'
        checked_line = re.sub(r"台词：[^\n]*", lambda _: canonical, shot_text)
        if adapted.count(shot_text) != 1:
            raise RuntimeError("Cannot uniquely adapt the dialogue time slice")
        adapted = adapted.replace(shot_text, checked_line, 1)
        captions.append({"shot": no, "start": start, "end": end,
                         "role": role, "tone": tone, "text": words})
    if len(captions) != 1 or (captions[0]["start"], captions[0]["end"]) != (12, 15):
        raise RuntimeError("Expected exactly one real dialogue at 12–15 seconds")
    checked_units = gate.parse_units(adapted)
    recognized = gate.parse_lines(checked_units[0][1])
    caption = captions[0]
    expected = (caption["role"], caption["tone"], caption["text"])
    if len(recognized) != 1 or recognized[0][:3] != expected:
        raise RuntimeError("The pinned gate did not recognize the actual dialogue exactly once")
    checked_shots = gate.parse_shots(checked_units[0][1])
    spoken_shots = [(no, start, end, gate.parse_lines(body))
                    for no, start, end, body in checked_shots if gate.parse_lines(body)]
    if (len(spoken_shots) != 1 or spoken_shots[0][:3] != (4, 12, 15)
            or len(spoken_shots[0][3]) != 1):
        raise RuntimeError("The pinned gate assigned dialogue to the wrong time slice")
    return adapted, captions


def adapt_board_srt(html: str, captions: list[dict]) -> str:
    """Deterministically replace the pinned compiler's SRT function, not its tools.

    Displayed model input is unchanged. Export only the actual words and authored
    time slice; these are planned subtitles, not a generated audio alignment.
    """
    start, end = "function exportSRT(){", "function exportTimelineCSV(){"
    if f"// {SRT_ADAPTER_MARKER}:" in html or html.count(start) != 1 or html.count(end) != 1:
        raise RuntimeError("Unexpected board exporter structure; review the SRT adapter")
    left, right = html.index(start), html.index(end)
    original = html[left:right]
    if "台词：【" not in original or "（无对白）" not in original:
        raise RuntimeError("The pinned SRT exporter changed; refusing to patch blindly")
    data = [{key: caption[key] for key in ("start", "end", "text")} for caption in captions]
    # Escape HTML-significant characters because this JSON lives inside <script>.
    encoded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace(
        ">", "\\u003e").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    replacement = (
        f"// {SRT_ADAPTER_MARKER}: Cogine adapter after the unmodified pinned compiler.\n"
        "// Planned shot timing only; no generated audio or word alignment.\n"
        f"const COMEDY_CHASE_CAPTIONS = {encoded};\n"
        "function exportSRT(){\n"
        "  const lines = COMEDY_CHASE_CAPTIONS.map((caption, index)=>\n"
        "    `${index + 1}\\n${fmtSrtTime(caption.start)} --> ${fmtSrtTime(caption.end)}\\n${caption.text}\\n`);\n"
        "  dlBlob((D.meta&&D.meta.title||'short_drama') + '.srt', lines.join('\\n'), 'text/plain;charset=utf-8');\n"
        "}\n"
    )
    return html[:left] + replacement + html[right:]


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

    gate_path = upstream / "sd-feed-engine/scripts/gate_check.py"
    gate = load_tool("pinned_gate_checker", gate_path)
    model_captions = []
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
        adapted, captions = adapt_gate_copy(feed.read_text(encoding="utf-8"), gate)
        model_captions.append(captions)
        # Do not let an empty parse turn into a false PASS. This explicitly uses
        # the unmodified gate's recognized tone and speech-time calculation.
        caption = captions[0]
        need_fast, need_slow, chars, _, _ = gate.speech_seconds(caption["text"], caption["tone"])
        if not caption["tone"] or need_fast > caption["end"] - caption["start"]:
            raise RuntimeError(f"{model}: actual dialogue tone/duration failed")
        print(f"{model}: pinned gate recognized 1 dialogue at 12–15s; {chars} characters; "
              f"tone={caption['tone']}; fastest={need_fast:.2f}s, comfortable={need_slow:.2f}s")
        with tempfile.TemporaryDirectory(prefix="comedy-chase-dialogue-") as directory:
            inspection = Path(directory) / f"seedance-{model}-gate-copy.txt"
            inspection.write_text(adapted, encoding="utf-8")
            gates = run([sys.executable, str(gate_path), str(inspection),
                         "--model", model, "--mode", "M0", "--assets", "0"])
        if "FAIL=0  WARN=0" not in gates:
            raise RuntimeError(f"Unexpected {model} gate result")
    if model_captions[0] != model_captions[1]:
        raise RuntimeError("The two model feeds disagree on their actual dialogue")

    previs = run([sys.executable, str(upstream / "sd-storyboard-engine/scripts/check_p45.py"),
                  str(ROOT / "帽子比人跑得快-预演故事板.md"), "--segments", "1", "--json"])
    if "FAIL 0 · WARN 0" not in previs:
        raise RuntimeError("The previs attachment needs review")

    compiler_path = upstream / "short-drama-director/scripts/build_board_lite.py"
    module = load_tool("pinned_board_compiler", compiler_path)
    data = module.parse_md(project)
    if (len(data["segments"]) != 1 or sum(len(item["shots"]) for item in data["segments"]) != 4
            or module.total_duration(data) != 15 or data["warnings"]):
        raise RuntimeError(f"Board compilation lost content or reported warnings: {data['warnings']}")
    if len(data["assets"]) != 5 or len(data["asset_prompts"]) != 5:
        raise RuntimeError("The board lost a text asset or optional asset prompt")
    board_captions = []
    for segment in data["segments"]:
        for shot in segment["shots"]:
            dialogue = dialogue_field(shot["text"])
            if dialogue is not None:
                board_captions.append({"shot": shot["no"], "start": segment.get("off", 0) + shot["start"],
                                       "end": segment.get("off", 0) + shot["end"],
                                       "role": dialogue[0], "tone": dialogue[1], "text": dialogue[2]})
    if board_captions != model_captions[0]:
        raise RuntimeError("The compiled board lost or changed the actual dialogue")

    output_dir.mkdir(parents=True, exist_ok=True)
    board = output_dir / "board.html"
    run([sys.executable, str(compiler_path), str(ROOT / "project.md"), "--out", str(board)])
    if not board.is_file() or board.stat().st_size < 1000:
        raise RuntimeError("HTML board was not produced")
    board.write_text(adapt_board_srt(board.read_text(encoding="utf-8"), board_captions), encoding="utf-8")
    print("Applied documented Cogine SRT adapter: one planned caption at 12–15s; model input unchanged.")
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

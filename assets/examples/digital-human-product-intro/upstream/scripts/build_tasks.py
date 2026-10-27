#!/usr/bin/env python3
"""口播稿 → Grok 分段任务（create_tasks 的 tasks 数组）+ 费用估算。

用法：
  python3 build_tasks.py script.json out_tasks.json [--purpose "teaching a beginner tutorial step by step"] [--all-720p]

script.json：[{"id": "s1", "shot": "full|pip|vlog", "t": "这一段要念的台词", "host": "tank|me", "lang": "Mandarin Chinese|English|Japanese|…"}, ...]
- host：tank = 白背心数字人（9:16，默认）；me = 用户本人数字人（16:9，persona.json → other_hosts.me）
- lang：不写就是普通话；外语段台词直接写目标语言
- 每段时长 = ceil(字数 / 5.4 + 1.0)，夹在 4–15 秒（Grok 单段上限 15 秒；5.4 字/秒是实测语速）
- full 段 720p，pip 段 480p（画中画里看不出差别，便宜四成）；--all-720p 全部 720p
- 超过 15 秒的段会报错：先把台词拆短再跑
输出的数组每 10 个一批交给 create_tasks；提交前一定先把总价和余额报给用户，等用户确认。
"""
import json, math, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
P = json.loads((HERE / "persona.json").read_text())

def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

def main():
    src, dst = sys.argv[1], sys.argv[2]
    purpose = arg("--purpose", "explaining clearly")
    all720 = "--all-720p" in sys.argv
    S = json.loads(Path(src).read_text())
    tasks, total = [], 0
    for s in S:
        lang = s.get("lang", "Mandarin Chinese")
        if lang.startswith("Mandarin") or lang == "Chinese":
            d = math.ceil(len(re.sub(r"[\s，。、：；！？,.:;!?“”]", "", s["t"])) / P["voice"]["speed_cps"] + 1.0)
        elif re.search(r"[\u3040-\u30ff\uac00-\ud7af]", s["t"]):     # 日文 / 韩文：约 7 字/秒
            d = math.ceil(len(re.sub(r"\s", "", s["t"])) / 7 + 1.0)
        else:                                                    # 拉丁 / 阿拉伯等按词：约 2.6 词/秒
            d = math.ceil(len(s["t"].split()) / 2.6 + 1.0)
        if d > P["model"]["max_seconds"]:
            sys.exit(f"{s['id']} 约 {d} 秒，超过 15 秒：拆成两段再跑")
        d = max(4, d)
        shot = s.get("shot", "full")
        res = P["model"]["full_shot_resolution"] if (all720 or shot != "pip") else P["model"]["pip_shot_resolution"]
        total += d * P["model"]["price_per_second"][res]
        act = P["acts"].get(shot, P["acts"]["full"])
        if s.get("host", "tank") == "me":
            H = P["other_hosts"]["me"]; ref = H["reference_material"]; ratio = H["ratio"]
            prompt = H["prompt_template"].format(ref="@" + ref, purpose=purpose, act=act, voice=H["voice"], language=lang, line=s["t"])
        else:
            ref = P["renoise"]["reference_material"]; ratio = P["model"]["ratio"]
            prompt = P["prompt_template"].format(ref="@" + ref, purpose=purpose, act=act, voice=P["voice"]["desc"], line=s["t"]).replace("Mandarin Chinese", lang)
        tasks.append({"model": P["model"]["name"], "kind": "video", "ratio": ratio, "resolution": res, "duration": d,
                      "label": f"口播 {s['id']}", "idempotencyKey": f"dh-{Path(src).stem}-{s['id']}-v1",
                      "references": [{"ref": ref, "role": "reference_image"}], "prompt": prompt})
    Path(dst).write_text(json.dumps(tasks, ensure_ascii=False, indent=1))
    secs = sum(t["duration"] for t in tasks)
    print(f"{len(tasks)} 段 · 口播约 {secs} 秒 · 预估 {total} credits · 分 {math.ceil(len(tasks) / 10)} 批提交")

if __name__ == "__main__":
    main()

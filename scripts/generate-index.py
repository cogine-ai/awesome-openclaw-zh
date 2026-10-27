#!/usr/bin/env python3
"""Generate the public Markdown index and README counts from the JSON catalog."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "社交媒体": "social", "创意与构建": "creative", "基础设施与 DevOps": "devops",
    "生产力": "productivity", "研究与学习": "research", "金融与交易": "finance",
    "日常生活": "everyday", "内容转换": "content", "内存管理": "memory",
    "夜间自动化": "automation", "数据分析": "data", "安全监控": "security", "工具开发": "tools",
}


def load_catalog():
    entries = json.loads((ROOT / "resources/usecases-index.json").read_text(encoding="utf-8"))
    seen = set()
    for entry in entries:
        for key in ("title", "desc", "category", "localPath", "sourceRepo", "sourcePath", "sourceUrl"):
            if not isinstance(entry.get(key), str) or not entry[key].strip():
                raise ValueError(f"Missing {key}: {entry}")
        category, path = entry["category"], entry["localPath"]
        if category not in CATEGORIES or not path.startswith(f"usecases/{CATEGORIES[category]}/"):
            raise ValueError(f"Wrong category/path: {path}")
        if path in seen:
            raise ValueError(f"Duplicate path: {path}")
        seen.add(path)
        target = (ROOT / path).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file() or target.suffix != ".md":
            raise ValueError(f"Missing or invalid document: {path}")
        source_url = entry["sourceUrl"]
        source = urlparse(source_url)
        if (source.scheme not in ("https", "http") or not source.hostname
                or any(character.isspace() for character in source_url)):
            raise ValueError(f"Invalid source URL: {path}")
        _ = source.port  # Parse invalid/out-of-range ports before website import.
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "usecases").glob("*/*.md")}
    if actual != seen:
        raise ValueError(f"Catalog mismatch: unindexed={sorted(actual-seen)}, missing={sorted(seen-actual)}")
    return entries


def markdown_index(entries):
    lines = ["# 用例总览", "", f"当前共收录 **{len(entries)}** 个中文案例与实验方案。", "",
             "案例是否经过本地实测，请查看各页的验证说明；收录和来源核对不等于端到端运行通过。", "",
             "[六个新玩法与实验](./07-new-playbooks-lab.md) · [本期可复刻成果](./06-reproducible-showcase.md) · [在线搜索](https://www.opcboost.com/usecases/)", "", "按分类浏览：", ""]
    for category in CATEGORIES:
        group = [entry for entry in entries if entry["category"] == category]
        lines += [f"## {category} ({len(group)})", "", "| 用例 | 能干什么 |", "|---|---|"]
        for entry in group:
            title = entry["title"].replace("|", "\\|").replace("\n", " ")
            desc = entry["desc"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| [{title}](../{entry['localPath']}) | {desc} |")
        lines.append("")
    return "\n".join(lines)


def readme_counts(readme, entries):
    counts = Counter(entry["category"] for entry in entries)
    readme = re.sub(r"使用场景：\d+", f"使用场景：{len(entries)}", readme)
    readme = re.sub(r"按分类找案例（\d+\s*个）", f"按分类找案例（{len(entries)} 个）", readme)
    readme = re.sub(r"全量用例索引（\d+）", f"全量用例索引（{len(entries)}）", readme)
    for category, directory in CATEGORIES.items():
        pattern = rf"\[([^\]\n]+)（\d+）\]\(\./usecases/{directory}\)"
        readme = re.sub(pattern, lambda match: f"[{match[1]}（{counts[category]}）](./usecases/{directory})", readme)
    return readme


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = parser.parse_args()
    entries = load_catalog()
    readme = ROOT / "README.md"
    generated = {ROOT / "resources/usecases-index.md": markdown_index(entries),
                 readme: readme_counts(readme.read_text(encoding="utf-8"), entries)}
    stale = []
    for path, content in generated.items():
        if path.read_text(encoding="utf-8") != content:
            stale.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.write_text(content, encoding="utf-8")
    if args.check and stale:
        print("Run python3 scripts/generate-index.py: " + ", ".join(stale), file=sys.stderr)
        return 1
    print(f"Catalog valid: {len(entries)} cases; generated files {'current' if args.check else 'updated'}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)

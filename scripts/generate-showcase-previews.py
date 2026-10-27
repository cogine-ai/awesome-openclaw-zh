#!/usr/bin/env python3
"""Generate two text-only previews from the actual published card and shot table."""
import argparse
import html
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def lines(text, width=22, limit=5):
    text = " ".join(text.split())
    result = [text[index:index + width] for index in range(0, len(text), width)]
    if len(result) > limit:
        result = result[:limit]
        result[-1] = result[-1][:-1] + "…"
    return result


def preview(title, notice, cards, columns):
    rows = (len(cards) + columns - 1) // columns
    cell_width = 1080 // columns
    height = 210 + rows * 260
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}">',
             '<rect width="100%" height="100%" fill="#f5f7f3"/>',
             '<g font-family="system-ui, sans-serif">',
             '<text x="60" y="55" font-size="20" fill="#047857">OPCBoost · Cogine</text>',
             f'<text x="60" y="105" font-size="34" font-weight="700" fill="#17392c">{html.escape(title)}</text>',
             f'<text x="60" y="150" font-size="19" fill="#52695d">{html.escape(notice)}</text>']
    for index, (label, text) in enumerate(cards):
        x, y = 60 + (index % columns) * cell_width, 190 + (index // columns) * 260
        parts.append(f'<rect x="{x}" y="{y}" width="{cell_width - 20}" height="240" rx="14" fill="white" stroke="#b9c8b9"/>')
        parts.append(f'<text x="{x + 20}" y="{y + 40}" font-size="22" font-weight="700" fill="#176c4e">{html.escape(label)}</text>')
        for line, value in enumerate(lines(text, 22 if columns == 2 else 14)):
            parts.append(f'<text x="{x + 20}" y="{y + 80 + line * 28}" font-size="19" fill="#17392c">{html.escape(value)}</text>')
    return "\n".join(parts + ['</g></svg>', ''])


def generate_experience():
    card_root = ROOT / 'assets/examples/experience-card'
    gallery = (card_root / 'gallery.html').read_text(encoding='utf-8')
    match = re.search(r'<script type="application/json" id="card-data">(.*?)</script>', gallery, re.S)
    if match is None:
        raise ValueError('Actual gallery data is missing')
    versions = json.loads(match[1])['versions']
    if [entry['num'] for entry in versions] != [1, 2]:
        raise ValueError('Expected the actual v1/v2 card pair')
    cards = [(f"v{entry['num']} · {entry['day']}", entry['fields']['point']) for entry in versions]
    (card_root / 'preview.svg').write_text(preview('同一张经验卡，保留两版理解', '真实脚本产物的文字预览 · 维护者编辑演练，未经受访者确认', cards, 2), encoding='utf-8')


def generate_comedy():
    shot_root = ROOT / 'assets/examples/comedy-chase'
    rows = []
    for line in (shot_root / 'project.md').read_text(encoding='utf-8').splitlines():
        if re.match(r'^\| S[1-4] \|', line):
            cells = [part.strip() for part in line.strip('|').split('|')]
            rows.append((f'{cells[0]} · {cells[1]}', f'{cells[2]}。{cells[6]}。{cells[7]}。出口：{cells[8]}'))
    if len(rows) != 4:
        raise ValueError('Expected the four published storyboard rows')
    (shot_root / 'preview.svg').write_text(preview('帽子连纸袋一起跑 · 15 秒计划', '实际四镜表的文字预览 · 未生成分镜图片或视频，字幕为计划时段', rows, 2), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pack', choices=['experience-card', 'comedy-chase', 'all'], default='all')
    args = parser.parse_args()
    if args.pack in {'experience-card', 'all'}:
        generate_experience()
    if args.pack in {'comedy-chase', 'all'}:
        generate_comedy()
    print(f'Generated deterministic text previews: {args.pack}.')


if __name__ == '__main__':
    main()

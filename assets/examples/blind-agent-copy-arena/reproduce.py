#!/usr/bin/env python3
"""Build a deterministic anonymous-copy rehearsal; never launch model calls."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent


def render(brief):
    rules=brief.get('rubric')
    if rules != [{'key':'specific','label':'具体：说清能得到什么','max':5},
                 {'key':'honest','label':'可信：承诺与事实相符','max':5},
                 {'key':'action','label':'行动：下一步容易理解','max':5}]:
        raise ValueError('This rehearsal requires the frozen three-rule, 15-point rubric')
    candidates = brief["candidates"]
    if len(candidates) != 3 or len({c["id"] for c in candidates}) != 3:
        raise ValueError("Exactly three distinct candidates are required")
    if any(not isinstance(c.get("text"), str) or not 1 <= len(c["text"]) <= 55 for c in candidates):
        raise ValueError("Each candidate must have 1–55 characters")
    # Fixed assignment makes published replay stable. It is not cryptographic concealment.
    ordered = sorted(candidates, key=lambda c: hashlib.sha256(("opcboost-copy-v1:" + c["id"]).encode()).hexdigest())
    cards, sources = [], []
    for index, candidate in enumerate(ordered):
        label = chr(65 + index)
        controls = ''.join(f'<label>{html.escape(rule["label"])} <select name="{rule["key"]}-{label}" required><option value="">请选择</option>' + ''.join(f'<option value="{score}">{score}</option>' for score in range(6)) + '</select></label>' for rule in brief["rubric"])
        cards.append(f'<article><h2>候选 {label}</h2><p class="copy">{html.escape(candidate["text"])}</p>{controls}</article>')
        sources.append({"label":label,"origin":candidate["origin"]})
    # Data is public, prewritten assistant-drafted rehearsal material; do not claim identity secrecy.
    data = json.dumps(sources,ensure_ascii=False).replace('<','\\u003c')
    return '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>OPCBoost 文案盲选演练</title>
<style>body{font:17px/1.7 system-ui;background:#f4f6ef;color:#183a30;max-width:1120px;margin:auto;padding:28px}a{color:#176c4e}h1{font-size:clamp(30px,6vw,52px);line-height:1.2}header{border-bottom:3px solid #176c4e}section{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin:28px 0}article{border:1px solid #b6c9bd;border-radius:16px;background:white;padding:24px}h2{font-size:20px}.copy{font-size:23px;min-height:130px}label{display:block;margin:14px 0}select{font:inherit;display:block;width:100%;padding:8px;background:#fff;border:1px solid #678879;border-radius:6px}button{font:inherit;padding:12px 24px;border:0;border-radius:8px;background:#176c4e;color:white;cursor:pointer}button:disabled{opacity:.55}#results{padding:20px;background:#e0eedf;border-radius:12px;margin:20px 0}.notice{background:#fff5d9;padding:16px;border-radius:10px}footer{margin-top:36px}nav a{display:inline-block;margin:6px 20px 6px 0}</style>
<header><p>OPCBOOST / 原创玩法实验</p><h1>先选文案，再看写法。</h1><p>TITLE · 三个匿名候选 · 一份固定评分表</p></header>
<p class="notice">NOTICE 这是浏览器端匿名展示演练，不是已执行的 OpenClaw 原生盲测；页面源数据公开，不提供身份保密。</p><p>受众：AUDIENCE</p><ul>FACTS</ul>
<form id="arena"><section>CARDS</section><button type="submit">锁定评分并揭晓写法</button></form><div id="results" role="status" hidden></div><noscript>此演练需要JavaScript交互；可下载 brief.json 阅读全部候选和评分规则。</noscript>
<nav><a href="brief.json">原始Brief与评分表</a><a href="native-trial.mjs">原生能力适配代码</a><a href="reproduce.py">复现脚本</a></nav><footer><a href="https://www.opcboost.com/usecases/creative/blind-agent-copy-arena/">阅读全文与原生接入条件</a> · <a href="https://github.com/cogine-ai/awesome-openclaw-zh">Star / 参与共建</a> · <a href="https://cogine.ai">Cogine</a><p>离线运行 · 不上传评分 · 不调用模型 · 没有客观模型排行</p></footer>
<script>
const sources=DATA;
document.getElementById('arena').addEventListener('submit',event=>{
 event.preventDefault();
 const form=event.currentTarget;
 if(!form.reportValidity())return;
 const rows=sources.map(s=>{const total=['specific','honest','action'].reduce((n,key)=>n+Number(form.elements[key+'-'+s.label].value),0);return {...s,total};});
 const results=document.getElementById('results');results.replaceChildren();
 const heading=document.createElement('h2');heading.textContent='评分已锁定：你的偏好，共15分';results.append(heading);
 rows.sort((a,b)=>b.total-a.total||a.label.localeCompare(b.label)).forEach(row=>{const p=document.createElement('p');p.textContent='候选 '+row.label+'：'+row.total+' / 15 · '+row.origin;results.append(p);});
 const note=document.createElement('p');note.textContent='这些分数只记录你对三句演练文案的判断。真实试验还需保留输入、原始回答和主机回执。刷新页面可重新评分。';results.append(note);
 results.hidden=false;form.querySelectorAll('select,button').forEach(control=>control.disabled=true);
});
</script></html>'''.replace('TITLE', html.escape(brief['title'])).replace('NOTICE',html.escape(brief['fixtureNotice'])).replace('AUDIENCE',html.escape(brief['audience'])).replace('FACTS',''.join('<li>'+html.escape(fact)+'</li>' for fact in brief['facts'])).replace('CARDS',''.join(cards)).replace('DATA',data)


def preview(brief):
    ordered=sorted(brief['candidates'],key=lambda c:hashlib.sha256(('opcboost-copy-v1:'+c['id']).encode()).hexdigest())
    rows=''
    for i,candidate in enumerate(ordered):
        y=210+i*105
        rows+=f'<rect x="50" y="{y-36}" width="1100" height="86" rx="14" fill="#ffffff" stroke="#bdcebf"/><text x="76" y="{y}" font-size="25" fill="#173f30">{chr(65+i)} · {html.escape(candidate["text"])}</text>'
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="预置文案匿名评分演练"><rect width="1200" height="630" fill="#f1f5ee"/><g font-family="system-ui,sans-serif"><text x="50" y="68" font-size="22" fill="#376b50">OPCBOOST / 原创交互演练</text><text x="50" y="135" font-size="46" font-weight="700" fill="#173f30">先打分，再揭晓写法。</text>'+rows+'<text x="50" y="555" font-size="23" fill="#526655">预置候选 · 具体 / 可信 / 行动 · 每项0–5分</text><text x="50" y="596" font-size="21" fill="#8b4f14">未执行原生Agent盲测，不构成模型排行</text></g></svg>\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=HERE)
    args=parser.parse_args()
    standalone=args.output_dir.resolve()!=HERE.resolve()
    if standalone and args.output_dir.exists():
        parser.error('--output-dir must name a new directory')
    try:
        brief=json.loads((HERE/'brief.json').read_text(encoding="utf-8"))
        content=render(brief)
    except (ValueError,KeyError) as error:
        parser.error(str(error))
    args.output_dir.mkdir(parents=True,exist_ok=True)
    if standalone:
        for name in ('brief.json','native-trial.mjs','test-native.mjs','reproduce.py','provenance.json'):
            shutil.copyfile(HERE/name,args.output_dir/name)
    (args.output_dir/'index.html').write_text(content,encoding='utf-8')
    (args.output_dir/'preview.svg').write_text(preview(brief),encoding='utf-8')
    print('Built three prewritten assistant-drafted rehearsal candidates. Native blind trial: not executed.')


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Build a study kit, viewpoint map, or product discussion page from input.json."""
import argparse
import html
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parent

def esc(value):
    return html.escape(str(value), quote=True)

def json_text(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def require_ids(items, label):
    ids = [item['id'] for item in items]
    for value in ids:
        require(isinstance(value, str) and re.fullmatch(r'[A-Za-z0-9_-]+', value),
                'Invalid ' + label + ' ID: ' + str(value))
    require(len(ids) == len(set(ids)), 'Duplicate ' + label + ' ID')


def plan_outputs(target, names):
    root = target.resolve()
    require(not target.exists() or target.is_dir(), 'Output directory is not a directory')
    planned = {}
    for name in names:
        relative = PurePosixPath(name)
        require(not relative.is_absolute() and '\\' not in name
                and all(part not in ('', '.', '..') for part in name.split('/')),
                'Invalid output path: ' + name)
        path = target / name
        require(all(not target.joinpath(*relative.parts[:index]).is_symlink()
                    for index in range(1, len(relative.parts) + 1)),
                'Symlinked output path: ' + name)
        for index in range(1, len(relative.parts)):
            parent = target.joinpath(*relative.parts[:index])
            require(not parent.exists() or parent.is_dir(), 'Output parent is not a directory: ' + name)
        require(path.resolve().is_relative_to(root), 'Output path escapes directory: ' + name)
        require(not path.exists() or path.is_file(), 'Output target is not a file: ' + name)
        planned[name] = path
    return planned


def validate(data):
    refs = {}
    kind = data['kind']
    for field in ('category', 'slug'):
        require(isinstance(data[field], str) and re.fullmatch(r'[A-Za-z0-9_-]+', data[field]),
                'Invalid URL segment: ' + field)
    require(kind in ('learning', 'podcast', 'townhall'), 'Unknown content kind')
    if kind == 'learning':
        require(len(data['sources']) == 3 and len(data['quiz']) == 10 and len(data['cards']) == 12,
                'Expected 3 sources, 10 questions, and 12 flashcards')
        require_ids(data['sources'], 'source')
        require_ids(data['quiz'], 'question')
        for source in data['sources']:
            require_ids(source['paragraphs'], 'paragraph')
            for paragraph in source['paragraphs']:
                key = source['id'] + '-' + paragraph['id']
                require(key not in refs, 'Duplicate source paragraph: ' + key)
                refs[key] = paragraph['text']
        for question in data['quiz']:
            require(question['ref'] in refs and question['evidence'] in refs[question['ref']],
                    'Question evidence does not match source: ' + question['id'])
            require(0 <= question['answer'] < len(question['options'])
                    and len(set(question['options'])) == len(question['options']), 'Invalid answer options')
        require(len({card['front'] for card in data['cards']}) == len(data['cards']), 'Duplicate flashcard')
        for card in data['cards']:
            require(card['ref'] in refs, 'Flashcard source not found')
    elif kind == 'podcast':
        require(len(data['episodes']) == 3, 'Expected 3 transcripts')
        require_ids(data['episodes'], 'episode')
        require_ids(data['relations'], 'relation')
        for episode in data['episodes']:
            require_ids(episode['segments'], 'segment')
            last = -1
            for segment in episode['segments']:
                key = episode['id'] + '-' + segment['id']
                require(key not in refs, 'Duplicate transcript segment')
                refs[key] = segment['text']
                minutes, seconds = map(int, segment['time'].split(':'))
                require(minutes >= 0 and 0 <= seconds < 60 and minutes * 60 + seconds > last,
                        'Transcript timestamps must increase')
                last = minutes * 60 + seconds
        for relation in data['relations']:
            require(len(relation['refs']) == len(relation['quotes']) >= 2, 'Relation needs matching citations')
            for ref, quote in zip(relation['refs'], relation['quotes']):
                require(ref in refs and quote in refs[ref], 'Relation evidence not found: ' + ref)
    else:
        require_ids(data['roles'], 'role')
        require_ids(data['turns'], 'turn')
        roles = {role['id'] for role in data['roles']}
        require(len(roles) == 5, 'Expected 5 distinct roles')
        require(len({turn['id'] for turn in data['turns']}) == len(data['turns']), 'Duplicate discussion turn')
        for turn in data['turns']:
            require(turn['role'] in roles and turn['scenario'] in ('A', 'B'), 'Unknown discussion role or scenario')
        require(all(sum(turn['role'] == role and turn['scenario'] == scenario for turn in data['turns']) == 1
                    for role in roles for scenario in ('A', 'B')), 'Expected one turn per role and scenario')

CSS = '''*{box-sizing:border-box}body{margin:0;background:#f6f6f1;color:#172b2a;font:16px/1.75 system-ui,-apple-system,"Noto Sans SC",sans-serif}main{max-width:1100px;margin:auto;padding:32px 24px 60px}a{color:#08694e;text-underline-offset:4px}a:hover{color:#07372c}header{border-bottom:1px solid #cbd6cc;padding-bottom:24px}nav{display:flex;gap:20px;flex-wrap:wrap}.eyebrow{letter-spacing:.12em;color:#36715c;font-weight:700;margin-top:32px}h1{font-size:clamp(28px,5vw,48px);line-height:1.25;max-width:850px;margin:12px 0}h2{font-size:25px;margin-top:38px}h3{font-size:18px;margin:0 0 12px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.box,.question,.source,.turn,.relation{background:white;border:1px solid #dbe1d9;border-radius:14px;padding:20px;min-width:0}.metric{font-size:32px;font-weight:750;line-height:1.3}.question{margin-top:16px}.question label{display:block;padding:8px;border:1px solid #dde4dc;border-radius:8px;margin:8px 0;cursor:pointer}.question input{margin-right:10px}.answer{background:#edf6ee;padding:12px;border-radius:8px}.source{margin-top:14px}.source p{scroll-margin-top:20px}.source p:target{background:#fff1bd;border-radius:5px;padding:8px}.toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:16px 0}button,select{font:inherit;border:1px solid #95b6a5;background:white;color:#164b36;border-radius:8px;padding:9px 14px;cursor:pointer}button:hover{background:#e5f1e6}button:focus-visible,a:focus-visible,select:focus-visible{outline:3px solid #d89425;outline-offset:3px}button[aria-pressed=true]{background:#164b36;color:white}.flash{width:100%;text-align:left;min-height:145px}.flash strong{display:block}.flash .back{display:none;color:#244e3b}.flash[aria-expanded=true] .back{display:block;margin-top:12px}.flash[aria-expanded=true]{background:#eaf4e9}.relation,.turn{margin-top:12px}.pill{display:inline-block;font-weight:700;background:#e4efdf;color:#284d31;padding:3px 9px;border-radius:20px}.cite{display:block;margin-top:9px}code{background:#eaf0e7;padding:2px 5px;border-radius:4px}footer{border-top:1px solid #ccd7cc;margin-top:40px;padding-top:18px}[hidden]{display:none!important}@media(max-width:700px){main{padding:22px 16px 40px}.grid{grid-template-columns:1fr}.box,.question,.source,.turn,.relation{padding:16px}nav{gap:12px}.toolbar>*{flex:1}h2{font-size:22px}}'''


def sources_view(sources):
    return ''.join('<section class="source"><h3>' + esc(source['title']) + '</h3>'
                   + ''.join('<p id="' + esc(source['id'] + '-' + p['id']) + '"><b>'
                             + esc(source['id'] + '-' + p['id']) + '</b> ' + esc(p['text']) + '</p>'
                             for p in source['paragraphs']) + '</section>' for source in sources)


def render(data):
    kind = data['kind']
    body, script = '', ''
    if kind == 'learning':
        body = '<div class="grid" style="margin-top:24px"><div class="box"><div class="metric">3</div>学习资料</div><div class="box"><div class="metric">10</div>测验题目</div><div class="box"><div class="metric">12</div>翻面闪卡</div></div>'
        body += '<h2>做十道题，回到原文找依据</h2><form id="quiz">'
        for q in data['quiz']:
            body += '<fieldset class="question"><legend>' + esc(q['id'] + ' · ' + q['question']) + '</legend>'
            for index, option in enumerate(q['options']):
                body += '<label><input type="radio" name="' + esc(q['id']) + '" value="' + str(index) + '">' + esc(option) + '</label>'
            body += '<div class="answer" id="answer-' + esc(q['id']) + '" hidden></div></fieldset>'
        body += '</form><div class="toolbar"><button id="grade" type="button">核对答案与依据</button><button id="reset" type="button">重新作答</button></div><p id="score" role="status" aria-live="polite"></p><h2>翻开一张闪卡</h2><div class="grid">'
        for index, card in enumerate(data['cards']):
            body += '<button type="button" class="box flash" aria-expanded="false"><strong>' + esc(str(index + 1) + ' · ' + card['front']) + '</strong><span class="back">' + esc(card['back']) + '<br>依据 ' + esc(card['ref']) + '</span></button>'
        body += '</div><h2>三份学习资料</h2>' + sources_view(data['sources'])
        script = '''document.querySelectorAll('.flash').forEach(b=>b.addEventListener('click',()=>b.setAttribute('aria-expanded',String(b.getAttribute('aria-expanded')!=='true'))));document.getElementById('grade').addEventListener('click',()=>{let correct=0,answered=0;DATA.quiz.forEach(q=>{const selected=document.querySelector('input[name="'+q.id+'"]:checked');if(selected){answered++;if(Number(selected.value)===q.answer)correct++;}const node=document.getElementById('answer-'+q.id);node.hidden=false;node.replaceChildren();const text=document.createElement('span');text.textContent=(selected?(Number(selected.value)===q.answer?'回答正确。':'再核对一下。'):'请选择一个答案。')+'答案：'+q.options[q.answer]+'。'+q.explanation;const link=document.createElement('a');link.href='#'+q.ref;link.textContent='查看依据 '+q.ref;link.className='cite';node.append(text,link);});document.getElementById('score').textContent='已答 '+answered+'/10，正确 '+correct+'/10。';});document.getElementById('reset').addEventListener('click',()=>{document.getElementById('quiz').reset();document.querySelectorAll('.answer').forEach(n=>n.hidden=true);document.getElementById('score').textContent='已清空。';});'''
    elif kind == 'podcast':
        body = '<h2>按观点关系阅读</h2><p>选择一种关系，再点击引文回到对应访谈。</p><div class="toolbar" id="filters">'
        for kind_name in ('全部', '条件差异', '共识', '补充'):
            body += '<button type="button" data-filter="' + esc(kind_name) + '" aria-pressed="' + str(kind_name == '全部').lower() + '">' + esc(kind_name) + '</button>'
        body += '</div><div id="relations">'
        for relation in data['relations']:
            body += '<section class="relation" data-relation="' + esc(relation['type']) + '"><span class="pill">' + esc(relation['type']) + '</span><h3>' + esc(relation['title']) + '</h3><p>' + esc(relation['summary']) + '</p>'
            for ref, quote in zip(relation['refs'], relation['quotes']):
                body += '<a class="cite" href="#' + esc(ref) + '">' + esc(ref) + ' · ' + esc(quote) + '</a>'
            body += '</section>'
        body += '</div><h2>访谈原文</h2>'
        for episode in data['episodes']:
            body += '<section class="source"><h3>' + esc(episode['title']) + '</h3>'
            for segment in episode['segments']:
                body += '<p id="' + esc(episode['id'] + '-' + segment['id']) + '"><b>' + esc(segment['time'] + ' · ' + segment['speaker']) + '</b><br>' + esc(segment['text']) + '</p>'
            body += '</section>'
        script = "document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(n=>n.setAttribute('aria-pressed',String(n===b)));document.querySelectorAll('[data-relation]').forEach(n=>n.hidden=b.dataset.filter!=='全部'&&n.dataset.relation!==b.dataset.filter);}));"
    else:
        facts = data['facts']
        body = '<h2>产品介绍与角色目标</h2><div class="grid"><section class="box"><h3>主要功能</h3><p>' + esc('、'.join(facts['supported'])) + '</p></section><section class="box"><h3>使用范围</h3><p>单机使用；' + esc('、'.join(facts['unsupported'])) + '可作为后续需求。</p></section><section class="box"><h3>讨论主题</h3><p>' + esc(facts['product']) + '</p></section></div><h2>五张角色卡</h2><div class="grid">'
        roles = {role['id']: role for role in data['roles']}
        for role in data['roles']:
            body += '<section class="box"><h3>' + esc(role['name']) + '</h3><p>' + esc(role['goal']) + '</p><p>' + esc(role['assumption']) + '</p></section>'
        body += '</div><h2>切换两种介绍</h2><div class="toolbar"><label for="scenario">查看情境</label><select id="scenario"><option value="A">A · 含糊介绍</option><option value="B">B · 明确范围</option></select></div><div class="box" id="intro">' + esc(facts['draftA']) + '</div>'
        for turn in data['turns']:
            body += '<section class="turn" data-scenario="' + esc(turn['scenario']) + '"' + (' hidden' if turn['scenario'] == 'B' else '') + '><span class="pill">' + esc(turn['kind']) + '</span><h3>' + esc(turn['id'] + ' · ' + roles[turn['role']]['name']) + '</h3><p>' + esc(turn['text']) + '</p></section>'
        script = "document.getElementById('scenario').addEventListener('change',e=>{const s=e.target.value;document.getElementById('intro').textContent=DATA.facts['draft'+s];document.querySelectorAll('[data-scenario]').forEach(n=>n.hidden=n.dataset.scenario!==s);});"
    back = 'https://www.opcboost.com/usecases/' + data['category'] + '/' + data['slug'] + '/'
    payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + esc(data['title']) + ' · OPCBoost</title><meta name="description" content="' + esc(data['subtitle']) + '"><style>' + CSS + '</style></head><body><main><header><nav><a href="' + back + '">阅读完整案例</a><a href="https://www.opcboost.com/resources/08-autumn-makers/">六案例专题</a><a href="https://github.com/cogine-ai/awesome-openclaw-zh">Star 收藏仓库</a></nav><p class="eyebrow">OPCBOOST · 龙虾造物工坊</p><h1>' + esc(data['title']) + '</h1><p>' + esc(data['subtitle']) + '</p></header>' + body + '<footer><p><a href="input.json">修改输入数据</a> · <a href="START-HERE.md">运行说明</a> · <a href="https://www.cogine.ai/">Cogine</a></p></footer></main><script>const DATA=' + payload + ';' + script + '</script></body></html>'


def preview(data):
    labels = {'learning': '10道测验 · 12张闪卡 · 3份资料', 'podcast': '3段示例访谈 · 4条观点关系', 'townhall': '5个角色 · 2种产品介绍'}
    titles = {'learning': '资料变成可核对的学习包', 'podcast': '同一问题，三种回答', 'townhall': '让不同角色说出关注点'}
    return '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540"><rect width="960" height="540" fill="#f6f6f1"/><rect x="35" y="35" width="890" height="470" rx="24" fill="white" stroke="#c8dac9"/><g font-family="system-ui,sans-serif" fill="#173c2c"><text x="70" y="95" font-size="22">OPCBoost · 龙虾造物工坊</text><text x="70" y="175" font-size="36" font-weight="700">' + esc(titles[data['kind']]) + '</text><text x="70" y="235" font-size="23">' + esc(labels[data['kind']]) + '</text><rect x="70" y="285" width="245" height="95" rx="12" fill="#eaf3e5"/><rect x="335" y="285" width="245" height="95" rx="12" fill="#eaf3e5"/><rect x="600" y="285" width="245" height="95" rx="12" fill="#eaf3e5"/><text x="95" y="343" font-size="24">修改输入</text><text x="360" y="343" font-size="24">运行脚本</text><text x="625" y="343" font-size="24">打开作品</text></g></svg>'


def build(data):
    validate(data)
    files = {'index.html': render(data), 'preview.svg': preview(data)}
    if data['kind'] == 'learning':
        files['quiz.json'] = json_text(data['quiz'])
        files['flashcards.json'] = json_text(data['cards'])
        for source in data['sources']:
            files['sources/' + source['id'] + '.md'] = '# ' + source['title'] + '\n\n' + '\n\n'.join('## ' + source['id'] + '-' + paragraph['id'] + '\n\n' + paragraph['text'] for paragraph in source['paragraphs']) + '\n'
    elif data['kind'] == 'podcast':
        files['relations.json'] = json_text(data['relations'])
        for episode in data['episodes']:
            files['transcripts/' + episode['id'] + '.md'] = '# ' + episode['title'] + '\n\n示例访谈：用于练习观点比较。\n\n' + '\n\n'.join('## ' + episode['id'] + '-' + segment['id'] + ' · ' + segment['time'] + '\n\n' + segment['speaker'] + '：' + segment['text'] for segment in episode['segments']) + '\n'
    else:
        files['scenario-config.json'] = json_text({'facts': data['facts'], 'roles': data['roles']})
        files['timeline.json'] = json_text(data['turns'])
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    data = json.loads((ROOT / 'input.json').read_text(encoding='utf-8'))
    files = build(data)
    target = args.output_dir or ROOT
    paths = plan_outputs(target, files)
    for name, value in files.items():
        path = paths[name]
        if args.check:
            if not path.exists() or path.read_text(encoding='utf-8') != value:
                raise ValueError('Generated file missing or stale: ' + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding='utf-8')
    print(f"{data['kind']}: {len(files)} files {'current' if args.check else 'written'}")

if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)

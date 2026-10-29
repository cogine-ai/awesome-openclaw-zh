"""Generate original editable SVGs and a 3-page office-print PDF. Requires reportlab."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

root=Path(__file__).parent
parser=argparse.ArgumentParser()
parser.add_argument('--output-dir',default=str(root))
parser.add_argument('--font', default=str(root/'NotoSansSC-Regular.subset.ttf'))
args=parser.parse_args()
out=Path(args.output_dir).resolve();out.mkdir(parents=True,exist_ok=True)
d=json.loads((root/'event.json').read_text(encoding='utf-8'))
font = TTFont('NotoSansSC', args.font)
required = ''.join([d['event'], d['theme'], d['name'], d['sticker'], d['showcase'], *d['steps']])
required += 'DONE / 做成一件事A4贴纸0123三个步骤把版本留下来保留输入和可编辑工程记录失败与下一步修改一个周末，一份自己的作品三折页'
missing = sorted({c for c in required if ord(c) not in font.face.charToGlyph})
if missing:
 raise ValueError('Font lacks ' + ''.join(missing) + '; supply an authorized full Chinese TTF using --font')
pdfmetrics.registerFont(font)
palette={'ink':'#163b3d','green':'#116e62','paper':'#f6f5eb','accent':'#ed784c'}
def svg(w,h,body):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="{palette["paper"]}"/><g font-family="sans-serif" fill="{palette["ink"]}">{body}</g></svg>'
def text(x,y,s,size=5,**attrs):
 a=' '.join(f'{k.replace("_","-")}="{v}"' for k,v in attrs.items())
 return f'<text x="{x}" y="{y}" font-size="{size}" {a}>{escape(s)}</text>'
fold='<path d="M8 74H202" stroke="#8b9e94" stroke-width=".3" stroke-dasharray="2 2"/>'
face=''.join([text(105,26,d['event'],5,text_anchor='middle'),text(105,49,d['name'],14,text_anchor='middle'),text(105,62,d['theme'],4,text_anchor='middle')])
name=svg(210,148,fold+f'<g transform="rotate(180 105 37)">{face}</g><g transform="translate(0 74)">{face}</g>')
(out/'nameplate.svg').write_text(name, encoding='utf-8')
body=text(15,19,d['event']+' / 贴纸 A4',6)
for row in range(4):
 for col in range(2):
  x,y=15+col*95,32+row*60
  body+=f'<rect x="{x}" y="{y}" width="85" height="48" rx="5" fill="#ffffff" stroke="#116e62" stroke-width=".4"/>'
  body+=text(x+8,y+16,'DONE / 做成一件事',4)+text(x+8,y+29,d['sticker'][:5],6)+text(x+8,y+40,d['sticker'][5:],6)
(out/'stickers.svg').write_text(svg(210,297,body), encoding='utf-8')
body=''.join(f'<path d="M{x} 6V204" stroke="#8b9e94" stroke-width=".3" stroke-dasharray="2 2"/>' for x in (99,198))
for i,(h,lines) in enumerate([(d['event'],[d['theme'],'一个周末，一份自己的作品','']),('三个步骤',d['steps']),('把版本留下来',['保留输入和可编辑工程','记录失败与下一步修改',d['showcase']])]):
 x=i*99+10
 body+=text(x,35,'0'+str(i+1),14,fill='#116e62')+text(x,57,h,7)
 for j,line in enumerate(lines): body+=text(x,85+j*16,line,4.5)
 body+=text(x,188,'A4三折页',3.2,fill='#53716b')
(out/'trifold.svg').write_text(svg(297,210,body), encoding='utf-8')

c=canvas.Canvas(str(out/'event-kit.pdf'),pagesize=(210*mm,148*mm),pageCompression=1, invariant=1, initialFontName='NotoSansSC')
c.setTitle(d['event']+' - office print sample')
def pdf_text(x,y,s,size=5,center=False):
 c.setFont('NotoSansSC',size*mm);c.setFillColor(palette['ink'])
 (c.drawCentredString if center else c.drawString)(x*mm,y*mm,s)
def background(w,h): c.setFillColor(palette['paper']);c.rect(0,0,w*mm,h*mm,fill=1,stroke=0)
background(210,148)
c.setStrokeColor('#8b9e94');c.setDash(2*mm,2*mm);c.line(8*mm,74*mm,202*mm,74*mm);c.setDash()
for rotation in (0,180):
 c.saveState()
 if rotation: c.translate(210*mm,148*mm);c.rotate(180)
 pdf_text(105,53,d['event'],5,True);pdf_text(105,30,d['name'],14,True);pdf_text(105,16,d['theme'],4,True)
 c.restoreState()
c.showPage();c.setPageSize((210*mm,297*mm));background(210,297);pdf_text(15,278,d['event']+' / 贴纸 A4',6)
for row in range(4):
 for col in range(2):
  x,y=15+col*95,217-row*60
  c.setFillColor('#ffffff');c.setStrokeColor(palette['green']);c.roundRect(x*mm,y*mm,85*mm,48*mm,5*mm,fill=1)
  pdf_text(x+8,y+32,'DONE / 做成一件事',4);pdf_text(x+8,y+19,d['sticker'][:5],6);pdf_text(x+8,y+8,d['sticker'][5:],6)
c.showPage();c.setPageSize((297*mm,210*mm));background(297,210)
c.setStrokeColor('#8b9e94');c.setDash(2*mm,2*mm)
for x in (99,198): c.line(x*mm,6*mm,x*mm,204*mm)
c.setDash()
for i,(h,lines) in enumerate([(d['event'],[d['theme'],'一个周末，一份自己的作品','']),('三个步骤',d['steps']),('把版本留下来',['保留输入和可编辑工程','记录失败与下一步修改',d['showcase']])]):
 x=i*99+10
 pdf_text(x,175,'0'+str(i+1),14);pdf_text(x,153,h,7)
 for j,line in enumerate(lines): pdf_text(x,125-j*16,line,4.5)
 pdf_text(x,22,'A4三折页',3.2)
c.save()
print('Generated nameplate.svg, stickers.svg, trifold.svg and event-kit.pdf')

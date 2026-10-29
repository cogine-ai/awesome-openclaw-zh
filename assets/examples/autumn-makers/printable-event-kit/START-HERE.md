# 活动打印物料

打开event-kit.pdf，修改event.json中的活动、主题、姓名与步骤，再生成自己的版本。

需要Python3.10+与ReportLab4.4.9：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install reportlab==4.4.9
.venv/bin/python reproduce.py --output-dir ./output
```

Windows使用`.venv/Scripts/python.exe`。输出nameplate.svg、stickers.svg、trifold.svg和三页event-kit.pdf。

## 修改文字与字体

先控制标题长度，再调整字号和换行。随包NotoSansSC字体子集附OFL许可。新文字提示`Font lacks`时指定包含所需字符的授权TTF：

```bash
.venv/bin/python reproduce.py --output-dir ./output --font /path/to/full-chinese.ttf
```

## 打印

选择“实际大小／100%”，先用普通纸确认折法。桌牌为210×148mm，贴纸为A4纸上自行裁切，三折页为A4横向等宽三折。具体检查项见print-checklist.md。

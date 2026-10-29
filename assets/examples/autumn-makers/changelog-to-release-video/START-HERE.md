# 30秒发布片

播放landscape.mp4和portrait.mp4，修改props.json中的产品、三条更新和结尾。

需要Node.js与Chrome，工程固定Remotion / CLI 4.0.539、React19.2.0。团队使用前查看 https://www.remotion.dev/license 。

```bash
npm ci --ignore-scripts
node render.mjs
```

使用已有Chrome可设置REMOTION_BROWSER_EXECUTABLE：

```bash
REMOTION_BROWSER_EXECUTABLE="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" node render.mjs
```

Windows在PowerShell设置`$env:REMOTION_BROWSER_EXECUTABLE`为实际路径，再运行node render.mjs。

先渲染一帧：

```bash
npx --no-install remotion still src.tsx Landscape variant.png --frame=192 --props=variant-props.json
```

两个组合为960×540和540×960，24fps，各30秒。planned-subtitles.srt按五个章节编排，可用于添加旁白时调整字幕。

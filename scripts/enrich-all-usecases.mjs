#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const indexPath = path.join(root, 'resources', 'usecases-index.json');
const cacheDir = path.join(root, 'resources', 'source-cache');
fs.mkdirSync(cacheDir, { recursive: true });

const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

function encodePath(p) {
  return p.split('/').map(encodeURIComponent).join('/');
}

function cacheFileName(repo, sourcePath) {
  const safe = `${repo}__${sourcePath}`.replace(/[\\/:*?"<>|\s]+/g, '__');
  return path.join(cacheDir, `${safe}.txt`);
}

async function fetchSource(repo, sourcePath) {
  const c = cacheFileName(repo, sourcePath);
  if (fs.existsSync(c)) {
    return { ok: true, text: fs.readFileSync(c, 'utf8') };
  }

  const url = `https://raw.githubusercontent.com/${repo}/main/${encodePath(sourcePath)}`;
  const res = await fetch(url);
  if (!res.ok) {
    return { ok: false, text: '', error: `${res.status} ${res.statusText}` };
  }
  const text = await res.text();
  fs.writeFileSync(c, text, 'utf8');
  return { ok: true, text };
}

function splitSections(text) {
  const lines = text.split('\n');
  const sections = [];
  let current = { heading: '__intro__', lines: [] };
  for (const line of lines) {
    if (/^#{1,6}\s+/.test(line)) {
      sections.push(current);
      current = { heading: line.replace(/^#{1,6}\s+/, '').trim(), lines: [] };
    } else {
      current.lines.push(line);
    }
  }
  sections.push(current);
  return sections;
}

function pickLines(lines, limit = 4) {
  const out = [];
  for (const raw of lines) {
    const l = raw.trim();
    if (!l) continue;
    if (l.startsWith('```')) continue;
    if (l.startsWith('![')) continue;
    if (l.startsWith('<img')) continue;
    if (l.startsWith('|')) continue;
    if (/^\|[-\s:|]+\|$/.test(l)) continue;
    if (l.length < 10 || l.length > 220) continue;
    out.push(l.replace(/^[-*]\s+/, '').replace(/^\d+\.\s+/, ''));
    if (out.length >= limit) break;
  }
  return out;
}

function sectionsByKeywords(sections, keys) {
  const lower = keys.map((k) => k.toLowerCase());
  return sections.filter((s) => lower.some((k) => s.heading.toLowerCase().includes(k)));
}

function extractHighlights(text) {
  const sections = splitSections(text);

  const intro = pickLines(sections.find((s) => s.heading === '__intro__')?.lines || [], 3);
  const painSec = sectionsByKeywords(sections, ['pain', '场景', '问题', '背景', 'introduction', 'overview', 'what this is']);
  const actionSec = sectionsByKeywords(sections, ['what it does', 'how to', 'setup', '配置', '步骤', 'quick start', 'guide', '实战', 'prerequisite', '前提']);
  const toolSec = sectionsByKeywords(sections, ['skill', 'tool', '所需技能', '工具', '权限', 'integrations', 'channel']);
  const riskSec = sectionsByKeywords(sections, ['security', '风险', '注意', '边界', 'troubleshooting', 'gotcha']);
  const metricSec = sectionsByKeywords(sections, ['success', 'metric', '数据', '效率', 'roi', '效果']);

  const pain = pickLines(painSec.flatMap((s) => s.lines), 4);
  let action = pickLines(actionSec.flatMap((s) => s.lines), 6);
  if (action.length === 0) {
    action = pickLines(text.split('\n'), 6);
  }
  const toolsRaw = pickLines(toolSec.flatMap((s) => s.lines), 8);
  const risks = pickLines(riskSec.flatMap((s) => s.lines), 4);
  const metrics = pickLines(metricSec.flatMap((s) => s.lines), 3);

  // Tool tokens from backticks and known words
  const knownTools = ['Telegram', 'WhatsApp', 'Discord', 'Slack', 'Todoist', 'Notion', 'n8n', 'GitHub', 'Google Calendar', 'Gmail', 'cron', 'heartbeat', 'OpenClaw'];
  const textAll = text.slice(0, 20000);
  const toolSet = new Set();
  for (const m of textAll.matchAll(/`([^`]{2,40})`/g)) {
    const v = m[1].trim();
    if (/^[a-zA-Z0-9_\-./]+$/.test(v) && v.length <= 30) toolSet.add(v);
  }
  for (const t of knownTools) {
    const re = new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
    if (re.test(textAll)) toolSet.add(t);
  }

  const schedules = [];
  const schedRegs = [/\b\d{1,2}:\d{2}\b/g, /\b\d+\s+\d+\s+\*\s+\*\s+\*/g, /every\s+\d+\s+(minutes?|hours?)/ig, /每天|每周|每小时|夜间|晨间|定时/g];
  for (const re of schedRegs) {
    const m = textAll.match(re);
    if (m) {
      for (const x of m) schedules.push(x);
    }
  }

  return {
    intro,
    pain,
    action,
    toolsRaw,
    tools: [...toolSet].slice(0, 8),
    risks,
    metrics,
    schedules: [...new Set(schedules)].slice(0, 5),
  };
}

function mdList(items, fallback) {
  if (!items || items.length === 0) return `- ${fallback}`;
  return items.map((x) => `- ${x}`).join('\n');
}

function promptBlock(title, desc, highlights) {
  const toolHint = highlights.tools.length ? highlights.tools.join('、') : '源头未明确固定工具';
  const scheduleHint = highlights.schedules.length ? highlights.schedules.join('；') : '源头未明确固定调度';
  const actionHint = highlights.action.slice(0, 3).join('；') || desc;

  return `你是我的 OpenClaw 助手，现在执行案例「${title}」。

目标（来自来源案例）：${desc}
来源关键动作：${actionHint}
优先工具/渠道：${toolHint}
来源节奏信息：${scheduleHint}

请按下面流程输出并执行：
1. 先给出“最小可运行版本（MVP）”执行计划（3-5条）
2. 立刻产出第一版结果（不要只讲思路）
3. 缺失的信息统一放到“待我补充信息”里，不要中断整体流程
4. 若涉及高风险操作（删除、外发、改密、生产写操作），先暂停并请求确认

输出格式：
## 今日执行计划
## 立即可执行动作
## 第一版结果
## 待我补充信息
## 风险与边界`;
}

let okCount = 0;
let failCount = 0;

for (const item of index) {
  const fetched = await fetchSource(item.sourceRepo, item.sourcePath);
  const localAbs = path.join(root, item.localPath);
  fs.mkdirSync(path.dirname(localAbs), { recursive: true });

  if (!fetched.ok) {
    failCount += 1;
    const fallback = `# ${item.title}\n\n> ${item.desc}\n\n## 来源与对齐\n\n- 来源仓库： [${item.sourceRepo}](https://github.com/${item.sourceRepo})\n- 原始条目： [${item.sourcePath}](https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath})\n- 状态：源文件拉取失败（${fetched.error}）\n\n## 说明\n\n源文件暂不可获取，为避免幻觉，本页暂不补充推断性细节。\n\n## 可复制提示词（保守版）\n\n\`\`\`text\n请按案例「${item.title}」的目标执行：${item.desc}\n\n要求：\n1. 先给最小可运行版本\n2. 再给第一版可执行结果\n3. 缺失信息统一列在最后\n\`\`\`\n`;
    fs.writeFileSync(localAbs, fallback, 'utf8');
    continue;
  }

  okCount += 1;
  const h = extractHighlights(fetched.text);

  const md = `# ${item.title}

> ${item.desc}

## 来源与对齐

- 来源仓库： [${item.sourceRepo}](https://github.com/${item.sourceRepo})
- 原始条目： [${item.sourcePath}](https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath})
- 对齐原则：本页仅使用来源可见信息提炼，不臆造未出现配置

## 源头里这个案例是怎么做的

### 场景/痛点（来源提炼）
${mdList(h.pain.length ? h.pain : h.intro, '源头未单列“痛点”段落，可从简介理解该场景目标。')}

### 核心动作（来源提炼）
${mdList(h.action, '源头未给出明确步骤，建议先按最小闭环跑通。')}

### 技能/工具/渠道（来源提炼）
${mdList(h.toolsRaw.length ? h.toolsRaw : h.tools, '源头未明确固定技能或工具，按你当前可用渠道先跑通。')}

### 风险与边界（来源提炼）
${mdList(h.risks, '源头未明确列出风险条目，默认采用最小权限与二次确认。')}

## 快速开始（贴近来源的最小闭环）

1. 准备来源里提到的核心输入（账号、渠道、数据源、任务目标）。
2. 先在单次会话里手动跑通一次，不要直接上全自动。
3. 结果符合预期后，再增加定时/自动化频率。

## 可复制提示词（增强版）

\`\`\`text
${promptBlock(item.title, item.desc, h)}
\`\`\`

## 可选补充信息（提高效果）

- 你的常用渠道：[Telegram/飞书/微信/邮箱]
- 你的时区与执行时间：[例如 UTC+8，每天 09:00]
- 你最在意的结果指标：[例如 节省时间、回复率、发布频次]

## 效果检查（非技术版）

${mdList(h.metrics, '优先检查：是否比手工更快、是否稳定、是否可持续复用。')}

## 参考来源

- [${item.sourceRepo}](https://github.com/${item.sourceRepo})
- [${item.sourcePath}](https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath})
`;

  fs.writeFileSync(localAbs, md, 'utf8');
}

console.log(`Enriched files. source_ok=${okCount}, source_fail=${failCount}`);

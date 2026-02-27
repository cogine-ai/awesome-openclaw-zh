#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const indexPath = path.join(root, 'resources', 'usecases-index.json');
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

const sampleLocalPaths = [
  'usecases/productivity/multi-agent-team.md',
  'usecases/devops/n8n-workflow-orchestration.md',
  'usecases/productivity/family-calendar-household-assistant.md',
  'usecases/research/knowledge-base-rag.md',
  'usecases/productivity/todoist-task-manager.md',
  'usecases/everyday/52-morning-briefing-telegram.md',
  'usecases/memory/04-three-tier-memory-system.md',
  'usecases/security/31-skill-supply-chain-audit.md',
  'usecases/devops/homelab-access-showcase.md',
  'usecases/productivity/knowledge-worker-day-workflow.md'
];

const byPath = new Map(index.map((x) => [x.localPath, x]));

function encodePath(p) {
  return p.split('/').map(encodeURIComponent).join('/');
}

async function fetchSource(repo, sourcePath) {
  const url = `https://raw.githubusercontent.com/${repo}/main/${encodePath(sourcePath)}`;
  const res = await fetch(url);
  if (!res.ok) {
    return { ok: false, text: '', reason: `${res.status} ${res.statusText}` };
  }
  return { ok: true, text: await res.text(), reason: '' };
}

function splitSections(md) {
  const lines = md.split('\n');
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

function sectionHas(sections, keywords) {
  const low = keywords.map((k) => k.toLowerCase());
  return sections.some((s) => low.some((k) => s.heading.toLowerCase().includes(k)));
}

function grepLine(md, patterns) {
  const lines = md.split('\n').map((x) => x.trim()).filter(Boolean);
  const regs = patterns.map((p) => new RegExp(p, 'i'));
  const hit = lines.find((l) => regs.some((r) => r.test(l)) && l.length >= 8 && !l.startsWith('!['));
  return hit || '';
}

function hasCronOrSchedule(md) {
  const regs = [
    /cron/i,
    /heartbeat/i,
    /daily|weekly|hourly/i,
    /每天|每周|每小时|定时|计划任务|晨间|夜间/,
    /\b\d{1,2}:\d{2}\b/
  ];
  return regs.some((r) => r.test(md));
}

function pickKeyPoints(md, n = 3) {
  const lines = md.split('\n').map((x) => x.trim()).filter(Boolean);
  const candidates = [];
  for (const l of lines) {
    if (l.startsWith('- ') || l.startsWith('* ') || /^\d+\./.test(l) || /^\|/.test(l)) {
      if (l.length >= 10 && l.length <= 200) candidates.push(l);
    }
  }
  if (candidates.length < n) {
    for (const l of lines) {
      if (l.length >= 20 && l.length <= 140 && !/^#{1,6}\s+/.test(l) && !l.startsWith('```')) {
        candidates.push(l);
      }
      if (candidates.length >= n) break;
    }
  }
  return [...new Set(candidates)].slice(0, n);
}

const rows = [];
for (const localPath of sampleLocalPaths) {
  const meta = byPath.get(localPath);
  if (!meta) continue;
  const fetched = await fetchSource(meta.sourceRepo, meta.sourcePath);
  if (!fetched.ok) {
    rows.push({
      localPath,
      title: meta.title,
      source: `${meta.sourceRepo}/${meta.sourcePath}`,
      sourceOk: false,
      gap: '源文件拉取失败，无法分析',
      evidence: fetched.reason,
    });
    continue;
  }

  const md = fetched.text;
  const sections = splitSections(md);
  const srcHas = {
    pain: sectionHas(sections, ['pain point', '场景描述', '问题', '背景', 'introduction', 'overview']),
    setup: sectionHas(sections, ['how to set it up', 'how to setup', 'setup', '配置', '步骤', 'quick start', '实战配置']),
    tools: sectionHas(sections, ['skills you need', 'skills', 'tools', '所需技能', '工具', '权限']),
    risk: sectionHas(sections, ['security', '风险', '注意事项', '边界', 'troubleshooting', 'gotchas']),
    schedule: hasCronOrSchedule(md),
    metrics: sectionHas(sections, ['success metrics', 'efficiency', '效果', '数据', 'roi', '提升'])
  };

  const gaps = [];
  if (srcHas.pain) gaps.push('缺少“场景/痛点”原文要点');
  if (srcHas.setup) gaps.push('缺少“配置/步骤”可执行细节');
  if (srcHas.tools) gaps.push('缺少“技能/工具/渠道”前置清单');
  if (srcHas.schedule) gaps.push('缺少“定时/节奏”落地说明');
  if (srcHas.risk) gaps.push('缺少“风险与边界”提醒');
  if (srcHas.metrics) gaps.push('缺少“效果指标/成功标准”信息');

  const evidence = pickKeyPoints(md, 3).join('；');

  rows.push({
    localPath,
    title: meta.title,
    source: `${meta.sourceRepo}/${meta.sourcePath}`,
    sourceOk: true,
    gap: gaps.length ? gaps.join('；') : '模板覆盖较完整',
    evidence: evidence || grepLine(md, ['pain', 'setup', 'skills', 'cron', 'daily', '场景', '配置', '效率']) || '未提取到有效片段'
  });
}

let out = '# 10个案例差异分析（来源 vs 现有模板）\n\n';
out += '说明：当前旧模板仅包含「能做什么 + 3步 + 通用提示词 + 适合人群 + 来源」，对来源里的细节覆盖不足。\n\n';
out += '| 案例 | 来源 | 发现的差异点 | 来源证据（节选） |\n';
out += '|---|---|---|---|\n';
for (const r of rows) {
  out += `| [${r.title}](../${r.localPath}) | \`${r.source}\` | ${r.gap} | ${r.evidence.replace(/\|/g, '\\|')} |\n`;
}

out += '\n## 总结\n\n';
out += '主要差异集中在 6 类：\n\n';
out += '1. 来源有“场景与痛点”，旧模板没有对应版块。\n';
out += '2. 来源有“配置步骤/实战配置”，旧模板缺少可执行落地细节。\n';
out += '3. 来源有“技能/工具/渠道”要求，旧模板没有前置清单。\n';
out += '4. 来源经常有“定时任务/cron/heartbeat”，旧模板未体现运行节奏。\n';
out += '5. 来源常见“风险/边界/安全”，旧模板没有明确风险收口。\n';
out += '6. 来源部分包含效果数据/ROI，旧模板没有“效果验证”区。\n';

fs.writeFileSync(path.join(root, 'resources', '06-gap-analysis-10-cases.md'), out, 'utf8');
console.log('Wrote resources/06-gap-analysis-10-cases.md');

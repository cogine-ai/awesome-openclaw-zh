#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const indexPath = path.join(root, 'resources', 'usecases-index.json');
const templatePath = path.join(root, 'usecases', 'TEMPLATE.md');
const cacheDir = path.join(root, 'resources', 'source-cache');
fs.mkdirSync(cacheDir, { recursive: true });

if (!fs.existsSync(indexPath)) {
  console.error('Missing resources/usecases-index.json');
  process.exit(1);
}

const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
const templateText = fs.existsSync(templatePath) ? fs.readFileSync(templatePath, 'utf8') : '';

const OPENAI_API_KEY = process.env.OPENAI_API_KEY || '';
const OPENAI_MODEL = process.env.OPENAI_MODEL || 'gpt-4.1-mini';
const LLM_ENABLED = OPENAI_API_KEY.length > 0 && process.env.NO_LLM !== '1';
const MAX_SOURCE_CHARS = Number(process.env.MAX_SOURCE_CHARS || 14000);

function encodePath(p) {
  return p.split('/').map(encodeURIComponent).join('/');
}

function cacheFileName(repo, sourcePath) {
  const safe = `${repo}__${sourcePath}`.replace(/[\\/:*?"<>|\s]+/g, '__');
  return path.join(cacheDir, `${safe}.txt`);
}

async function fetchSource(repo, sourcePath) {
  const c = cacheFileName(repo, sourcePath);
  if (fs.existsSync(c)) return { ok: true, text: fs.readFileSync(c, 'utf8') };

  const url = `https://raw.githubusercontent.com/${repo}/main/${encodePath(sourcePath)}`;
  const res = await fetch(url);
  if (!res.ok) return { ok: false, text: '', error: `${res.status} ${res.statusText}` };

  const text = await res.text();
  fs.writeFileSync(c, text, 'utf8');
  return { ok: true, text };
}

function uniq(arr) {
  return [...new Set(arr.filter(Boolean))];
}

function cleanLine(s) {
  return s.replace(/^[-*]\s+/, '').replace(/^\d+\.\s+/, '').trim();
}

function extractCommands(text) {
  const lines = text.split('\n');
  const out = [];
  let inFence = false;
  let fenceLang = '';

  for (const raw of lines) {
    const line = raw.trim();
    if (line.startsWith('```')) {
      if (!inFence) {
        inFence = true;
        fenceLang = line.replace(/```+/, '').trim().toLowerCase();
      } else {
        inFence = false;
        fenceLang = '';
      }
      continue;
    }
    if (!inFence) continue;

    const shellLang = /^(bash|sh|shell|zsh|console|terminal)?$/i.test(fenceLang);
    if (!shellLang) continue;

    const cmdLike = /^(openclaw|npm|pnpm|yarn|npx|curl|wget|bash|sh|python|node|docker|git|tailscale|crontab|ssh|scp|export|jq|awk|sed|find|rg)\b/i.test(line);
    const noisy = /[：。！？【】《》“”]|^openclaw[:：]/.test(line);
    if (!cmdLike || noisy) continue;

    // Keep exact command line but avoid broken JSON snippets or pure braces.
    if (/^[{}\[\]",']+$/.test(line)) continue;
    out.push(line);
  }

  for (const m of text.matchAll(/`([^`\n]{3,140})`/g)) {
    const v = m[1].trim();
    if (/^(openclaw|npm|pnpm|npx|docker|git|tailscale|crontab|ssh)\b/i.test(v) && !/[：。！？【】《》“”]/.test(v)) {
      out.push(v);
    }
  }

  return uniq(out).slice(0, 12);
}

function extractSkillsAndTools(text) {
  const out = [];

  for (const m of text.matchAll(/`([^`\n]{2,60})`/g)) {
    const v = m[1].trim();
    if (/^[a-zA-Z0-9_./:-]+$/.test(v) && v.length <= 40) out.push(v);
  }

  const keywords = [
    'Telegram', 'WhatsApp', 'Discord', 'Slack', 'Notion', 'Todoist', 'n8n',
    'Google Calendar', 'Gmail', 'GitHub', 'Web Search', 'filesystem',
    'cron', 'heartbeat', 'OpenClaw', 'Tailscale', 'WireGuard', 'ZeroTier',
    'RSS', 'MCP'
  ];

  for (const k of keywords) {
    const re = new RegExp(k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i');
    if (re.test(text)) out.push(k);
  }

  const blacklist = new Set(['text', 'json', 'yaml', 'md', 'README', 'SOUL.md', 'AGENTS.md']);
  return uniq(out).filter((x) => !blacklist.has(x)).slice(0, 14);
}

function extractSchedule(text) {
  const out = [];
  for (const m of text.matchAll(/\b(?:\d+|\*)\s+(?:\d+|\*|\*\/\d+)\s+\*\s+\*\s+(?:\d+|\*|[0-7]-[0-7])\b/g)) out.push(m[0]);
  for (const m of text.matchAll(/\b\d{1,2}:\d{2}\b/g)) out.push(m[0]);
  for (const m of text.matchAll(/每天|每周|每小时|夜间|晨间|定时|每日/g)) out.push(m[0]);
  return uniq(out).slice(0, 10);
}

function extractRiskLines(text) {
  const lines = text.split('\n').map((l) => l.trim()).filter(Boolean);
  const sections = [];
  let heading = '__intro__';
  let bucket = [];
  for (const l of lines) {
    if (/^#{1,6}\s+/.test(l)) {
      sections.push({ heading, lines: bucket });
      heading = l.replace(/^#{1,6}\s+/, '').trim();
      bucket = [];
    } else {
      bucket.push(l);
    }
  }
  sections.push({ heading, lines: bucket });

  const riskSections = sections.filter((s) => /(risk|security|安全|风险|注意|边界|warning|troubleshooting|guardrail)/i.test(s.heading));
  const target = riskSections.length ? riskSections.flatMap((s) => s.lines) : lines;

  const out = [];
  const re = /(risk|security|安全|权限|边界|warning|注意|confirm|确认|漏洞|泄露|密码|secret|credential|key|token|ssh|acl|least|minimal|backup|restore)/i;
  for (const l of target) {
    if (!re.test(l)) continue;
    if (l.startsWith('#') || l.startsWith('|') || l.startsWith('```')) continue;
    const c = cleanLine(l);
    if (c.length < 8 || c.length > 180) continue;
    out.push(c);
    if (out.length >= 8) break;
  }
  return uniq(out);
}

function extractBenefitLines(text) {
  const lines = text.split('\n').map((l) => l.trim()).filter(Boolean);
  const out = [];
  const re = /(pain|problem|benefit|value|效率|提升|节省|场景|收益|目标|what it does|introduction|overview)/i;
  for (const l of lines) {
    if (l.startsWith('#') || l.startsWith('|') || l.startsWith('```')) continue;
    if (!re.test(l)) continue;
    const c = cleanLine(l);
    if (c.length >= 12 && c.length <= 180) out.push(c);
    if (out.length >= 4) break;
  }
  return uniq(out);
}

function extractActionLines(text) {
  const lines = text.split('\n').map((l) => l.trim()).filter(Boolean);
  const out = [];
  const re = /(setup|quick start|how to|步骤|配置|workflow|执行|daily|weekly|monitor|schedule|集成|自动)/i;
  for (const l of lines) {
    if (l.startsWith('#') || l.startsWith('|') || l.startsWith('```')) continue;
    const c = cleanLine(l);
    if (!re.test(c)) continue;
    if (c.length >= 10 && c.length <= 180) out.push(c);
    if (out.length >= 6) break;
  }
  return uniq(out);
}

function summarizeBenefitsChinese(item, ev) {
  const out = [];
  out.push(`你可以先把「${item.desc}」做成一个可重复执行的小流程。`);
  if (ev.schedule.length) out.push('这个场景适合加上定时执行，减少手动重复操作。');
  if (ev.skills.length) out.push('可结合现有技能与渠道，把结果直接推送到你常用入口。');
  if (ev.actions.length) out.push('建议先跑最小闭环，再按实际反馈逐步扩展。');
  return uniq(out).slice(0, 3);
}

function summarizeRisksChinese(lines) {
  if (!lines.length) return [];
  const text = lines.join(' ').toLowerCase();
  const out = [];
  if (/confirm|确认|destructive|danger/.test(text)) out.push('涉及删除、外发、改密等动作时，先确认再执行。');
  if (/password|secret|credential|token|key|apikey|密钥|凭证|密码/.test(text)) out.push('密钥与凭证不要放在公开文本或提示词中。');
  if (/ssh|tailscale|wireguard|zerotier|acl|permission|least|minimal|权限|最小/.test(text)) out.push('远程访问和权限建议按最小授权配置。');
  if (/backup|restore|回滚|rollback/.test(text)) out.push('关键变更前先备份，确保可回滚。');
  if (!out.length) out.push('先在测试环境验证，再应用到生产或长期任务。');
  return uniq(out).slice(0, 4);
}

function buildPrompt(item, sourceText, ev) {
  const truncated = sourceText.slice(0, MAX_SOURCE_CHARS);

  return {
    system: `你是严谨的文档编辑。目标是把来源文档改写成中文用户可读案例。
规则：
1) 不能编造来源没有的信息。
2) 不要出现“原文未提供/原文未单列/保持原文/非技术版”等元话术。
3) 如果某章节没有证据，直接省略该章节。
4) 命令与skills必须逐字保留，不要改写命令。
5) 说明性文字全部用中文。`,
    user: `请根据下面输入生成一个 Markdown 案例页。

【标题】${item.title}
【一句话目标】${item.desc}

【模板】
${templateText}

【可用证据(JSON)】
${JSON.stringify(ev, null, 2)}

【来源原文（截断）】
${truncated}

【输出要求】
- 只输出 Markdown 正文，不要解释过程。
- 必须包含：
  - 一级标题（案例标题）
  - 引用式一句话目标
  - 可复制提示词代码块
  - CITATION章节
- 可选章节（有证据才写）：
  - 这个案例能帮你做什么
  - 开始前准备
    - 技能与工具
    - 命令片段
    - 调度信息
  - 风险与边界
  - 使用建议
- 提示词不要出现“来自来源案例”等措辞。`,
  };
}

async function callOpenAIForMarkdown(item, sourceText, ev) {
  const { system, user } = buildPrompt(item, sourceText, ev);

  const body = {
    model: OPENAI_MODEL,
    input: [
      { role: 'system', content: system },
      { role: 'user', content: user }
    ],
    temperature: 0.2,
  };

  const res = await fetch('https://api.openai.com/v1/responses', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${OPENAI_API_KEY}`,
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const t = await res.text();
    throw new Error(`OpenAI API ${res.status}: ${t.slice(0, 300)}`);
  }

  const data = await res.json();
  const text = data.output_text || '';
  if (!text.trim()) throw new Error('Empty output_text from OpenAI');
  return text.trim() + '\n';
}

function formatDeterministic(item, ev) {
  const sections = [];

  sections.push(`# ${item.title}`);
  sections.push('');
  sections.push(`> ${item.desc}`);
  sections.push('');

  const benefitLines = summarizeBenefitsChinese(item, ev);
  if (benefitLines.length) {
    sections.push('## 这个案例能帮你做什么');
    sections.push('');
    for (const b of benefitLines) sections.push(`- ${b}`);
    sections.push('');
  }

  const hasPrep = ev.skills.length || ev.commands.length || ev.schedule.length;
  if (hasPrep) {
    sections.push('## 开始前准备');
    sections.push('');

    if (ev.skills.length) {
      sections.push('### 技能与工具');
      sections.push('');
      for (const s of ev.skills) sections.push(`- \`${s}\``);
      sections.push('');
    }

    if (ev.commands.length) {
      sections.push('### 命令片段');
      sections.push('');
      sections.push('```bash');
      for (const c of ev.commands) sections.push(c);
      sections.push('```');
      sections.push('');
    }

    if (ev.schedule.length) {
      sections.push('### 调度信息');
      sections.push('');
      for (const s of ev.schedule) sections.push(`- ${s}`);
      sections.push('');
    }
  }

  sections.push('## 可复制提示词');
  sections.push('');

  const skillHint = ev.skills.length ? ev.skills.slice(0, 6).join('、') : '你已启用的相关技能';
  sections.push('```text');
  sections.push(`你是我的 OpenClaw 助手，请帮我完成「${item.title}」。`);
  sections.push('');
  sections.push(`任务目标：${item.desc}`);
  sections.push('');
  sections.push('请按这个顺序执行：');
  sections.push('1. 先给出今天可落地的最小版本（3-5步）。');
  sections.push('2. 直接产出第一版结果，不要只讲思路。');
  sections.push('3. 如果缺少信息，把问题集中放在最后让我一次补全。');
  sections.push(`4. 使用我已启用的技能（优先：${skillHint}）。`);
  sections.push('5. 涉及高风险动作（删除、外发、改密、生产写操作）先暂停并请求确认。');
  sections.push('');
  sections.push('输出格式：');
  sections.push('## 今日执行计划');
  sections.push('## 立即可执行动作');
  sections.push('## 第一版结果');
  sections.push('## 我需要补充的信息');
  sections.push('## 风险提醒');
  sections.push('```');
  sections.push('');

  const riskLines = summarizeRisksChinese(ev.risks);
  if (riskLines.length) {
    sections.push('## 风险与边界');
    sections.push('');
    for (const r of riskLines) sections.push(`- ${r}`);
    sections.push('');
  }

  sections.push('## 使用建议');
  sections.push('');
  sections.push('- 先手动跑通一次，再设置自动化。');
  sections.push('- 先用一个渠道验证结果，再扩到更多渠道。');
  sections.push('- 关键动作建议保留确认步骤。');
  sections.push('');

  sections.push('## CITATION');
  sections.push('');
  sections.push(`- 来源仓库： [${item.sourceRepo}](https://github.com/${item.sourceRepo})`);
  sections.push(`- 原始条目： [${item.sourcePath}](https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath})`);
  sections.push('');

  return sections.join('\n');
}

function postClean(text) {
  let out = text;
  const banned = [
    '（保持原文）', '（非技术版）', '来自来源案例', '来源关键动作',
    '原文未提供', '原文未单列', '原文未给出', '原文未明确'
  ];
  for (const b of banned) {
    out = out.replaceAll(b, '');
  }
  // Clean accidental double spaces and duplicate blank lines
  out = out.replace(/[ \t]+\n/g, '\n').replace(/\n{3,}/g, '\n\n');
  return out.trim() + '\n';
}

let sourceOk = 0;
let sourceFail = 0;
let llmOk = 0;
let llmFail = 0;

for (const item of index) {
  const fetched = await fetchSource(item.sourceRepo, item.sourcePath);
  const abs = path.join(root, item.localPath);
  fs.mkdirSync(path.dirname(abs), { recursive: true });

  if (!fetched.ok) {
    sourceFail += 1;
    const fallback = `# ${item.title}\n\n> ${item.desc}\n\n## CITATION\n\n- 来源仓库： [${item.sourceRepo}](https://github.com/${item.sourceRepo})\n- 原始条目： [${item.sourcePath}](https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath})\n`;
    fs.writeFileSync(abs, fallback, 'utf8');
    continue;
  }

  sourceOk += 1;

  const sourceText = fetched.text;
  const evidence = {
    commands: extractCommands(sourceText),
    skills: extractSkillsAndTools(sourceText),
    schedule: extractSchedule(sourceText),
    risks: extractRiskLines(sourceText),
    benefits: extractBenefitLines(sourceText),
    actions: extractActionLines(sourceText),
  };

  let md = '';
  if (LLM_ENABLED) {
    try {
      md = await callOpenAIForMarkdown(item, sourceText, evidence);
      llmOk += 1;
    } catch (err) {
      llmFail += 1;
      md = formatDeterministic(item, evidence);
      console.error(`[LLM-FALLBACK] ${item.localPath}: ${String(err.message || err)}`);
    }
  } else {
    md = formatDeterministic(item, evidence);
  }

  md = postClean(md);
  fs.writeFileSync(abs, md, 'utf8');
}

console.log(`Done. source_ok=${sourceOk}, source_fail=${sourceFail}, llm_enabled=${LLM_ENABLED}, llm_ok=${llmOk}, llm_fail=${llmFail}`);

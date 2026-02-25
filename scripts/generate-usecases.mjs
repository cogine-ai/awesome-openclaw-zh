#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();

const files = {
  hesamCn: '/tmp/oc_hesam_README_CN.md',
  moltZh: '/tmp/oc_moltbook_README_zh.md',
};

for (const p of Object.values(files)) {
  if (!fs.existsSync(p)) {
    console.error(`Missing source file: ${p}`);
    process.exit(1);
  }
}

const categoryMap = {
  '社交媒体': { dir: 'social', label: '社交媒体' },
  '创意与构建': { dir: 'creative', label: '创意与构建' },
  '基础设施与 DevOps': { dir: 'devops', label: '基础设施与 DevOps' },
  '生产力': { dir: 'productivity', label: '生产力' },
  '研究与学习': { dir: 'research', label: '研究与学习' },
  '金融与交易': { dir: 'finance', label: '金融与交易' },
  '⭐ 日常生活 (20)': { dir: 'everyday', label: '日常生活' },
  '内容转换 (7)': { dir: 'content', label: '内容转换' },
  '内存管理 (8)': { dir: 'memory', label: '内存管理' },
  '夜间自动化 (12)': { dir: 'automation', label: '夜间自动化' },
  '数据分析 (11)': { dir: 'data', label: '数据分析' },
  '安全监控 (10)': { dir: 'security', label: '安全监控' },
  '工具开发 (2)': { dir: 'tools', label: '工具开发' },
};

const sourceMeta = {
  hesam: {
    repo: 'hesamsheikh/awesome-openclaw-usecases',
    mainUrl: 'https://github.com/hesamsheikh/awesome-openclaw-usecases',
  },
  moltbook: {
    repo: 'EvoLinkAI/awesome-openclaw-usecases-moltbook',
    mainUrl: 'https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook',
  },
};

function clean(s) {
  return s.trim().replace(/\s+/g, ' ');
}

function parseMarkdownRows(text, mode) {
  const lines = text.split('\n');
  const out = [];
  let currentHeading = '';

  for (const raw of lines) {
    const line = raw.trim();

    if (line.startsWith('## ')) {
      currentHeading = clean(line.replace(/^##\s+/, ''));
      continue;
    }

    if (!line.startsWith('|')) continue;

    if (mode === 'hesam') {
      // | [名称](usecases/xxx.md) | 描述 |
      const m = line.match(/^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*$/);
      if (!m) continue;
      const title = clean(m[1]);
      const sourcePath = clean(m[2]);
      const desc = clean(m[3]);
      if (title === '名称' || title === 'Name' || desc === '描述' || !sourcePath.startsWith('usecases/')) continue;
      if (!categoryMap[currentHeading]) continue;

      out.push({
        source: 'hesam',
        sourceRepo: sourceMeta.hesam.repo,
        sourceMain: sourceMeta.hesam.mainUrl,
        sourcePath,
        sourceUrl: `https://github.com/${sourceMeta.hesam.repo}/blob/main/${sourcePath}`,
        categoryRaw: currentHeading,
        categoryDir: categoryMap[currentHeading].dir,
        categoryLabel: categoryMap[currentHeading].label,
        title,
        desc,
      });
    } else {
      // | 51 | [标题](usecases/xx.md) | 描述 |
      const m = line.match(/^\|\s*([0-9]{1,2})\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.*?)\s*\|\s*$/);
      if (!m) continue;
      const idx = m[1].padStart(2, '0');
      const title = clean(m[2]);
      const sourcePath = clean(m[3]);
      const desc = clean(m[4]);
      if (!categoryMap[currentHeading]) continue;

      out.push({
        source: 'moltbook',
        sourceRepo: sourceMeta.moltbook.repo,
        sourceMain: sourceMeta.moltbook.mainUrl,
        sourcePath,
        sourceUrl: `https://github.com/${sourceMeta.moltbook.repo}/blob/main/${sourcePath}`,
        categoryRaw: currentHeading,
        categoryDir: categoryMap[currentHeading].dir,
        categoryLabel: categoryMap[currentHeading].label,
        title,
        desc,
        idx,
      });
    }
  }

  return out;
}

function slugFromPath(sourcePath) {
  const base = path.basename(sourcePath, '.md');
  return base
    .toLowerCase()
    .replace(/[^a-z0-9\-]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

const hesamCases = parseMarkdownRows(fs.readFileSync(files.hesamCn, 'utf8'), 'hesam');
const moltCases = parseMarkdownRows(fs.readFileSync(files.moltZh, 'utf8'), 'moltbook');

const combined = [...hesamCases, ...moltCases];

const seen = new Set();
const unique = [];

for (const c of combined) {
  const slug = slugFromPath(c.sourcePath);
  const key = `${slug}`;
  if (seen.has(key)) continue;
  seen.add(key);
  unique.push({ ...c, slug });
}

for (const c of unique) {
  const dir = path.join(root, 'usecases', c.categoryDir);
  fs.mkdirSync(dir, { recursive: true });
  const fp = path.join(dir, `${c.slug}.md`);

  const md = `# ${c.title}\n\n> ${c.desc}\n\n## 你可以拿它做什么\n\n这个案例的目标很直接：**${c.desc}**。\n\n如果你是第一次用 OpenClaw，建议先看 [5分钟快速上手](../../quickstart/00-5min-quickstart.md)。\n\n## 3 步快速开始\n\n1. 打开 OpenClaw（Web 控制台或你常用的聊天渠道，如 Telegram / 微信 / 飞书）。\n2. 把下面的提示词直接发给你的 OpenClaw。\n3. 根据你的实际信息替换方括号内容（如 [城市]、[邮箱]、[项目名]）。\n\n## 复制即用提示词\n\n\`\`\`text\n你是我的 OpenClaw 助手，请帮我完成「${c.title}」。\n\n目标：${c.desc}\n\n请按这个结构执行：\n1. 先用不超过 3 句话告诉我今天要做什么\n2. 再输出可直接执行的步骤（从现在开始）\n3. 需要我确认的地方，集中放到最后并给出默认建议\n4. 输出尽量简洁、可直接复制\n\n我的背景信息（按需补充）：\n- 城市/时区：[你的城市]\n- 常用渠道：[Telegram/飞书/微信/邮箱]\n- 关注主题：[例如 AI、产品、运营、家庭日程]\n\`\`\`\n\n## 适合人群\n\n- 想用 OpenClaw 快速见到结果的非技术用户\n- 想把重复事务自动化的内容创作者、运营、独立开发者\n- 想要一个可持续迭代工作流的个人或小团队\n\n## 来源\n\n- 来源仓库： [${c.sourceRepo}](https://github.com/${c.sourceRepo})\n- 原始条目： [${c.sourcePath}](${c.sourceUrl})\n- 本仓库首页： [awesome-openclaw-zh](../../README.md)\n\n`; 
  fs.writeFileSync(fp, md, 'utf8');
}

// Build category index
const byCategory = new Map();
for (const c of unique) {
  if (!byCategory.has(c.categoryLabel)) byCategory.set(c.categoryLabel, []);
  byCategory.get(c.categoryLabel).push(c);
}

for (const [k, arr] of byCategory.entries()) {
  arr.sort((a, b) => a.title.localeCompare(b.title, 'zh-Hans-CN'));
}

const categoryOrder = [
  '社交媒体',
  '创意与构建',
  '基础设施与 DevOps',
  '生产力',
  '研究与学习',
  '金融与交易',
  '日常生活',
  '内容转换',
  '内存管理',
  '夜间自动化',
  '数据分析',
  '安全监控',
  '工具开发',
];

let index = '# 用例总览\n\n';
index += `当前共收录 **${unique.length}** 个中文可用案例。\n\n`;
index += '按分类浏览：\n\n';

for (const cat of categoryOrder) {
  const arr = byCategory.get(cat) || [];
  if (!arr.length) continue;
  index += `## ${cat} (${arr.length})\n\n`;
  index += '| 用例 | 能干什么 |\n|---|---|\n';
  for (const c of arr) {
    const rel = `../usecases/${c.categoryDir}/${c.slug}.md`;
    index += `| [${c.title}](${rel}) | ${c.desc} |\n`;
  }
  index += '\n';
}

fs.writeFileSync(path.join(root, 'resources', 'usecases-index.md'), index, 'utf8');

// machine-readable index
const machine = unique.map((c) => ({
  title: c.title,
  desc: c.desc,
  category: c.categoryLabel,
  localPath: `usecases/${c.categoryDir}/${c.slug}.md`,
  sourceRepo: c.sourceRepo,
  sourcePath: c.sourcePath,
  sourceUrl: c.sourceUrl,
}));
fs.writeFileSync(path.join(root, 'resources', 'usecases-index.json'), JSON.stringify(machine, null, 2) + '\n', 'utf8');

console.log(`Generated ${unique.length} usecases.`);

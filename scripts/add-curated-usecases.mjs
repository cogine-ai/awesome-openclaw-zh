#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const indexJsonPath = path.join(root, 'resources', 'usecases-index.json');

if (!fs.existsSync(indexJsonPath)) {
  console.error('Missing resources/usecases-index.json');
  process.exit(1);
}

const existing = JSON.parse(fs.readFileSync(indexJsonPath, 'utf8'));

const extras = [
  {
    title: '社区版每日简报（Daily Brief）',
    desc: '每天自动汇总天气、日程、任务和重点信息，早上一次看完。',
    category: '生产力',
    localPath: 'usecases/productivity/daily-brief-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/daily-brief.md',
  },
  {
    title: '想法漏斗自动推进（Idea Pipeline）',
    desc: '把零散想法自动收集、筛选、排序并推进到下一步执行。',
    category: '研究与学习',
    localPath: 'usecases/research/idea-pipeline-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/idea-pipeline.md',
  },
  {
    title: '自托管知识库助手（Coeus）',
    desc: '把资料持续沉淀到可检索知识库，支持长期复用。',
    category: '研究与学习',
    localPath: 'usecases/research/coeus-knowledge-base-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/coeus-knowledge-base.md',
  },
  {
    title: 'LinkedIn 周更草稿助手',
    desc: '按你的口吻自动生成周更内容草稿，减少写作启动成本。',
    category: '内容转换',
    localPath: 'usecases/content/linkedin-drafter-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/linkedin-drafter.md',
  },
  {
    title: '每周技术发现精选',
    desc: '自动追踪和筛选技术动态，输出可读性高的周报。',
    category: '社交媒体',
    localPath: 'usecases/social/tech-discoveries-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/tech-discoveries.md',
  },
  {
    title: '家庭实验室远程安全访问',
    desc: '通过聊天工具安全触发远程运维操作，降低误操作风险。',
    category: '基础设施与 DevOps',
    localPath: 'usecases/devops/homelab-access-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/homelab-access.md',
  },
  {
    title: '编码任务编排中心（Agent Orchestrator）',
    desc: '把编码任务路由给最合适的工具链，提升多任务效率。',
    category: '基础设施与 DevOps',
    localPath: 'usecases/devops/agent-orchestrator-showcase.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'showcases/agent-orchestrator.md',
  },
  {
    title: '轮询心跳巡检模式',
    desc: '用单一心跳任务轮流检查关键事项，稳定且省成本。',
    category: '夜间自动化',
    localPath: 'usecases/automation/heartbeat-rotating-checks.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/heartbeat-example.md',
  },
  {
    title: 'API配额监控与提醒',
    desc: '自动检查模型配额与调用消耗，避免突发中断。',
    category: '安全监控',
    localPath: 'usecases/security/api-quota-monitor.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/check-quotas-README.md',
  },
  {
    title: '技能构建提示词工厂',
    desc: '用标准提示词批量生成可维护技能，减少重复劳动。',
    category: '工具开发',
    localPath: 'usecases/tools/skill-builder-prompt-workflow.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/skill-builder-prompt.md',
  },
  {
    title: '任务追踪透明化中心',
    desc: '把智能体任务状态结构化记录，随时看到进展与阻塞。',
    category: '生产力',
    localPath: 'usecases/productivity/task-tracking-workflow-center.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/task-tracking-prompt.md',
  },
  {
    title: '生产级安全加固包',
    desc: '按最小权限和隔离原则配置运行环境，降低长期风险。',
    category: '安全监控',
    localPath: 'usecases/security/production-security-hardening.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/security-hardening.md',
  },
  {
    title: '安全快速启动模板',
    desc: '快速建立基础安全策略，适合新手的第一套防护。',
    category: '安全监控',
    localPath: 'usecases/security/security-quickstart-guardrails.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/security-quickstart.md',
  },
  {
    title: '提示词注入防护清单',
    desc: '为外部信息输入建立防注入规则，减少被诱导执行。',
    category: '安全监控',
    localPath: 'usecases/security/prompt-injection-defense-playbook.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/security-patterns.md',
  },
  {
    title: 'VPS部署与加固流程',
    desc: '从部署到安全收口的一体化流程，适合长期在线运行。',
    category: '基础设施与 DevOps',
    localPath: 'usecases/devops/vps-deployment-hardening.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/vps-setup.md',
  },
  {
    title: '子代理并发调度模式',
    desc: '把复杂任务拆分为多个子代理并行执行，缩短总耗时。',
    category: '夜间自动化',
    localPath: 'usecases/automation/subagent-spawning-patterns.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/spawning-patterns.md',
  },
  {
    title: '可公开配置基线模板',
    desc: '通过脱敏配置建立团队基线，方便复制和协作。',
    category: '工具开发',
    localPath: 'usecases/tools/sanitized-config-baseline.md',
    sourceRepo: 'digitalknk/openclaw-runbook',
    sourcePath: 'examples/config-example-guide.md',
  },
  {
    title: '知识工作者全天工作流',
    desc: '覆盖日报、资料、会议、复盘的一整天效率流程。',
    category: '生产力',
    localPath: 'usecases/productivity/knowledge-worker-day-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '程序员开发助手工作流',
    desc: '从代码检索到Bug处理的日常开发支持方案。',
    category: '生产力',
    localPath: 'usecases/productivity/programmer-dev-assistant-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '学生学习助手工作流',
    desc: '课程管理、复习规划、作业辅助的一体化学习流程。',
    category: '生产力',
    localPath: 'usecases/productivity/student-learning-assistant-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '云端智能日报系统',
    desc: '在云端固定时间推送个性化日报，适合长期运营。',
    category: '日常生活',
    localPath: 'usecases/everyday/cloud-daily-report-system.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '云端智能备忘录管理',
    desc: '把碎片想法自动沉淀成可检索备忘录。',
    category: '内存管理',
    localPath: 'usecases/memory/cloud-smart-memo-manager.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '滚动式待办提醒系统',
    desc: '按优先级持续滚动提醒，降低待办遗漏。',
    category: '生产力',
    localPath: 'usecases/productivity/rolling-todo-reminder.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '云端内容创作工作流',
    desc: '把选题、写作、发布串成全自动内容生产线。',
    category: '内容转换',
    localPath: 'usecases/content/cloud-content-creation-flow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: 'AI编程协作模式',
    desc: '把编码、测试、修复流程交给AI协作完成。',
    category: '基础设施与 DevOps',
    localPath: 'usecases/devops/ai-coding-collaboration.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/12-personal-productivity.md',
  },
  {
    title: '全自动信息收集系统',
    desc: '从多来源持续收集信息并自动归类。',
    category: '数据分析',
    localPath: 'usecases/data/full-auto-info-collector.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '智能任务管理系统',
    desc: '自动拆解任务、安排优先级并跟踪进度。',
    category: '生产力',
    localPath: 'usecases/productivity/intelligent-task-management-system.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '自动化内容创作流水线',
    desc: '从资料收集到成稿发布的一体化内容自动化。',
    category: '内容转换',
    localPath: 'usecases/content/auto-content-creation-pipeline.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '效率数据监控系统',
    desc: '持续记录效率指标并给出优化建议。',
    category: '数据分析',
    localPath: 'usecases/data/efficiency-metrics-monitoring.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '全自动学习系统（Skills组合）',
    desc: '把学习任务自动化，形成持续学习闭环。',
    category: '研究与学习',
    localPath: 'usecases/research/skills-combo-auto-learning-system.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '数据分析工作流（Skills组合）',
    desc: '通过多个技能协同完成数据处理和输出。',
    category: '数据分析',
    localPath: 'usecases/data/skills-combo-data-analysis-flow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: '个人知识图谱构建',
    desc: '把知识点和关系沉淀成图谱，提升检索与复盘效率。',
    category: '内存管理',
    localPath: 'usecases/memory/personal-knowledge-graph-builder.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/13-advanced-automation.md',
  },
  {
    title: 'AI绘画生产工作流',
    desc: '从想法到配图的批量化创作流程，适合内容团队。',
    category: '创意与构建',
    localPath: 'usecases/creative/ai-image-generation-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/14-creative-applications.md',
  },
  {
    title: '视频脚本生成工作流',
    desc: '短视频与长视频脚本自动生成，支持系列化输出。',
    category: '创意与构建',
    localPath: 'usecases/creative/video-script-generator-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/14-creative-applications.md',
  },
  {
    title: '多语言翻译助手',
    desc: '支持文档、对话、批量翻译的多语种工作流。',
    category: '内容转换',
    localPath: 'usecases/content/multilingual-translation-assistant.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/14-creative-applications.md',
  },
  {
    title: '多Agent头脑风暴',
    desc: '用多代理并行讨论复杂问题，快速收敛可执行方案。',
    category: '创意与构建',
    localPath: 'usecases/creative/multi-agent-brainstorm-workflow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/14-creative-applications.md',
  },
  {
    title: '10分钟全平台内容发布',
    desc: '把选题、成稿、分发整合为一个快节奏发布流程。',
    category: '内容转换',
    localPath: 'usecases/content/ten-minute-multi-platform-publishing.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/15-solo-entrepreneur-cases.md',
  },
  {
    title: '多机器人多Agent矩阵',
    desc: '多渠道机器人协同，按角色分工处理不同业务任务。',
    category: '生产力',
    localPath: 'usecases/productivity/multi-bot-multi-agent-matrix.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/15-solo-entrepreneur-cases.md',
  },
  {
    title: '1天冷启动付费社群流程',
    desc: '从定位到执行的高密度冷启动运营打法。',
    category: '研究与学习',
    localPath: 'usecases/research/one-day-paid-community-launch.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/15-solo-entrepreneur-cases.md',
  },
  {
    title: 'Notion全自动运营工作流',
    desc: '把内容与运营动作自动落到 Notion，减少手工维护。',
    category: '生产力',
    localPath: 'usecases/productivity/notion-automatic-operation-flow.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'docs/04-practical-cases/15-solo-entrepreneur-cases.md',
  },
  {
    title: '批量文件处理助手',
    desc: '批量处理文档并生成摘要，适合资料密集型任务。',
    category: '生产力',
    localPath: 'usecases/productivity/batch-file-processing-assistant.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'examples/automation/batch-process-files.sh',
  },
  {
    title: '网站更新监控通知',
    desc: '自动监控目标网站变化并在有更新时提醒。',
    category: '数据分析',
    localPath: 'usecases/data/website-change-monitor-alert.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'examples/automation/website-monitor.sh',
  },
  {
    title: '配置自动备份与保留',
    desc: '定时备份配置并自动清理旧文件，降低故障损失。',
    category: '安全监控',
    localPath: 'usecases/security/config-backup-automation.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'examples/automation/backup-config.sh',
  },
  {
    title: '每日AI行业日报推送',
    desc: '每天定时推送 AI 行业动态，快速掌握最新趋势。',
    category: '社交媒体',
    localPath: 'usecases/social/daily-ai-news-report-push.md',
    sourceRepo: 'xianyu110/awesome-openclaw-tutorial',
    sourcePath: 'examples/automation/daily-report.sh',
  }
];

function buildUsecaseMd(item) {
  const sourceUrl = `https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath}`;
  return `# ${item.title}\n\n> ${item.desc}\n\n## 你可以拿它做什么\n\n这个案例重点是：**${item.desc}**\n\n适合希望“少折腾、快见效”的用户。\n\n## 3 步快速开始\n\n1. 打开 OpenClaw（建议先连接一个常用聊天渠道）。\n2. 复制下面提示词并发给 OpenClaw。\n3. 按你的场景替换方括号内容，先跑通一次再逐步优化。\n\n## 复制即用提示词\n\n\`\`\`text\n请帮我执行「${item.title}」。\n\n目标：${item.desc}\n\n输出要求：\n1. 先给我一个今日执行版本（可直接用）\n2. 再给我一个每周复用版本（可持续）\n3. 如果有风险或需要确认，放在最后单独列出\n\n我的信息：\n- 使用场景：[个人/团队]\n- 常用渠道：[微信/飞书/Telegram/邮箱]\n- 时间偏好：[如每天9点]\n\`\`\`\n\n## 适合人群\n\n- 希望快速落地 OpenClaw 的非技术用户\n- 想把重复事项交给自动化的内容/运营/产品用户\n- 想建立长期可复用流程的小团队\n\n## 来源\n\n- 来源仓库： [${item.sourceRepo}](https://github.com/${item.sourceRepo})\n- 原始条目： [${item.sourcePath}](${sourceUrl})\n- 本仓库首页： [awesome-openclaw-zh](../../README.md)\n`;
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

const combined = [...existing];
const existingByPath = new Set(existing.map((x) => x.localPath));

for (const item of extras) {
  if (existingByPath.has(item.localPath)) continue;

  const abs = path.join(root, item.localPath);
  fs.mkdirSync(path.dirname(abs), { recursive: true });
  fs.writeFileSync(abs, buildUsecaseMd(item), 'utf8');

  combined.push({
    title: item.title,
    desc: item.desc,
    category: item.category,
    localPath: item.localPath,
    sourceRepo: item.sourceRepo,
    sourcePath: item.sourcePath,
    sourceUrl: `https://github.com/${item.sourceRepo}/blob/main/${item.sourcePath}`,
  });
}

// Sort stable by category order then title
const categoryRank = new Map(categoryOrder.map((c, i) => [c, i]));
combined.sort((a, b) => {
  const ra = categoryRank.has(a.category) ? categoryRank.get(a.category) : 999;
  const rb = categoryRank.has(b.category) ? categoryRank.get(b.category) : 999;
  if (ra !== rb) return ra - rb;
  return a.title.localeCompare(b.title, 'zh-Hans-CN');
});

fs.writeFileSync(indexJsonPath, JSON.stringify(combined, null, 2) + '\n', 'utf8');

// rebuild markdown index
const byCat = new Map();
for (const c of combined) {
  if (!byCat.has(c.category)) byCat.set(c.category, []);
  byCat.get(c.category).push(c);
}

let md = '# 用例总览\n\n';
md += `当前共收录 **${combined.length}** 个中文可用案例。\n\n`;
md += '按分类浏览：\n\n';
for (const cat of categoryOrder) {
  const arr = byCat.get(cat) || [];
  if (!arr.length) continue;
  md += `## ${cat} (${arr.length})\n\n`;
  md += '| 用例 | 能干什么 |\n|---|---|\n';
  for (const c of arr) {
    md += `| [${c.title}](../${c.localPath}) | ${c.desc} |\n`;
  }
  md += '\n';
}
fs.writeFileSync(path.join(root, 'resources', 'usecases-index.md'), md, 'utf8');

console.log(`Combined usecases: ${combined.length}`);

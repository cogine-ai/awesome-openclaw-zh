# X 个人资料抓取器

> 定时抓取 X 账号资料、近期帖子和外链内容，形成可复盘数据集。

## 这个案例能帮你做什么

- 自动保存目标账号画像，避免信息丢失和手工收集。
- 自动展开短链并补抓标题，提高线索可读性。
- 统一导出 CSV 与按天归档，方便销售/研究使用。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `web_fetch` | 抓取资料页与链接内容 | OpenClaw Built-in |
| 外部 | [`web_search`](https://clawhub.ai/skills/searching-assistant) | 补充关联信息 | ClawHub |
| 内置 | `csv` | 输出结构化报表 | OpenClaw Built-in |
| 内置 | `filesystem` | 按日期归档抓取结果 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先抓 3 个账号做验证：

```text
你是我的 OpenClaw 助手。
请帮我做“X 个人资料抓取器”的预演版：
1. 读取目标账号列表中的前3个账号。
2. 抓取资料和最近10条帖子。
3. 尝试展开 t.co 链接并提取标题。
4. 输出 CSV 预览和失败项。
```

## 稳定自动版（可长期运行）

### 1) 目标配置 `config/x-targets.json`

```json
{
  "profiles": [
    { "handle": "elonmusk", "category": "tech", "priority": "high" },
    { "handle": "sama", "category": "ai", "priority": "high" },
    { "handle": " Naval", "category": "philosophy", "priority": "medium" }
  ],
  "schedule": "daily",
  "posts_to_capture": 10,
  "follow_links": true
}
```

### 2) 抓取脚本 `skills/x-scraper/index.js`

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

async function scrapeProfile(handle) {
  const url = `https://nitter.net/${handle}`; // Or similar proxy
  const html = await web_fetch(url);
  const $ = cheerio.load(html);

  const profile = {
    handle,
    display_name: $('.profile-card-fullname').text(),
    bio: $('.profile-card-bio').text(),
    followers: parseNumber($('.followers .profile-stat-num').text()),
    following: parseNumber($('.following .profile-stat-num').text()),
    posts: []
  };

  $('.timeline-item').slice(0, 10).each((i, el) => {
    const $post = $(el);
    profile.posts.push({
      date: $post.find('.tweet-date').attr('title'),
      content: $post.find('.tweet-content').text(),
      links: $post.find('a').map((i, a) => $(a).attr('href')).get(),
      replies: parseInt($post.find('.icon-comment').next().text()) || 0,
      retweets: parseInt($post.find('.icon-retweet').next().text()) || 0,
      likes: parseInt($post.find('.icon-heart').next().text()) || 0
    });
  });

  return profile;
}
```

### 3) 短链展开逻辑

```javascript
async function expandLinks(posts) {
  for (const post of posts) {
    post.expanded_links = await Promise.all(
      post.links
        .filter(l => l.includes('t.co'))
        .map(async shortUrl => {
          try {
            const full = await resolveRedirect(shortUrl);
            const content = await web_fetch(full);
            return { url: full, title: extractTitle(content) };
          } catch (e) {
            return { url: shortUrl, error: e.message };
          }
        })
    );
  }
  return posts;
}
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“X Profile Scraper”。
请使用 Skills：web_fetch、web_search、csv、filesystem。

每天 06:00：
1. 读取 config/x-targets.json。
2. 抓取账号资料与最近10条帖子。
3. 展开 t.co 链接并抓取标题。
4. 保存到 data/x-profiles/YYYY-MM-DD/。
5. 生成 CSV 摘要。
6. 对 follower 增长 >20% 的账号标记提醒。

限速规则：
- Max 1 request per 5 seconds
- Rotate User-Agent
- Respect robots.txt
```

### 5) 调度配置

```json
{
  "schedule": "0 6 * * *",
  "task": "x_profile_scraper",
  "concurrency": 1,
  "delay_between_requests": 5000
}
```

## 成功标准

- [ ] 100% of target profiles captured daily
- [ ] Link expansion success > 90%
- [ ] Data archived for 90 days
- [ ] Keyword alerts within 1 hour

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/08-x-profile-scraper.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/08-x-profile-scraper.md)

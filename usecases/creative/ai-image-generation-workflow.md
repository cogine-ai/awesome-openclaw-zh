# AI绘画生产工作流

> 把“想法到配图”做成可复用流程，支持手机下发、语音修改和批量出图。

## 这个案例能帮你做什么

- 在一个入口里完成绘图、改图、批量生成，减少来回切工具。
- 更适合教程配图、白板总结图、社媒配图等高频内容场景。
- 通过批量参数和自动同步配置，稳定提升出图效率。

## 你需要的 Skills（按类型）

| 类型 | Skill / 工具 | 用途 | 来源 |
|---|---|---|---|
| 外部 | `bananapro-image-gen` | Gemini 图像生成主流程 | xianyu110/my-awesome-skills |
| 外部 | `banana-pro` | OpenClaw 图像能力扩展 | ClawHub |
| 外部 | `fal-ai` / `nvidia-image-gen` / `pollinations` / `venice-ai` / `recraft` | 备选绘图能力 | ClawHub |

## 快速体验版（先跑一轮）

先跑一张图 + 一次改图：

```text
你是我的 OpenClaw 助手。
请帮我做“AI绘画生产工作流”的预演版：
1. 生成一张“可爱的小龙虾，赛博朋克风格”的图片。
2. 再按“更酷一点，增加机械感”修改一次。
3. 输出最终图和提示词优化结果。
4. 本轮只做单图演示，不做批量任务。
```

## 稳定自动版（可长期运行）

### 1) 安装 `bananapro-image-gen`

```bash
# 方式1：GitHub安装（推荐）
git clone https://github.com/xianyu110/my-awesome-skills.git
cp -r my-awesome-skills/.claude/skills/bananapro-image-gen ~/.openclaw/skills/
cd ~/.openclaw/skills/bananapro-image-gen
pip3 install -r requirements.txt

# 方式2：npx安装
npx skills add https://github.com/xianyu110/my-awesome-skills --skill bananapro-image-gen
```

### 2) 验证安装

```bash
ls ~/.openclaw/skills/bananapro-image-gen
```

### 3) API 配置

```bash
nano ~/.openclaw/openclaw.json
```

```json
{
  "api": {
    "gemini": {
      "apiKey": "your-api-key-here",
      "baseUrl": "https://apipro.maynor1024.live",
      "model": "gemini-3-pro-image-preview"
    }
  }
}
```

### 4) OpenClaw 参数配置（批量模式）

```bash
# 1. 安装Banana Pro Skills
clawhub install banana-pro
openclaw config set banana.api-key "YOUR_API_KEY"

# 2. 配置Gemini API（Banana Pro需要）
openclaw config set gemini.api-key "YOUR_GEMINI_KEY"
openclaw config set gemini.model "gemini-2.0-flash-exp"

# 3. 配置图片保存
openclaw config set image.save-path "~/Pictures/OpenClaw"
openclaw config set image.auto-sync true
openclaw config set image.sync-to "feishu,notion"

# 4. 配置批量处理
openclaw config set image.batch-size 10
openclaw config set image.parallel-tasks 3

# 5. 配置提示词优化
openclaw config set image.prompt-enhance true
openclaw config set image.prompt-language "en"
```

### 5) 批量生成测试

```bash
cd ~/.openclaw/skills/bananapro-image-gen
bash test_chapters.sh
```

### 6) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“AI绘画生产工作流”。
请使用 bananapro-image-gen 与 banana-pro。

执行流程：
1. 接收主题并自动优化提示词。
2. 生成目标风格图片（默认 1K）。
3. 支持语音/文本二次修改。
4. 批量任务按 image.batch-size 和 image.parallel-tasks 执行。
5. 自动保存并同步到配置目标（feishu/notion）。
```

## 成功标准

| 任务类型 | 使用前 | 使用后 | 节省时间 | 提升比例 |
|---|---:|---:|---:|---:|
| 单张绘画 | 5分钟 | 30秒 | 4.5分钟 | 90% |
| 修改图片 | 3分钟 | 20秒 | 2.7分钟 | 88.9% |
| 批量生成 | 50分钟 | 5分钟 | 45分钟 | 90% |
| 风格转换 | 10分钟 | 40秒 | 9.3分钟 | 93.3% |
| 平均 | 68分钟 | 6.5分钟 | 61.5分钟 | 90.4% |

## 引用来源

- 来源仓库： [xianyu110/awesome-openclaw-tutorial](https://github.com/xianyu110/awesome-openclaw-tutorial)
- 原始条目： [docs/04-practical-cases/14-creative-applications.md](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/04-practical-cases/14-creative-applications.md)

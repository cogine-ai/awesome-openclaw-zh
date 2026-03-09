# 仓库目录重构方案（2026-03-08）

目标：把仓库从“以案例为主的中文整理仓”升级成“中文上手 + 部署 + 接入 + 使用场景”的标准库。

## 一、重构原则

- 不打散现有 `usecases/` 结构，避免伤到已有索引和分类。
- 把“部署”和“渠道接入”从 `resources/` 提升为一级目录，因为它们已经不是附属信息。
- `quickstart/` 只负责“上手路径”，不再承担完整安装说明。
- `resources/` 回归为“说明型资料”和“辅助决策资料”。

## 二、建议目录树

```text
awesome-openclaw-zh/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── deploy/
│   ├── README.md
│   ├── 01-macos-local.md
│   ├── 02-windows.md
│   ├── 03-linux-vps-baseline.md
│   ├── 11-aliyun-ecs.md
│   ├── 12-tencent-cvm.md
│   └── 13-volcengine-ecs.md
├── channels/
│   ├── README.md
│   ├── 01-feishu.md
│   ├── 02-dingtalk.md
│   ├── 03-wecom.md
│   └── 04-qq.md
├── quickstart/
│   ├── 00-5min-quickstart.md
│   └── 01-7day-path.md
├── resources/
│   ├── 01-install-and-deploy.md
│   ├── 02-model-channel-skill-guide.md
│   ├── 03-source-map.md
│   ├── 04-top5-repos-notes.md
│   ├── usecases-index.md
│   └── usecases-index.json
├── playbooks/
├── usecases/
└── draft/
```

## 三、现有文件怎么调整

### 1. `README.md`

要改，而且建议改成“分阶段入口”。

现在的问题：

- “新手先看（3步）”默认把部署压缩得过轻
- `5分钟快速上手` 文档还承担了“先安装”职责
- 新增部署文档后，用户路径会混乱

建议改成：

- `还没部署`
- `已经部署好`
- `想直接找案例`

### 2. `quickstart/00-5min-quickstart.md`

要重写定位，但不需要改名。

建议新的角色是：

- “部署后 5 分钟快速体验”

文档开头明确写：

- 还没部署：先看 `deploy/README.md`
- 已经部署：继续本篇

### 3. `quickstart/01-7day-path.md`

只需要小改。

Day 1 应该改成：

- 选部署路径
- 完成安装
- 跑通第一条消息

并且把 Day 1 的入口改到 `deploy/README.md`。

### 4. `resources/01-install-and-deploy.md`

建议从“正文型文档”降级成“索引页 / 跳转页”。

它的职责改成：

- 指向 `deploy/README.md`
- 指向后续 `channels/README.md`
- 保留对模型、技能、低成本运行的辅助入口

## 四、README 新版文案骨架

下面这版是可以直接继续打磨的骨架。

---

# OpenClaw 中文最佳实践库

一个面向中文用户的 OpenClaw 开源仓库：
**先部署成功，再接入渠道，再跑通第一个场景。**

本仓库覆盖三类核心内容：

- 部署安装：Mac、Windows、Linux VPS
- 渠道接入：飞书、钉钉、企业微信、QQ
- 使用场景：176 个真实案例与工作流

## 开始这里

### 还没部署

1. [部署与安装中心](./deploy/README.md)
2. [部署后 5 分钟快速体验](./quickstart/00-5min-quickstart.md)
3. [7 天上手路径](./quickstart/01-7day-path.md)

### 已经部署好

1. [部署后 5 分钟快速体验](./quickstart/00-5min-quickstart.md)
2. [7 天上手路径](./quickstart/01-7day-path.md)
3. [按分类找案例（176个）](./resources/usecases-index.md)

### 想先看完整能力范围

- [部署文档](./deploy/README.md)
- [案例索引](./resources/usecases-index.md)
- [模型、渠道、技能怎么选](./resources/02-model-channel-skill-guide.md)
- [低成本稳定运行](./playbooks/01-low-cost-stable-run.md)

## 推荐入口

- 有 Mac：看 [macOS 本地部署](./deploy/01-macos-local.md)
- 用 Windows：看 [Windows 部署](./deploy/02-windows.md)
- 想 24 小时在线：看 [Linux VPS 通用部署](./deploy/03-linux-vps-baseline.md)

## 你可以先从这 10 个场景开始

保留现有 10 个精选案例列表。

## 分类导航

保留现有分类导航。

## 部署与运行

- [部署与安装中心](./deploy/README.md)
- [模型、渠道、技能怎么选](./resources/02-model-channel-skill-guide.md)
- [低成本稳定运行](./playbooks/01-low-cost-stable-run.md)
- [安全与权限边界](./playbooks/02-safe-usage-boundary.md)

## 投稿与共建

- [贡献指南](./CONTRIBUTING.md)
- 用例投稿模板
- 部署文档投稿规范（后续新增）
- 渠道接入投稿规范（后续新增）

## 说明与致谢

保留现有上游仓库致谢，但建议把 `xianyu110/awesome-openclaw-tutorial` 和 OpenClaw 官方文档单独点出来，说明部署文档参考来源。

---

## 五、落地顺序建议

第一批：

1. `deploy/README.md`
2. `deploy/01-macos-local.md`
3. `deploy/02-windows.md`
4. `deploy/03-linux-vps-baseline.md`

第二批：

5. `channels/README.md`
6. `channels/01-feishu.md`
7. `channels/02-dingtalk.md`
8. `channels/03-wecom.md`
9. `channels/04-qq.md`

第三批：

10. `resources/01-install-and-deploy.md` 改为索引页
11. `README.md` 正式改版
12. `quickstart/00-5min-quickstart.md` 改成“部署后 5 分钟快速体验”
13. `quickstart/01-7day-path.md` 调整 Day 1 入口

## 六、我的判断

这个重构不会破坏你原来的案例仓结构，反而会把用户路径顺成：

`先部署 -> 再接入 -> 再体验 -> 再找案例`

这会比现在更像“中文最佳实践库”，而不是“中文案例整理仓”。

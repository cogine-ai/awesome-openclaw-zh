# 部署指南候选资料（2026-03-08）

目标：为以下 3 篇教程筛选可靠、详细、适合二次改写的中文资料源。

- `macOS 本地部署`
- `Windows 部署`
- `Linux VPS 通用部署`

## 结论

当前最强的中文主来源是：

- [xianyu110/awesome-openclaw-tutorial - 第2章：环境搭建](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/01-basics/02-installation.md)

这份文档同时覆盖：

- Mac 本地部署
- Windows 本地部署
- Linux 本地部署
- 腾讯云 Lighthouse 云端部署
- 火山引擎部署
- 阿里云部署
- Docker 部署
- 升级、排错、API 配置

它的优点是图文细、步骤长、面向中文新手，明显比零散博客更适合作为改写底稿。

## 建议用法

- `macOS 本地部署`：以 xianyu 章节为中文主底稿，以 OpenClaw 官方平台页为命令与路径校验源。
- `Windows 部署`：以 xianyu 的 WSL2 + Ubuntu 路线为主，PowerShell 原生部署作为备选；发布前必须对照官方 Windows 页校验。
- `Linux VPS 通用部署`：不要直接照搬任何云厂商教程，建议改写成“通用 Linux 基线部署”，再从腾讯云 / 阿里云 / 火山引擎官方文档补控制台差异。

## 文件说明

- [macos-local.md](./macos-local.md)：Mac 本地部署候选资料卡
- [windows.md](./windows.md)：Windows 部署候选资料卡
- [linux-vps.md](./linux-vps.md)：Linux VPS 通用部署候选资料卡

## 说明

- 我没有把外部文章原文搬进仓库，只整理了候选链接、覆盖面、可信度和改写建议。
- 截至 `2026-03-08`，我没有找到第二个在“完整度 + 维护度 + 中文新手友好度”上能明显超过 xianyu 这份教程的中文主来源。

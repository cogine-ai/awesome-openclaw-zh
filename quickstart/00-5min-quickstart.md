# 5分钟快速上手（部署后）

这篇文档默认你已经把 OpenClaw 装好了。

如果你还没部署，请先看：

- [部署与安装中心](../deploy/README.md)
- [安装与部署入口（小白版）](../resources/01-install-and-deploy.md)

## 1) 先确认 Gateway 已经正常运行

本地或服务器里执行：

```bash
openclaw status
openclaw health
```

如果这里就报错，先不要继续跑场景，回到部署文档把安装链路补完整。

## 2) 打开控制台，先在浏览器里说上第一句话

优先用 Web UI 验证，而不是一上来就折腾渠道。

本地部署：

```text
http://127.0.0.1:18789/
```

如果你是 VPS 部署，先建立 SSH 隧道，再在本地浏览器打开同一个地址。

第一条测试消息建议直接发：

```text
你好，请确认你已经正常运行，并用 3 条简短内容告诉我你现在能做什么。
```

## 3) 再跑一个“马上见效”的场景

推荐从这 3 个开始：

- [每日晨间简报](../usecases/everyday/52-morning-briefing-telegram.md)
- [收件箱整理](../usecases/productivity/inbox-declutter.md)
- [会议纪要生成](../usecases/everyday/68-meeting-notes-generator.md)

## 4) 复制提示词，直接发给 OpenClaw

```text
你是我的 OpenClaw 助手。
请先帮我做一个「今日晨间简报」，包含：天气、日程、待办、3条重点新闻。
输出要简洁，3分钟内可以读完。
```

## 5) 如果这一步有效，再进入下一层

建议按这个顺序继续：

1. 绑定 1 个你常用的聊天入口
2. 跑第 2 个和第 3 个场景
3. 看 [7天上手路径](./01-7day-path.md)

完成以上步骤，你已经不是“刚装好 OpenClaw”，而是“已经开始真正使用它”。

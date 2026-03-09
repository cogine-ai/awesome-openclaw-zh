# Windows 部署（WSL2 主线）

这篇文档适合：

- 你在 Windows 10 / 11 上使用 OpenClaw
- 你希望优先走稳定、兼容性更好的官方路径
- 你能接受在 WSL2 里的 Ubuntu 环境中运行 OpenClaw

这篇文档的主线是：

- Windows 提供系统环境
- WSL2 + Ubuntu 运行 OpenClaw CLI 和 Gateway
- 浏览器依然在 Windows 侧使用

![Windows 部署架构：WSL2 + Ubuntu](../assets/deploy/windows-wsl2-architecture.png)

## 先说结论

Windows 上最推荐的方式不是原生 PowerShell，而是：

`Windows -> WSL2 -> Ubuntu -> OpenClaw Gateway`

原因很简单：

- 上游官方文档明确推荐 WSL2
- Linux 工具链兼容性更稳定
- Node、pnpm、脚本、Skills 的行为更接近官方主线
- 后续排错更容易对照 Linux 文档

## 这篇会完成什么

完成后你应该能做到：

- 在 Windows 上安装 WSL2 和 Ubuntu
- 在 WSL2 内安装 OpenClaw
- 启用 systemd
- 跑完初始化向导
- 在 Windows 浏览器打开 `http://127.0.0.1:18789/`

## 系统要求

- Windows 10 或 Windows 11
- 建议至少 8 GB 内存
- 建议 10 GB 以上可用磁盘
- 管理员权限

## 第 1 步：安装 WSL2

以管理员身份打开 PowerShell，执行：

```powershell
wsl --install
```

如果你想显式选择 Ubuntu 版本：

```powershell
wsl --list --online
wsl --install -d Ubuntu-24.04
```

安装完成后，如果系统要求，重启 Windows。

### 补充：如果这里卡在“虚拟化未开启”

Windows 安装 WSL2 时，一个非常常见的问题是：

- `wsl --install` 失败
- `wsl --set-default-version 2` 失败
- 系统提示需要启用 `Virtual Machine Platform`
- 或提示需要在 BIOS / UEFI 里开启虚拟化

这时候按这个顺序检查：

1. 打开“任务管理器” -> “性能” -> “CPU”
2. 看右下角的 `Virtualization` / “虚拟化”是否为 `Enabled`
3. 如果是 `Disabled`，重启电脑进入 BIOS / UEFI
4. 找到并开启 Intel VT-x / Intel Virtualization Technology，或 AMD-V / SVM Mode
5. 保存 BIOS 设置并重启 Windows
6. 重新执行本节里的 WSL 安装命令

另外，再确认这两个 Windows 组件已经启用：

```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

如果你之前已经执行过，也建议在开启 BIOS 虚拟化后再执行一遍，然后重启。

## 第 2 步：首次启动 Ubuntu

重启后打开 Ubuntu。

首次启动会要求你设置：

- Linux 用户名
- Linux 密码

这一步设置的不是 Windows 密码，而是 WSL 里的 Ubuntu 账号。

## 第 3 步：为 WSL2 启用 systemd

这是关键步骤。后面 `openclaw onboard --install-daemon` 需要 systemd。

在 Ubuntu 终端中执行：

```bash
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
EOF
```

然后回到 PowerShell 执行：

```powershell
wsl --shutdown
```

重新打开 Ubuntu，再检查：

```bash
systemctl --user status
```

如果命令能正常返回，说明 systemd 已可用。

## 第 4 步：在 WSL2 内安装 OpenClaw

重新进入 Ubuntu 后，执行：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

如果你只是想先安装，暂时不跑引导：

```bash
curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
```

安装完成后检查：

```bash
openclaw --version
openclaw doctor
```

## 第 5 步：运行初始化向导

在 Ubuntu 终端中执行：

```bash
openclaw onboard --install-daemon
```

推荐选择：

- Gateway 位置：`local`
- 安装后台服务：`yes`
- 运行时：优先 `Node`
- 渠道：先不绑也可以

## 第 6 步：在 Windows 浏览器验证

向导完成后，在 Ubuntu 终端先确认状态：

```bash
openclaw gateway status
openclaw status
openclaw health
```

然后在 Windows 浏览器打开：

```text
http://127.0.0.1:18789/
```

如果控制 UI 需要令牌，就按终端提示填写。

多数情况下，Windows 本机访问 WSL2 内的 `127.0.0.1:18789` 是通的，不需要额外折腾。

## 第 7 步：发送第一条测试消息

在浏览器里发送：

```text
你好，请确认你已经在 Windows + WSL2 环境中正常运行。
```

如果能得到正常回复，说明主线已经打通。

## 高级：如果你要让局域网其他机器访问

默认不建议把 Gateway 直接暴露到公网。

如果只是让局域网其他机器访问 Windows 里的 WSL 服务，可以按官方思路使用 `portproxy`。

PowerShell（管理员）示例：

```powershell
$Distro = "Ubuntu-24.04"
$ListenPort = 2222
$TargetPort = 22

$WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]
if (-not $WslIp) { throw "WSL IP not found." }

netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `
  connectaddress=$WslIp connectport=$TargetPort
```

再开放 Windows 防火墙端口：

```powershell
New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `
  -Protocol TCP -LocalPort $ListenPort -Action Allow
```

这属于进阶用法。对绝大多数用户来说，本地浏览器访问已经够了。

## 备选：PowerShell 原生部署

如果你明确不想使用 WSL2，可以走官方 PowerShell 安装器：

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

但不建议把它当仓库里的主推荐路径，原因是：

- 上游文档更推荐 WSL2
- 原生 Windows 的兼容性和排错成本更高
- 后续大量 Linux 风格工具更难处理

更合适的写法是：把它放在文末“备选路线”。

## 常见问题

### 1. `systemctl --user status` 不正常

大概率是你没有启用 WSL systemd，或者改完 `/etc/wsl.conf` 后忘了执行：

```powershell
wsl --shutdown
```

### 2. Windows 浏览器打不开 `127.0.0.1:18789`

先在 Ubuntu 里检查：

```bash
openclaw gateway status
openclaw health
```

如果 Gateway 没跑起来，重新执行：

```bash
openclaw onboard --install-daemon
```

### 3. 我能不能直接按 Linux 文档走？

可以，但前提是你已经在 WSL2 里面。

WSL2 里的 Ubuntu，本质上就是你这台 Windows 机器上的 Linux 环境。

## 上游参考

- OpenClaw 官方中文： [Windows (WSL2)](https://docs.openclaw.ai/platforms/windows)
- OpenClaw 官方中文： [入门指南](https://docs.openclaw.ai/start/getting-started)
- OpenClaw 官方中文： [安装](https://docs.openclaw.ai/install)
- OpenClaw 官方中文： [安装器内部机制](https://docs.openclaw.ai/install/installer)
- Microsoft 官方： [Install WSL](https://learn.microsoft.com/windows/wsl/install)
- Microsoft 官方： [WSL Troubleshooting](https://learn.microsoft.com/windows/wsl/troubleshooting)
- Microsoft 官方： [Enable virtualization on Windows](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)
- 中文开源教程： [xianyu110/awesome-openclaw-tutorial - 环境搭建](https://github.com/xianyu110/awesome-openclaw-tutorial/blob/main/docs/01-basics/02-installation.md)

截图说明：

- 本文顶部架构图整理自上游开源教程仓库 `xianyu110/awesome-openclaw-tutorial`

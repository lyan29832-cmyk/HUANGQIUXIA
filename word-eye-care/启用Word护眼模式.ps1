#Requires -Version 5.1
<#
.SYNOPSIS
  一键为 Microsoft Word 启用护眼模式（米黄纸张底色 + 默认模板 + 已打开文档）
  并尽量开启 Windows 夜间模式（降蓝光）
#>
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# 护眼米黄 RGB(250, 245, 220) —— Word COM 使用 R + G*256 + B*65536
$EyeCareRgb = 250 + (245 * 256) + (220 * 65536)
$BackupDir = Join-Path $env:USERPROFILE "Documents\Word护眼备份_$(Get-Date -Format 'yyyyMMdd_HHmmss')"

function Write-Step([string]$msg) {
    Write-Host "`n==> $msg" -ForegroundColor Cyan
}

function Write-Ok([string]$msg) {
    Write-Host "    [完成] $msg" -ForegroundColor Green
}

function Write-Warn([string]$msg) {
    Write-Host "    [提示] $msg" -ForegroundColor Yellow
}

function Write-Fail([string]$msg) {
    Write-Host "    [失败] $msg" -ForegroundColor Red
}

function Set-DocumentEyeCare($doc) {
    # 显示背景色（打印布局下可见）
    try { $doc.Application.Options.DisplayBackgrounds = $true } catch {}

    $fill = $doc.Background.Fill
    $fill.Visible = $true
    $fill.Solid()
    $fill.ForeColor.RGB = $EyeCareRgb
}

function Backup-NormalTemplates {
    Write-Step "备份 Word 默认模板 Normal.dotm / Normal.dotx"
    $templates = Join-Path $env:APPDATA "Microsoft\Templates"
    if (-not (Test-Path $templates)) {
        Write-Warn "未找到模板目录：$templates"
        return
    }

    New-Item -ItemType Directory -Path $BackupDir -Force | Out-Null
    $copied = $false
    foreach ($name in @('Normal.dotm', 'Normal.dotx', 'Normal.dot')) {
        $src = Join-Path $templates $name
        if (Test-Path $src) {
            Copy-Item -LiteralPath $src -Destination (Join-Path $BackupDir $name) -Force
            Write-Ok "已备份 $name -> $BackupDir"
            $copied = $true
        }
    }
    if (-not $copied) {
        Write-Warn "未找到现有 Normal 模板（将在首次保存时由 Word 生成）"
    }
}

function Set-WordEyeCare {
    Write-Step "通过 Word 自动化设置护眼底色"

    $word = $null
    $createdHere = $false
    $normalDoc = $null

    try {
        try {
            $word = [Runtime.InteropServices.Marshal]::GetActiveObject('Word.Application')
            Write-Ok "检测到已在运行的 Word，将一并处理已打开文档"
        } catch {
            $word = New-Object -ComObject Word.Application
            $createdHere = $true
            $word.Visible = $false
            Write-Ok "已启动 Word（后台）"
        }

        $word.Options.DisplayBackgrounds = $true

        # 1) 已打开的文档全部改成护眼色
        $openCount = 0
        foreach ($doc in @($word.Documents)) {
            try {
                Set-DocumentEyeCare $doc
                $openCount++
            } catch {
                Write-Warn "无法处理文档：$($doc.Name) — $($_.Exception.Message)"
            }
        }
        if ($openCount -gt 0) {
            Write-Ok "已为 $openCount 个已打开文档设置护眼底色"
        } else {
            Write-Warn "当前没有已打开的文档（仅更新默认模板）"
        }

        # 2) 修改默认模板，让以后新建文档也是护眼色
        try {
            $normalDoc = $word.NormalTemplate.OpenAsDocument()
            Set-DocumentEyeCare $normalDoc
            $normalDoc.Save()
            $normalDoc.Close($false)
            $normalDoc = $null
            Write-Ok "已更新默认模板 Normal（新建 Word 默认护眼底色）"
        } catch {
            Write-Fail "更新默认模板失败：$($_.Exception.Message)"
            Write-Warn "可手动：设计 → 页面颜色 → 选米黄后另存为 Normal.dotx 模板"
        }
    }
    finally {
        if ($null -ne $normalDoc) {
            try { $normalDoc.Close($false) } catch {}
        }
        if ($createdHere -and $null -ne $word) {
            try { $word.Quit() } catch {}
        }
        if ($null -ne $word) {
            try { [Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null } catch {}
        }
        [GC]::Collect()
        [GC]::WaitForPendingFinalizers()
    }
}

function Set-OfficeDarkGrayTheme {
    Write-Step "将 Office 主题设为「深灰色」（降低界面刺眼）"
    $common = 'HKCU:\Software\Microsoft\Office\16.0\Common'
    if (-not (Test-Path $common)) {
        # 尝试 15.0 (Office 2013)
        $common = 'HKCU:\Software\Microsoft\Office\15.0\Common'
    }
    if (-not (Test-Path $common)) {
        Write-Warn "未找到 Office 注册表项，跳过主题设置"
        return
    }
    # 1 = 深灰色（多数 Office 2016/365）
    New-ItemProperty -Path $common -Name 'UI Theme' -PropertyType DWord -Value 1 -Force | Out-Null
    Write-Ok "已写入 Office UI Theme = 深灰色（重启 Word 后生效）"
}

function Enable-WindowsNightLight {
    Write-Step "尝试开启 Windows 夜间模式（系统降蓝光）"
    try {
        # 打开夜间模式设置页，并提示用户一键打开（注册表二进制因版本差异不稳定）
        Start-Process 'ms-settings:nightlight'
        Write-Ok "已打开「夜间模式」设置页"
        Write-Warn "请在弹出的窗口中打开「夜间模式」，并把强度调高一些"
    } catch {
        Write-Warn "无法自动打开夜间模式设置：$($_.Exception.Message)"
        Write-Warn "请手动：设置 → 系统 → 显示 → 夜间模式"
    }
}

# ========== 主流程 ==========
Write-Host ""
Write-Host "========================================" -ForegroundColor Magenta
Write-Host "   Word 护眼模式一键配置" -ForegroundColor Magenta
Write-Host "   底色：米黄 RGB(250,245,220)" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Magenta

try {
    Backup-NormalTemplates
    Set-WordEyeCare
    Set-OfficeDarkGrayTheme
    Enable-WindowsNightLight

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  配置完成！" -ForegroundColor Green
    Write-Host "  · 已打开的 Word：已改护眼底色" -ForegroundColor Green
    Write-Host "  · 新建 Word：默认护眼底色" -ForegroundColor Green
    Write-Host "  · Office 界面：深灰色（重启 Word 生效）" -ForegroundColor Green
    Write-Host "  · 请在弹出的设置里打开「夜间模式」" -ForegroundColor Green
    if (Test-Path $BackupDir) {
        Write-Host "  · 模板备份：$BackupDir" -ForegroundColor Green
    }
    Write-Host "========================================" -ForegroundColor Green
} catch {
    Write-Host ""
    Write-Fail $_.Exception.Message
    Write-Host "若提示找不到 Word，请确认已安装 Microsoft Word（不是仅 WPS）。" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "按任意键退出..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')

@echo off
chcp 65001 >nul
title Word 护眼模式一键配置
cd /d "%~dp0"

echo.
echo  正在以当前用户权限运行护眼配置...
echo  （不需要管理员，但电脑上需已安装 Microsoft Word）
echo.

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0启用Word护眼模式.ps1"
if errorlevel 1 (
  echo.
  echo  运行失败。可尝试：右键此文件 → 用 PowerShell 运行
  pause
)

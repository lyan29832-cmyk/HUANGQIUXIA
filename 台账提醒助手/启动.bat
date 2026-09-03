@echo off
chcp 65001 >nul
cd /d "%~dp0"
title 台账提醒助手

where python >nul 2>&1
if %errorlevel%==0 (
    set "PY=python"
    goto :install
)
where py >nul 2>&1
if %errorlevel%==0 (
    set "PY=py -3"
    goto :install
)

echo.
echo 还没有安装 Python，正在打开下载页面。
echo 安装时请务必勾选：Add python.exe to PATH
echo 装完以后，再双击本文件一次。
echo.
start https://www.python.org/downloads/windows/
pause
exit /b 1

:install
echo 正在准备运行环境，请稍等…
%PY% -m pip install -r requirements.txt -q
if %errorlevel% neq 0 (
    echo 安装依赖失败，请检查网络后重试。
    pause
    exit /b 1
)
%PY% app.py
if %errorlevel% neq 0 pause

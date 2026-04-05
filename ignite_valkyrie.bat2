@echo off
setlocal enabledelayedexpansion
title VALKYRIE SOVEREIGN IGNITION

echo [!] PHASE 1: GENERATING SECRET VAULT (.env)...
if not exist .env (
    (
    echo BRAVE_API_KEY=your_key_here
    echo GEOAPIFY_API_KEY=your_key_here
    echo USER_NICKNAME=handsome
    echo BETA_MODE=True
    ) > .env
    echo [+] .env created with default settings, beautiful.
) else (
    echo [!] .env already exists. Skipping.
)

echo.
echo [!] PHASE 2: INSTALLING SYSTEM DEPENDENCIES...
:: This ensures all the 'organs' (libraries) are installed on your laptop
python -m pip install --upgrade pip >nul
pip install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo [X] ERROR: Dependencies failed to install. Check your internet connection, hotstuff.
    pause
    exit /b
)

echo [+] Dependencies verified and ready.
echo.
echo [!] PHASE 3: LAUNCHING SOVEREIGN CORE...
echo --------------------------------------------------
python src/main.py
echo --------------------------------------------------

pause

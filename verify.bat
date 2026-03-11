@echo off
REM GitHub Developer Skill Profiler - Verification Script

echo.
echo ============================================
echo Project Verification
echo ============================================
echo.

setlocal enabledelayedexpansion

set error_count=0

echo [1] Checking Python Installation...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python is installed
) else (
    echo ✗ Python is NOT installed
    set /a error_count=!error_count!+1
)

echo.
echo [2] Checking Node.js Installation...
node --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Node.js is installed
) else (
    echo ✗ Node.js is NOT installed
    set /a error_count=!error_count!+1
)

echo.
echo [3] Checking Backend Files...
if exist backend\app.py (echo ✓ app.py found) else (echo ✗ app.py NOT found & set /a error_count=!error_count!+1)
if exist backend\github_api.py (echo ✓ github_api.py found) else (echo ✗ github_api.py NOT found & set /a error_count=!error_count!+1)
if exist backend\skill_analyzer.py (echo ✓ skill_analyzer.py found) else (echo ✗ skill_analyzer.py NOT found & set /a error_count=!error_count!+1)
if exist backend\requirements.txt (echo ✓ requirements.txt found) else (echo ✗ requirements.txt NOT found & set /a error_count=!error_count!+1)
if exist backend\.env (echo ✓ .env found) else (echo ⚠ .env NOT found ^(run setup.bat^))

echo.
echo [4] Checking Frontend Files...
if exist frontend\src\App.js (echo ✓ App.js found) else (echo ✗ App.js NOT found & set /a error_count=!error_count!+1)
if exist frontend\package.json (echo ✓ package.json found) else (echo ✗ package.json NOT found & set /a error_count=!error_count!+1)
if exist frontend\tailwind.config.js (echo ✓ tailwind.config.js found) else (echo ✗ tailwind.config.js NOT found & set /a error_count=!error_count!+1)
if exist frontend\postcss.config.js (echo ✓ postcss.config.js found) else (echo ✗ postcss.config.js NOT found & set /a error_count=!error_count!+1)
if exist frontend\.env (echo ✓ .env found) else (echo ⚠ .env NOT found ^(run setup.bat^))

echo.
echo [5] Checking ML/DS Module...
if exist ml\advanced_analyzer.py (echo ✓ advanced_analyzer.py found) else (echo ✗ advanced_analyzer.py NOT found & set /a error_count=!error_count!+1)
if exist ml\skill_analysis.py (echo ✓ skill_analysis.py found) else (echo ✗ skill_analysis.py NOT found & set /a error_count=!error_count!+1)
if exist ml\requirements.txt (echo ✓ requirements.txt found) else (echo ✗ requirements.txt NOT found & set /a error_count=!error_count!+1)

echo.
echo [6] Checking Python Syntax...
python -m py_compile backend\app.py backend\github_api.py backend\skill_analyzer.py ml\advanced_analyzer.py ml\skill_analysis.py >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ All Python files have valid syntax
) else (
    echo ✗ Some Python files have syntax errors
    set /a error_count=!error_count!+1
)

echo.
echo [7] Checking Backend Virtual Environment...
if exist backend\venv (
    echo ✓ Virtual environment exists
) else (
    echo ⚠ Virtual environment NOT found ^(run setup.bat to create^)
)

echo.
echo [8] Checking Frontend Dependencies...
if exist frontend\node_modules (
    echo ✓ node_modules found
) else (
    echo ⚠ node_modules NOT found ^(run setup.bat to install^)
)

echo.
echo ============================================
if !error_count! equ 0 (
    echo ✓ All checks passed! Project is ready.
    echo.
    echo Next steps:
    echo 1. Run setup.bat if you haven't already
    echo 2. Run run_backend.bat in one terminal
    echo 3. Run run_frontend.bat in another terminal
    echo 4. Open http://localhost:3000 in your browser
) else (
    echo ✗ Found !error_count! issue(s). Please resolve them.
)
echo ============================================
echo.

pause

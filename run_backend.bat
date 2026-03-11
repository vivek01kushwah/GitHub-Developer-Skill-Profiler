@echo off
REM GitHub Developer Skill Profiler - Start Backend

echo.
echo ============================================
echo Starting GitHub Developer Skill Profiler
echo Backend Server
echo ============================================
echo.

cd backend

if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run setup.bat first
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

if not exist .env (
    echo ERROR: .env file not found!
    echo Please run setup.bat first
    exit /b 1
)

echo.
echo Starting Flask server on http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

@echo off
REM GitHub Developer Skill Profiler - Start Frontend

echo.
echo ============================================
echo Starting GitHub Developer Skill Profiler
echo Frontend Server
echo ============================================
echo.

cd frontend

if not exist node_modules (
    echo ERROR: node_modules not found!
    echo Please run setup.bat first
    exit /b 1
)

if not exist .env (
    echo ERROR: .env file not found!
    echo Please run setup.bat first
    exit /b 1
)

echo.
echo Starting React development server on http://localhost:3000
echo Press Ctrl+C to stop the server
echo.

npm start

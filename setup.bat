@echo off
REM GitHub Developer Skill Profiler - Setup Script

echo.
echo ============================================
echo GitHub Developer Skill Profiler - Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ and add it to your PATH
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js 16+ and add it to your PATH
    exit /b 1
)

echo.
echo [1/5] Setting up backend...
cd backend

if exist venv (
    echo Virtual environment already exists, skipping creation...
) else (
    echo Creating Python virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing backend dependencies...
pip install -r requirements.txt

if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo NOTE: Update .env with your GitHub token if needed
)

cd ..

echo.
echo [2/5] Setting up frontend...
cd frontend

if exist node_modules (
    echo node_modules already exists, skipping npm install...
) else (
    echo Installing frontend dependencies...
    call npm install
)

if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
)

cd ..

echo.
echo [3/5] Setting up ML/DS module...
if exist venv (
    call venv\Scripts\activate.bat
    pip install -r ml/requirements.txt
) else (
    echo ERROR: Virtual environment not created. Running backend setup first...
)

echo.
echo [4/5] Verifying project structure...
if exist backend\app.py (echo ✓ Backend app.py found) else (echo ✗ Backend app.py NOT found)
if exist backend\github_api.py (echo ✓ Backend github_api.py found) else (echo ✗ Backend github_api.py NOT found)
if exist backend\skill_analyzer.py (echo ✓ Backend skill_analyzer.py found) else (echo ✗ Backend skill_analyzer.py NOT found)
if exist frontend\src\App.js (echo ✓ Frontend App.js found) else (echo ✗ Frontend App.js NOT found)
if exist frontend\package.json (echo ✓ Frontend package.json found) else (echo ✗ Frontend package.json NOT found)

echo.
echo [5/5] Setup complete!
echo.
echo ============================================
echo Next Steps:
echo ============================================
echo.
echo 1. Start the backend:
echo    - Open a terminal
echo    - cd backend
echo    - venv\Scripts\activate
echo    - python app.py
echo.
echo 2. Start the frontend (in a new terminal):
echo    - cd frontend
echo    - npm start
echo.
echo 3. Open your browser to http://localhost:3000
echo.
echo For more info, see SETUP.md
echo.
pause

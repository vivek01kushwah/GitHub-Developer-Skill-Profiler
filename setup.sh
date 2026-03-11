#!/bin/bash
# GitHub Developer Skill Profiler - Setup Script for macOS/Linux

echo ""
echo "============================================"
echo "GitHub Developer Skill Profiler - Setup"
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.9+ and add it to your PATH"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed or not in PATH"
    echo "Please install Node.js 16+ and add it to your PATH"
    exit 1
fi

echo ""
echo "[1/5] Setting up backend..."
cd backend

if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping creation..."
else
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing backend dependencies..."
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "NOTE: Update .env with your GitHub token if needed"
fi

cd ..

echo ""
echo "[2/5] Setting up frontend..."
cd frontend

if [ -d "node_modules" ]; then
    echo "node_modules already exists, skipping npm install..."
else
    echo "Installing frontend dependencies..."
    npm install
fi

if [ ! -f ".env" ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
fi

cd ..

echo ""
echo "[3/5] Setting up ML/DS module..."
if [ -d "venv" ]; then
    source venv/bin/activate
    pip install -r ml/requirements.txt
else
    echo "ERROR: Virtual environment not created. Running backend setup first..."
fi

echo ""
echo "[4/5] Verifying project structure..."
[ -f "backend/app.py" ] && echo "✓ Backend app.py found" || echo "✗ Backend app.py NOT found"
[ -f "backend/github_api.py" ] && echo "✓ Backend github_api.py found" || echo "✗ Backend github_api.py NOT found"
[ -f "backend/skill_analyzer.py" ] && echo "✓ Backend skill_analyzer.py found" || echo "✗ Backend skill_analyzer.py NOT found"
[ -f "frontend/src/App.js" ] && echo "✓ Frontend App.js found" || echo "✗ Frontend App.js NOT found"
[ -f "frontend/package.json" ] && echo "✓ Frontend package.json found" || echo "✗ Frontend package.json NOT found"

echo ""
echo "[5/5] Setup complete!"
echo ""
echo "============================================"
echo "Next Steps:"
echo "============================================"
echo ""
echo "1. Start the backend:"
echo "   - Open a terminal"
echo "   - cd backend"
echo "   - source venv/bin/activate"
echo "   - python app.py"
echo ""
echo "2. Start the frontend (in a new terminal):"
echo "   - cd frontend"
echo "   - npm start"
echo ""
echo "3. Open your browser to http://localhost:3000"
echo ""
echo "For more info, see SETUP.md"
echo ""

# Quick Reference Card

## 🎯 Project: GitHub Developer Skill Profiler

### What It Does
Analyzes a GitHub user's repositories and generates a skill radar chart showing their programming abilities.

### Quick Commands

#### Backend
```bash
cd backend
python -m venv venv          # Create environment
venv\Scripts\activate        # Activate (Windows)
source venv/bin/activate     # Activate (Mac/Linux)
pip install -r requirements.txt
python app.py                # Runs on http://localhost:5000
```

#### Frontend  
```bash
cd frontend
npm install                  # Install dependencies
npm start                    # Runs on http://localhost:3000
```

### URLs
| Purpose | URL |
|---------|-----|
| Frontend App | http://localhost:3000 |
| Backend API | http://localhost:5000 |
| API Health | http://localhost:5000/api/health |

### API Endpoints
```
GET /api/profile/<username>      # Full analysis (user + skills)
GET /api/repos/<username>         # Repository list
GET /api/skills/<username>        # Skills only
GET /api/rate-limit               # GitHub API status
GET /api/health                   # Server health check
```

### Technologies

**Backend:** Python, Flask, Requests  
**Frontend:** React, Recharts, Tailwind CSS  
**Data Science:** Pandas, NumPy, Scikit-learn  
**External:** GitHub API v3  

### Project Structure
```
github-skill-profiler/
  ├── backend/          # Flask API
  ├── frontend/         # React app
  ├── ml/              # ML/DS modules
  ├── README.md        # Overview
  ├── SETUP.md         # Installation guide
  ├── ARCHITECTURE.md  # System design
  ├── EXAMPLES.md      # Usage examples
  └── PROJECT_SUMMARY.md # This project
```

### Key Files

**Backend:**
- `app.py` - Flask application & routes
- `github_api.py` - GitHub API client
- `skill_analyzer.py` - Skill analysis engine

**Frontend:**
- `App.js` - Main component
- `components/SkillRadar.js` - Visualization
- `components/ProfileCard.js` - User info display

**ML/DS:**
- `advanced_analyzer.py` - Advanced analysis
- `skill_analysis.py` - Language analysis

### Setup Checklist
- [ ] Clone/download project
- [ ] Create `backend/.env` (optional: add GitHub token)
- [ ] Install backend dependencies (`pip install -r requirements.txt`)
- [ ] Install frontend dependencies (`npm install`)
- [ ] Start backend (`python app.py`)
- [ ] Start frontend (`npm start`)
- [ ] Open http://localhost:3000
- [ ] Enter a GitHub username
- [ ] View skill analysis!

### Skill Score Calculation
1. **Count languages** across all repositories
2. **Extract topics** (machine-learning, web-dev, etc.)
3. **Weight by popularity** (stars, forks)
4. **Normalize to 0-100%**
5. **Filter** (minimum 5% score)
6. **Sort** by skill score (highest first)

### Example Usage
```
Enter: "torvalds"
Result: Linux creator's profile
Top Skills: C (99%), Git (97%), Kernel (96%)
```

### Rate Limiting
- GitHub free API: 5,000 requests/hour
- Each profile analysis: ~3-5 API calls
- Add token to `.env` for higher limits

### Troubleshooting

**Can't connect to backend?**
- Check if `python app.py` is running
- Verify `http://localhost:5000/api/health`

**Getting "User not found"?**
- Username doesn't exist on GitHub
- Try: "torvalds", "gvanrossum", "dhh"

**Rate limit exceeded?**
- Add GitHub Personal Access Token to `.env`
- Or wait 1 hour for reset

**CORS errors?**
- Both servers must be running
- Frontend on 3000, Backend on 5000
- Check `.env` files are configured

### Files to Customize

**Add new skills:**
- Edit `backend/skill_analyzer.py`
- Add to `LANGUAGE_SKILLS` or `TECH_SKILLS` dicts

**Change colors:**
- Edit `frontend/src/components/SkillRadar.js`
- Modify Tailwind CSS classes in components

**Adjust weights:**
- Edit `backend/skill_analyzer.py`
- Modify `WEIGHTS` dict

### Performance
- Single profile analysis: 2-5 seconds
- API calls used: 3-5 per analysis
- Frontend chart render: <1 second
- No data stored/persisted

### Deployment Ready?

Backend (Flask):
```bash
pip install gunicorn
gunicorn app:app
```

Frontend (React):
```bash
npm run build
# Deploy 'build/' folder to static host
```

### Monitoring
Check `/api/rate-limit` endpoint:
```bash
curl http://localhost:5000/api/rate-limit
```

Returns:
```json
{
  "limit": 5000,
  "remaining": 4923,
  "reset": 1234567890
}
```

### Resources
- GitHub API Docs: https://docs.github.com/en/rest
- React Docs: https://react.dev
- Flask Docs: https://flask.palletsprojects.com
- Recharts: https://recharts.org

### Key Features Implemented ✅
- ✅ GitHub username search
- ✅ Real-time repository fetching
- ✅ Skill extraction algorithm
- ✅ Interactive radar chart
- ✅ Responsive UI design
- ✅ API rate limit tracking
- ✅ Error handling
- ✅ Loading indicators
- ✅ ML/DS analysis modules
- ✅ Comprehensive documentation

### Support
1. Check [SETUP.md](SETUP.md) for setup issues
2. Check [EXAMPLES.md](EXAMPLES.md) for usage examples
3. Check [ARCHITECTURE.md](ARCHITECTURE.md) for technical details

---
**Status:** ✅ Complete & Ready  
**Version:** 1.0.0  
**Last Updated:** 2024

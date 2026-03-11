# GitHub Developer Skill Profiler

A web application that analyzes your GitHub profile and generates a skill radar chart based on your repositories, contributing languages, commit patterns, and project topics.

## Features

- 📊 **Skill Radar Chart**: Visualize your top skills based on GitHub data
- 🔍 **Repository Analysis**: Deep dive into languages, commit patterns, and topics
- 🤖 **ML-Powered Insights**: Topic clustering and skill extraction
- ⚡ **Fast API**: Powered by Flask backend
- 📱 **Responsive UI**: Modern React frontend
- 🔌 **GitHub API Integration**: Seamless GitHub username lookup

## Tech Stack

**Frontend:**
- React.js
- Chart.js / Recharts (for radar charts)
- Axios
- Tailwind CSS

**Backend:**
- Flask
- Flask-CORS
- Requests (GitHub API)
- Python-dotenv

**Data Science:**
- Pandas
- NumPy
- Scikit-learn
- NLTK

## Project Structure

```
.
├── backend/              # Flask API server
├── frontend/             # React application
├── ml/                   # Data science & ML modules
└── README.md
```

## Setup Instructions

### Backend Setup
1. Navigate to `backend/` directory
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with GitHub token (optional, for higher API limits)
6. Run: `python app.py`

### Frontend Setup
1. Navigate to `frontend/` directory
2. Install dependencies: `npm install`
3. Configure API endpoint in `.env`
4. Run: `npm start`

## API Endpoints

- `GET /api/profile/<username>` - Get complete skill profile
- `GET /api/repos/<username>` - List repositories
- `GET /api/skills/<username>` - Get analyzed skills

## How It Works

1. User enters GitHub username
2. Backend fetches user data via GitHub API
3. ML module analyzes:
   - Programming languages used
   - Repository topics
   - Commit frequency patterns
   - Repository stars/forks
4. Generates skill scores (0-100)
5. Frontend displays interactive radar chart

## API Rate Limiting

GitHub API free tier: 5000 requests/hour per IP/token
Rate limiting headers included in responses

## Future Enhancements

- Collaboration network analysis
- Contribution timeline visualization
- Skill trend predictions
- Peer comparison
- Export reports as PDF

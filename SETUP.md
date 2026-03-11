# GitHub Developer Skill Profiler - Getting Started

## Quick Setup

### 1. Backend Setup (Flask API)
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy example environment file
copy .env.example .env
# Edit .env and add your GitHub token (optional but recommended)

# Run the server
python app.py
```

The API will be available at `http://localhost:5000`

### 2. Frontend Setup (React)
```bash
cd frontend

# Install dependencies
npm install

# Copy example environment file
copy .env.example .env

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000`

## Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Enter a GitHub username
3. Click "Analyze" to fetch and analyze the profile
4. View your skill radar chart and detailed statistics

## API Endpoints

### Get Complete Profile
```
GET /api/profile/<username>
```
Returns user info, analyzed skills, and rate limit status

**Example Response:**
```json
{
  "user": {
    "login": "torvalds",
    "name": "Linus Torvalds",
    "avatar_url": "https://...",
    "public_repos": 5,
    "followers": 200000,
    "following": 0
  },
  "skills": {
    "C": 95.5,
    "Git": 98.0,
    "Linux": 99.0
  },
  "repositories_analyzed": 5
}
```

### Get Repositories
```
GET /api/repos/<username>
```
Returns list of user's repositories

### Get Skills Analysis
```
GET /api/skills/<username>
```
Returns just the analyzed skills

### Check API Rate Limit
```
GET /api/rate-limit
```
Returns current GitHub API rate limit status

## Technologies Used

### Backend
- **Python 3.9+**
- **Flask** - Web framework
- **Requests** - HTTP library for GitHub API
- **Pandas/NumPy** - Data analysis
- **Scikit-learn** - ML algorithms

### Frontend
- **React 18** - UI library
- **Recharts** - Radar chart visualization
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### Data Science
- Language distribution analysis
- Topic clustering
- Activity pattern analysis
- Skill prediction models

## GitHub API Rate Limiting

- **Free tier**: 5000 requests/hour per IP
- **With token**: Higher limits
- Each profile analysis uses ~3-5 API calls

## Environment Variables

### Backend (.env)
```
GITHUB_TOKEN=your_token_here          # Optional GitHub Personal Access Token
FLASK_ENV=development                 # development or production
DEBUG=True                             # Enable Flask debug mode
PORT=5000                              # Server port
CORS_ORIGINS=http://localhost:3000    # Allowed frontend URLs
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:5000
```

## Features

✅ GitHub profile data fetching
✅ Programming language analysis
✅ Repository topic clustering  
✅ Contribution metrics
✅ Interactive radar chart visualization
✅ Skill scoring algorithm
✅ Rate limit tracking
✅ Responsive UI design

## Troubleshooting

### CORS Errors
Ensure both backend and frontend are running and CORS is properly configured in Flask

### GitHub API Rate Limit Exceeded
- Add a GitHub Personal Access Token to your `.env` file
- Wait for rate limit to reset (displayed with remaining calls)

### Frontend can't connect to Backend
- Ensure backend is running (`python app.py`)
- Check that `REACT_APP_API_URL` matches your backend URL
- Verify CORS settings in `app.py`

## Future Enhancements

- [ ] Collaboration network analysis
- [ ] More advanced ML models (clustering, classification)
- [ ] Contribution timeline visualization  
- [ ] Peer comparison features
- [ ] PDF report export
- [ ] GitHub authentication integration
- [ ] Skill trend predictions
- [ ] Repository recommendation engine

## Contributing

Feel free to fork and submit pull requests!

## License

MIT License

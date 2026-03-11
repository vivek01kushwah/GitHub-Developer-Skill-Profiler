# Project Architecture

## Overview

The GitHub Developer Skill Profiler is a full-stack web application that analyzes a GitHub user's repositories to determine their programming skills and expertise areas.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (React)                         │
│  - SearchForm component                                      │
│  - ProfileCard component                                     │
│  - SkillRadar component (Recharts)                           │
│  - LoadingSpinner & ErrorMessage components                 │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP Requests
                     │ JSON Responses
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              Backend (Flask API Server)                      │
├─────────────────────────────────────────────────────────────┤
│ app.py - Main Flask application & route handlers            │
│ github_api.py - GitHub API client (fetch user/repo data)    │
│ skill_analyzer.py - Basic skill extraction & scoring        │
└────────────────────┬────────────────────────────────────────┘
                     │ GitHub API Calls
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              GitHub API (External Service)                   │
│  - Get user profile                                          │
│  - Get user repositories                                     │
│  - Get repository languages                                  │
│  - Get rate limit status                                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│          ML/DS Module (Advanced Analysis)                    │
├─────────────────────────────────────────────────────────────┤
│ advanced_analyzer.py                                         │
│  ├─ RepositoryAnalyzer - Detailed repo metrics             │
│  ├─ LanguageAnalyzer - Language distribution                │
│  ├─ TopicClusterer - Topic-based clustering                │
│  ├─ CommitPatternAnalyzer - Activity metrics                │
│  ├─ SkillPredictor - ML-based skill prediction             │
│  └─ ComprehensiveAnalyzer - Unified analysis               │
└─────────────────────────────────────────────────────────────┘
```

## Directory Structure

```
github-skill-profiler/
├── README.md                    # Project documentation
├── SETUP.md                     # Setup instructions
├── ARCHITECTURE.md              # This file
│
├── backend/                     # Flask API Backend
│   ├── app.py                   # Main Flask application
│   ├── github_api.py            # GitHub API client
│   ├── skill_analyzer.py        # Basic skill analysis
│   ├── requirements.txt         # Python dependencies
│   └── .env.example             # Environment variables template
│
├── frontend/                    # React Frontend
│   ├── package.json             # Node.js dependencies
│   ├── public/
│   │   └── index.html           # HTML entry point
│   ├── src/
│   │   ├── App.js               # Main React component
│   │   ├── index.js             # React root
│   │   ├── index.css            # Global styles
│   │   └── components/
│   │       ├── SearchForm.js     # Username search input
│   │       ├── ProfileCard.js    # User profile display
│   │       ├── SkillRadar.js     # Radar chart visualization
│   │       ├── LoadingSpinner.js # Loading indicator
│   │       └── ErrorMessage.js   # Error display
│   ├── .env.example             # Environment variables
│   └── tsconfig.json            # TypeScript configuration
│
└── ml/                          # Machine Learning Module
    ├── __init__.py              # Package initialization
    ├── advanced_analyzer.py     # Advanced analysis classes
    └── requirements.txt         # ML dependencies
```

## Data Flow

### 1. User Input
User enters GitHub username in SearchForm

### 2. Frontend Request
React App sends `GET /api/profile/<username>` to Flask backend

### 3. Backend Processing
1. Flask app receives request
2. GitHubClient fetches user data via GitHub API
3. GitHubClient fetches user's repositories
4. SkillAnalyzer processes repositories:
   - Analyzes programming languages
   - Extracts topics/tags
   - Calculates skill scores
5. Returns JSON response with user data + skills

### 4. Advanced Analysis (Optional)
ComprehensiveAnalyzer can be integrated for:
- Detailed language distributions
- Topic clustering
- Activity pattern analysis
- ML-based skill predictions

### 5. Frontend Display
React components render:
- UserProfile card (avatar, stats)
- Skill radar chart (top 6 skills)
- Detailed skill breakdown (all skills with percentages)

## Key Components

### Backend Components

#### app.py (Flask Application)
- **Health Check**: `/api/health` - Server status
- **Profile Endpoint**: `/api/profile/<username>` - Complete analysis
- **Repos Endpoint**: `/api/repos/<username>` - Repository list
- **Skills Endpoint**: `/api/skills/<username>` - Skill scores only
- **Rate Limit**: `/api/rate-limit` - GitHub API rate limit status

#### github_api.py (GitHub Client)
- Handles all GitHub API v3 communications
- Methods:
  - `get_user()` - Fetch user profile
  - `get_user_repos()` - Fetch all public repos (with pagination)
  - `get_repo_details()` - Detailed repo info
  - `get_repo_languages()` - Programming languages used
  - `get_user_commits()` - User's commits in a repo
  - `get_rate_limit()` - Current API limits

#### skill_analyzer.py (Skill Analysis)
- `SkillAnalyzer` class processes repositories
- Language mapping (maps to skill categories)
- Technology/framework detection
- Score normalization (0-100 scale)
- Skill weighting by repository popularity

### Frontend Components

#### App.js (Main Component)
- State management (profileData, loading, error)
- Handles search form submission
- Fetches data from backend API
- Renders profile view or empty state

#### SearchForm.js
- Text input for GitHub username
- Submit button with loading state
- Input validation

#### ProfileCard.js
- Displays user avatar
- Shows GitHub profile stats
- Links to GitHub profile
- Shows repositories analyzed count

#### SkillRadar.js
- Recharts RadarChart component
- Top 6 skills visualization
- Detailed skill breakdown (all skills)
- Progress bars for each skill

## Technology Stack

### Backend
- **Python 3.9+**
- **Flask 2.3** - Web framework
- **Requests** - HTTP library
- **CORS** - Cross-origin support
- **python-dotenv** - Environment management

### Frontend
- **React 18** - UI library
- **Recharts** - Chart library
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### Data Science/ML
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - ML algorithms
- **NLTK** - NLP toolkit (future)

### External APIs
- **GitHub API v3** - User & repository data

## API Design

### Request/Response Pattern

**Request:**
```
GET /api/profile/torvalds
```

**Response (200 OK):**
```json
{
  "user": {
    "login": "torvalds",
    "name": "Linus Torvalds",
    "bio": "...",
    "avatar_url": "https://...",
    "public_repos": 5,
    "followers": 200000,
    "following": 0
  },
  "skills": {
    "C": 98.5,
    "Git": 97.2,
    "Kernel": 96.8
  },
  "repositories_analyzed": 5,
  "rate_limit": {
    "limit": 5000,
    "remaining": 4995,
    "reset": 1234567890
  }
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "User not found"
}
```

## Skill Scoring Algorithm

1. **Language Analysis**
   - Count repositories by language
   - Weight by repository popularity (stars)

2. **Topic Analysis**
   - Extract topics/tags from repositories
   - Map to technology skills

3. **Combination**
   - Merge language and topic scores
   - Average the frequencies

4. **Weighting**
   - Language contribution: 40%
   - Repository stars: 20%
   - Repository count: 15%
   - Domain expertise: 15%
   - Recency: 10%

5. **Normalization**
   - Scale to 0-100 range
   - Filter skills with score < 5
   - Sort by score (descending)

## Future Enhancements

### Phase 2: Advanced ML
- Clustering algorithms for skill categorization
- Natural language processing for repo descriptions
- Predictive models for skill trends

### Phase 3: Social Features
- User comparison (skill vs skill)
- Collaboration network analysis
- Peer ranking

### Phase 4: Reporting
- PDF skill report generation
- Historical tracking
- Trend analysis

### Phase 5: Integration
- GitHub authentication (OAuth)
- Real-time webhooks
- Advanced GitHub API usage

## Performance Considerations

- GitHub API rate limiting (5000 requests/hour)
- Repository pagination (max 100 per request)
- Frontend chart rendering optimization
- Caching strategies for repeated queries

## Security

- No sensitive data stored
- GitHub token in environment variable
- CORS properly configured
- Input validation on username
- Error handling without exposing internals

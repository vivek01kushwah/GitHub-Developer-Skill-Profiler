# Example Usage Guide

## Analyzing Different GitHub Users

Here are some example GitHub users you can analyze:

### Popular Open Source Developers

```
Username: torvalds
Profile: Creator of Linux
Expected Skills: C, Git, Kernel Development

Username: gvanrossum  
Profile: Python Creator
Expected Skills: Python, Design Patterns

Username: dhh
Profile: Ruby on Rails Creator
Expected Skills: Ruby, Web Development, Backend

Username: yyx990803
Profile: Vue.js Creator  
Expected Skills: JavaScript, Vue, TypeScript, Frontend

Username: tensorflow
Profile: TensorFlow Organization
Expected Skills: Machine Learning, Python, C++
```

## Testing the Application

### Test Case 1: Single Language Developer
Search for a developer known for one primary language:
- Username: `torvalds`
- Expected: High C score, Linux kernel topics
- Verify: C language shows as top skill

### Test Case 2: Full Stack Developer
Search for someone with front and backend skills:
- Username: `dhh`
- Expected: Ruby, JavaScript, multiple repo types
- Verify: Multiple language skills shown

### Test Case 3: Data Science Focus
Search for data science contributor:
- Username: `gvanrossum`
- Expected: Python dominance, multiple implementations
- Verify: Python > 80% skill score

## API Testing Examples

### Using cURL

```bash
# Get profile
curl -X GET "http://localhost:5000/api/profile/torvalds"

# Get repositories
curl -X GET "http://localhost:5000/api/repos/dhh"

# Get skills only
curl -X GET "http://localhost:5000/api/skills/gvanrossum"

# Check rate limit
curl -X GET "http://localhost:5000/api/rate-limit"

# Health check
curl -X GET "http://localhost:5000/api/health"
```

### Using Python

```python
import requests

# Get profile data
response = requests.get('http://localhost:5000/api/profile/torvalds')
data = response.json()

print(f"User: {data['user']['login']}")
print(f"Repos analyzed: {data['repositories_analyzed']}")
print(f"Top skills: {list(data['skills'].items())[:5]}")
```

### Using JavaScript/Node.js

```javascript
// Fetch with browser fetch API
fetch('http://localhost:5000/api/profile/torvalds')
  .then(res => res.json())
  .then(data => {
    console.log('User:', data.user.login);
    console.log('Skills:', data.skills);
  })
  .catch(err => console.error('Error:', err));
```

## Troubleshooting Tests

### Test: Check if Backend is Running
```bash
curl http://localhost:5000/api/health
# Should return: {"status": "healthy", "service": "GitHub Skill Profiler API"}
```

### Test: Check GitHub API Access
```bash
curl http://localhost:5000/api/rate-limit
# Should return rate limit info
```

### Test: Check CORS
```bash
# From browser console
fetch('http://localhost:5000/api/profile/torvalds')
  .then(r => r.json())
  .then(d => console.log(d))
```

### Test: Check User Exists
```bash
curl http://localhost:5000/api/repos/nonexistentuser12345
# Should return 404 error
```

## Performance Testing

### Light Load (Single Request)
```bash
curl http://localhost:5000/api/profile/torvalds
# Expected response time: 2-5 seconds
# Rate limit used: ~3-5 calls
```

### Heavy Load (Multiple Requests)
```bash
# Run 10 sequential requests
for i in {1..10}; do
  echo "Request $i..."
  curl http://localhost:5000/api/profile/torvalds
  sleep 1
done
```

### Rate Limit Testing
```bash
# Check remaining rate limit
curl http://localhost:5000/api/rate-limit | grep remaining
```

## Example Response Analysis

### User with High Language Diversity
```
Username: facebook (Meta)
Expected Output:
- Many languages (JavaScript, Python, C++, Java, etc.)
- High diversity score
- Multiple domains (Frontend, Backend, Mobile)
- Many starred repositories
```

### Specialized Developer
```
Username: torvalds
Expected Output:
- Dominant language: C (95%+)
- Few other languages
- Specialized domain (Linux, Kernel)
- Very high star counts
```

### New Developer
```
Username: newly-started-developer
Expected Output:
- 1-3 languages
- Lower overall skill scores
- Recent repositories (2023-2024)
- Low star counts
```

## Advanced Testing

### Test ML Module Directly

```python
from ml.advanced_analyzer import ComprehensiveAnalyzer

# Create analyzer
analyzer = ComprehensiveAnalyzer()

# Analyze repositories (would come from GitHub API)
repos = [
    {
        'name': 'example-repo',
        'language': 'Python',
        'topics': ['machine-learning', 'ai'],
        'stargazers_count': 100,
        'forks_count': 50
    }
]

# Run comprehensive analysis
results = analyzer.analyze_complete(repos)
print(results)
```

## Common Issues & Solutions

### Issue: "No skills detected"
**Solution:** User may have no repositories with detected languages
- Try a user with more public repositories
- Check if repositories have language field populated

### Issue: "Rate limit exceeded"
**Solution:** Too many API calls in short time
- Add GitHub Personal Access Token to .env
- Wait 1 hour for reset
- Use local caching

### Issue: "CORS error"
**Solution:** Frontend can't reach backend
- Ensure backend is running on :5000
- Check CORS_ORIGINS in backend/.env
- Verify frontend API URL matches

### Issue: "Invalid response format"
**Solution:** Backend returned unexpected data
- Check Flask logs for errors
- Verify GitHub API is accessible
- Check if username exists on GitHub

## Next Steps

1. **Deploy**: Move to production with Gunicorn/Nginx
2. **Scale**: Add caching layer (Redis)
3. **Enhance**: Integrate more GitHub data
4. **Share**: Deploy to Heroku, AWS, or Google Cloud
5. **Monetize**: Consider premium features

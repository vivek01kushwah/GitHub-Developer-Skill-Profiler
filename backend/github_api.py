"""
GitHub API Client for fetching user and repository data
Handles pagination and rate limiting
"""

import requests
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class GitHubClient:
    """Client for interacting with GitHub API v3"""
    
    BASE_URL = 'https://api.github.com'
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize GitHub API client
        
        Args:
            token: GitHub personal access token (optional, for higher rate limits)
        """
        self.token = token
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Skill-Profiler'
        }
        
        if token:
            self.headers['Authorization'] = f'token {token}'
    
    def _request(self, endpoint: str, params: Dict = None) -> Optional[Dict]:
        """
        Make request to GitHub API
        
        Args:
            endpoint: API endpoint (without base URL)
            params: Query parameters
            
        Returns:
            JSON response or None if failed
        """
        url = f'{self.BASE_URL}{endpoint}'
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e}")
            return None
        except Exception as e:
            logger.error(f"Request Error: {e}")
            return None
    
    def get_user(self, username: str) -> Optional[Dict]:
        """
        Get user information
        
        Args:
            username: GitHub username
            
        Returns:
            User data dict or None
        """
        return self._request(f'/users/{username}')
    
    def get_user_repos(self, username: str, per_page: int = 100) -> List[Dict]:
        """
        Get all public repositories for a user
        
        Args:
            username: GitHub username
            per_page: Results per page (1-100)
            
        Returns:
            List of repositories
        """
        all_repos = []
        page = 1
        
        while True:
            params = {
                'per_page': per_page,
                'page': page,
                'sort': 'updated',
                'direction': 'desc'
            }
            
            repos = self._request(f'/users/{username}/repos', params)
            
            if not repos or len(repos) == 0:
                break
            
            # Filter out forks by default (can be parameterized)
            repos = [r for r in repos if not r.get('fork')]
            all_repos.extend(repos)
            
            # Continue to next page if we got full page
            if len(repos) < per_page:
                break
            
            page += 1
        
        return all_repos
    
    def get_repo_details(self, owner: str, repo: str) -> Optional[Dict]:
        """
        Get detailed information about a repository
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Repository data dict or None
        """
        return self._request(f'/repos/{owner}/{repo}')
    
    def get_repo_languages(self, owner: str, repo: str) -> Dict[str, int]:
        """
        Get programming languages used in a repository
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Dict with language names and bytes of code
        """
        data = self._request(f'/repos/{owner}/{repo}/languages')
        return data or {}
    
    def get_user_commits(self, owner: str, repo: str, username: str) -> List[Dict]:
        """
        Get commits by a specific user in a repository
        
        Args:
            owner: Repository owner
            repo: Repository name
            username: User to filter commits by
            
        Returns:
            List of commits
        """
        params = {
            'author': username,
            'per_page': 100
        }
        
        data = self._request(f'/repos/{owner}/{repo}/commits', params)
        return data or []
    
    def get_rate_limit(self) -> Dict:
        """
        Get current GitHub API rate limit status
        
        Returns:
            Rate limit information
        """
        data = self._request('/rate_limit')
        
        if data and 'rate_limit' in data:
            limit_info = data['rate_limit']
            return {
                'limit': limit_info.get('limit'),
                'remaining': limit_info.get('remaining'),
                'reset': limit_info.get('reset')
            }
        
        return {'error': 'Could not fetch rate limit'}

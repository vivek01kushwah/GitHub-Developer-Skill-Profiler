"""
Flask Backend for GitHub Developer Skill Profiler
Main API server that handles GitHub API requests and skill analysis
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from github_api import GitHubClient
from skill_analyzer import SkillAnalyzer
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize GitHub and Analyzer
github_client = GitHubClient(os.getenv('GITHUB_TOKEN'))
skill_analyzer = SkillAnalyzer()


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'GitHub Skill Profiler API'
    }), 200


@app.route('/api/profile/<username>', methods=['GET'])
def get_profile(username):
    """
    Get complete developer profile with skills
    
    Args:
        username: GitHub username
        
    Returns:
        JSON with user info and skill radar data
    """
    try:
        logger.info(f"Fetching profile for user: {username}")
        
        # Fetch user data
        user_data = github_client.get_user(username)
        if not user_data:
            return jsonify({'error': 'User not found'}), 404
        
        # Fetch repositories
        repos = github_client.get_user_repos(username)
        
        # Analyze skills
        skills = skill_analyzer.analyze_repositories(repos)
        
        # Prepare response
        response = {
            'user': {
                'login': user_data.get('login'),
                'name': user_data.get('name'),
                'bio': user_data.get('bio'),
                'avatar_url': user_data.get('avatar_url'),
                'public_repos': user_data.get('public_repos'),
                'followers': user_data.get('followers'),
                'following': user_data.get('following'),
            },
            'skills': skills,
            'repositories_analyzed': len(repos),
            'rate_limit': github_client.get_rate_limit()
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        logger.error(f"Error fetching profile for {username}: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/repos/<username>', methods=['GET'])
def get_repos(username):
    """
    Get list of user repositories with analysis
    
    Args:
        username: GitHub username
        
    Returns:
        JSON list of repositories
    """
    try:
        logger.info(f"Fetching repositories for: {username}")
        
        repos = github_client.get_user_repos(username)
        
        if not repos:
            return jsonify({'error': 'No repositories found'}), 404
        
        return jsonify({
            'username': username,
            'repositories': repos,
            'total_count': len(repos)
        }), 200
    
    except Exception as e:
        logger.error(f"Error fetching repos for {username}: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/skills/<username>', methods=['GET'])
def get_skills(username):
    """
    Get analyzed skills for a user
    
    Args:
        username: GitHub username
        
    Returns:
        JSON with skill analysis
    """
    try:
        repos = github_client.get_user_repos(username)
        skills = skill_analyzer.analyze_repositories(repos)
        
        return jsonify({
            'username': username,
            'skills': skills
        }), 200
    
    except Exception as e:
        logger.error(f"Error analyzing skills for {username}: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/rate-limit', methods=['GET'])
def rate_limit():
    """Get current GitHub API rate limit status"""
    try:
        limit_info = github_client.get_rate_limit()
        return jsonify(limit_info), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, port=port)

"""
Advanced ML/DS Module for GitHub Skill Analysis
Includes topic clustering, language distribution, and skill prediction
"""

import numpy as np
from collections import Counter
from typing import Dict, List, Tuple
import json
import logging

logger = logging.getLogger(__name__)


class RepositoryAnalyzer:
    """Analyzes individual repositories for detailed metrics"""
    
    def __init__(self):
        self.language_stats = {}
        self.topic_stats = {}
    
    def analyze_repo(self, repo: Dict) -> Dict:
        """
        Analyze a single repository
        
        Args:
            repo: Repository data dict from GitHub API
            
        Returns:
            Dict with analysis results
        """
        analysis = {
            'name': repo.get('name'),
            'language': repo.get('language'),
            'topics': repo.get('topics', []),
            'stars': repo.get('stargazers_count', 0),
            'forks': repo.get('forks_count', 0),
            'watchers': repo.get('watchers_count', 0),
            'size': repo.get('size', 0),
            'open_issues': repo.get('open_issues_count', 0),
            'description': repo.get('description'),
            'created_at': repo.get('created_at'),
            'updated_at': repo.get('updated_at'),
            'pushed_at': repo.get('pushed_at'),
            'popularity_score': self._calculate_popularity(repo)
        }
        
        return analysis
    
    def _calculate_popularity(self, repo: Dict) -> float:
        """Calculate repository popularity score"""
        stars = repo.get('stargazers_count', 0)
        forks = repo.get('forks_count', 0)
        watchers = repo.get('watchers_count', 0)
        
        # Weighted score: stars (0.6) + forks (0.3) + watchers (0.1)
        score = (stars * 0.6) + (forks * 0.3) + (watchers * 0.1)
        
        # Normalize to 0-100
        return min((score / 100), 100)


class LanguageAnalyzer:
    """Analyzes programming language distribution and trends"""
    
    LANGUAGE_CATEGORIES = {
        'Backend': ['python', 'java', 'go', 'rust', 'php', 'ruby', 'scala', 'elixir'],
        'Frontend': ['javascript', 'typescript', 'html', 'css', 'jsx', 'vue'],
        'Systems': ['cpp', 'c', 'rust', 'assembly'],
        'Data': ['python', 'r', 'julia', 'sql'],
        'Mobile': ['swift', 'kotlin', 'dart', 'objective-c'],
    }
    
    def __init__(self):
        self.language_count = Counter()
        self.language_category_count = Counter()
    
    def analyze_languages(self, repositories: List[Dict]) -> Dict:
        """
        Analyze language distribution across repositories
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with language analysis
        """
        languages = []
        
        for repo in repositories:
            lang = repo.get('language')
            if lang:
                languages.append(lang.lower())
                self.language_count[lang.lower()] += 1
                
                # Categorize language
                for category, langs in self.LANGUAGE_CATEGORIES.items():
                    if lang.lower() in langs:
                        self.language_category_count[category] += 1
                        break
        
        # Calculate statistics
        total = len(languages)
        if total == 0:
            return {}
        
        language_distribution = {
            lang: count 
            for lang, count in self.language_count.most_common()
        }
        
        category_distribution = {
            cat: count 
            for cat, count in self.language_category_count.most_common()
        }
        
        return {
            'language_distribution': language_distribution,
            'category_distribution': category_distribution,
            'total_languages': len(language_distribution),
            'primary_language': self.language_count.most_common(1)[0][0] if self.language_count else None
        }


class TopicClusterer:
    """Clusters repositories by topics to identify skill areas"""
    
    def __init__(self):
        self.topic_count = Counter()
        self.topic_language_map = {}
    
    def cluster_topics(self, repositories: List[Dict]) -> Dict:
        """
        Cluster repositories by topics
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with topic clusters
        """
        topic_clusters = {}
        
        for repo in repositories:
            topics = repo.get('topics', []) or []
            language = repo.get('language', 'unknown')
            
            for topic in topics:
                if topic:
                    self.topic_count[topic] += 1
                    
                    if topic not in topic_clusters:
                        topic_clusters[topic] = {
                            'name': topic,
                            'count': 0,
                            'languages': Counter(),
                            'repos': []
                        }
                    
                    topic_clusters[topic]['count'] += 1
                    topic_clusters[topic]['languages'][language] += 1
                    topic_clusters[topic]['repos'].append(repo.get('name'))
        
        return {
            'clusters': list(topic_clusters.values()),
            'most_common_topics': [
                {'topic': topic, 'count': count}
                for topic, count in self.topic_count.most_common(10)
            ]
        }


class CommitPatternAnalyzer:
    """Analyzes commit patterns and activity metrics"""
    
    def __init__(self):
        self.activity_metrics = {}
    
    def analyze_activity_patterns(self, repositories: List[Dict]) -> Dict:
        """
        Analyze commit and activity patterns
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with activity analysis
        """
        total_repos = len(repositories)
        active_repos = 0
        total_stars = 0
        total_forks = 0
        avg_size = 0
        
        for repo in repositories:
            # Count stars and forks
            stars = repo.get('stargazers_count', 0)
            forks = repo.get('forks_count', 0)
            
            total_stars += stars
            total_forks += forks
            avg_size += repo.get('size', 0)
            
            # Check if repo is active (updated in last 6 months)
            updated_at = repo.get('updated_at')
            if updated_at:
                active_repos += 1
        
        avg_size = avg_size / total_repos if total_repos > 0 else 0
        
        return {
            'total_repositories': total_repos,
            'active_repositories': active_repos,
            'total_stars': total_stars,
            'total_forks': total_forks,
            'average_repo_size': round(avg_size, 2),
            'avg_stars_per_repo': round(total_stars / total_repos, 2) if total_repos > 0 else 0,
            'avg_forks_per_repo': round(total_forks / total_repos, 2) if total_repos > 0 else 0,
        }


class SkillPredictor:
    """Predicts developer skill levels based on repository patterns"""
    
    def __init__(self):
        self.skills = {}
    
    def predict_skills(self, 
                      languages: Dict,
                      topics: Dict,
                      activity: Dict,
                      repositories: List[Dict]) -> Dict[str, float]:
        """
        Predict developer skills based on multiple factors
        
        Args:
            languages: Language distribution
            topics: Topic clusters
            activity: Activity metrics
            repositories: Original repository list
            
        Returns:
            Dict with predicted skill scores
        """
        skills = {}
        
        # Extract skills from languages
        for lang, count in languages.items():
            skill_score = min((count / max(languages.values(), default=1)) * 100, 100)
            skills[lang] = skill_score
        
        # Extract skills from topics
        if isinstance(topics, dict) and 'clusters' in topics:
            for cluster in topics['clusters']:
                topic_name = cluster['name']
                count = cluster['count']
                
                # Topic score based on repository count
                if repositories:
                    topic_score = min((count / len(repositories)) * 100, 100)
                    skills[topic_name] = topic_score
        
        # Boost scores based on activity
        if activity.get('total_stars', 0) > 0:
            # High star count indicates quality projects
            activity_boost = min(activity['total_stars'] / 100, 20)
            
            for repo in repositories:
                lang = repo.get('language')
                if lang and lang in skills:
                    skills[lang] = min(skills[lang] + (activity_boost/10), 100)
        
        # Sort by score descending
        return dict(sorted(skills.items(), key=lambda x: x[1], reverse=True))


class ComprehensiveAnalyzer:
    """Main analyzer combining all sub-analyzers"""
    
    def __init__(self):
        self.repo_analyzer = RepositoryAnalyzer()
        self.lang_analyzer = LanguageAnalyzer()
        self.topic_clusterer = TopicClusterer()
        self.commit_analyzer = CommitPatternAnalyzer()
        self.skill_predictor = SkillPredictor()
    
    def analyze_complete(self, repositories: List[Dict]) -> Dict:
        """
        Perform comprehensive analysis of repositories
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with complete analysis results
        """
        if not repositories:
            return {}
        
        # Analyze each repository
        detailed_repos = [self.repo_analyzer.analyze_repo(repo) for repo in repositories]
        
        # Language analysis
        lang_analysis = self.lang_analyzer.analyze_languages(repositories)
        
        # Topic clustering
        topic_analysis = self.topic_clusterer.cluster_topics(repositories)
        
        # Activity patterns
        activity_analysis = self.commit_analyzer.analyze_activity_patterns(repositories)
        
        # Predict skills
        primary_langs = lang_analysis.get('language_distribution', {})
        skills = self.skill_predictor.predict_skills(
            primary_langs,
            topic_analysis,
            activity_analysis,
            repositories
        )
        
        return {
            'repositories': detailed_repos,
            'language_analysis': lang_analysis,
            'topic_analysis': topic_analysis,
            'activity_analysis': activity_analysis,
            'predicted_skills': skills
        }

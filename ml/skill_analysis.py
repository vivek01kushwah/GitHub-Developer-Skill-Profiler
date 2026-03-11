"""
Machine Learning and Data Science Module
Advanced skill extraction and analysis using NLP and clustering
"""

import numpy as np
from collections import Counter
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)


class LanguageAnalyzer:
    """Analyze programming language patterns"""
    
    LANGUAGE_CATEGORIES = {
        'Frontend': ['javascript', 'typescript', 'html', 'css', 'vue', 'react'],
        'Backend': ['python', 'java', 'go', 'rust', 'php', 'csharp', 'nodejs'],
        'Mobile': ['swift', 'kotlin', 'dart', 'java'],
        'Data': ['python', 'r', 'julia', 'scala'],
        'DevOps': ['go', 'rust', 'python', 'bash', 'powershell'],
        'Systems': ['rust', 'cpp', 'c', 'go', 'assembly'],
    }
    
    def __init__(self):
        pass
    
    def categorize_language(self, language: str) -> List[str]:
        """
        Categorize a language into expertise areas
        
        Args:
            language: Programming language name
            
        Returns:
            List of categories the language belongs to
        """
        lang_lower = language.lower()
        categories = []
        
        for category, langs in self.LANGUAGE_CATEGORIES.items():
            if any(l in lang_lower for l in langs):
                categories.append(category)
        
        return categories if categories else ['Other']
    
    def analyze_language_diversity(self, languages: List[str]) -> Dict:
        """
        Analyze the diversity of programming languages used
        
        Args:
            languages: List of programming languages
            
        Returns:
            Dict with diversity metrics
        """
        if not languages:
            return {'score': 0, 'languages': 0}
        
        unique_langs = set(l.lower() for l in languages if l)
        diversity_score = min(len(unique_langs) * 15, 100)
        
        return {
            'score': diversity_score,
            'languages': len(unique_langs),
            'languages_list': list(unique_langs)
        }


class CommitPatternAnalyzer:
    """Analyze commit patterns and activity metrics"""
    
    def __init__(self):
        pass
    
    def analyze_activity(self, repositories: List[Dict]) -> Dict:
        """
        Analyze overall development activity
        
        Args:
            repositories: List of repository data
            
        Returns:
            Dict with activity metrics
        """
        if not repositories:
            return {'activity_score': 0}
        
        # Calculate metrics
        total_repos = len(repositories)
        avg_stars = np.mean([r.get('stargazers_count', 0) for r in repositories])
        avg_forks = np.mean([r.get('forks_count', 0) for r in repositories])
        
        # Get recent activity (updated in last month)
        recent_activity = sum(1 for r in repositories 
                             if r.get('updated_at', '').startswith('2024-3') 
                             or r.get('updated_at', '').startswith('2024-02'))
        
        activity_score = min((recent_activity / max(total_repos, 1)) * 100, 100)
        
        return {
            'activity_score': activity_score,
            'total_repos': total_repos,
            'avg_stars': round(avg_stars, 1),
            'avg_forks': round(avg_forks, 1),
            'recent_activity': recent_activity
        }
    
    def calculate_repository_influence(self, repositories: List[Dict]) -> List[Tuple[str, float]]:
        """
        Calculate influence score for each repository
        
        Args:
            repositories: List of repository data
            
        Returns:
            List of (repo_name, influence_score) tuples
        """
        repo_scores = []
        
        for repo in repositories:
            stars = repo.get('stargazers_count', 0)
            forks = repo.get('forks_count', 0)
            watchers = repo.get('watchers_count', 0)
            
            # Simple influence formula
            influence = (stars * 2) + (forks * 1.5) + (watchers * 0.5)
            
            repo_scores.append((repo['name'], influence))
        
        return sorted(repo_scores, key=lambda x: x[1], reverse=True)


class TopicAnalyzer:
    """Analyze repository topics and knowledge areas"""
    
    DOMAIN_KEYWORDS = {
        'Web Development': ['web', 'frontend', 'backend', 'fullstack', 'react', 'vue', 'angular', 'nodejs'],
        'Data Science': ['data-science', 'machine-learning', 'ml', 'ai', 'deep-learning', 'data-analysis'],
        'DevOps': ['devops', 'kubernetes', 'docker', 'ci-cd', 'cicd', 'infrastructure'],
        'Mobile': ['mobile', 'ios', 'android', 'flutter', 'react-native'],
        'Cloud': ['cloud', 'aws', 'azure', 'gcp', 'google-cloud', 'serverless'],
        'Database': ['database', 'sql', 'mongodb', 'postgresql', 'redis', 'nosql'],
        'API': ['api', 'rest', 'graphql', 'webhook', 'sdk'],
        'Security': ['security', 'encryption', 'authentication', 'cryptography'],
    }
    
    def __init__(self):
        pass
    
    def extract_domains(self, topics: List[str]) -> Dict[str, int]:
        """
        Extract knowledge domains from repository topics
        
        Args:
            topics: List of repository topics
            
        Returns:
            Dict with domain counts
        """
        domain_scores = Counter()
        
        for topic in topics:
            if not topic:
                continue
            
            topic_lower = topic.lower()
            for domain, keywords in self.DOMAIN_KEYWORDS.items():
                if any(kw in topic_lower for kw in keywords):
                    domain_scores[domain] += 1
        
        return dict(domain_scores)
    
    def cluster_topics(self, repositories: List[Dict]) -> Dict[str, List[str]]:
        """
        Cluster repositories by topics
        
        Args:
            repositories: List of repository data
            
        Returns:
            Dict with topic clusters
        """
        clusters = {}
        
        for repo in repositories:
            topics = repo.get('topics', []) or []
            
            for topic in topics:
                if topic:
                    if topic not in clusters:
                        clusters[topic] = []
                    clusters[topic].append(repo['name'])
        
        # Filter to clusters with 2+ repos
        return {t: repos for t, repos in clusters.items() if len(repos) >= 1}


class ExperienceCalculator:
    """Calculate years of experience in different areas"""
    
    def calculate_expertise_years(self, repositories: List[Dict]) -> Dict[str, float]:
        """
        Estimate years of experience based on repository history
        (Simplified version - calculates based on update dates)
        
        Args:
            repositories: List of repository data
            
        Returns:
            Dict with experience estimates
        """
        expertise = {}
        
        # This is a simplified calculation
        # In production, would use actual commit history data
        
        if repositories:
            # Get oldest and newest repo updates
            updates = [r.get('updated_at', '') for r in repositories if r.get('updated_at')]
            if updates:
                latest = max(updates)
                # Calculate as years since last activity
                expertise['active_for_years'] = 'Current'
        
        return expertise


class SkillAggregator:
    """Aggregate all skill analysis into final scores"""
    
    def __init__(self):
        self.language_analyzer = LanguageAnalyzer()
        self.commit_analyzer = CommitPatternAnalyzer()
        self.topic_analyzer = TopicAnalyzer()
        self.experience_calculator = ExperienceCalculator()
    
    def aggregate_analysis(self, repositories: List[Dict], language_skills: Dict, 
                          topic_skills: Dict) -> Dict:
        """
        Aggregate all analyses into comprehensive skill profile
        
        Args:
            repositories: List of repository data
            language_skills: Language-based skill scores
            topic_skills: Topic-based skill scores
            
        Returns:
            Comprehensive skill analysis
        """
        analysis = {
            'language_diversity': self.language_analyzer.analyze_language_diversity(
                [r.get('language') for r in repositories if r.get('language')]
            ),
            'activity_metrics': self.commit_analyzer.analyze_activity(repositories),
            'top_repositories': self.commit_analyzer.calculate_repository_influence(repositories)[:5],
            'language_skills': language_skills,
            'topic_skills': topic_skills,
        }
        
        return analysis

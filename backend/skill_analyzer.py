"""
Skill Analyzer Module
Analyzes GitHub repositories to extract developer skills
Uses language analysis, topic extraction, and contribution metrics
"""

from typing import Dict, List
from collections import Counter
import logging

logger = logging.getLogger(__name__)


class SkillAnalyzer:
    """Analyzes GitHub repositories to extract and score developer skills"""
    
    # Language skill categories
    LANGUAGE_SKILLS = {
        'Python': ['python'],
        'JavaScript': ['javascript', 'typescript'],
        'Java': ['java'],
        'C++': ['cpp', 'c++'],
        'C#': ['csharp', 'c#'],
        'Go': ['go'],
        'Rust': ['rust'],
        'PHP': ['php'],
        'Ruby': ['ruby'],
        'Swift': ['swift'],
        'Kotlin': ['kotlin'],
        'SQL': ['sql'],
        'HTML': ['html'],
        'CSS': ['css'],
        'Scala': ['scala'],
    }
    
    # Technology skill categories
    TECH_SKILLS = {
        'React': ['react', 'reactjs'],
        'Vue': ['vue', 'vuejs'],
        'Angular': ['angular'],
        'Django': ['django'],
        'Flask': ['flask'],
        'FastAPI': ['fastapi', 'fast-api'],
        'Node.js': ['nodejs', 'node'],
        'Docker': ['docker', 'containerization'],
        'Kubernetes': ['kubernetes', 'k8s'],
        'AWS': ['aws', 'amazon'],
        'GCP': ['gcp', 'google-cloud'],
        'Azure': ['azure', 'microsoft-azure'],
        'Machine Learning': ['ml', 'machine-learning', 'tensorflow', 'pytorch'],
        'Data Science': ['data-science', 'pandas', 'numpy'],
        'DevOps': ['devops', 'ci', 'cd', 'cicd'],
    }
    
    # Skill weight factors
    WEIGHTS = {
        'language_contribution': 0.4,
        'repository_stars': 0.2,
        'repository_count': 0.15,
        'domain_expertise': 0.15,
        'recency': 0.1
    }
    
    def __init__(self):
        """Initialize skill analyzer"""
        self.languages_by_repo = []
        self.topics_by_repo = []
        self.stars_by_language = {}
    
    def analyze_repositories(self, repositories: List[Dict]) -> Dict[str, float]:
        """
        Analyze repositories and extract skill scores
        
        Args:
            repositories: List of repository dicts from GitHub API
            
        Returns:
            Dict with skill names and scores (0-100)
        """
        if not repositories:
            return {}
        
        # Extract language frequencies
        language_stats = self._analyze_languages(repositories)
        
        # Extract topic-based skills
        topic_stats = self._analyze_topics(repositories)
        
        # Combine and score
        all_skills = self._combine_skills(language_stats, topic_stats, repositories)
        
        # Normalize to 0-100 scale
        normalized_skills = self._normalize_scores(all_skills)
        
        return normalized_skills
    
    def _analyze_languages(self, repositories: List[Dict]) -> Dict[str, int]:
        """
        Analyze programming languages across repositories
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with language frequencies
        """
        language_count = Counter()
        
        for repo in repositories:
            languages = repo.get('language') or []
            
            if isinstance(languages, str):
                languages = [languages]
            elif not isinstance(languages, list):
                languages = []
            
            # Map to skill categories
            for lang in languages:
                if lang:
                    lang_lower = lang.lower()
                    for skill_name, skill_aliases in self.LANGUAGE_SKILLS.items():
                        if lang_lower in skill_aliases:
                            language_count[skill_name] += 1
                            break
        
        return dict(language_count)
    
    def _analyze_topics(self, repositories: List[Dict]) -> Dict[str, int]:
        """
        Analyze topics and tags across repositories
        
        Args:
            repositories: List of repository dicts
            
        Returns:
            Dict with topic frequencies
        """
        topic_count = Counter()
        
        for repo in repositories:
            topics = repo.get('topics', []) or []
            
            if isinstance(topics, list):
                for topic in topics:
                    topic_lower = topic.lower() if topic else ''
                    
                    # Check against tech skills
                    for skill_name, skill_aliases in self.TECH_SKILLS.items():
                        if any(alias in topic_lower for alias in skill_aliases):
                            topic_count[skill_name] += 1
                            break
        
        return dict(topic_count)
    
    def _combine_skills(self, language_stats: Dict, topic_stats: Dict, 
                       repositories: List[Dict]) -> Dict[str, float]:
        """
        Combine language and topic stats into skill scores
        
        Args:
            language_stats: Language frequency dict
            topic_stats: Topic frequency dict
            repositories: Original repository list
            
        Returns:
            Dict with combined skill scores
        """
        combined = {}
        all_skills = set(language_stats.keys()) | set(topic_stats.keys())
        
        # Calculate scores
        for skill in all_skills:
            language_score = language_stats.get(skill, 0)
            topic_score = topic_stats.get(skill, 0)
            
            # Calculate average
            combined[skill] = (language_score + topic_score) / 2
        
        # Weight by repository stars for top skills
        for repo in repositories:
            if repo.get('language'):
                lang = repo['language'].lower()
                stars = max(repo.get('stargazers_count', 0), 1)
                
                for skill_name, skill_aliases in self.LANGUAGE_SKILLS.items():
                    if lang in skill_aliases and skill_name in combined:
                        combined[skill_name] += (stars / 10)
        
        return combined
    
    def _normalize_scores(self, scores: Dict[str, float]) -> Dict[str, float]:
        """
        Normalize scores to 0-100 scale
        
        Args:
            scores: Raw skill scores
            
        Returns:
            Normalized scores (0-100)
        """
        if not scores:
            return {}
        
        max_score = max(scores.values()) if scores.values() else 1
        
        if max_score == 0:
            max_score = 1
        
        normalized = {}
        for skill, score in scores.items():
            # Cap at 100
            normalized_score = min((score / max_score) * 100, 100)
            # Only include skills with score > 5
            if normalized_score > 5:
                normalized[skill] = round(normalized_score, 1)
        
        # Sort by score descending
        return dict(sorted(normalized.items(), key=lambda x: x[1], reverse=True))
    
    def get_skill_distribution(self, skills: Dict[str, float]) -> Dict[str, float]:
        """
        Get distribution of skills by category
        
        Args:
            skills: Skill scores dict
            
        Returns:
            Grouped skill distribution
        """
        distribution = {
            'languages': {},
            'technologies': {},
            'other': {}
        }
        
        for skill, score in skills.items():
            if skill in self.LANGUAGE_SKILLS:
                distribution['languages'][skill] = score
            elif skill in self.TECH_SKILLS:
                distribution['technologies'][skill] = score
            else:
                distribution['other'][skill] = score
        
        return distribution

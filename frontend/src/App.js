import React, { useState } from 'react';
import SearchForm from './components/SearchForm';
import ProfileCard from './components/ProfileCard';
import SkillRadar from './components/SkillRadar';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';
import './App.css';

function App() {
  const [profileData, setProfileData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (username) => {
    setLoading(true);
    setError(null);
    setProfileData(null);

    try {
      const response = await fetch(`http://localhost:5000/api/profile/${username}`);
      
      if (!response.ok) {
        throw new Error(`User not found: ${response.status}`);
      }

      const data = await response.json();
      setProfileData(data);
    } catch (err) {
      setError(err.message || 'Failed to fetch profile');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      {/* Header */}
      <header>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '2rem' }}>
          <div>
            <h1>GitHub Developer Skill Profiler</h1>
            <p>Enter your GitHub username to discover your coding skills</p>
          </div>
          <div style={{ marginTop: '0.5rem', minWidth: '380px' }}>
            <SearchForm onSearch={handleSearch} loading={loading} />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main>

        {/* Error Message */}
        {error && <ErrorMessage message={error} />}

        {/* Loading State */}
        {loading && <LoadingSpinner />}

        {/* Results Section */}
        {profileData && !loading && (
          <div className="results-grid">
            {/* Profile Card */}
            <ProfileCard user={profileData.user} stats={profileData} />

            {/* Skill Radar Chart */}
            <SkillRadar skills={profileData.skills} />
          </div>
        )}

        {/* Empty State */}
        {!profileData && !loading && !error && (
          <div className="empty-state">
            <p>Enter a GitHub username to get started</p>
            <p className="subtitle">
              Analyze your skills based on your repositories, languages, and contributions
            </p>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer style={{ background: 'rgba(15, 23, 42, 0.5)', textAlign: 'center', color: '#cbd5e1', padding: '0.75rem' }}>
        <p style={{ margin: 0, fontSize: '0.8rem' }}>&copy; 2026 GitHub Skill Profiler. Powered by GitHub API.</p>
      </footer>
    </div>
  );
}

export default App;

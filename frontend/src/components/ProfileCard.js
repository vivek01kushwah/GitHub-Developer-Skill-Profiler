import React from 'react';

function ProfileCard({ user, stats }) {
  if (!user) return null;

  return (
    <div className="card" style={{ minHeight: '450px', display: 'flex', flexDirection: 'column' }}>
      {/* Header Background */}
      <div className="profile-header"></div>

      {/* Content */}
      <div style={{ padding: '0.75rem 1rem 1rem 1rem', flex: 1, display: 'flex', flexDirection: 'column' }}>
        {/* Avatar */}
        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '0.5rem' }}>
          <img
            src={user.avatar_url}
            alt={user.login}
            className="profile-avatar"
          />
        </div>

        {/* User Info */}
        <div style={{ textAlign: 'center', marginBottom: '0.75rem' }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: 700, color: '#1e293b', margin: '0 0 0.15rem 0' }}>
            {user.name || user.login}
          </h2>
          <p style={{ color: '#667eea', margin: '0.15rem 0 0 0', fontSize: '0.85rem', fontWeight: 500 }}>
            @{user.login}
          </p>
          {user.bio && (
            <p style={{ fontSize: '0.75rem', color: '#64748b', marginTop: '0.5rem', margin: '0.5rem 0 0 0' }}>
              {user.bio}
            </p>
          )}
        </div>

        {/* Stats Grid */}
        <div className="stats-grid">
          <div className="stat-item">
            <div className="stat-value">{user.public_repos}</div>
            <div className="stat-label">Repositories</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{user.followers}</div>
            <div className="stat-label">Followers</div>
          </div>
          <div className="stat-item">
            <div className="stat-value">{user.following}</div>
            <div className="stat-label">Following</div>
          </div>
        </div>

        {/* Analysis Stats */}
        <div style={{ marginTop: '0.5rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', fontSize: '0.8rem' }}>
            <span style={{ color: '#64748b' }}>Analyzed:</span>
            <span style={{ fontWeight: 600, color: '#1e293b' }}>{stats.repositories_analyzed}</span>
          </div>
          {stats.rate_limit && (
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem' }}>
              <span style={{ color: '#64748b' }}>API:</span>
              <span style={{ fontWeight: 600, color: stats.rate_limit.remaining > 100 ? '#10b981' : '#f59e0b' }}>
                {stats.rate_limit.remaining} left
              </span>
            </div>
          )}
        </div>

        {/* Link to GitHub */}
        <a
          href={`https://github.com/${user.login}`}
          target="_blank"
          rel="noopener noreferrer"
          style={{
            display: 'block',
            marginTop: 'auto',
            padding: '0.75rem',
            background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            fontWeight: 600,
            textAlign: 'center',
            borderRadius: '8px',
            textDecoration: 'none',
            transition: 'all 0.3s ease',
            cursor: 'pointer'
          }}
          onMouseEnter={(e) => {
            e.target.style.transform = 'translateY(-2px)';
            e.target.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.3)';
          }}
          onMouseLeave={(e) => {
            e.target.style.transform = 'translateY(0)';
            e.target.style.boxShadow = 'none';
          }}
        >
          View on GitHub
        </a>
      </div>
    </div>
  );
}

export default ProfileCard;

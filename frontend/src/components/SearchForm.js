import React, { useState } from 'react';

function SearchForm({ onSearch, loading }) {
  const [username, setUsername] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username.trim()) {
      onSearch(username);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{
      display: 'flex',
      justifyContent: 'center',
      width: '100%',
      maxWidth: '600px',
      margin: '0 auto'
    }}>
      <div style={{
        display: 'flex',
        gap: '0.75rem',
        width: '100%'
      }}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter GitHub username..."
          style={{
            flex: 1,
            padding: '1rem 1.5rem',
            borderRadius: '8px',
            border: 'none',
            fontSize: '1rem',
            color: '#1e293b',
            backgroundColor: '#ffffff',
            boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)',
            fontFamily: 'inherit',
            outline: 'none',
            transition: 'all 0.3s ease'
          }}
          onFocus={(e) => {
            e.target.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.3)';
          }}
          onBlur={(e) => {
            e.target.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
          }}
          disabled={loading}
          autoComplete="off"
        />
        <button
          type="submit"
          disabled={loading || !username.trim()}
          style={{
            padding: '1rem 2rem',
            background: loading || !username.trim() 
              ? 'linear-gradient(135deg, #94a3b8 0%, #64748b 100%)'
              : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            color: 'white',
            border: 'none',
            borderRadius: '8px',
            fontSize: '1rem',
            fontWeight: 600,
            cursor: loading || !username.trim() ? 'not-allowed' : 'pointer',
            transition: 'all 0.3s ease',
            boxShadow: '0 4px 12px rgba(102, 126, 234, 0.3)',
            whiteSpace: 'nowrap'
          }}
          onMouseEnter={(e) => {
            if (!loading && username.trim()) {
              e.target.style.transform = 'translateY(-2px)';
              e.target.style.boxShadow = '0 6px 20px rgba(102, 126, 234, 0.4)';
            }
          }}
          onMouseLeave={(e) => {
            e.target.style.transform = 'translateY(0)';
            if (!loading && username.trim()) {
              e.target.style.boxShadow = '0 4px 12px rgba(102, 126, 234, 0.3)';
            }
          }}
        >
          {loading ? 'Searching...' : 'Analyze'}
        </button>
      </div>
    </form>
  );
}

export default SearchForm;

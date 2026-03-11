import React from 'react';

function ErrorMessage({ message }) {
  return (
    <div className="error-container">
      <p style={{ fontWeight: 600, fontSize: '1rem', margin: '0 0 0.5rem 0' }}>Error</p>
      <p style={{ fontSize: '0.9rem', margin: 0 }}>{message}</p>
    </div>
  );
}

export default ErrorMessage;

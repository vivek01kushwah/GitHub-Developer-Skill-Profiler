import React from 'react';
import { RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar, Legend, Tooltip, ResponsiveContainer } from 'recharts';

function SkillRadar({ skills }) {
  if (!skills || Object.keys(skills).length === 0) {
    return (
      <div className="skill-radar-container" style={{ textAlign: 'center' }}>
        <p style={{ color: '#64748b', fontSize: '1rem' }}>No skills data available</p>
      </div>
    );
  }

  // Transform skills object to array and get top 6 skills
  const skillsArray = Object.entries(skills)
    .map(([name, score]) => ({
      name,
      score: Math.round(score)
    }))
    .sort((a, b) => b.score - a.score)
    .slice(0, 6);

  return (
    <div className="skill-radar-container">
      <h2>Your Top 5 Skills</h2>
      
      <ResponsiveContainer width="100%" height={350}>
        <RadarChart data={skillsArray.slice(0, 5)}>
          <PolarGrid stroke="#e2e8f0" />
          <PolarAngleAxis 
            dataKey="name" 
            tick={{ fill: '#667eea', fontSize: 12, fontWeight: 600 }}
            orientation="outer"
          />
          <PolarRadiusAxis 
            angle={90} 
            domain={[0, 100]} 
            tick={{ fill: '#94a3b8', fontSize: 11 }} 
          />
          <Radar 
            name="Skill Score" 
            dataKey="score" 
            stroke="#667eea" 
            fill="#667eea" 
            fillOpacity={0.6}
            isAnimationActive={true}
          />
          <Tooltip 
            contentStyle={{ 
              backgroundColor: '#fff', 
              border: '2px solid #667eea',
              borderRadius: '8px',
              padding: '0.5rem',
              boxShadow: '0 4px 12px rgba(102, 126, 234, 0.2)'
            }}
            formatter={(value) => `${value}%`}
            labelStyle={{ color: '#667eea', fontWeight: 600 }}
          />
          <Legend 
            wrapperStyle={{ paddingTop: '0.75rem' }}
            iconType="line"
          />
        </RadarChart>
      </ResponsiveContainer>

      {/* Skills List */}
      <div style={{ marginTop: '1rem' }}>
        <h3 style={{ fontSize: '1.1rem', fontWeight: 700, color: '#1e293b', margin: '0 0 0.75rem 0' }}>
          All Skills
        </h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.5rem' }}>
          {Object.entries(skills)
            .sort(([,a], [,b]) => b - a)
            .map(([skill, score]) => (
              <div key={skill} className="skill-item">
                <span className="skill-name">{skill}</span>
                <div className="skill-bar">
                  <div 
                    className="skill-bar-fill"
                    style={{ width: `${score}%` }}
                  ></div>
                </div>
                <span className="skill-percent">{Math.round(score)}%</span>
              </div>
            ))}
        </div>
      </div>
    </div>
  );
}

export default SkillRadar;

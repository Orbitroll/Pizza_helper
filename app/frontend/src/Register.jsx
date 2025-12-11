import React, { useState } from 'react';
import { useAuth } from './AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import bg1 from './backround-photos/ninja1.jpg';

export default function Register() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await register(username, password);
      navigate('/login');
    } catch (err) {
      setError(err.response?.data?.error || 'Registration failed');
    }
  };

  return (
    <div className="auth-page" style={{ backgroundImage: `url(${bg1})` }}>
      <div className="auth-card">
        <h2 style={{ textAlign: 'center', marginBottom: '30px', fontSize: '2em' }}>📝 Register</h2>
        {error && <div style={{ background: '#ffebee', color: '#c62828', padding: '10px', borderRadius: '8px', marginBottom: '20px', textAlign: 'center' }}>{error}</div>}
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label style={{ fontWeight: 'bold', color: '#555' }}>Username</label>
            <input 
              className="auth-input"
              type="text" 
              value={username} 
              onChange={(e) => setUsername(e.target.value)} 
              required 
              placeholder="Choose a username"
            />
          </div>
          <div className="input-group">
            <label style={{ fontWeight: 'bold', color: '#555' }}>Password</label>
            <input 
              className="auth-input"
              type="password" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              required 
              placeholder="Choose a password"
            />
          </div>
          <button className="submit-btn" type="submit">Register</button>
        </form>
        <p style={{ marginTop: '20px', textAlign: 'center', color: '#666' }}>
          Already have an account? <Link to="/login" style={{ color: '#ff6b6b', fontWeight: 'bold', textDecoration: 'none' }}>Login</Link>
        </p>
        <div style={{ textAlign: 'center', marginTop: '20px' }}>
            <Link to="/" style={{ color: '#888', textDecoration: 'none' }}>&larr; Back to Home</Link>
        </div>
      </div>
    </div>
  );
}

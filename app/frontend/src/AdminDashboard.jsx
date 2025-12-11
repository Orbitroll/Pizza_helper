import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

export default function AdminDashboard() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { user } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (!user || !user.is_admin) {
      navigate('/');
      return;
    }

    const fetchData = async () => {
      try {
        const res = await axios.get('/api/auth/admin/data');
        setUsers(res.data);
      } catch (err) {
        setError('Failed to fetch admin data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [user, navigate]);

  if (loading) return <div className="container">Loading...</div>;
  if (error) return <div className="container" style={{color: 'red'}}>{error}</div>;

  return (
    <div className="container" style={{ marginTop: '50px' }}>
      <h1 style={{ textAlign: 'center', marginBottom: '30px' }}>🛡️ Admin Dashboard</h1>
      
      <div style={{ display: 'grid', gap: '20px' }}>
        {users.map(u => (
          <div key={u.id} className="card" style={{ padding: '20px', cursor: 'default' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #eee', paddingBottom: '10px', marginBottom: '10px' }}>
              <h3 style={{ margin: 0 }}>👤 {u.username} {u.is_admin ? '(Admin)' : ''}</h3>
              <span style={{ color: '#666' }}>ID: {u.id}</span>
            </div>
            
            <h4>History ({u.history.length})</h4>
            {u.history.length === 0 ? (
              <p style={{ color: '#999', fontStyle: 'italic' }}>No history recorded.</p>
            ) : (
              <div style={{ maxHeight: '200px', overflowY: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '0.9em' }}>
                  <thead>
                    <tr style={{ background: '#f9f9f9' }}>
                      <th style={{ padding: '8px', textAlign: 'left' }}>Date</th>
                      <th style={{ padding: '8px', textAlign: 'left' }}>Recipe</th>
                      <th style={{ padding: '8px', textAlign: 'left' }}>Details</th>
                    </tr>
                  </thead>
                  <tbody>
                    {u.history.map((h, idx) => (
                      <tr key={idx} style={{ borderBottom: '1px solid #eee' }}>
                        <td style={{ padding: '8px' }}>{new Date(h.date).toLocaleDateString()}</td>
                        <td style={{ padding: '8px' }}>{h.recipe_name}</td>
                        <td style={{ padding: '8px' }}>
                          Flour: {h.details.flour}g, Water: {h.details.water}g
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        ))}
      </div>
      
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button className="btn" onClick={() => navigate('/')}>Back to Home</button>
      </div>
    </div>
  );
}

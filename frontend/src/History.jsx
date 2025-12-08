import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

export default function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('/api/history/')
      .then(res => setHistory(res.data))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="container">Loading...</div>;

  return (
    <div className="container">
      <Link to="/" className="btn" style={{ marginBottom: '20px', display: 'inline-block' }}>&larr; Back to Home</Link>
      <h2>Calculation History</h2>
      <div className="category-grid" style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {history.map(item => (
          <div key={item.id} className="card" style={{ padding: '20px', cursor: 'default' }}>
            <h3>{item.recipe_name}</h3>
            <p style={{ color: '#666', fontSize: '0.9em' }}>{new Date(item.date).toLocaleString()}</p>
            <div style={{ marginTop: '10px', background: '#f9f9f9', padding: '10px', borderRadius: '5px' }}>
              <p><strong>Flour:</strong> {item.details.flour}g</p>
              <p><strong>Water:</strong> {item.details.water}g</p>
              <p><strong>Yeast:</strong> {item.details.yeast}g</p>
              <p><strong>Salt:</strong> {item.details.salt}g</p>
            </div>
          </div>
        ))}
        {history.length === 0 && <p>No history found.</p>}
      </div>
    </div>
  );
}

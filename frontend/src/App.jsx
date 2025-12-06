import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import axios from 'axios';
import { recipes } from './recipes';
import logo from './assets/pizzahelperlogo.png';
import oliveFocacciaImg from './assets/photos/olive-focaccia.png';
import bg1 from './backround-photos/ninja1.jpg';
import bg2 from './backround-photos/ninja2.jpg';
import bg3 from './backround-photos/ninja3.jpg';
import bg4 from './backround-photos/ninja4.jpg';
import bg5 from './backround-photos/ninja5.jpg';

const backgroundImages = [bg1, bg2, bg3, bg4, bg5];

function StepTimer({ duration, onComplete }) {
  const [timeLeft, setTimeLeft] = useState(duration * 60);
  const [isActive, setIsActive] = useState(false);

  React.useEffect(() => {
    let interval = null;
    if (isActive && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft(timeLeft => timeLeft - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      setIsActive(false);
      if (onComplete) onComplete();
    }
    return () => clearInterval(interval);
  }, [isActive, timeLeft, onComplete]);

  const formatTime = (seconds) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = seconds % 60;
    return `${h > 0 ? h + ':' : ''}${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  return (
    <div className={`step-timer ${isActive ? 'active' : ''}`}>
      <span className="timer-display">{formatTime(timeLeft)}</span>
      <button onClick={() => setIsActive(!isActive)}>
        {isActive ? '⏸️' : '▶️'}
      </button>
      <button onClick={() => { setIsActive(false); setTimeLeft(duration * 60); }}>
        🔄
      </button>
    </div>
  );
}

function App() {
  const { t, i18n } = useTranslation();
  const [selectedRecipe, setSelectedRecipe] = useState(null);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [weather, setWeather] = useState(null);
  const [locationName, setLocationName] = useState(null);
  const [yeastResult, setYeastResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [completedSteps, setCompletedSteps] = useState(new Set());
  const [timerDoneSteps, setTimerDoneSteps] = useState(new Set());
  const [bgIndex, setBgIndex] = useState(0);

  React.useEffect(() => {
    const interval = setInterval(() => {
      setBgIndex((prev) => (prev + 1) % backgroundImages.length);
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  // New state for calculator
  const [numPizzas, setNumPizzas] = useState(4);
  const [ballWeight, setBallWeight] = useState(250);
  const [hydration, setHydration] = useState(60);

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
    document.body.dir = lng === 'he' ? 'rtl' : 'ltr';
  };

  const handleRecipeClick = (recipe) => {
    setSelectedRecipe(recipe);
    setWeather(null);
    setLocationName(null);
    setYeastResult(null);
    setError(null);
    setCompletedSteps(new Set());
    setTimerDoneSteps(new Set());
    // Set default hydration from recipe or default to 60
    setHydration(recipe.hydration ? recipe.hydration * 100 : 60);
  };

  const handleStepComplete = (index) => {
    setCompletedSteps(prev => {
      const newSet = new Set(prev);
      newSet.add(index);
      return newSet;
    });
  };

  const handleTimerDone = (index) => {
    setTimerDoneSteps(prev => {
      const newSet = new Set(prev);
      newSet.add(index);
      return newSet;
    });
  };

  const fetchWeatherAndCalculate = () => {
    setLoading(true);
    setError(null);

    if (!navigator.geolocation) {
      setError("Geolocation is not supported by your browser");
      setLoading(false);
      return;
    }

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        try {
          const { latitude, longitude } = position.coords;
          
          // 1. Get Weather
          const weatherRes = await axios.get(`/api/weather/temperature`, {
            params: { latitude, longitude }
          });
          
          // The backend returns { temperature: ..., ... }
          const temp = weatherRes.data.temperature !== undefined ? weatherRes.data.temperature : 20; 
          setWeather(temp);
          if (weatherRes.data.location_name) {
            setLocationName(weatherRes.data.location_name);
          }

          // 2. Calculate Yeast

          const yeastRes = await axios.get(`/api/dough/calculate_yeast`, {
            params: {
              hours: selectedRecipe.hours,
              temperature: temp
            }
          });

          setYeastResult(yeastRes.data);
        } catch (err) {
          console.error(err);
          setError("Failed to fetch data");
        } finally {
          setLoading(false);
        }
      },
      (err) => {
        setError("Unable to retrieve your location");
        setLoading(false);
      }
    );
  };

  return (
    <>
      <div style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        zIndex: -1,
        backgroundImage: `url(${backgroundImages[bgIndex]})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        opacity: 0.3,
        transition: 'background-image 1s ease-in-out'
      }} />
      <div className="container">
      <header className="header">
        <div className="header-content">
          <img src={logo} alt="Pizza Helper Logo" className="app-logo" />
          {locationName && (
            <div className="location-badge">
              📍 {locationName}
            </div>
          )}
        </div>
        <div className="lang-switcher">
          <button className={i18n.language === 'en' ? 'active' : ''} onClick={() => changeLanguage('en')}>EN</button>
          <button className={i18n.language === 'he' ? 'active' : ''} onClick={() => changeLanguage('he')}>HE</button>
        </div>
      </header>

      {!selectedRecipe ? (
        !selectedCategory ? (
          <div className="category-selection fade-in">
            <h2>{t('select_category')}</h2>
            <div className="category-grid" style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '20px'}}>
              <div className="card category-card" onClick={() => setSelectedCategory('pizza')}>
                <img src="https://images.unsplash.com/photo-1574071318508-1cdbab80d002?auto=format&fit=crop&w=600&q=80" alt="Pizza" className="recipe-image" />
                <div className="card-content">
                  <h3>🍕 Pizza</h3>
                </div>
              </div>
              <div className="card category-card" onClick={() => setSelectedCategory('focaccia')}>
                <img src={oliveFocacciaImg} alt="Focaccia" className="recipe-image" />
                <div className="card-content">
                  <h3>🍞 Focaccia</h3>
                </div>
              </div>
            </div>
          </div>
        ) : (
          <div className="recipe-list fade-in">
            <button className="btn" onClick={() => setSelectedCategory(null)} style={{marginBottom: '20px'}}>
              &larr; Back
            </button>
            <h2>{selectedCategory === 'pizza' ? '🍕 Pizza' : '🍞 Focaccia'}</h2>
            
            <div className="category-grid" style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '20px'}}>
              {recipes.filter(r => r.category === selectedCategory).map((recipe) => (
                <div key={recipe.id} className="card" onClick={() => handleRecipeClick(recipe)}>
                  {recipe.image && <img src={recipe.image} alt={t(recipe.nameKey)} className="recipe-image" />}
                  <div className="card-content">
                    <h3>{t(recipe.nameKey)}</h3>
                    <p>{t('hours')}: {recipe.hours}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )
      ) : (
        <div className="recipe-detail">
          <button className="btn" onClick={() => setSelectedRecipe(null)} style={{marginBottom: '20px'}}>
            &larr; Back
          </button>
          
          {selectedRecipe.image && <img src={selectedRecipe.image} alt={t(selectedRecipe.nameKey)} className="detail-image" />}
          
          <h2>{t(selectedRecipe.nameKey)}</h2>
          
          <div className="recipe-meta">
             <span><strong>{t('hours')}:</strong> {selectedRecipe.hours}</span>
             <span><strong>{t('temperature')}:</strong> {selectedRecipe.defaultTemp}°C</span>
          </div>

          {selectedRecipe.ingredients && (
            <div className="ingredients-list" style={{marginBottom: '20px', padding: '15px', backgroundColor: '#fff', borderRadius: '8px', border: '1px solid #eee'}}>
              <h3>{t('ingredients')} (Base Recipe)</h3>
              <ul>
                {(i18n.language === 'he' && selectedRecipe.ingredients_he ? selectedRecipe.ingredients_he : selectedRecipe.ingredients).map((ing, i) => (
                  <li key={i}>{ing}</li>
                ))}
              </ul>
            </div>
          )}

          <div className="calculator-section">
            <h3>{t('dough_calculator')}</h3>
            <div className="input-group">
              <label>{t('num_pizzas')}</label>
              <input 
                type="number" 
                value={numPizzas} 
                onChange={(e) => setNumPizzas(Number(e.target.value))}
              />
            </div>
            <div className="input-group">
              <label>{t('ball_weight')}</label>
              <select 
                value={ballWeight} 
                onChange={(e) => setBallWeight(Number(e.target.value))}
                style={{
                  width: '100%',
                  padding: '12px',
                  border: '2px solid #eee',
                  borderRadius: '8px',
                  fontSize: '16px',
                  backgroundColor: 'white'
                }}
              >
                <option value={250}>{t('personal')}</option>
                <option value={500}>{t('family')}</option>
              </select>
            </div>
            <div className="input-group">
              <label>{t('hydration_label')}</label>
              <input 
                type="number" 
                value={hydration} 
                onChange={(e) => setHydration(Number(e.target.value))}
              />
            </div>
          </div>
          
          <div className="action-area">
            <button className="btn" onClick={fetchWeatherAndCalculate} disabled={loading}>
              {loading ? t('loading') : t('calculate')}
            </button>
          </div>

          {error && <p style={{color: 'red'}}>{error}</p>}

          {weather !== null && yeastResult && (
            <div className="result-box">
              <h3>
                {t('current_temp')}: {weather}°C 
              </h3>
              {locationName && (
                <p style={{margin: '5px 0', fontWeight: 'bold'}}>
                  📍 {locationName}
                </p>
              )}
              <p style={{fontSize: '0.8em', color: '#666'}}>{t('source')}: Open-Meteo</p>
              
              <table className="ingredients-table">
                <thead>
                  <tr>
                    <th>{t('ingredients')}</th>
                    <th>{t('percentage')}</th>
                    <th>{t('weight_g')}</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>🌾 {t('flour')} ({selectedRecipe.flour})</td>
                    <td>100%</td>
                    <td>{Math.round((numPizzas * ballWeight) / (1 + (hydration/100) + 0.03 + (yeastResult.yeast_percentage/100)))}g</td>
                  </tr>
                  <tr>
                    <td>💧 {t('water')}</td>
                    <td>{hydration}%</td>
                    <td>{Math.round(((numPizzas * ballWeight) / (1 + (hydration/100) + 0.03 + (yeastResult.yeast_percentage/100))) * (hydration/100))}g</td>
                  </tr>
                  <tr>
                    <td>🧂 {t('salt')}</td>
                    <td>3%</td>
                    <td>{Math.round(((numPizzas * ballWeight) / (1 + (hydration/100) + 0.03 + (yeastResult.yeast_percentage/100))) * 0.03)}g</td>
                  </tr>
                  <tr>
                    <td>🦠 {t('yeast_idy')}</td>
                    <td>{yeastResult.yeast_percentage}%</td>
                    <td>{(((numPizzas * ballWeight) / (1 + (hydration/100) + 0.03 + (yeastResult.yeast_percentage/100))) * (yeastResult.yeast_percentage/100)).toFixed(2)}g</td>
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {selectedRecipe.steps && (
            <div className="instructions-list">
              <h3>{t('instructions')}</h3>
              <div className="steps-container">
                {selectedRecipe.steps.map((step, index) => (
                  <div key={index} className={`step-item ${timerDoneSteps.has(index) ? 'timer-done' : ''}`}>
                    <div className="step-header">
                      <div>
                        <strong>Step {index + 1}:</strong> {t(step.text)}
                      </div>
                    </div>
                    {step.duration && (
                      <StepTimer duration={step.duration} onComplete={() => handleTimerDone(index)} />
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}
          
          {selectedRecipe.instructions && !selectedRecipe.steps && (
            <div className="instructions-list">
              <h3>{t('instructions')}</h3>
              <ol>
                {selectedRecipe.instructions.map((step, index) => (
                  <li key={index}>{step}</li>
                ))}
              </ol>
            </div>
          )}
        </div>
      )}
      </div>
    </>
  );
}

export default App;

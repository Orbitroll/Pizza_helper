import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import axios from 'axios';
import { recipes } from './recipes';

function App() {
  const { t, i18n } = useTranslation();
  const [selectedRecipe, setSelectedRecipe] = useState(null);
  const [weather, setWeather] = useState(null);
  const [yeastResult, setYeastResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
    document.body.dir = lng === 'he' ? 'rtl' : 'ltr';
  };

  const handleRecipeClick = (recipe) => {
    setSelectedRecipe(recipe);
    setWeather(null);
    setYeastResult(null);
    setError(null);
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
    <div className="container">
      <header className="header">
        <h1>{t('title')}</h1>
        <div>
          <button onClick={() => changeLanguage('en')}>EN</button>
          <button onClick={() => changeLanguage('he')}>HE</button>
        </div>
      </header>

      {!selectedRecipe ? (
        <div className="recipe-list">
          <h2>{t('recipes')}</h2>
          {recipes.map((recipe) => (
            <div key={recipe.id} className="card" onClick={() => handleRecipeClick(recipe)}>
              <h3>{t(recipe.nameKey)}</h3>
              <p>{t('hours')}: {recipe.hours}</p>
            </div>
          ))}
        </div>
      ) : (
        <div className="recipe-detail">
          <button className="btn" onClick={() => setSelectedRecipe(null)} style={{marginBottom: '20px'}}>
            &larr; Back
          </button>
          
          <h2>{t(selectedRecipe.nameKey)}</h2>
          <p>{t('hours')}: {selectedRecipe.hours}</p>
          
          <div className="action-area">
            <button className="btn" onClick={fetchWeatherAndCalculate} disabled={loading}>
              {loading ? t('loading') : t('calculate')}
            </button>
          </div>

          {error && <p style={{color: 'red'}}>{error}</p>}

          {weather !== null && (
            <div className="result-box">
              <h3>{t('current_temp')}: {weather}°C</h3>
              {yeastResult && (
                <div>
                  <h4>{t('yeast_result')}:</h4>
                  <p style={{fontSize: '24px', fontWeight: 'bold'}}>
                    {yeastResult.yeast_percentage}%
                  </p>
                  <p>({t('yeast')} IDY)</p>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;

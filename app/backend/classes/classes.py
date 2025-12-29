from flask import Flask , request, jsonify
import requests
import json
import time
from pathlib import Path
from prometheus_client import Counter, Histogram

geo_search = "https://geocoding-api.open-meteo.com/v1/search"
get_temperature = "https://api.open-meteo.com/v1/forecast"

# Prometheus Metrics
WEATHER_API_REQUESTS = Counter('weather_api_requests_total', 'Total requests to Weather APIs', ['api', 'status'])
WEATHER_API_LATENCY = Histogram('weather_api_latency_seconds', 'Latency of Weather API requests', ['api'])

class Weather:
    def get_location_name(self, latitude: float, longitude: float):
        start_time = time.time()
        try:
            # Use OpenStreetMap Nominatim for reverse geocoding
            headers = {'User-Agent': 'PizzaHelper/1.0'}
            res = requests.get(
                "https://nominatim.openstreetmap.org/reverse",
                params={"lat": latitude, "lon": longitude, "format": "json"},
                headers=headers,
                timeout=10
            )
            
            # Record metrics
            WEATHER_API_LATENCY.labels(api='nominatim').observe(time.time() - start_time)
            WEATHER_API_REQUESTS.labels(api='nominatim', status=res.status_code).inc()

            if res.status_code == 200:
                data = res.json()
                address = data.get("address", {})
                # Try to find the most relevant name
                return address.get("city") or address.get("town") or address.get("village") or address.get("suburb") or address.get("county")
        except Exception as e:
            print(f"Error getting location: {e}")
            WEATHER_API_REQUESTS.labels(api='nominatim', status='error').inc()
            pass
        return None

    def city(self, name: str, country_code: str | None = None):
        start_time = time.time()
        try:
            weather = requests.get(
                geo_search,
                params={"name": name, "country_code": country_code},
                timeout=10
            )
            
            # Record metrics
            WEATHER_API_LATENCY.labels(api='open-meteo-geo').observe(time.time() - start_time)
            WEATHER_API_REQUESTS.labels(api='open-meteo-geo', status=weather.status_code).inc()

            if weather.status_code != 200:
                return {"error": f"Request failed with {weather.status_code}"}
            weather_data = weather.json()
            results = weather_data.get("results") or []
            if not results:
                return {"error": f' no results for place:{name}'}
            if country_code:
                filtered = [r for r in results if r.get("country_code") == country_code]
                results = filtered or results
            r = results[0]
            return {
                "name": r.get("name"),
                "latitude": r.get("latitude"),
                "longitude": r.get("longitude"),
                "timezone": r.get("timezone"),
                "country": r.get("country"),
                "country_code": r.get("country_code"),
            }
        except Exception as e:
            WEATHER_API_REQUESTS.labels(api='open-meteo-geo', status='error').inc()
            raise e

    def get_City(self):
        city = request.args.get("city")
        if not city:
            return jsonify({"error": "city query parameter required"}), 400
        country_code = request.args.get("country_code", "IL")
        weather = Weather()
        return jsonify(weather.city(name=city, country_code=country_code))
    
    def temperature(self, latitude: float, longitude: float):
        start_time = time.time()
        try:
            weather = requests.get(
                get_temperature,
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "current_weather": True,
                },
                timeout=10
            )
            
            # Record metrics
            WEATHER_API_LATENCY.labels(api='open-meteo-forecast').observe(time.time() - start_time)
            WEATHER_API_REQUESTS.labels(api='open-meteo-forecast', status=weather.status_code).inc()

            if weather.status_code != 200:
                return {"error": f"Request failed with {weather.status_code}"}
            weather_data = weather.json()
            current_weather = weather_data.get("current_weather")
            if not current_weather:
                return {"error": "no current weather data available"}
            return {
                "temperature": current_weather.get("temperature"),
                "windspeed": current_weather.get("windspeed"),
                "winddirection": current_weather.get("winddirection"),
                "weathercode": current_weather.get("weathercode"),
                "time": current_weather.get("time"),
            }
        except Exception as e:
            WEATHER_API_REQUESTS.labels(api='open-meteo-forecast', status='error').inc()
            raise e
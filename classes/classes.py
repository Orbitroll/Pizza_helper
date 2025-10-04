from flask import Flask , request, jsonify
import requests
import json
from pathlib import Path

geo_search = "https://geocoding-api.open-meteo.com/v1/search"
get_temperature = "https://api.open-meteo.com/v1/forecast"

class Weather:
    def city(self, name: str, country_code: str | None = None):
        weather = requests.get(
            geo_search,
            params={"name": name, "country_code": country_code},
            timeout=10
        )
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

    def get_weather(self):
        city = request.args.get("city")
        if not city:
            return jsonify({"error": "city query parameter required"}), 400
        country_code = request.args.get("country_code", "IL")
        weather = Weather()
        return jsonify(weather.city(name=city, country_code=country_code))
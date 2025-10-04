# ...existing code...
from flask import Blueprint, request, jsonify
from classes.classes import Weather

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET'])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "city query parameter required"}), 400
    country_code = request.args.get("country_code", "IL")
    result = Weather().city(name=city, country_code=country_code)
    return jsonify(result)

@weather_bp.route('/temperature', methods=['GET'])
def temperature():
    latitude = request.args.get("latitude", type=float)
    longitude = request.args.get("longitude", type=float)
    if latitude is None or longitude is None:
        return jsonify({"error": "latitude and longitude query parameters are required"}), 400
    result = Weather().temperature(latitude=latitude, longitude=longitude)
    return jsonify(result)
# ...existing code...
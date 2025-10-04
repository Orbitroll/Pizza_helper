from flask import Flask, request, jsonify
import requests
from classes.classes import Weather

app = Flask('pizza_daw_maker')

@app.route('/weather', methods=['GET'])
def weather():
    return Weather().get_weather()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
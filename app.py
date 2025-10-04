from flask import Flask
from weather.weather import weather_bp

app = Flask('pizza_daw_maker')
app.register_blueprint(weather_bp, url_prefix='/weather')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
from flask import Flask
from weather.weather import weather_bp
from ingridiens.flour import flour_bp 
from ingridiens.yeast import yeast_bp

app = Flask('pizza_daw_maker')
app.register_blueprint(weather_bp, url_prefix='/weather')
app.register_blueprint(flour_bp, url_prefix='/flour')
app.register_blueprint(yeast_bp, url_prefix='/yeast')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
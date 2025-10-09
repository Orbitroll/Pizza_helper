from flask import Flask
from weather.weather import weather_bp
from ingredients.flour import flour_bp 
from ingredients.yeast import yeast_bp
from ingredients.dough import dough_bp

app = Flask('pizza_daw_maker')
app.register_blueprint(weather_bp, url_prefix='/weather')
app.register_blueprint(flour_bp, url_prefix='/flour')
app.register_blueprint(yeast_bp, url_prefix='/yeast')
app.register_blueprint(dough_bp, url_prefix='/dough')

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
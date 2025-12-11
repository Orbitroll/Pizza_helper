from flask import Flask
from flask_login import LoginManager
from models import db, User
import os

# Blueprints
from weather.weather import weather_bp
from ingredients.flour import flour_bp 
from ingredients.yeast import yeast_bp
from ingredients.dough import dough_bp
from auth import auth_bp
from history import history_bp
from chat import chat_bp

app = Flask('pizza_daw_maker')
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(weather_bp, url_prefix='/weather')
app.register_blueprint(flour_bp, url_prefix='/flour')
app.register_blueprint(yeast_bp, url_prefix='/yeast')
app.register_blueprint(dough_bp, url_prefix='/dough')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(history_bp, url_prefix='/history')
app.register_blueprint(chat_bp, url_prefix='/chat')

import time
from sqlalchemy.exc import OperationalError

with app.app_context():
    retries = 10
    while retries > 0:
        try:
            db.create_all()
            print("Database connected and tables created!")
            break
        except OperationalError:
            retries -= 1
            print(f"Database not ready yet, retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)
    else:
        print("Could not connect to database after multiple retries.")

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)


from click import argument, echo
from flask.cli import AppGroup
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from environs import Env
from app.configs import database
from app.models.users import Users
from app.tst import teste
from flask_migrate import Migrate
from app.configs import migrations

env = Env()
env.read_env()

def create_app():
    app = Flask(__name__)
    env = Env()
    env.read_env()

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@localhost:5432/e15'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    
    
    database.init_app(app)
    teste.init_app(app)
    migrations.init_app(app)
    
    return app
    




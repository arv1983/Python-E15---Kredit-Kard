from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db
    
    from app.models.users import Users
    from app.models.credit_cards import CreditCard

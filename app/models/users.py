from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False)
    is_admin = Column(Boolean, default=False)
    password_hash = Column(String)


from datetime import timedelta


class Config:
    SECRET_KEY = 'yeudSNtTD6EaJoJo1hKJtYgSnsqCcANK'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////sqlite/todo.sql'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=50)
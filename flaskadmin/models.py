from flaskadmin import db, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


class Users(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.VARCHAR(length=128), nullable=False)
    user_name = db.Column(db.TEXT, nullable=False)
    id_hash = db.Column(db.VARCHAR(length=128), nullable=False)
    balance = db.Column(db.Integer, server_default='5', nullable=False)
    rate = db.Column(db.Integer, server_default='0', nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    address = db.Column(db.VARCHAR(length=128), nullable=True)
    reg_time = db.Column(db.DATETIME, server_default=func.now(), nullable=False)
    invest = db.Column(db.Boolean, server_default='0', nullable=False)


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.VARCHAR(length=128), nullable=False)
    password = db.Column(db.VARCHAR(length=128), nullable=False)


class Items(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    btn_name = db.Column(db.VARCHAR(length=128), nullable=False)
    btn_text = db.Column(db.TEXT, nullable=False)


class Percent(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    per_name = db.Column(db.VARCHAR(length=128), nullable=False)
    per_count = db.Column(db.Integer, nullable=False)
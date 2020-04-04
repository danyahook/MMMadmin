from flask import Blueprint, render_template, request, abort
from flaskadmin.models import Users, Items, Percent
from datetime import date, timedelta, datetime
from flaskadmin import db
from flask_login import login_required, current_user


stats = Blueprint('stats', __name__, template_folder='templates/statistics')


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


@stats.route('/', methods=['GET'])
@login_required
def get_all_users(sort_by=None):
    sort_by = request.args.get('sortby') if sort_by is None else sort_by

    if sort_by == 'day':
        name = 'Пользователи за день'
        users = Users.query.filter(Users.reg_time >= date.today()).all()
    elif sort_by == 'week':
        name = 'Пользователи за неделю'
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        users = Users.query.filter(Users.reg_time >= start).all()
    elif sort_by == 'month':
        name = 'Пользователи за месяц'
        today = date.today()
        start = today.replace(day=1)
        users = Users.query.filter(Users.reg_time >= start).all()
    elif sort_by == 'status':
        name = 'Пользователи выполнившие условия'
        status = True if sort_by == 'status' else False
        users = Users.query.filter_by(status=status).all()
    else:
        name = 'Все пользователи'
        users = Users.query.all()
    users_data = list()

    sum_balance = 0
    user_count = len(users)

    for user in users:
        user_data = {'id': user.id, 'user_name': user.user_name, 'balance': user.balance,
                     'rate': user.rate, 'address': user.address, 'invest': user.invest
                     }
        sum_balance += user.balance
        users_data.append(user_data)

    general_info = {'sum_balance': sum_balance, 'user_count': user_count}
    return render_template('users.html', users_data=users_data, general_info=general_info, name=name)


@stats.route('/user/<uid>', methods=['GET', 'POST'])
@login_required
def edit(uid):
    user = Users.query.filter_by(id=uid).first()

    if user is not None and request.method == 'POST':
        balance = request.form.get("balance")
        investor = request.form.get("investor")

        if is_number(balance) and (investor == '0' or investor == '1'):

            investor = True if investor == '1' else False

            user.balance = balance
            user.invest = investor

            if user.status is False and investor is True:
                user.status = True

            db.session.commit()
        else:
            abort(404)

    return render_template('edit.html', user=user)


@stats.route('/items', methods=['GET', 'POST'])
@login_required
def edit_items():
    items = Items.query.all()

    if items is not None and request.method == 'POST':
        texts = request.form.getlist("btntext")
        j = 0

        for item in items:
            item.btn_text = texts[j]
            j += 1

        db.session.commit()

    return render_template('edit_items.html', items=items)


@stats.route('/percent', methods=['GET', 'POST'])
@login_required
def edit_percent():
    percent = Percent.query.all()

    if percent is not None and request.method == 'POST':
        values = request.form.getlist("percents")
        j = 0

        for per in percent:
            per.per_count = values[j]
            j += 1

        db.session.commit()

    return render_template('edit_percent.html', percent=percent)


@stats.route('/qwe', methods=['GET', 'POST'])
def qwe():
    items = Items(btn_name='📥 Внести', btn_text='')
    db.session.add(items)
    items = Items(btn_name='📤 Вывести > 100 USDN', btn_text='')
    db.session.add(items)
    items = Items(btn_name='📘 О нас', btn_text='')
    db.session.add(items)
    items = Percent(per_name='Обычный пользователь', per_count='')
    db.session.add(items)
    items = Percent(per_name='Инвестор', per_count='')
    db.session.add(items)

    db.session.commit()
    return 'ok'
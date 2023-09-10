"""
Задание №9
📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""
from flask import Flask, render_template, request, make_response, session, url_for, redirect
import secrets

app = Flask(__name__)
# secrets.token_hex()
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    if 'name' in session:
        print(session['name'])
        return render_template('index.html', name=session['name'])
    else:
        return redirect(url_for('form'))


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        session['name'] = request.form.get('name') or 'NoName'
        session['email'] = request.form.get('email') or 'NoEmail'
        return redirect(url_for('index'))
    return render_template('form.html')


@app.route('/logout/')
def logout():
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

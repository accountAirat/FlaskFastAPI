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
from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    if request.cookies.get('name'):
        name = request.cookies.get('name')
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('form'))


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name_form = request.form.get('name')
        email_form = request.form.get('email')

        response = make_response(redirect('/index'))
        response.set_cookie('name', name_form)
        response.set_cookie('email', email_form)
        return response
    return render_template('form.html')


@app.post('/logout')
def logout():
    response = make_response(redirect('/form'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run()

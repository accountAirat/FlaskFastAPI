# Задание №5
# 📌 Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.


# Задание №6
# 📌 Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request, redirect, flash, url_for

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
@application.route('/<string:page_name>')
def index(page_name='index.html'):
    return render_template(page_name)


# @application.get('/math/')
# def math_get():
#     return render_template('math.html')
#
#
# @application.post('/math/')
# def math_post():
#     res = 0
#     num1 = int(request.form.get('num1'))
#     num2 = int(request.form.get('num2'))
#     operation = request.form.get('operation')
#     if operation == 'plus':
#         res = num1 + num2
#     elif operation == 'minus':
#         res = num1 - num2
#     elif operation == 'mult':
#         res = num1 * num2
#     elif operation == 'div':
#         if num2 == 0:
#             return 'На ноль делить нельзя!'
#         res = num1 / num2
#     return str(res)

# @application.get('/checker/')
# def checker_get():
#     return render_template('checker.html')
#
#
# @application.post('/checker/')
# def checker_post():
#     name = request.form.get('name')
#     age = request.form.get('age')
#     if name == 'mike' and age == '18':
#         return render_template('index.html')
#     else:
#         return render_template('404.html')

# 📌 Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.


# @application.get('/sqrt/')
# def sqrt_get():
#     return render_template('sqrt.html')
#
#
# @application.post('/sqrt/')
# def sqrt_post():
#     num = int(request.form.get('num'))
#     return f'{num} в квадрате = {num ** 2}'


# Задание №8
# 📌 Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# 📌 При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!"


# @application.route('/flashform/', methods=['POST', 'GET'])
# def flashform():
#     if request.method == 'POST':
#         if not request.form['name']:
#             flash('Ошибка, введите имя!', 'danger')
#             return redirect(url_for('flashform'))
#         name = request.form['name']
#         flash('Сообщение отправлено', 'success')
#         return f'Привет, {name}'
#     return render_template('flashform.html')


if __name__ == '__main__':
    application.run(host='')

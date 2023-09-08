from flask import Flask

app = Flask(__name__)


# 1
# @app.route('/')
# def hello_world():
#     return 'Hello world'
# 2
@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'


# 3
@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Феодор!'


# 4
@app.route('/')
@app.route('/<name>/')
def hello(name='незнакомец'):
    return f'Привет, {name.capitalize()}!'


# 5
@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Путь до файла "{file}"'


# 6
@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run()

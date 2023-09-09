"""
Задание №1
Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.

Задание №2
Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""
from pathlib import PurePath, Path
from flask import Flask, render_template, redirect, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/hi/<name>')
def hi(name):
    return render_template('hi.html', name=name)


@app.get('/btn/')
def get_touch_me():
    return render_template('form.html')


@app.post('/btn/')
def post_touch_me():
    name = request.form.get('name')
    return redirect(url_for('hi', name=name))


# @app.route('/image/')
@app.route('/image/<file_name>')
def image(file_name):
    image_path = PurePath.joinpath(Path.cwd(), 'static', 'uploads', file_name)
    print(image_path)
    return render_template('image.html', file_name=image_path)


@app.get('/image_load/')
def get_image_load():
    return render_template('image_load.html')


@app.post('/image_load/')
def post_image_load():
    file = request.files.get('file')
    file_name = secure_filename(file.filename)
    image_path = PurePath.joinpath(Path.cwd(), 'static', 'uploads', file_name)
    file.save(image_path)
    return redirect(f'image.html/{file_name}')


if __name__ == "__main__":
    app.run()

from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'Харитон'
    }
    response = make_response(render_template('index.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response


if __name__ == '__main__':
    app.run()
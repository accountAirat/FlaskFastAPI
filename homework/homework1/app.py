from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/catalog/')
def catalog():
    _catalog = [
        {
            "name": "Одежда",
            "link": "cloth.html"
        },
        {
            "name": "Обувь",
            "link": "cloth.html"
        },
        {
            "name": "Куртки",
            "link": "cloth.html"
        }
    ]
    context = {'catalog': _catalog}
    return render_template('catalog.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

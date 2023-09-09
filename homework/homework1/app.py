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
    context = [
        {
            "name": "Одежда",
            "link": "cloth"
        },
        {
            "name": "Обувь",
            "link": "cloth"
         },
        {
            "name": "Куртки",
            "link": "cloth"
        }
    ]
    return render_template('catalog.html', context=context)


if __name__ == '__main__':
    app.run('')

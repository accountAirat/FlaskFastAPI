from os.path import exists

from flask import Flask, render_template, request, url_for, redirect
from .models import db, User
from .forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect
import secrets
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/users/<username>/')
def users(username):
    user = User.query.filter(User.username == username).first()
    context = {'user': user}
    return render_template('users.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.username == form.username.data).first()

        if user:
            db.session.delete(user)
            db.session.commit()
        db.session.add(User(username=form.username.data, lastname=form.lastname.data,
                            email=form.email.data, password=generate_password_hash(form.password.data)))
        db.session.commit()
        return redirect(url_for('users', username=form.username.data))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()

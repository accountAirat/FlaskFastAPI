from flask import Flask
from lesson.lesson3.models import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

'''
MySQL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =
'mysql+pymysql://username:password@hostname/database_name'
db = SQLAlchemy(app)

PostgreSQL
postgresql+psycopg2://username:password@hostname/database_name
'''


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


if __name__ == '__main__':
    add_user()
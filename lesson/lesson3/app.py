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

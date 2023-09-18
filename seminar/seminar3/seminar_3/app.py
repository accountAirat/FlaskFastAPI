from flask import Flask, render_template, url_for
from models import db, Student, Faculty, Author, Book, Mark
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seminar3.db'
db.init_app(app)
migrate = Migrate(app, db)


@app.context_processor
def menu_items():
    menu_items = [
        {'name': 'Home', 'url': url_for("index")},
        {'name': 'Task 1', 'url': url_for("task1")},
        {'name': 'Task 2', 'url': url_for("task2")},
        {'name': 'Task 3', 'url': url_for("task3")},
        # {'name': 'Task 4', 'url': url_for("task4")},
        # {'name': 'Task 9', 'url': url_for("task9")},
    ]
    return dict(menu_items=menu_items)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task1')
def task1():
    all_students = Student.query.order_by(-Student.id).all()
    return render_template('task1.html', students=all_students)


@app.route('/task2')
def task2():
    all_books = Book.query.all()
    return render_template('task2.html', all_books=all_books)


@app.route('/task3')
def task3():
    students = Student.query.all()  # Получаем всех студентов
    student_data = []

    for student in students:
        marks = Mark.query.filter_by(student_id=student.id).all()  # Получаем оценки для каждого студента
        mark_data = [{'subject_name': mark.subject_name, 'mark': mark.mark} for mark in marks]
        student_info = {
            'id': student.id,
            'name': student.name,
            'surname': student.surname,
            'age': student.age,
            'gender': student.gender,
            'group': student.group,
            'email': student.email,
            'marks': mark_data
        }
        student_data.append(student_info)

    return render_template('task3.html', students=student_data)


@app.cli.command('init_db')
def initdb_command():
    db.create_all()
    print('New DB just created.')

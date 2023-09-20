import random

from flask import Flask, render_template, request

from models import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

from flask_wtf.csrf import CSRFProtect

app.config['SECRET_KEY'] = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'
csrf = CSRFProtect(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/about/')
def about():  # put application's code here
    return render_template('about.html')


@app.route('/contact/')
def contact():  # put application's code here
    return render_template('contact.html')


@app.route('/add-nums/<int:num>/<int:num2>')
def add_nums(num, num2):
    return str(num + num2)


@app.route('/str-len/<str_inp>')
def str_len(str_inp):
    return str(len(str_inp))


# @app.route('/students/')
# def students():
#     _students = [
#         {
#             "name": "John",
#             "surname": "Doe",
#             "age": 20,
#             "average": 85
#         },
#         {
#             "name": "Jane",
#             "surname": "Smith",
#             "age": 22,
#             "average": 92
#         },
#     ]
#     context = {'students': _students}
#     return render_template('students.html', **context)

@app.route('/news/')
def news():
    _news = [
        {
            "title": "John1",
            "descr": "Doe",
            "date": 201
        },
        {
            "title": "John2",
            "descr": "Doe",
            "date": 202
        },
        {
            "title": "John3",
            "descr": "Doe",
            "date": 203
        },
    ]
    context = {'news': _news}
    return render_template('news.html', **context)




@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


# @app.cli.command("fill-db")
# def fill_tables():
#     sex_var = ['M', 'F']
#     group_var = []
#     count = 5
#
#     for elem in range(1, count + 1):
#         new_group = Groups(group_name=f'Group{elem}')
#         group_var.append(new_group.group_name)
#         rnd_val = random.choice(group_var)
#         db.session.add(new_group)

        # new_student = Students(firstname=f'f-name{elem}',
        #                        lastname=f'l-name{elem}',
        #                        age=f'{random.randint(18, 65)}',
        #                        sex=f'{random.choice(sex_var)}',
        #                        group=f'{rnd_val}',
        #                        group_id=f'{group_var.index(rnd_val) + 1}',
        #                        )
        # db.session.add(new_student)
        ##########################################################################
#
#         new_student = Students(firstname=f'f-name{elem}',
#                                lastname=f'l-name{elem}',
#                                group=f'{rnd_val}',
#                                mail=f'mail{elem}@mail.ru',
#                                )
#         db.session.add(new_student)
#
#
#
#
#         new_grad = Grads(student_id=new_student.id,
#                          subj_name=f'Subj{elem}',
#                          grad=elem)
#
#         db.session.add(new_grad)
#
#         db.session.commit()
#
#
# @app.route('/students/')
# def all_students():
#     students = Students.query.all()
#     grads = Grads.query.all()
#     context = {'students': students,
#                'grads': grads
#                }
#     return render_template('students.html', **context)


####################################################################


from forms import RegistrationForm


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     username = form.username.data
#     email = form.email.data
#     password = form.password.data
#     if request.method == 'POST' and form.validate():
#         if Users.query.filter(Users.username == username).all() or Users.query.filter(Users.email == email).all():
#             context = {'alert_message': "Пользователь уже существует!"}
#             return render_template('login.html', form=form, **context)
#         else:
#             print(Users.query.filter(Users.username == username).all())
#             new_user = Users(username=username, email=email, password=password)
#             db.session.add(new_user)
#             db.session.commit()
#     return render_template('login.html', form=form)

#########################################################################

@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    context = {'alert_message': "Добро пожаловать!"}
    form = RegistrationForm()
    username = form.username.data
    email = form.email.data
    password = form.password.data
    birthday = form.birthday.data
    terms = form.terms.data
    if request.method == 'POST' and form.validate():
        if Users.query.filter(Users.username == username).all() or Users.query.filter(Users.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('registration.html', form=form, **context)
        else:
            print(Users.query.filter(Users.username == username).all())
            new_user = Users(username=username, email=email, password=password, birthday=birthday, terms=terms)
            db.session.add(new_user)
            db.session.commit()
            return render_template('registration.html', form=form, **context)
    return render_template('registration.html', form=form)

if __name__ == '__main__':
    app.run()

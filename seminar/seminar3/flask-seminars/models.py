from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# class Students(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(80), nullable=False)
#     lastname = db.Column(db.String(80), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     sex = db.Column(db.String(5), nullable=False)
#     group = db.Column(db.String(120), nullable=False)
#     group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
#
#     def __repr__(self):
#         return f'User({self.firstname}, {self.lastname},{self.group})'


# class Students(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     firstname = db.Column(db.String(80), nullable=False)
#     lastname = db.Column(db.String(80), nullable=False)
#     group = db.Column(db.String(120), nullable=False)
#     mail = db.Column(db.String(120), nullable=False)
#
#     def __repr__(self):
#         return f'User({self.firstname}, {self.lastname},{self.group})'
#
#
# class Groups(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     group_name = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return f'Group({self.id}, {self.group_name})'
#
#
# class Grads(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
#     subj_name = db.Column(db.String(120), unique=True, nullable=False)
#     grad = db.Column(db.Integer)
#
#     def __repr__(self):
#         return f'Grad({self.id}, {self.grad})'


#########################################################################################

# Задание №5
# 📌 Создать форму регистрации для пользователя.
# 📌 Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# 📌 Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# 📌 При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.

# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#
#     def __repr__(self):
#         return f'User({self.username},{self.email})'

#########################################################################################

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.String(80), nullable=False)
    terms = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'User({self.username},{self.email})'
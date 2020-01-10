from app import db
from flask_security import UserMixin, RoleMixin
import datetime


class Quizz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer1 = db.Column(db.String(100))
    answer2 = db.Column(db.String(100))
    answer3 = db.Column(db.String(100))
    right_answer = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Quizz, self).__init__(*args, **kwargs)

    def __repr__(self):
        return 'Question id: %s, Question: %s, Right_answer: %s' % (self.id, self.question, self.right_answer)


roles_users = db.Table('roles_user',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(255))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    active = db.Column(db.Boolean())



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(255))

from wtforms import Form, StringField, TextAreaField, DateTimeField


class QuestionForm(Form):
    question = TextAreaField('Quote')
    answer1 = StringField('Answer 1')
    answer2 = StringField('Answer 2')
    answer3 = StringField('Answer 3')
    right_answer = StringField('The right answer')


class CreateUser(Form):
    email = StringField('email', default='')
    name = StringField('Name', default='')
    password = StringField('Password')

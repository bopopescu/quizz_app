from wtforms import Form, StringField, TextAreaField


class QuestionForm(Form):
    question = TextAreaField('Quote')
    answer1 = StringField('Answer 1')
    answer2 = StringField('Answer 2')
    answer3 = StringField('Answer 3')
    right_answer = StringField('The right answer')

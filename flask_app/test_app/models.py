from app import db


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

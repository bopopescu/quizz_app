from app import app, db
from models import Quizz
from flask import render_template
from forms import QuestionForm
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf import CSRFProtect

CSRFProtect(app)

@app.route('/create', methods=['POST', 'GET'])
def create_question():
    form = QuestionForm(request.form)
    if request.method == 'POST':
        question = request.form['question']
        answer1 = request.form['answer1']
        answer2 = request.form['answer2']
        answer3 = request.form['answer3']
        right_answer = request.form['right_answer']

        try:
            que = Quizz(question=question, answer1=answer1,
                        answer2=answer2, answer3=answer3,
                        right_answer=right_answer)
            db.session.add(que)
            db.session.commit()

        except:
            print('Something has gone wrong')

        return redirect( url_for('base') )

    return render_template('create_que.html', form=form)


@app.route('/')
def base():
    welcome = "Welcome to flask application about quotes"
    return render_template('base.html',welcome=welcome)

@app.route('/quotes')
def quotes():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    quotes = Quizz.query.all()
    pages = Quizz.query.paginate(page=page, per_page=6)
    return render_template('quotes.html', quotes=quotes, pages=pages)

@app.route('/test')
def test():
    return render_template('test.html')

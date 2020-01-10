from app import app, db
from models import Quizz, User
from flask import render_template
from forms import QuestionForm, CreateUser
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf import CSRFProtect
from flask_security import login_required
from sqlalchemy.sql.expression import func, select


CSRFProtect(app)

@app.route('/create_user', methods=['POST', 'GET'])
def user():
    form = CreateUser(request.form)
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        try:
            user = User(email=email, name=name,
                            password=password)
            db.session.add(user)
            db.session.commit()
        except:
            print('Something wrong!')

    return render_template('create_user.html', form=form)

@app.route('/create', methods=['POST', 'GET'])
@login_required
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



@app.route('/test', methods=["GET", "POST"])
def test():

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    selected = db.session.query(Quizz).order_by(func.rand()).limit(10)
    selected = selected.from_self()
    pages = selected.paginate(page=page, per_page=1, error_out=False)

    if request.method == "POST":
        curr_answer = request.form['answer_form']
        correct_answer = Quizz.right_answer
        score = 0
        print(score)
        if not pages.has_next:
            return redirect(url_for('/result', score=score))
    return render_template('test.html', pages=pages)


@app.route('/result')
def result():

    return render_template('end_test.html', score=score)


@app.route('/quiz')
def quiz():
    quizes = Quizz.query.all()
    return render_template('quiz.html',quizes=quizes)

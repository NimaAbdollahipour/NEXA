from .main import db


question_exam = db.Table(
    'question_exam',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('exam_id', db.Integer, db.ForeignKey('exam.id'), primary_key=True)
)
tag_question = db.Table(
    'tag_question',
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), unique=True, nullable=False)
    exams = db.relationship('Exam', backref='user')
    results = db.relationship('Result', backref='user')
    answers = db.relationship('Answer', backref='user')
    questions = db.relationship('Question', backref='user')


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    updated_date = db.Column(db.Date)
    access_key = db.Column(db.String(16), nullable=False, unique=True)
    duration = db.Column(db.Integer, nullable=False)
    pass_score = db.Column(db.Integer)
    is_active = db.Boolean(db.Boolean, nullable=False)
    rules = db.Column(db.String(8), nullable=False, unique=True)
    results = db.relationship('Result', backref='exam')
    questions = db.relationship('Question', backref='exam')


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    private = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    options = db.relationship('Option', backref='question')
    tags = db.relationship('Tag', secondary=tag_question, lazy="subquery",
                           backref=db.backref("questions", lazy=True))
    exams = db.relationship('Exam', secondary=question_exam, lazy="subquery",
                            backref=db.backref("questions", lazy=True))
    answers = db.relationship('Answer', backref='question')


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    selected = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)


class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    passed = db.Column(db.Boolean, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True, unique=True)



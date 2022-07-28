from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "42b5ebdc531959a8ffb5736e99ddd2e048fa1276aaf4e354c77a823435a7983a"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DB.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/dashboard', methods=["GET"])
def dashboard():
    return render_template('dashboard.html')
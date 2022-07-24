from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask()
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "acdc6c33b12bec322f9c269a5234d187"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///DB.sqlite3"





from project import app
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    first_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    password = db.Column(db.String(150))
db.create_all()

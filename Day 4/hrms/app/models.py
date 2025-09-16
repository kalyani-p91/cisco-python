from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)  # <-- PRIMARY KEY
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)
    is_active = db.Column(db.Boolean)
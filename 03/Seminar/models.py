from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()


class Fakultet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}'


class Gender(enum.Enum):
    male = 'male'
    female = 'femail'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Enum(Gender))
    group = db.Column(db.String(80))
    id_faculteta = db.Column(db.Integer, db.ForeignKey('fakultet.id'), nullable=False)

    def __repr__(self):
        return f'{self.name} {self.last_name}'

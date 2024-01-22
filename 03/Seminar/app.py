from flask import Flask, render_template
from models import db, Student, Fakultet, Gender

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем факультеты
    # for fakultet in range(1, 4):
    #     new_facultet = Fakultet(name=f'факультет{fakultet}')
    #     db.session.add(new_facultet)
    # db.session.commit()
    for fakultet in Fakultet.query.all():
        for students in range(1, 4):
            new_student = Student(name=f'Иван{fakultet}{students}',
                                  last_name=f'Петров{fakultet}{students}',
                                  age=fakultet.id*3 + students*3,
                                  gender=Gender.male,
                                  group=f'{fakultet} {students}',
                                  id_faculteta=fakultet.id)
            db.session.add(new_student)
    db.session.commit()


if __name__ == '__main__':
    app.run()

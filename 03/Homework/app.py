from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
from models import db, User
from forms import RegistrationForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'f33391ec192db476746254dcd74d32c1c5f9da332183f0d26fb8176a92ce3694'
csrf = CSRFProtect(app)


@app.cli.command("check")
def check():
    user = User(username='Сергей',
                email='вфыафыа',
                password='ssa'
                )


@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate():
            user = User(user_name=form.username.data,
                email=form.email.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            flash(f'Пользователь {form.username.data} создан!', 'success')
            return redirect(url_for('index'))
        flash('что-то не правильно', 'danger')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()

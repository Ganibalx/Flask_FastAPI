from flask import Flask, render_template, request, flash, redirect, url_for



app = Flask(__name__)
app.config['SECRET_KEY'] = 'f33391ec192db476746254dcd74d32c1c5f9da332183f0d26fb8176a92ce3694'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('index'))  # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

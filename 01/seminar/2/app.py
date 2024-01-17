from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Это индекс'


@app.route('/about')
def about():
    return 'Это страница эбоут'


@app.route('/contact')
def contact():
    return 'Это страница контактов'


@app.route('/func/<int:a>/<int:b>/')
def func(a, b):
    return f'Ваша сумма {a + b}'


@app.route('/string/<my_str>/')
def string_length(my_str):
    return f'Длина строки - {len(my_str)}'


students = (
    {'name': 'Иван', 'fam': 'Иванов', 'age': 10, 'score': 4.5},
    {'name': 'Иван2', 'fam': 'Иванов2', 'age': 11, 'score': 4.2},
    {'name': 'Иван3', 'fam': 'Иванов3', 'age': 12, 'score': 3.8},
)


@app.route('/index/')
def index2():
    context = students
    return render_template('index.html', context=context)


@app.route('/news/')
def news():
    context = [
        {'title': 'Новость1', 'content': 'Описание новости', 'data': '10.03.2022'},
        {'title': 'Новость2', 'content': 'Описание новости тут побольше', 'data': '11.12.2023'},
        {'title': 'Новость3', 'content': 'Описание новости это третья новость', 'data': '12.12.2023'}
    ]
    return render_template('news.html', context=context)


if __name__ == '__main__':
    app.run()

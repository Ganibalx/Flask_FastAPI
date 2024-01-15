from flask import Flask
from flask import render_template

app = Flask(__name__)

categoryes = (
    {'name': 'Куртки', 'href': 'kurtki'},
    {'name': 'Штаны', 'href': 'shtani'}
)


@app.route('/')
def index():
    context = {
        'title': 'Это главная страница'
    }
    return render_template('index.html', **context, category=categoryes)


@app.route('/about')
def about():
    context = {
        'title': 'О нас'
    }
    return render_template('about.html', **context, category=categoryes)


@app.route('/contact')
def contact():
    context = {
        'title': 'Контакты'
    }
    return render_template('contact.html', **context, category=categoryes)


@app.route('/cat/<cat_name>')
def category(cat_name):
    for cat in categoryes:
        print(cat)
        if cat['href'] == cat_name:
            context = {
                'title': f'страница {cat["name"]}',
                'categor': cat['name']
            }
    return render_template('caterory.html', **context, category=categoryes)


if __name__ == '__main__':
    app.run()
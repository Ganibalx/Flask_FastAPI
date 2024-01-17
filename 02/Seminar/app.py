from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/page')
def page():
    return render_template('page.html')


@app.post('/page')
def upload():
    f = request.files['file']
    print(f)
    return 'Файл загружен'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == 'admin' and password == 'pass':
            return redirect(url_for('index'))
        else:
            return 'ты кто'
    return render_template('login.html')


@app.route('/counter', methods=['GET', 'POST'])
def counter():
    if request.method == 'POST':
        text = request.form.get('text')
        count = len(text.split())
        return render_template('result.html', count=count)
    return render_template('counter.html')


if __name__ == '__main__':
    app.run()

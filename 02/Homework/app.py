from flask import Flask, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        o = request.form.get('oper')
        match o:
            case '+':
                result = a+b
            case '-':
                result = a-b
            case '*':
                result = a*b
            case '/':
                result = a/b
        return render_template('calc.html', result=result)
    return render_template('calc.html')


@app.route('/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if age > 0 and age<120:
            return render_template('age.html', name=name, age=age)
        return render_template('age.html', fail=1)
    return render_template('age.html')

if __name__ == "__main__":
    app.run()

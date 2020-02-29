from flask import Flask

app = Flask(__name__)
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', otto=name)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/')
@app.route('/')
def predict():
    return render_template('predict.html')

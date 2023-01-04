from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
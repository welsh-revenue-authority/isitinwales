from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<uprn>')
def result(uprn=None):
    return render_template('result.html')


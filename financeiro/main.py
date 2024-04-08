from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/financeiro'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/entrar')
def entrar():
    return render_template('Entrar.html')

@app.route('/principal')
def principal():
    return render_template('principal.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)


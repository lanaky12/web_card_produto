from datetime import datetime
from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, and_, func

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/produtos')
def produtos():
    return render_template("produtos.html")
@app.route('/produtos')
def listar_produtos(): #Esse DEF precisa ser um VERBO
    produtos = api_endpoints.get_produtos()
    for produto in produtos:
        produto["image"] = api_endpoints.get_image()
    return render_template('produtos.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
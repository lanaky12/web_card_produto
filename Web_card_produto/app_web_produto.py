from flask import Flask, render_template, url_for, flash, request, redirect
import asyncio
from api_endpoints import get_produtos

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/produtos')
def produtos():
    return render_template("produtos.html")

if __name__ == '__main__':
    app.run(debug=True)

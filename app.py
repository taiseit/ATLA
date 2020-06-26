from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from random import randint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ATLA.db'
db = SQLAlchemy(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['POST', 'GET'])
def main_page():
    random_int = randint(1, 54)
    if request.method == 'POST':
        quote = Quotes.query.filter_by(id = str(random_int)).first()
        return render_template('index.html', quote=quote)
    else:
       quote = Quotes.query.filter_by(id = '5').first()
       return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
    

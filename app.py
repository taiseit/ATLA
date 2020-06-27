from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ATLA.db'
db = SQLAlchemy(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)

# @app.route('/', methods=['POST', 'GET'])
# def main_page():
#     count = Quotes.query.count()
#     random_int = randint(1, count)
#     if request.method == 'POST':
#         quote = Quotes.query.filter_by(id = str(random_int)).first()
#         return render_template('index.html', quote=quote, count=count)
#     else:
#        quote = Quotes.query.filter_by(id = '1').first()
#        return render_template('index.html', quote=quote)

@app.route('/', methods=['POST', 'GET'])
def main_page():
    index = 0
    count = Quotes.query.count()
    scramble_index = random.sample(range(1, count + 1), count)
    def helper():
        nonlocal index
        if request.method == 'POST':
            index += 1
            id = str(scramble_index[index])
            quote = Quotes.query.filter_by(id = id).first()
            return render_template('index.html', quote=quote)
        else:     
            quote = Quotes.query.filter_by(id = '1').first()
            return render_template('index.html', quote=quote)
    return helper()

condition = 0
index = 0
count = 10
scramble_index = random.sample(range(1, count + 1), count)
@app.route('/test')
def test():
    def helper():
        global index
        if abs(index) > len(scramble_index) - 2:
            index = 0
            print(index)
        # next button 
        elif condition:
            index += 1
            print(index)
        # previous button
        else:
            index -= 1
            print(index)
        x = scramble_index[index]
        return render_template('test.html', x=x)
    return helper()

if __name__ == '__main__':
    app.run(debug=True)


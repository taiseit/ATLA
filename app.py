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

array_index = 0
count = 10 # Quotes.query.count()
scramble_index = random.sample(range(1, count + 1), count)
@app.route('/', methods=['POST', 'GET'])
def main_page():
    def helper():
        global array_index
        # reset index 
        if abs(array_index) > len(scramble_index) - 3:
            array_index = 0
        # next button 
        # requires a way to detect the right button is clicked
        elif request.method == 'POST':
            array_index += 1
        # previous button
        # requires a way to detect the left button is clicked 
        else:
            array_index -= 1
        quote_index = str(scramble_index[array_index])
        quote = Quotes.query.filter_by(id = quote_index).first()
        return render_template('index.html', quote=quote)
    return helper()

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ATLA.db'
db = SQLAlchemy(app)

class Quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET'])
def main_page():
    names = Quotes.query.first()
    return render_template('index.html', names=names)

if __name__ == '__main__':
    app.run(debug=True)
    

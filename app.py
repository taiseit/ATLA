from flask import Flask, render_template, url_for, g
import sqlite3
app = Flask(__name__)

DATABASE = 'database.db'

@app.route('/')
def main_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    

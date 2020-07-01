import sqlite3
import pandas as pd

conn = sqlite3.connect('ATLA.db')
c = conn.cursor()

def create_table():
    """Creates a table containing author and text columns if it doesn't already exist."""
    
    c.execute("""CREATE TABLE IF NOT EXISTS quotes (
        author TEXT, 
        text TEXT
    )
    """)

def import_data():
    """Imports ../data/ATLA_quotes.csv into the quotes table if the table is empty, else return print statement."""
    
    c.execute('SELECT * FROM quotes')
    num_rows = len(c.fetchall())
    path = '../data/ATLA_quotes.csv'
    if num_rows == 0: 
        quotes = pd.read_csv(path)
        quotes = quotes[['author', 'text']]
        quotes.to_sql('quotes', conn, if_exists='append', index=False)
    else:
        print('Table already contains data!')

create_table()
import_data()
conn.commit()
conn.close()
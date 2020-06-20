import sqlite3
import pandas as pd

conn = sqlite3.connect('ATLA.db')
c = conn.cursor()

def create_table():
    """Creates a table containing author and text columns."""
    
    c.execute("""CREATE TABLE IF NOT EXISTS quotes (
        index integer,
        author text, 
        text text
    )
    """)

def import_data():
    """Import data/ATLA_quotes.csv into ATLA.db."""

    quotes = pd.read_csv('data/ATLA_quotes.csv')
    quotes.to_sql('quotes', conn, if_exists='append', index=False)

create_table()
import_data()
conn.commit()
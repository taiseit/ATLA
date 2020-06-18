import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("ATLA.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS quotes (
        quote text, 
        character_name text
    )
    """)

def insert_data():
    c.execute_many()

create_table()
conn.commit()
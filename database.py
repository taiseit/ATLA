# import sqlite3
# from sqlite3 import Error

# def create_connection(db):
#     """ create a db connection to SQLite db """
#     conn = None
#     try:
#         conn = sqlite3.connect(db)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()

# if __name__=='main':
#     create_connection(r"pythonsqlite.db")
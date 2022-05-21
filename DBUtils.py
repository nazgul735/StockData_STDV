import sqlite3 as sql

class DBUtils:

    dbQuery = [
        """CREATE TABLE IF NOT EXISTS "Portfolio" ( 
        TICKER  TEXT PRIMARY KEY,
        STDV TEXT NOT NULL,
        MEAN  TEXT NOT NULL,
        STDVMEANRATE  TEXT NOT NULL);"""
        ]

    def create_connection():
            cur = None
            try:
                conn = sql.connect('portfolio.db')
                cur = conn.cursor()
                return cur
            except sql.Error as e:
                print(e)

            return cur
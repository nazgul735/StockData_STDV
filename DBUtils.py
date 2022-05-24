import sqlite3 as sql

class DBUtils:

    dbQuery = [
        """CREATE TABLE IF NOT EXISTS "Portfolio" ( 
        ticker  TEXT PRIMARY KEY,
        stdv TEXT NOT NULL,
        mean  TEXT NOT NULL,
        stdvMeanRate  TEXT NOT NULL,
        period TEXT NOT NULL);"""  
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
    
    def initialiseDB(cursor):
        for table in dbQuery:
            cursor.execute(table)
    
    def setRating(cursor, ticker: str, stdv: str, mean: str, stdvMeanRate: str, period: str):
        ticker = input("ID: ")
        stdv = input("Email: ")
        mean = input("CoffeeID: ")
        stdvMeanRate: input("Note: ")
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)", [
            ticker, stdv, mean, stdvMeanRate])
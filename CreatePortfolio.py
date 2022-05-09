import pandas as pd
import yfinance as yf

class CreatePortfolio:
    def readCsv():
        df = pd.read_csv('data.csv')
        print(df.to_string()) 

    def addTicker(list):
        portfolio=[]
        for ticker in list:
            portfolio.append(ticker.upper())
        return portfolio
    
    def dwnLdTicker():
        msft = yf.Ticker("MSFT")
    
    



        

            
 




        
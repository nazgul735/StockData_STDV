import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

class CreatePortfolio:
    def addTicker(list):
        portfolio=[]
        for ticker in list:
            portfolio.append(ticker.upper())
        return portfolio

    def get_closing_prices(period, list):
        allPrices={}
        portfolio=CreatePortfolio.addTicker(list)
        try:
            for tckr in portfolio:
                tempTicker = yf.Ticker(tckr)
                tempData = tempTicker.history(period)
                tempClosingPrice= tempData["Close"]
                allPrices[tckr]=[round(val, 2) for val in tempClosingPrice.tolist()]
            return allPrices
        except Exception as e:
            print("Failed to get required data.", e)        
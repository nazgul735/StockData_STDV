from traceback import print_tb
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

class CreatePortfolio:
    def get_closing_prices(portfolio, period):
        allPrices={}
        try:
            for tckr in portfolio:
                tckr=tckr.upper()
                tempTicker = yf.Ticker(tckr)
                tempData = tempTicker.history(period)
                tempClosingPrice= tempData["Close"]
                allPrices[tckr]=[round(val, 2) for val in tempClosingPrice.tolist()]
            return allPrices
        except Exception as e:
            print("Failed to get required data.", e)       


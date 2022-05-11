from CreatePortfolio import CreatePortfolio
import pandas as pd
import yfinance as yf


class CalcValues:
    def getPortfolio(period, list):
        portfolio=CreatePortfolio.get_closing_prices(period, list)
        return portfolio
    
    def standardDeviation(period, list):
        portfolio = CalcValues.getPortfolio(period, list)
        standardDeviatedDict={}
        try:
            for key in portfolio.keys():
                serie=pd.Series(portfolio.get(key))
                standardDeviatedDict[key]=serie.std()
            return standardDeviatedDict
        except Exception as e:
            print("Failed to calculate standard deviation", e)
    
    def mean(period, list):
        portfolio = CalcValues.getPortfolio(period, list)
        df = pd.DataFrame(portfolio)
        meanDictionary={}
        try:
            for ticker in df:
                meanDictionary[ticker]=round(df[ticker].mean(), 2)
            return meanDictionary
        except Exception as e:
            print("Failed to calculate mean", e)
    
    def currentPrice(portfolio):
        currentPriceDict={}
        for ticker in portfolio:
            ticker = yf.Ticker(ticker)
            todays_data = ticker.history(period="0")
            currentPriceDict[ticker]=round(todays_data['Close'][0],2)
        return currentPriceDict

o=CalcValues
period="1mo"
l={'BABA': [101.55, 99.75, 100.03, 95.49, 94.71, 93.5, 89.41, 85.99, 86.49, 85.84, 83.99, 88.32, 90.91, 97.09, 101.21, 100.38, 101.41, 94.64, 90.05, 84.84, 84.57], 'FB': [216.46, 214.14, 214.99, 210.18, 210.77, 217.31, 200.42, 188.07, 184.11, 186.99, 180.95, 174.95, 205.73, 200.47, 211.13, 212.03, 223.41, 208.28, 203.77, 196.21, 197.65]}
list=["baba", "fb"]

print(o.currentPrice(list))
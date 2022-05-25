from CalcValues import CalcValues as value
from CreatePortfolio import CreatePortfolio as cp
import pandas as pd

class Commands: 
    portfolio=None
    period=""
    def addTickers():
        global portfolio
        global period
        list=[]
        stop=False
        while not stop:
            list.append(input("Ticker: "))
            state=input("More tickers?(y/n): ")
            if state=="n" or state=="no":
                stop=True    
        period=input("Period frame (d, mo, y): ")
        portfolio=cp.createPortfolio(list, period)

    def getStdv():
        global portfolio
        df=pd.DataFrame(list(value.standardDeviation(portfolio).items()),columns=["Ticker", "STDV"])
        print(df)
        # print(value.standardDeviation(portfolio))

    def getMeanPrice():
        global portfolio
        df=pd.DataFrame(list(value.averagePrice(portfolio).items()),columns=["Ticker", "Mean"])
        print(df)
        # print(value.averagePrice(portfolio))

    def getCurrentPrice():
        global portfolio
        df=pd.DataFrame(list(value.currentPrice(portfolio).items()),columns=["Ticker", "Price"])
        print(df)
        # print(value.currentPrice(portfolio))
    
    def getPriceToMean():
        global portfolio
        df=pd.DataFrame(list(value.priceToMean(portfolio).items()),columns=["Ticker", "Price/Mean"])
        print(df)
        # print(value.priceToMean(portfolio))

    def getStdvToPriceRatio():
        global portfolio
        df=pd.DataFrame(list(value.standardDeviationPriceRatio(portfolio).items()),columns=["Ticker", "STDV/P"])
        print(df)
        # print(value.standardDeviationPriceRatio(portfolio))
    
    def help():
        print("type '1' for current closing price")
        print("type '2' for mean price")
        print("type '3' for standard deviation")
        print("type '4' for price/mean relation")
        print("type '5' for how many stdv relative to mean")




    



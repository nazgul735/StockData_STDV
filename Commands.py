from CalcValues import CalcValues as value
from CreatePortfolio import CreatePortfolio as cp


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
        print(value.standardDeviation(portfolio))

    def getMeanPrice():
        global portfolio
        print(value.averagePrice(portfolio))

    def getCurrentPrice():
        global portfolio
        print(value.currentPrice(portfolio))
    
    def getPriceToMean():
        global portfolio
        print(value.priceToMean(portfolio))

    def getStdvToPriceRatio():
        global portfolio
        print(value.standardDeviationPriceRatio(portfolio))




    


# o=Commands
# o.addTickers()
# o.getStdv()
# o.getMeanPrice()
# o.getCurrentPrice()
# o.getPriceToMean()
# o.getStdvToMeanRatio()

import pandas as pd
import yfinance as yf
from CreatePortfolio import CreatePortfolio as c
 
class CalcValues:
    meanPriceDict=None
    currentPriceDict=None
    standardDeviationDict=None

    def standardDeviation(portfolio):
        global standardDeviationDict
        standardDeviation={}
        try:
            for key in portfolio.keys():
                serie=pd.Series(portfolio.get(key))
                standardDeviation[key]=serie.std()
        except Exception as e:
            print("Failed to calculate standard deviation", e)
        finally:
            standardDeviationDict=standardDeviation
        return standardDeviation
    
    def averagePrice(portfolio): 
        global meanPriceDict 
        meanPrice={}  
        df = pd.DataFrame(portfolio)
        try:
            for ticker in df:
                meanPrice[ticker]=df[ticker].mean()
        except Exception as e:
            print("Failed to calculate mean", e)
        finally:
            meanPriceDict=meanPrice 
        return meanPrice

    def currentPrice(portfolio):
        global currentPriceDict
        currentPrice={}
        try:
            for ticker in portfolio.keys():
                tempTicker = yf.Ticker(ticker)
                todays_data = tempTicker.history(period="0")
                currentPrice[ticker]=float(todays_data['Close'][0])
        except Exception as e:
            print("Failed to find current price", e)
        finally:
            currentPriceDict=currentPrice
        return currentPrice
    
    def priceToMean(portfolio):
        global meanPriceDict
        global currentPriceDict
        currentPrice=CalcValues.currentPrice(portfolio)
        priceToMeanDict={}
        for ticker in portfolio.keys():
            try:
                priceToMeanDict[ticker]=currentPrice[ticker]-meanPriceDict[ticker]
            except Exception as e:
                print("Failed to calculate the spead", e)
        return priceToMeanDict

    def standardDeviationPriceRatio(portfolio):
        global standardDeviationDict
        currentPrice=CalcValues.currentPrice(portfolio)
        mean=CalcValues.averagePrice(portfolio)
        meanStdvRatio={}
        try:
            for ticker in portfolio.keys():
                meanStdvRatio[ticker]=(currentPrice[ticker]-mean[ticker])/standardDeviationDict[ticker]
        except Exception as e:
            print("Failed to calculate ratio", e)
        return meanStdvRatio



    





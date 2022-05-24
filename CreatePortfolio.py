import yfinance as yf

class CreatePortfolio:
    def createPortfolio(portfolio, period):
        finalPortfolio={}
        for tckr in portfolio:
            tckr=tckr.upper()
            try:
                tempTicker = yf.Ticker(tckr)
                tempData = tempTicker.history(period)
                tempClosingPrice= tempData["Close"]
                finalPortfolio[tckr]=[round(val, 2) for val in tempClosingPrice.tolist()]
            except:
                print(f"Couldn't find data for {tckr}")
                continue 
        return finalPortfolio



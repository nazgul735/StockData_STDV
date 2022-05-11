import CreatePortfolio

class Commands: 
    def noMoreTickers(list, period):
        CreatePortfolio.get_closing_prices(list, period)

o=Commands
o.tickerAppending()


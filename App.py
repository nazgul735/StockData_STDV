from Commands import Commands as cmd
print("Add tickers")
cmd.addTickers()
print("To see the menu, press help (h)")
while (ui := input("> ").lower()) != "q":
    cmd.getStdv() if (ui == ("stdv")) else next
    cmd.getMeanPrice() if (ui == ("mean")) else next
    cmd.getCurrentPrice() if (ui == ("currprc")) else next
    cmd.getPriceToMean() if (ui == ("p/m")) else next
    cmd.getStdvToPriceRatio() if (ui == ("Stdv/Mean")) else next





    
    




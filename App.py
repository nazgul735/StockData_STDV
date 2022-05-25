from Commands import Commands as cmd
from pyfiglet import Figlet


f = Figlet(font="slant")
print(f.renderText("Quantalyst"))

    
print("Add tickers")
cmd.addTickers()
print("To see the menu, press help (h)")
while (ui := input("> ").lower()) != "q":
    cmd.help() if (ui == ("help")) or (ui==("h")) else next
    cmd.getStdv() if (ui == ("3")) else next
    cmd.getMeanPrice() if (ui == ("2")) else next
    cmd.getCurrentPrice() if (ui == ("1")) else next
    cmd.getPriceToMean() if (ui == ("4")) else next
    cmd.getStdvToPriceRatio() if (ui == ("5")) else next


print("")
print("Goodbye!")



    
    




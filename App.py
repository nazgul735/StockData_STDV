import pandas as pd
import matplotlib.pyplot as plt
from Commands import Commands
while (ui := input("> ").lower()) != "q":
    while (ui := input("> ").lower()) != "n":
        print("Would you like to add another ticker?: ", end=" ")
        if ui=="y":
            Commands.tickerAppending()
        else:
            print("Please answer yes (y) or no (n)")




    
    




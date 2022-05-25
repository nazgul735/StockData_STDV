import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf

def makeDistribution(portfolio):
    df = get_historical_data("DIS", start, end, output_format='pandas')
    plt.figure(figsize=(10,10))
    plt.plot(df.index, df['close'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title("DIS Stock Price 1/1/17 - 8/1/19")
    return None


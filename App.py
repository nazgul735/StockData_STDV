import pandas as pd
import matplotlib.pyplot as plt

portfolio=[]
while (ui := input("> ").lower()) != "n":
    ticker=input("Tickers: ")
    portfolio.append(ticker)

def get_dataframe_from_csv(filename):
    df = pd.read_csv(filename)
    return df


stock = "BABA"
df = get_dataframe_from_csv('{}.csv'.format(stock))

data = df['Close']
mean = df['Close'].mean()
std = df['Close'].std()
min_value = min(data)
max_value = max(data)

plt.title("BABA Dataset")
plt.ylim(min_value - 100, max_value + 100)
plt.scatter(x=df.index, y=df['Close'])
plt.hlines(y=mean, xmin=0, xmax=len(data))
plt.show()

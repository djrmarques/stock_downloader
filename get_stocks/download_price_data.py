import yfinance

with open("tickers.txt", "r") as f:
    tickers =  f.readlines()[0].split(";")


tickers
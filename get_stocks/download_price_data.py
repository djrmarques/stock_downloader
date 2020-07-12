import yfinance as yf
import os
from itertools import cycle
from tqdm import tqdm
from numpy.random import uniform  
from shutil import rmtree
import pandas as pd
from random import choice

tickers_file = "tickers.txt"
proxies_file = "proxies.txt"

with open(tickers_file, "r") as f:
    tickers =  f.readlines()[0].split(";")

with open(proxies_file, "r") as f:
    proxies = [f"http://{l.strip()}" for l in f.readlines()]

output_folder = "stock_data"
if  os.path.exists(output_folder):
    rmtree(output_folder)
os.makedirs(output_folder)
 

for ticker in tqdm(tickers):
    print(ticker)
    tic = yf.Ticker(ticker)
    try:
        data = tic.history(period="max", proxy="http://34.91.135.38:80")
        data.to_csv(os.path.join(output_folder, ticker + ".csv"))
        sucess=True
    except Exception as error:
        print(error)


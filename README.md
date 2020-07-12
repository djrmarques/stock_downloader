# stock_downloader
Downloads tickers and historic stock price data using yahoo finance

# USAGE

First get the tickers. Use the yahoo finance screener to create tables with tickers, and then copy that url. 

USe the GetTickers object to create a textfile "tickers.txt", that contains the stock tickers. 
```python

from get_stocks.get_tickers import GetTickers

url = "https://finance.yahoo.com/screener/unsaved/c97bc7b4-0e94-43dc-9df1-b46f936742e6?count=100&offset=0"
GetTickers(url).get_tickers()
```

Then, just run the the download_price_data.py script to downloads the historical data. This will create a folder with the dataframes of the historical data.

# TODO

- [ ] Turn this into a proper package
- [ ] Put package on pipy

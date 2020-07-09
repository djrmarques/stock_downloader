import logging
import re
from time import sleep

from numpy.random import uniform
import pandas as pd 


class GetTickers:

    def __init__(self, url: str):
        assert re.match(r"https://finance.yahoo.com/screener/\w+count=\d+&offset=\d+", url), "Please insert a url similar to https://finance.yahoo.com/screener/unsaved/c97bc7b4-0e94-43dc-9df1-b46f936742e6?count=25&offset=0"

        self.sleep_between_requests = 5  # Time betwee downloads in seconds
        self.url = url
        self.tickers_list = []  # This will be the list of the tickers
        self.lim_pages = 5

    def get_tickers(self):

        for offset in range(25, int(10e6), 25):
            print(f"Now with offset {offset}")
            try:
                url = re.sub(r"offset=\d+", f"offset={offset}", self.url)
                ticker_df = pd.read_html(url)[0]  # We take the index zero because it's the only table in the page
                self.tickers_list += ticker_df["Symbol"].tolist()
            except:
                print(f"Stopped at offset {offset}.")
            return self.tickers_list

            sleep(self.tickers_list * uniform(0.9, 1.5, 1))




if __name__ == "__main__":
    url = "https://finance.yahoo.com/screener/unsaved/c97bc7b4-0e94-43dc-9df1-b46f936742e6?count=25&offset=0"
    tickers_df = GetTickers(url).get_tickers()
import yfinance as yf
import streamlit as st
import pandas as pd
from get_all_tickers import get_tickers as gt
import numpy as np
from collections import defaultdict
# get tickers symbols
with open("symbol.txt", "r") as f:
    # all tickers
    tickerList = f.read().split(',')
    st.write(f"""# stocks prices
    Closing data for all stocks prices
    """)
    prices = []
    for ticker in tickerList:
        tickerData = yf.Ticker(ticker)
        #np.append(prices, tickerData.history().Close[-1])
        try:
            price = tickerData.history().Close[-1]
            st.write(f"""
            {ticker}: {price}
            """)
        except Exception:
            continue
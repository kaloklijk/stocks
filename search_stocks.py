import numpy as np
import streamlit as st
import yfinance as yf
import pandas as pd
from collections import defaultdict
st.write("""
# stocks
""")
with open("symbol.txt", "r") as f:
    tickers = f.read().split(",")
    selects = st.multiselect("stocks symbols", tickers)
    startdate = defaultdict()
    enddate = defaultdict()
    for ticker in selects:
        st.write(f"""
        # {ticker}
        """)
        try:
            startdate[ticker] = st.date_input("start")
            enddate[ticker] = st.date_input("end")
        except Exception:
            pass
        ticker_price = yf.Ticker(ticker).history(period="1d", start=startdate, end=enddate).Close
        ticker_analysis = yf.download(ticker, start=startdate, end=enddate)

        st.write(f"""
        ## Recent Close Price: {ticker_price[-1]}

        """)
        st.line_chart(ticker_price)
        st.write(f"""
        ## stocks prices info: 
        
        """)
        st.table(ticker_analysis)
  
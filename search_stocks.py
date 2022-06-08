import numpy as np
import streamlit as st
import yfinance as yf
import pandas as pd
from collections import defaultdict
import datetime
with open('style.css', "r") as stylesheet:
    st.markdown(f'<style>{stylesheet.read()}</style>', unsafe_allow_html=True)
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
        startdate[ticker] = st.date_input(f"{ticker} start", value=datetime.date(2022, 6, 3))
        enddate[ticker] = st.date_input(f"{ticker} end", value=datetime.date(2022, 6, 8))
        ticker_price = yf.Ticker(ticker).history(period="1d", start=startdate[ticker], end=enddate[ticker]).Close
        ticker_analysis = yf.download(ticker, start=startdate[ticker], end=enddate[ticker])

        st.write(f"""
        ## Recent Close Price: {ticker_price[-1]}

        """)
        st.line_chart(ticker_price)
        st.write(f"""
        ## stocks prices info: 
        
        """)
        st.table(ticker_analysis)
  
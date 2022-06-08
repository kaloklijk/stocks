import numpy as np
import streamlit as st
import yfinance as yf

st.write("""
# stocks basic information

""")
with open("symbol.txt", "r") as f:
    tickers = f.read().split(",")
    selects = st.multiselect("stocks symbols", tickers)
    for ticker in selects:
        ticker_price = yf.Ticker(ticker).history(period="1d", start='2018-1-1').Close
        ticker_analysis = yf.Ticker(ticker).analysis
        ticker_info = yf.Ticker(ticker).info
        st.write(f"""
        # {ticker}
        """)
        st.write(f"""
        ## Recent Close Price: {ticker_price[-1]}
        ## stocks analysis: 
        {ticker_analysis}
        """)
        st.line_chart(ticker_price)
import numpy as np
import streamlit as st
import yfinance as yf
import pandas as pd
st.write("""
# stocks
""")
with open("symbol.txt", "r") as f:
    tickers = f.read().split(",")
    selects = st.multiselect("stocks symbols", tickers)
    for ticker in selects:
        st.write(f"""
        # {ticker}
        """)
        startdate = st.date_input("start")
        enddate = st.date_input("end")
        ticker_price = yf.Ticker(ticker).history(period="1d", start=startdate, end=enddate).Close
        ticker_analysis = yf.download(ticker, start=startdate, end=enddate)

        st.write(f"""
        ## Recent Close Price: {ticker_price[-1]}

        """)
        st.line_chart(ticker_price)
        st.write(f"""
        ## stocks analysis: 
        
        """)
        st.table(ticker_analysis)
  
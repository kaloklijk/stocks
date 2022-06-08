import yfinance as yf
import tensorflow as tf
import pandas as pd
import numpy as np



if __name__ == '__main__':
    with open('symbol.txt', 'r') as f:
        ticker = f.read().split(',')
        df = pd.DataFrame(yf.download(ticker, start='2022-05-01'))
        print(df.columns)

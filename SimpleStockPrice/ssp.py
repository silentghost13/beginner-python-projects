import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **open price**, **closing price** and **volume** of Microsoft Corporation
         
""")

#https://github.com/dataprofessor/streamlit_freecodecamp/blob/main/app_1_simple_stock_price/myapp.py
#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define ticker symbol
tickerSymbol = 'MSFT'
#get data from this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2011-8-31', end='2021-8-31')
#Column : Open High Low Close Volume Dividends Stock_Price

st.write("""
## Open price
""")
st.line_chart(tickerDf.Open)
st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

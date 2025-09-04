import streamlit as st
import yfinance as yf

st.title("Stock Price Analyzer")
title = st.text_input("Which Stock Price you want to analyze", "MSFT")
#st.write("The current ticker is", title)
ticker_data = yf.Ticker(title)
ticker_df = ticker_data.history(start="2023-12-1",end="2025-07-01")
#ticker_df = ticker_data.history(period="3y")
st.write(ticker_df)
st.subheader("Raw day wise closing stock price")
st.line_chart(ticker_df.Close)
st.subheader("Raw day wise volume over time")
st.line_chart(ticker_df.Volume)
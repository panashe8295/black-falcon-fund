# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:20:27 2025

@author: Tanaka
"""

import yfinance as yf
import streamlit as st
import pandas as pd

st.title("📈 Investment Tracker")

# User inputs
tickers = st.text_input("Enter stock tickers (comma-separated):", "AAPL,MSFT,GOOG")
tickers = [t.strip().upper() for t in tickers.split(",")]

# Download stock data safely
try:
    data = yf.download(tickers, period="6mo", auto_adjust=True)

    if data.empty:
        st.error("⚠️ No data was downloaded. Please check your ticker symbols or internet connection.")
    else:
        # Handle missing 'Adj Close'
        if "Adj Close" in data:
            prices = data["Adj Close"]
        elif "Close" in data:
            prices = data["Close"]
        else:
            st.error("⚠️ Neither 'Adj Close' nor 'Close' data available.")
            prices = pd.DataFrame()

        if not prices.empty:
            st.subheader("Stock Prices (last 6 months)")
            st.line_chart(prices)

except Exception as e:
    st.error(f"❌ An error occurred while fetching data: {e}")

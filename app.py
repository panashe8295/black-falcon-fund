# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:20:27 2025

@author: Tanaka
"""
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# Title
st.title("Bar Chart")

# Define tickers
tickers = ["JPM", "AAPL", "GOOG", "NVDA"]

# Fetch latest prices from Yahoo Finance
prices = yf.download(tickers, period="1d")["Close"].iloc[-1]

# Slider inputs
jpm = st.slider("JPM", 0, 1000, 250)
aapl = st.slider("AAPL", 0, 1000, 250)
goog = st.slider("GOOG", 0, 1000, 250)
nvda = st.slider("NVDA", 0, 1000, 250)

# Create DataFrame
df = pd.DataFrame({
    "Stock": ["JPM", "AAPL", "GOOG", "NVDA"],
    "Investment ($)": [jpm, aapl, goog, nvda],
    "Price ($)": [prices["JPM"], prices["AAPL"], prices["GOOG"], prices["NVDA"]]
})

# Calculate portfolio percentages
total = df["Investment ($)"].sum()
if total > 0:
    df["Portfolio (%)"] = (df["Investment ($)"] / total) * 100
else:
    df["Portfolio (%)"] = 0

# --- Create Plotly bar chart with 0–100% y-axis ---
fig = px.bar(
    df,
    x="Stock",
    y="Portfolio (%)",
    text=df["Portfolio (%)"].map(lambda x: f"{x:.1f}%"),
    range_y=[0, 100],
    color="Stock",
    color_discrete_sequence=px.colors.qualitative.Set2,
title="Allocation Breakdown (%)"# ✅ Chart title added
)

fig.update_traces(textposition="outside")
fig.update_layout(
    yaxis_title="Percentage of Portfolio (%)",
    xaxis_title="Stock",
    yaxis=dict(tickformat=".0f"),
    template="simple_white",
    title_font=dict(size=20, family="Arial Black", color="#2E86C1"),  # ✅ Cool title style
    title_x=0.5
)

# Display chart
st.plotly_chart(fig, use_container_width=True)

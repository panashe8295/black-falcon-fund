# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:20:27 2025

@author: Tanaka
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("🧮 Valuation Model (DCF)")

revenue = st.number_input("Current Revenue ($M)", 0.0, 10000.0, 500.0)
growth = st.slider("Growth Rate (%)", 0.0, 30.0, 10.0)
discount = st.slider("Discount Rate (%)", 0.0, 20.0, 8.0)
margin = st.slider("Profit Margin (%)", 0.0, 50.0, 20.0)
years = st.slider("Projection Period (Years)", 1, 10, 5)

cashflows = []
for i in range(1, years + 1):
    cf = revenue * (1 + growth / 100) ** i * (margin / 100)
    discounted_cf = cf / ((1 + discount / 100) ** i)
    cashflows.append(discounted_cf)

value = sum(cashflows)
st.metric("Enterprise Value ($M)", f"{value:,.2f}")

fig, ax = plt.subplots()
ax.plot(range(1, years + 1), cashflows, marker='o')
ax.set_xlabel("Year")
ax.set_ylabel("Discounted Cash Flow ($M)")
st.pyplot(fig)



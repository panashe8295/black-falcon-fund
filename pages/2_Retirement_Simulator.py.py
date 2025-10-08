# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:20:27 2025

@author: Tanaka
"""

import streamlit as st
import numpy as np

st.title("💰 Retirement Simulator")

age = st.slider("Current Age", 18, 70, 30)
ret_age = st.slider("Retirement Age", age, 80, 60)
monthly_contrib = st.number_input("Monthly Contribution ($)", 100, 10000, 500)
annual_return = st.slider("Expected Annual Return (%)", 0.0, 15.0, 7.0)
years = ret_age - age

future_value = 0
monthly_rate = (annual_return / 100) / 12
months = years * 12
for _ in range(months):
    future_value = (future_value + monthly_contrib) * (1 + monthly_rate)

st.metric("Projected Retirement Fund", f"${future_value:,.2f}")


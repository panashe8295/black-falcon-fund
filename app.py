# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 15:20:27 2025

@author: Tanaka
"""
import streamlit as st

st.set_page_config(page_title="Black Falcon Finance Suite", page_icon="🦅")

st.title("🦅 Black Falcon Finance Suite")
st.markdown("""
Welcome!  
This application includes three modules:

1. **Investment Tracker** – Track live stock data and performance.  
2. **Retirement Simulator** – Run Monte Carlo simulations for future value.  
3. **Valuation Model** – Estimate firm value via DCF and sensitivity analysis.  

Use the **sidebar** on the left to navigate between modules.
""")

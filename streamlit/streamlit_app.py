# Welcome to the code for polymer solubilization analysis

import pandas as pd                       # pandas = package for excel
from pandas import ExcelWriter            # save to excel
import numpy as np                        # another package for number and excel analysis
from itertools import groupby
from datetime import datetime             # append current time to any output
from datetime import date    
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import interactive

import streamlit as st

# import pages
from singlePage import single
from multiplePage import multiple


with open('./streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Using object notation
method = st.sidebar.selectbox(
    "Method",
    ("Single", "Multiple")
)

if method == "Single":
    single()
elif method == "Multiple":
    multiple()
    
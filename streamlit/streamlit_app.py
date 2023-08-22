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
from homePage import home
from generalPage import general

from streamlit_option_menu import option_menu

# Apply custom CSS styling
# st.markdown(
#     """
#     <style>
#     .main {
#         background: grey;
#     }
    
#     .sub-title {
#         color: green;
#     }
#     .css-10trblm.e1nzilvr0 {
#         color: green;
#     }
    
#     .css-gggys9.eczjsme0 {
#         background: grey;
#     }
    
#     .css-18ni7ap.ezrtsby2 {
#         background: grey;
#     }
    
#     .block-container {
#         background: grey;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single Protein Search", "Multi-protein Network Analysis", "General Methods"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single Protein Search", "Multi-protein Network Analysis", "General Methods"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single Protein Search", "Multi-protein Network Analysis", "General Methods"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
        )
        return selected

    if example == 4:
        # 2. horizontal menu with custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single Protein Search", "Multi-protein Network Analysis", "General Methods"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
    )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    home()
if selected == "Single Protein Search":
    single()
if selected == "Multi-protein Network Analysis":
    multiple()
if selected == "General Methods":
    general()
    
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

from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single", "Multiple", "Calculations"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single", "Multiple", "Calculations"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single", "Multiple", "Calculations"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
        )
        return selected

    if example == 4:
        # 2. horizontal menu with custom style
        selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Single", "Multiple", "Calculations"],  # required
                icons=["house", "book", "book", "book"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
    )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Single":
    single()
if selected == "Multiple":
    multiple()
if selected == "Calculations":
    st.title(f"You have selected {selected}")
    
    


# with open('./streamlit/style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # Using object notation
# method = st.sidebar.selectbox(
#     label="Select a Method",
#     options=("Single", "Multiple"),
#     index=0,
#     key="method_select",
#     help="Choose a method",
#     label_visibility="hidden"  # Hide the label from view
# )
    
# if method == "Single":
#     single()
# elif method == "Multiple":
#     multiple()
    
import streamlit as st 
import pandas as pd                       # pandas = package for excel
from pandas import ExcelWriter            # save to excel
import numpy as np                        # another package for number and excel analysis
from itertools import groupby
from datetime import datetime             # append current time to any output
from datetime import date    
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import interactive

def single():
    
    normalized2_df = pd.read_csv('dataframes/normalized2_df.csv')
    normalizedto100_df = pd.read_csv('dataframes/normalizedto100_df.csv')
    sample_df = pd.read_csv('dataframes/sample_df.csv')
    ref_df = pd.read_csv('dataframes/ref_df.csv')
    sample_df_avg = pd.read_csv('dataframes/sample_df_avg.csv')
    sample_df_avg_sum = pd.read_csv('dataframes/sample_df_avg_sum.csv')
    normalized_df = pd.read_csv('dataframes/normalized_df.csv')

    with st.form("my_form"):
        st.write("Form Title")
        label_text = "<div class='custom-label'>What gene name would you like to search for? (Or enter 'done') to finish...</div>"
        st.markdown(label_text, unsafe_allow_html=True)

        gene_name = st.text_input("", "Search...", key=np.random.randint(1))

        # Every form must have a submit button.
        submitted = st.form_submit_button("Search")
        if submitted:
            if gene_name.lower() == "done":
                now = datetime.now()
                now = now.strftime("%H_%M_%S")
                today = date.today()
                filename = "Proteomics output" + str(today) + '_' + str(now) + ".xlsx" # Change to designated file path
                writer = pd.ExcelWriter(filename, engine='xlsxwriter')

                frames = {'Original data':sample_df,'Reference':ref_df,'Averages added':sample_df_avg,'Averages and sums':sample_df_avg_sum,'Simplified':normalized_df,'Normalized':normalized2_df,
                        'Relative percent sol':normalizedto100_df}

                for sheet, frame in  frames.items():                   # .use .items for python 3.X
                    frame.to_excel(writer, sheet_name = sheet)
                    
                writer.save()
                print('Done!')
            else:
                display_1 = normalized2_df[normalized2_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=0)
                display_3 = normalizedto100_df[normalizedto100_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=0)
                display_4 = [display_3]
                display_2 = normalized2_df[normalized2_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=1)
                display_22 = display_2.to_string()
                display_23 = display_22.split()
                display_2_value = display_23[-1]
                
                # Create the bar plot
                fig, ax = plt.subplots()
                display_3.T.plot.bar(ax=ax)

                # Display the plot using st.pyplot
                st.pyplot(fig)
            
    
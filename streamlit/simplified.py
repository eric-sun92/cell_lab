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

normalized2_df = pd.read_csv('dataframes/normalized2_df.csv')
normalizedto100_df = pd.read_csv('dataframes/normalizedto100_df.csv')
sample_df = pd.read_csv('dataframes/sample_df.csv')
ref_df = pd.read_csv('dataframes/ref_df.csv')
sample_df_avg = pd.read_csv('dataframes/sample_df_avg.csv')
sample_df_avg_sum = pd.read_csv('dataframes/sample_df_avg_sum.csv')
normalized_df = pd.read_csv('dataframes/normalized_df.csv')

# Using object notation
method = st.sidebar.selectbox(
    "Method",
    ("Single", "Multiple")
)


def single():
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
            

# Export Excel!

# now = datetime.now()
# now = now.strftime("%H_%M_%S")
# today = date.today()
# filename = "Proteomics output" + str(today) + '_' + str(now) + ".xlsx" # Change to designated file path
# writer = pd.ExcelWriter(filename, engine='xlsxwriter')

# frames = {'Original data':sample_df,'Reference':ref_df,'Averages added':sample_df_avg,'Averages and sums':sample_df_avg_sum,'Simplified':normalized_df,'Normalized':normalized2_df,
#           'Relative percent sol':normalizedto100_df}

# for sheet, frame in  frames.items():                   # .use .items for python 3.X
#     frame.to_excel(writer, sheet_name = sheet)
    
# writer.save()
# print('Done!')
    

def multiple():
    # Load the Excel file
    # filename = input("Enter the name of the Excel file with the data (include the '.xlsx' at the end): ")
    data = pd.read_excel("initialCode/solubilization_index.xlsx")

    # Remove the last column from the data
    data = data.iloc[:, :-1]

    # Remove " index" from column headers
    data.columns = [col.replace(" index", "") for col in data.columns]

    # Set the first column as the index
    data.set_index(data.columns[0], inplace=True)

    # Initialize dictionary with column names as keys
    gene_data = {col: 0 for col in data.columns[1:]}

    # Function to update gene data in the dictionary
    def update_gene_data(gene_name):
        # while gene_name not in data.index:
        #     print(f"Gene '{gene_name}' not found in the Excel sheet.")
        #     gene_name = input("Please enter a valid gene name: ")
        if gene_name in data.index:
            row_data = data.loc[gene_name]
            for col in gene_data.keys():
                gene_data[col] += row_data[col]

    # Prompt the user for the number of genes
    # num_genes = int(input("Enter how many genes you will input: "))
    with st.form("my_form"):
        st.write("Form Title")
        label_text = "<div class='custom-label'>Enter genes separated with a comma:</div>"
        st.markdown(label_text, unsafe_allow_html=True)

        genes = st.text_input("", "Gene Names...", key=np.random.randint(1))

        submitted = st.form_submit_button("Search")
        if submitted:
            gene_array = genes.split(", ")
            
            for g in gene_array:
                st.write(g)
                update_gene_data(g)
                
            # # Prompt the user to enter gene names
            # for i in range(num_genes):
            #     gene_name = input(f"Enter gene #{i+1}: ")
            #     update_gene_data(gene_name)

            for col in gene_data.keys():
                gene_data[col] /= len(gene_array)

            print("\nFinal solubilization data by index:")
            for col, value in gene_data.items():
                print(f"{col}: {value}")

            fig, ax = plt.subplots()
                
            plt.bar(gene_data.keys(), gene_data.values())
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.title('Solubilization Index Calculator')
            plt.xticks(rotation=90)

            # Display the value inside each bar
            for i, (col, value) in enumerate(gene_data.items()):
                plt.annotate(f"{value:.10f}", xy=(i, value), xytext=(0, -10), textcoords="offset points",
                            ha='center', va='top', fontsize=8, color='white', rotation='vertical')

            # Show the plot
            # plt.show()
            st.pyplot(fig)

if method == "Single":
    single()
elif method == "Multiple":
    multiple()
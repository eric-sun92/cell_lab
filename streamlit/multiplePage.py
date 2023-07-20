import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np                       


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
    
    # data = pd.read_csv("dataframes/solubilization.csv")

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
        else:
            st.write(f"Gene '{gene_name}' not found in the Excel sheet.")

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

            for col in gene_data.keys():
                gene_data[col] /= len(gene_array)

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
            st.pyplot(fig)

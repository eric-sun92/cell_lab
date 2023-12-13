import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np  
from datetime import datetime             # append current time to any output
from datetime import date   
import io                      

normalized2_df = pd.read_csv('dataframes/normalized2_df.csv', low_memory=False)
normalizedto100_df = pd.read_csv('dataframes/normalizedto100_df.csv', low_memory=False)
sample_df = pd.read_csv('dataframes/sample_df.csv', low_memory=False)
ref_df = pd.read_csv('dataframes/ref_df.csv', low_memory=False)
sample_df_avg = pd.read_csv('dataframes/sample_df_avg.csv', low_memory=False)
sample_df_avg_sum = pd.read_csv('dataframes/sample_df_avg_sum.csv', low_memory=False)
normalized_df = pd.read_csv('dataframes/normalized_df.csv', low_memory=False)

# SessionState class for maintaining app state
class SessionState:
    def __init__(self):
        self.done_clicked = False

def process_and_save_data(gene_data):
    # print(list(gene_data.items()))
    gene_df = pd.DataFrame(list(gene_data.items()), columns=['Gene Name', 'Value'])

    # Prepare the DataFrame to be saved as a binary format
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    gene_df.to_excel(writer, sheet_name='GeneData', index=True)
    writer.save()
    output.seek(0)
    
    now = datetime.now()
    now = now.strftime("%H_%M_%S")
    today = date.today()
    filename = "Proteomics output" + str(today) + '_' + str(now) + ".xlsx" # Change to designated file path
    
    return output, filename


# Function to update gene data in the dictionary
def update_gene_data(gene_name, data, gene_data):
    # while gene_name not in data.index:
    #     print(f"Gene '{gene_name}' not found in the Excel sheet.")
    #     gene_name = input("Please enter a valid gene name: ")
    print(data)
    print(gene_data)
    if gene_name in data.index:
        row_data = data.loc[gene_name]
        for col in gene_data.keys():
            gene_data[col] += row_data[col]
    else:
        st.write(f"Gene '{gene_name}' not found in the Excel sheet.")
    
    return gene_data
    
def multiple():
    st.title("Multi-protein Network Analysis:")
    # Initialize SessionState
    session_state = SessionState()
    
    global gene_data

    # Load the Excel file
    data = pd.read_excel("dataframes/solubilization_index_1.xlsx")
    data = data.iloc[:, :-1]
    data.columns = [col.replace(" index", "") for col in data.columns]
    data.set_index(data.columns[0], inplace=True)

    # Initialize dictionary with column names as keys
    gene_data = {col: 0 for col in data.columns[1:]}

    # Form for entering multiple gene names and Done button
    with st.form("multi_submit"):
        # st.write("Multi-Gene Graph Search")
        label_text = "<div class='custom-label'>Enter genes separated with a comma:</div>"
        st.markdown(label_text, unsafe_allow_html=True)

        genes = st.text_input("", "Gene Names...", key=np.random.randint(1))
        genes = genes.upper()

        col1, col2 = st.columns([0.85, 0.15])

        submitted = col1.form_submit_button("Search")
        done_submitted = col2.form_submit_button("Export")     

    if submitted:
        gene_array = genes.split(", ")
        
        gene_data = {col: 0 for col in data.columns[:]}
        st.markdown("**Searched for gene names:**")

        for g in gene_array:
            st.write(g)
            gene_data = update_gene_data(g, data, gene_data)

        for col in gene_data.keys():
            gene_data[col] /= len(gene_array)

        fig, ax = plt.subplots()
        
        plt.bar(gene_data.keys(), gene_data.values())
        plt.ylabel('Value')
        plt.title('Native Extraction Index')
        plt.xlabel('Extraction Condition')
        plt.xticks(rotation=90)

        # Display the value inside each bar
        for i, (col, value) in enumerate(gene_data.items()):
            plt.annotate(f"{value:.10f}", xy=(i, value), xytext=(0, -10), textcoords="offset points",
                        ha='center', va='top', fontsize=8, color='white', rotation='vertical')
        st.pyplot(fig)
    
    if session_state.done_clicked or done_submitted:
        gene_array = genes.split(", ")
        
        gene_data = {col: 0 for col in data.columns[1:]}
        
        st.write("Searched for gene names:")
        
        for g in gene_array:
            st.write(g)
            gene_data = update_gene_data(g, data, gene_data)

        for col in gene_data.keys():
            gene_data[col] /= len(gene_array)
        
        st.write("Data processed and Excel file saved!")
        
        # Provide download button for the 'gene_data' DataFrame
        st.write("Download the Gene Data Excel Sheet:")
        data, filename = process_and_save_data(gene_data)
        st.download_button(
            label="Click to Download",
            data=data,
            file_name=filename,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            key="download_multi"
        )
        
 
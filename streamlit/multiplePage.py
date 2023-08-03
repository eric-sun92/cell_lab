import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np                       

# SessionState class for maintaining app state
class SessionState:
    def __init__(self):
        self.done_clicked = False

def process_and_save_data():
    now = datetime.now()
    now = now.strftime("%H_%M_%S")
    today = date.today()
    filename = "Proteomics output" + str(today) + '_' + str(now) + ".xlsx" # Change to designated file path
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    frames = {'Original data': sample_df, 'Reference': ref_df, 'Averages added': sample_df_avg,
              'Averages and sums': sample_df_avg_sum, 'Simplified': normalized_df, 'Normalized': normalized2_df,
              'Relative percent sol': normalizedto100_df}

    for sheet, frame in frames.items():
        frame.to_excel(writer, sheet_name=sheet)

    writer.save()
    st.write('Done!')

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

    # Initialize SessionState
    session_state = SessionState()

    # Form for entering multiple gene names and Done button
    with st.form("multi_submit"):
        st.write("Multi-Gene Graph Search")
        label_text = "<div class='custom-label'>Enter genes separated with a comma:</div>"
        st.markdown(label_text, unsafe_allow_html=True)

        genes = st.text_input("", "Gene Names...", key=np.random.randint(1))

        submitted = st.form_submit_button("Search")

        # Custom label for the Done button
        done_submitted = st.form_submit_button("Export")

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
        
        if session_state.done_clicked or done_submitted:
            process_and_save_data()
            st.write("Data processed and Excel file saved!")

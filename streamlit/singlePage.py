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

normalized2_df = pd.read_csv('new/normalized2_df.csv', low_memory=False)
normalizedto100_df = pd.read_csv('new/normalizedto100_df.csv', low_memory=False)
sample_df = pd.read_csv('new/sample_df.csv', low_memory=False)
ref_df = pd.read_csv('new/ref_df.csv', low_memory=False)
sample_df_avg = pd.read_csv('new/sample_df_avg.csv', low_memory=False)
sample_df_avg_sum = pd.read_csv('new/sample_df_avg_sum.csv', low_memory=False)
normalized_df = pd.read_csv('new/normalized_df.csv', low_memory=False)

# SessionState class for maintaining app state
class SessionState:
    def __init__(self):
        self.done_clicked = False

def process_and_save_data(gene_name):
    now = datetime.now()
    now = now.strftime("%H_%M_%S")
    today = date.today()
    filename = "Proteomics output" + str(today) + '_' + str(now) + ".xlsx" # Change to designated file path
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    
    selected_row = normalizedto100_df[normalizedto100_df['Gene names'] == gene_name]
    final_df = pd.DataFrame(selected_row)


    # frames = {'Original data': sample_df, 'Reference': ref_df, 'Averages added': sample_df_avg,
    #           'Averages and sums': sample_df_avg_sum, 'Simplified': normalized_df, 'Normalized': normalized2_df,
    #           'Relative percent sol': normalizedto100_df, 'final': final_df}
    
    frames = {'final': final_df}

    for sheet, frame in frames.items():
        frame.to_excel(writer, sheet_name=sheet)

    writer.save()
    print('Done!')
    return filename

def single():
    # Include the CSS file
    st.title("Single Protein Search:")

    # Include the JavaScript file
    st.markdown('<script src="./streamlit/script.js"></script>', unsafe_allow_html=True)

    # Initialize SessionState
    session_state = SessionState()

    # Form for searching gene name and Done button
    with st.form("my_form"):
        label_text = "<div class='custom-label'>What gene name would you like to search for?</div>"
        st.markdown(label_text, unsafe_allow_html=True)

        gene_name = st.text_input("", "Search...", key="gene_name")
        gene_name = gene_name.upper()
        
        col1, col2 = st.columns([0.85, 0.15])

        # Add the "Search" button to the first column
        search_submitted = col1.form_submit_button("Search")

        # Add the "Export" (Done) button to the second column
        done_submitted = col2.form_submit_button("Export")      

    if search_submitted:
        if gene_name.lower() == "done":
            session_state.done_clicked = True
        else:
            gene_name_exact_match = normalizedto100_df['Gene names'] == gene_name

            if gene_name == '':
                st.write("Please enter a gene name before searching...")
            # elif gene_name not in normalizedto100_df['Gene names']:
            #     st.write(f"{gene_name} not found in database")
            elif not gene_name_exact_match.any():
                st.write(f"{gene_name} not found in database")
            # elif not normalizedto100_df['Gene names'].str.contains(gene_name, na=False).any():
            #     st.write(f"{gene_name} not found in database")
            else:
            # Create the bar plot
                fig, ax = plt.subplots()
                plt.ylabel('Extraction Efficiency')
                plt.xlabel('Extraction Condition')
                display_3 = normalizedto100_df[normalizedto100_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=0)
                print(display_3)
                display_3 = display_3.drop("Mol. weight [kDa]", axis=0)
                display_3.T.plot.bar(ax=ax)

                # Display the plot using st.pyplot
                st.pyplot(fig)

    if session_state.done_clicked or done_submitted:
        filename = process_and_save_data(gene_name)
        st.write("Data processed and Excel file saved!")
        
        # Create a download button to allow the user to download the Excel file
        with open(filename, 'rb') as f:
            st.download_button(
                label="Click to Download Excel",
                data=f,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_button"
        )
    
    # Footer
    from PIL import Image

    image = Image.open('streamlit/your_banner_image.jpg')
    
    st.markdown("---")
    st.image(image)
    st.write("© 2023 Yale School of Medicine. All rights reserved.")

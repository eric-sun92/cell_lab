# Welcome to the code for polymer solubilization analysis


import pandas as pd                       # pandas = package for excel
from pandas import ExcelWriter            # save to excel
import numpy as np                        # another package for number and excel analysis
from datetime import datetime             # append current time to any output
from datetime import date                 # append current date to any output
from itertools import groupby
import ast
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import interactive

import streamlit as st


# # 1. Introduction
     
# # print('This will analyze your samples and generate an excel output - afterwards you can type in a gene name to plot for that protein OR use the excel output for other analyses!')
# # print('Before continuing, make sure you have updated your reference excel to describe the polymers you are analyzing')
# # input('Press Enter to continue...')


# # 2. Upload files 

# ## There are two options, have files in code already (for optimization/testing of code) or have files inputted each run (for analysis)
# ## To switch between, alternate between the lines that have ##### in front and back which are commented out

# # 2a. Upload sample info

# # sample_file = input('Enter file path containing the MaxQuant(?) output - all you need to do prior is convert from txt to excel:\n')
# ####sample_file = "/Users/rachel/Desktop/proteinGroups_dummydata.xlsx"          #####
# sample_file = '/Users/ericsun/Desktop/polymer/fulloutput_filtered.xlsx'
# # print ("Starting sample upload....")            
# # start = datetime.now()                                                  # Define start to see how long it takes
# sample_array = pd.read_excel(sample_file, header = None).to_numpy()                              # Parse the file and send it to an array format
# # end = datetime.now()                                                    # Define end to see how long it takes
# # ingesttime = end - start                                                # Define time it took
# # print("Finished reading Samples in", ingesttime.total_seconds(), "seconds into array of shape", sample_array.shape)       # Define time it took and print the number of rows and columns
# column_list_sample = sample_array[0,]
# sample_array = sample_array[1:]
# sample_df = pd.DataFrame(sample_array, columns = column_list_sample)

# # 2b. Upload reference info


# # ref_file = input('Enter file path for reference polymers:\n')# File name containing samples in local directory (MSDial output directly converted to excel)
# ######ref_file = "/Users/rachel/Desktop/dummy_ref_polymer.xlsx"       #####
# ref_file = '/Users/ericsun/Desktop/polymer/polymer_ref_filtered.xlsx'
# # print("Starting sample file upload...")                           # Code is running
# # start2 = datetime.now()                                           # Define start to see how long it takes
# ref_array = pd.read_excel(ref_file, header = None).to_numpy()                    # Parse the file and send it to an array format
# # end2 = datetime.now()                                             # Define end to see how long it takes
# # ingesttime2 = end2 - start2                                       # Define time it took
# # print("Finished reading reference file in", ingesttime2.total_seconds(), "seconds into array of shape", ref_array.shape)     # Define time it took and print numbers of rows and columns in file
# ref_list = ref_array[1:,0]
# ref_list2 = [str(x) for x in ref_list]
# column_list_ref = ref_array[0,]
# ref_array = ref_array[1:]
# ref_df = pd.DataFrame(ref_array, columns = column_list_ref)
# # print('Sample file:',sample_array,'Sample dataframe:',sample_df)
# # print('Ref file:',ref_array)
# # print('Rep list:',ref_list)
# # print('Ref df',ref_df)
# sample_df_avg = sample_df.copy()

# for ref in ref_list2:
#     name = ref_df[ref_df['Replicate Name'] == int(ref)]['Polymer Name'].item()
#     sample_df_avg[name + ' sample avg'] = sample_df_avg.filter(regex='LFQ intensity '+str(ref)+'_rep').mean(axis = 1)
#     # print(ref,name)
# ##    print(sample_df)

# sample_df_avg_sum = sample_df_avg.copy()
# sample_df_avg_sum.loc['Column_Sum']= sample_df_avg_sum.sum(numeric_only=True, axis=0)

# normalized_df = sample_df_avg_sum[['Protein IDs','Majority protein IDs','Protein names','Gene names','Mol. weight [kDa]']]
# ## normalized_df = normalized_df.join[sample_df_avg_sum.filter(regex = ' sample avg')]
# ##print('Normalized',normalized_df)

# for ref in ref_list2:
#     name = ref_df[ref_df['Replicate Name'] == int(ref)]['Polymer Name'].item()
#     normalized_df.loc[:,name + ' sample avg'] = sample_df_avg_sum[name + ' sample avg']
# ##print(normalized_df)

# max_sol_df = normalized_df.filter(regex=(' sample avg'))
# ##print(max_sol_df)

# max_value = max_sol_df.loc['Column_Sum'].max(axis=0)
# # print('Max sum',max_value)

# normalized2_df = normalized_df.copy()

# for ref in ref_list2:
#     name = ref_df[ref_df['Replicate Name'] == int(ref)]['Polymer Name'].item()
#     normalized2_df.loc[:,name+' sample avg'] = normalized2_df.loc[:,name+' sample avg'].div(normalized2_df.iloc[-1][name+' sample avg'])
#     normalized2_df.loc[:,name+' sample avg'] = normalized2_df.loc[:,name+' sample avg'].multiply(max_value)


# normalizedto100_df = normalized2_df.copy()
# ###normalizedto100_df.loc[~ (normalizedto100_df.select_dtypes(include=['number']) == 0).all(axis='columns'), :]
# ##normalizedto100_df = normalizedto100_df[normalizedto100_df.columns[4:]].replace(0, np.nan)
# ##normalizedto100_df[any(normalizedto100_df[normalizedto100_df.columns[4:]] != 0, axis=1)]
# ##normalizedto100_df = normalizedto100_df.loc[~(normalizedto100_df.filter(regex='sample avg') == 0)]
# ##df1[df1['col'].str.contains(r'foo(?!$)')]
# ##df = df[(df[['c', 'd', 'e', 'f']] != 0).any(axis=1)]

# ##transpose_df = normalizedto100_df.transpose(copy=True)
# ##print(transpose_df)
# ##num_samples = transpose_df[index].str.contains('sample avg').value_counts()
# ##print(num_samples)

# header_list = normalizedto100_df.columns.values.tolist()
# # print('Header list:',header_list)
# sample_count = sum('sample avg' in s for s in header_list)
# # print('Number of samples:',sample_count)
# sample_count2 = sample_count - 9

# normalizedto100_df = normalizedto100_df.replace(0, np.nan)
# normalizedto100_df = normalizedto100_df.dropna(thresh=sample_count2, axis=0)
# normalizedto100_df = normalizedto100_df.replace(np.nan, 0)

# # print(normalized2_df)

# for index,row in normalizedto100_df.iterrows():
#    ## print(index)
#    ## print(row)
#     ##print(row[4:])
#     values = row[4:]
#     max_in_row = values.max(skipna=True,axis=0)
#     ##print(max_in_row)
#     for ref in ref_list2:
#         name = ref_df[ref_df['Replicate Name'] == int(ref)]['Polymer Name'].item()
#         amount = normalizedto100_df.loc[index,name+' sample avg'].item()
#         normalizedto100_df.loc[index,name+' sample avg'] = (amount/max_in_row)*100

# # print(normalizedto100_df)

# ##print(normalized2_df)



# normalized2_df.to_csv('normalized2_df.csv', index=False)
# normalizedto100_df.to_csv('normalizedto100_df.csv', index=False)

normalized2_df = pd.read_csv('normalized2_df.csv')
normalizedto100_df = pd.read_csv('normalizedto100_df.csv')

with st.form("my_form"):
    st.write("Inside the form")
    label_text = "<div class='custom-label'>What gene name would you like to search for? (Or enter 'done') to finish...</div>"
    st.markdown(label_text, unsafe_allow_html=True)

    gene_name = st.text_input("", "Search...", key=np.random.randint(1))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Search")
    if submitted:
        if gene_name == 'done':
            active_searching = False
            print('Ending now...')
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
            # print('disp 3:',display_3,type(display_3),display_4,type(display_4))
            # display_3.T.plot.bar()
            # # st.pyplot(display_3)

            # # plt.show()
            # print('/n')
            # print(display_1,'\n','Max:',display_2,'Value:',display_2_value,'\n',display_3)



# active_searching = True
# while active_searching:
    
#     label_text = "<div class='custom-label'>What gene name would you like to search for? (Or enter 'done') to finish...</div>"
#     st.markdown(label_text, unsafe_allow_html=True)

#     gene_name = st.text_input("", "Search...", key=np.random.randint(1))
    
#     # gene_name = input('What gene name would you like to search for? (Or enter "done") to finish \n')
#     if gene_name == 'done':
#         active_searching = False
#         print('Ending now...')
#     else:
#         display_1 = normalized2_df[normalized2_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=0)
#         display_3 = normalizedto100_df[normalizedto100_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=0)
#         display_4 = [display_3]
#         display_2 = normalized2_df[normalized2_df['Gene names'].str.contains(gene_name,na=False)].max(numeric_only=True,axis=1)
#         display_22 = display_2.to_string()
#         display_23 = display_22.split()
#         display_2_value = display_23[-1]
#         print('disp 3:',display_3,type(display_3),display_4,type(display_4))
#         display_3.T.plot.bar()
#         plt.show()
#         print('/n')
#         print(display_1,'\n','Max:',display_2,'Value:',display_2_value,'\n',display_3)



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
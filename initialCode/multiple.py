import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

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
    while gene_name not in data.index:
        print(f"Gene '{gene_name}' not found in the Excel sheet.")
        gene_name = input("Please enter a valid gene name: ")
    row_data = data.loc[gene_name]
    for col in gene_data.keys():
        gene_data[col] += row_data[col]

# Prompt the user for the number of genes
num_genes = int(input("Enter how many genes you will input: "))

# Prompt the user to enter gene names
for i in range(num_genes):
    gene_name = input(f"Enter gene #{i+1}: ")
    update_gene_data(gene_name)

for col in gene_data.keys():
    gene_data[col] /= num_genes

print("\nFinal solubilization data by index:")
for col, value in gene_data.items():
    print(f"{col}: {value}")

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
st.pyplot()

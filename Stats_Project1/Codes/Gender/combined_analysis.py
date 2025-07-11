import pandas as pd

# Load the summary statistics from the Excel files
male_file = 'c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Gender/Male/summary_stats_male.xlsx'
female_file = 'c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Gender/Female/summary_stats_female.xlsx'

male_data = pd.read_excel(male_file, index_col=0)
female_data = pd.read_excel(female_file, index_col=0)

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([male_data.columns, ['Male', 'Female']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in male_data.columns:
    combined_data[(column, 'Male')] = male_data[column]
    combined_data[(column, 'Female')] = female_data[column]

# Save the combined data to a new Excel file
combined_data.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Gender/combined_summary_stats.xlsx')


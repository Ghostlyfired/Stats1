import pandas as pd

# Load the summary statistics from the Excel files
smokers_file = 'c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/smoking/smoker/summary_stats_smokers.xlsx'
non_smokers_file = 'c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/smoking/non_smoker/summary_stats_non_smokers.xlsx'

smokers_data = pd.read_excel(smokers_file, index_col=0)
non_smokers_data = pd.read_excel(non_smokers_file, index_col=0)

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([smokers_data.columns, ['Smokers', 'Non-Smokers']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in smokers_data.columns:
    combined_data[(column, 'Smokers')] = smokers_data[column]
    combined_data[(column, 'Non-Smokers')] = non_smokers_data[column]

# Save the combined data to a new Excel file
combined_data.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/smoking/combined_summary_stats.xlsx')
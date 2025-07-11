import pandas as pd

# Load the low alcohol data
low_alcohol_data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Alcohol/Low/low_alcohol_data.csv')

# Analyze the low alcohol data
analysis_columns = [
    'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 
    'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings'
]

# Print summary statistics for each column in table format and save to an Excel file
summary_stats_low_alcohol = low_alcohol_data[analysis_columns].describe().drop('count', axis=0)
summary_stats_low_alcohol.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Alcohol/Low/summary_stats_low_alcohol.xlsx')

# Load the high alcohol data
high_alcohol_data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Alcohol/High/high_alcohol_data.csv')

# Analyze the high alcohol data
summary_stats_high_alcohol = high_alcohol_data[analysis_columns].describe().drop('count', axis=0)
summary_stats_high_alcohol.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Alcohol/High/summary_stats_high_alcohol.xlsx')

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([summary_stats_low_alcohol.columns, ['Low Alcohol', 'High Alcohol']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in summary_stats_low_alcohol.columns:
    combined_data[(column, 'Low Alcohol')] = summary_stats_low_alcohol[column]
    combined_data[(column, 'High Alcohol')] = summary_stats_high_alcohol[column]

# Save the combined data to a new Excel file
combined_data.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Alcohol/combined_summary_stats_alcohol.xlsx')
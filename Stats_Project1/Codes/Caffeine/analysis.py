import pandas as pd
import os

# Load the low caffeine data
low_caffeine_data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Caffeine/Low/low_caffeine_data.csv')

# Analyze the low caffeine data
analysis_columns = [
    'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 
    'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings'
]

summary_stats_low_caffeine = low_caffeine_data[analysis_columns].describe().drop('count', axis=0)
median_low_caffeine = low_caffeine_data[analysis_columns].median()
mode_low_caffeine = low_caffeine_data[analysis_columns].mode().iloc[0]

# Combine mean, median, and mode
summary_stats_low_caffeine.loc['median'] = median_low_caffeine
summary_stats_low_caffeine.loc['mode'] = mode_low_caffeine

summary_stats_low_caffeine.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Caffeine/Low/summary_stats_low_caffeine.xlsx')

# Load the high caffeine data
high_caffeine_data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Caffeine/High/high_caffeine_data.csv')

# Analyze the high caffeine data
summary_stats_high_caffeine = high_caffeine_data[analysis_columns].describe().drop('count', axis=0)
median_high_caffeine = high_caffeine_data[analysis_columns].median()
mode_high_caffeine = high_caffeine_data[analysis_columns].mode().iloc[0]

# Combine mean, median, and mode
summary_stats_high_caffeine.loc['median'] = median_high_caffeine
summary_stats_high_caffeine.loc['mode'] = mode_high_caffeine

summary_stats_high_caffeine.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Caffeine/High/summary_stats_high_caffeine.xlsx')

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([summary_stats_low_caffeine.columns, ['Low Caffeine', 'High Caffeine']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in summary_stats_low_caffeine.columns:
    combined_data[(column, 'Low Caffeine')] = summary_stats_low_caffeine[column]
    combined_data[(column, 'High Caffeine')] = summary_stats_high_caffeine[column]

# Save the combined data to a new Excel file
combined_data.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Caffeine/combined_summary_stats_caffeine.xlsx')
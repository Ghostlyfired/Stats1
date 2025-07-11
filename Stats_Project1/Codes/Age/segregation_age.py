import pandas as pd
import os

# Load the data
data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Sleep_Efficiency_no_dates_modified_wakeup.csv')

# Segregate the data based on age groups
young_people_data = data[(data['Age'] >= 9) & (data['Age'] <= 24)]
working_class_data = data[(data['Age'] >= 25) & (data['Age'] <= 45)]
old_aged_data = data[(data['Age'] >= 46) & (data['Age'] <= 69)]

# Create directories if they do not exist
os.makedirs('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Young', exist_ok=True)
os.makedirs('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Working', exist_ok=True)
os.makedirs('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Old', exist_ok=True)

# Save the segregated data to new CSV files
young_people_data.to_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Young/young_people_data.csv', index=False)
working_class_data.to_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Working/working_class_data.csv', index=False)
old_aged_data.to_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Old/old_aged_data.csv', index=False)

# Analyze the young people data
analysis_columns = [
    'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 
    'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings'
]

summary_stats_young = young_people_data[analysis_columns].describe().drop('count', axis=0)
summary_stats_young.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Young/summary_stats_young.xlsx')

# Analyze the working class data
summary_stats_working = working_class_data[analysis_columns].describe().drop('count', axis=0)
summary_stats_working.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Working/summary_stats_working.xlsx')

# Analyze the old aged data
summary_stats_old = old_aged_data[analysis_columns].describe().drop('count', axis=0)
summary_stats_old.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/Old/summary_stats_old.xlsx')

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([summary_stats_young.columns, ['Young', 'Working', 'Old']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in summary_stats_young.columns:
    combined_data[(column, 'Young')] = summary_stats_young[column]
    combined_data[(column, 'Working')] = summary_stats_working[column]
    combined_data[(column, 'Old')] = summary_stats_old[column]

# Save the combined data to a new Excel file
combined_data.to_excel('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Age/combined_summary_stats_age.xlsx')
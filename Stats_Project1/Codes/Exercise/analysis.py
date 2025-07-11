import pandas as pd
import os

# Load the data
file_path = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Sleep_Efficiency_no_dates_modified_wakeup.csv'
data = pd.read_csv(file_path)

# Create the exercise folder if it doesn't exist
exercise_folder = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\exercise'
os.makedirs(exercise_folder, exist_ok=True)

# Segregate the data
no_exercise = data[data['Exercise frequency'] == 0]
light_exercise = data[(data['Exercise frequency'] >= 1) & (data['Exercise frequency'] <= 2)]
heavy_exercise = data[(data['Exercise frequency'] >= 3) & (data['Exercise frequency'] <= 5)]

# Save the segregated data into separate CSV files
no_exercise.to_csv(os.path.join(exercise_folder, 'no_exercise.csv'), index=False)
light_exercise.to_csv(os.path.join(exercise_folder, 'light_exercise.csv'), index=False)
heavy_exercise.to_csv(os.path.join(exercise_folder, 'heavy_exercise.csv'), index=False)

# Analysis columns
analysis_columns = [
    'Bedtime', 'Wakeup time', 'Sleep duration', 'Sleep efficiency', 
    'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage', 'Awakenings'
]

# Analyze the no exercise data
summary_stats_no_exercise = no_exercise[analysis_columns].describe().drop('count', axis=0)
summary_stats_no_exercise.to_excel(os.path.join(exercise_folder, 'summary_stats_no_exercise.xlsx'))

# Analyze the light exercise data
summary_stats_light_exercise = light_exercise[analysis_columns].describe().drop('count', axis=0)
summary_stats_light_exercise.to_excel(os.path.join(exercise_folder, 'summary_stats_light_exercise.xlsx'))

# Analyze the heavy exercise data
summary_stats_heavy_exercise = heavy_exercise[analysis_columns].describe().drop('count', axis=0)
summary_stats_heavy_exercise.to_excel(os.path.join(exercise_folder, 'summary_stats_heavy_exercise.xlsx'))

# Create a MultiIndex for the columns
columns = pd.MultiIndex.from_product([summary_stats_no_exercise.columns, ['No Exercise', 'Light Exercise', 'Heavy Exercise']])

# Combine the data
combined_data = pd.DataFrame(columns=columns)

for column in summary_stats_no_exercise.columns:
    combined_data[(column, 'No Exercise')] = summary_stats_no_exercise[column]
    combined_data[(column, 'Light Exercise')] = summary_stats_light_exercise[column]
    combined_data[(column, 'Heavy Exercise')] = summary_stats_heavy_exercise[column]

# Save the combined data to a new Excel file
combined_data.to_excel(os.path.join(exercise_folder, 'combined_summary_stats_exercise.xlsx'))

print("Data segregation and analysis complete.")
import pandas as pd
import os

# Define the base directory
base_dir = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Age and Caffeine'

# Define age groups and caffeine levels
age_groups = ['young', 'working', 'old']
caffeine_levels = ['low', 'high']

# Initialize a list to store all analysis results
combined_analysis = []

# Function to load data
def load_data(age_group, caffeine_level):
    file_path = os.path.join(base_dir, age_group, caffeine_level, f'{age_group}_{caffeine_level}.csv')
    return pd.read_csv(file_path)

# Function to perform basic analysis
def analyze_data(data):
    analysis = {
        'mean_sleep_duration': data['Sleep duration'].mean(),
        'mean_sleep_efficiency': data['Sleep efficiency'].mean(),
        'mean_rem_sleep_percentage': data['REM sleep percentage'].mean(),
        'mean_deep_sleep_percentage': data['Deep sleep percentage'].mean(),
        'mean_light_sleep_percentage': data['Light sleep percentage'].mean(),
        'mean_awakenings': data['Awakenings'].mean(),
        'mean_caffeine_consumption': data['Caffeine consumption'].mean(),
        'mean_alcohol_consumption': data['Alcohol consumption'].mean(),
        'mean_exercise_frequency': data['Exercise frequency'].mean()
    }
    return analysis

# Perform analysis for each group and collect results
for age_group in age_groups:
    for caffeine_level in caffeine_levels:
        data = load_data(age_group, caffeine_level)
        analysis = analyze_data(data)
        analysis['age_group'] = age_group
        analysis['caffeine_level'] = caffeine_level
        combined_analysis.append(analysis)

# Convert combined analysis to DataFrame
combined_analysis_df = pd.DataFrame(combined_analysis)

# Reorder columns to have age_group and caffeine_level at the start
columns_order = ['age_group', 'caffeine_level'] + [col for col in combined_analysis_df.columns if col not in ['age_group', 'caffeine_level']]
combined_analysis_df = combined_analysis_df[columns_order]

# Define output file path for combined analysis
output_file = os.path.join(base_dir, 'combined_analysis.xlsx')

# Save combined analysis to Excel
combined_analysis_df.to_excel(output_file, index=False)

print(f'Combined analysis saved to {output_file}')
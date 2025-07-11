import pandas as pd
from scipy import stats

# Load the data
file_path = r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Sleep_Efficiency_no_dates_modified_wakeup.csv'
data = pd.read_csv(file_path)

# Calculate mean, median, and mode for REM sleep percentage
rem_mean = data['REM sleep percentage'].mean()
rem_median = data['REM sleep percentage'].median()
rem_mode = data['REM sleep percentage'].mode()[0]

# Calculate mean, median, and mode for Deep sleep percentage
deep_mean = data['Deep sleep percentage'].mean()
deep_median = data['Deep sleep percentage'].median()
deep_mode = data['Deep sleep percentage'].mode()[0]

# Calculate mean, median, and mode for Light sleep percentage
light_mean = data['Light sleep percentage'].mean()
light_median = data['Light sleep percentage'].median()
light_mode = data['Light sleep percentage'].mode()[0]

# Create a DataFrame to store the results
results = pd.DataFrame({
    'Metric': ['Mean', 'Median', 'Mode'],
    'REM Sleep Percentage': [rem_mean, rem_median, rem_mode],
    'Deep Sleep Percentage': [deep_mean, deep_median, deep_mode],
    'Light Sleep Percentage': [light_mean, light_median, light_mode]
})

# Calculate the correlation matrix
correlation_matrix = data[['Sleep efficiency', 'REM sleep percentage', 'Deep sleep percentage', 'Light sleep percentage']].corr()

# Write the results to an Excel file
output_file_path = r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Sleep_Composition_Analysis.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    results.to_excel(writer, sheet_name='Summary', index=False)
    correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

print(f"Analysis results have been written to {output_file_path}")
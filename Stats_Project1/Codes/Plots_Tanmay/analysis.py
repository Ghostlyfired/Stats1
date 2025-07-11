import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Sleep_Efficiency_no_dates_modified_wakeup.csv'
data = pd.read_csv(file_path)

# Select only numeric columns for grouping
numeric_columns = ['Deep sleep percentage', 'Light sleep percentage', 'REM sleep percentage', 'Sleep efficiency']

# Alcohol vs Sleep Efficiency Ogive
plt.figure(figsize=(10, 6))
data_sorted = data.sort_values(by='Alcohol consumption')
cumulative = data_sorted['Sleep efficiency'].cumsum()
plt.plot(data_sorted['Alcohol consumption'], cumulative / cumulative.max(), label='Alcohol vs Sleep Efficiency Ogive')
plt.xlabel('Alcohol Consumption')
plt.ylabel('Cumulative Sleep Efficiency')
plt.title('Alcohol vs Sleep Efficiency Ogive')
plt.legend(loc='upper left')
plt.savefig(r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Plots_Tanmay\alcohol_vs_sleep_efficiency_ogive.png')
plt.close()

# Grouped data for Alcohol vs Sleep Metrics
alcohol_groups = data.groupby('Alcohol consumption')[numeric_columns].mean()

# Alcohol vs Sleep Metrics Histogram
plt.figure(figsize=(10, 6))
bar_width = 0.2
index = range(len(alcohol_groups))
plt.bar(index, alcohol_groups['Deep sleep percentage'], bar_width, label='Deep Sleep')
plt.bar([i + bar_width for i in index], alcohol_groups['Light sleep percentage'], bar_width, label='Light Sleep')
plt.bar([i + bar_width*2 for i in index], alcohol_groups['REM sleep percentage'], bar_width, label='REM Sleep')
plt.xlabel('Alcohol Consumption')
plt.ylabel('Percentage')
plt.title('Alcohol vs Sleep Metrics')
plt.xticks([i + bar_width for i in index], alcohol_groups.index)
plt.legend(loc='upper right')
plt.savefig(r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Plots_Tanmay\alcohol_vs_sleep_metrics.png')
plt.close()

# Grouped data for Smoking vs Sleep Metrics
smoking_groups = data.groupby('Smoking status')[numeric_columns].mean()

# Smoking vs Sleep Metrics Histogram
plt.figure(figsize=(10, 6))
bar_width = 0.2
index = range(len(smoking_groups))
plt.bar(index, smoking_groups['Deep sleep percentage'], bar_width, label='Deep Sleep')
plt.bar([i + bar_width for i in index], smoking_groups['Light sleep percentage'], bar_width, label='Light Sleep')
plt.bar([i + bar_width*2 for i in index], smoking_groups['REM sleep percentage'], bar_width, label='REM Sleep')
plt.xlabel('Smoking Status')
plt.ylabel('Percentage')
plt.title('Smoking vs Sleep Metrics')
plt.xticks([i + bar_width for i in index], smoking_groups.index)
plt.legend(loc='upper right')
plt.savefig(r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Plots_Tanmay\smoking_vs_sleep_metrics.png')
plt.close()

# Grouped data for Caffeine vs Sleep Metrics
caffeine_groups = data.groupby('Caffeine consumption')[numeric_columns].mean()

# Caffeine vs Sleep Metrics Histogram
plt.figure(figsize=(10, 6))
index = range(len(caffeine_groups))
plt.bar(index, caffeine_groups['Deep sleep percentage'], bar_width, label='Deep Sleep')
plt.bar([i + bar_width for i in index], caffeine_groups['Light sleep percentage'], bar_width, label='Light Sleep')
plt.bar([i + bar_width*2 for i in index], caffeine_groups['REM sleep percentage'], bar_width, label='REM Sleep')
plt.xlabel('Caffeine Consumption')
plt.ylabel('Percentage')
plt.title('Caffeine vs Sleep Metrics')
plt.xticks([i + bar_width for i in index], caffeine_groups.index)
plt.legend(loc='upper right')
plt.savefig(r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\Plots_Tanmay\caffeine_vs_sleep_metrics.png')
plt.close()
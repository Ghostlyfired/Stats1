import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Sleep_Efficiency_no_dates_modified_wakeup.csv'
data = pd.read_csv(file_path)

# Define age groups
age_groups = {
    'Young': data[data['Age'] <= 24],
    'Working': data[(data['Age'] > 24) & (data['Age'] <= 45)],
    'Old': data[data['Age'] > 45]
}

# Gender: Light Sleep Percentage - Cumulative Relative Frequency Ogive
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=data, x='Light sleep percentage', hue='Gender', palette=['blue', 'red'])
plt.title('Cumulative Relative Frequency Ogive of Light Sleep Percentage by Gender')
plt.xlabel('Light Sleep Percentage')
plt.ylabel('Cumulative Frequency')
plt.legend(title='Gender', labels=['Men', 'Women'])
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\light_sleep_percentage_cumulative_frequency_gender.png')
plt.show()

# Gender: IQR Values for Deep, Light, REM Sleep Proportions
iqr_values = data.groupby('Gender')[['Deep sleep percentage', 'Light sleep percentage', 'REM sleep percentage']].quantile(0.75) - data.groupby('Gender')[['Deep sleep percentage', 'Light sleep percentage', 'REM sleep percentage']].quantile(0.25)
iqr_values.plot(kind='bar', figsize=(10, 6), color=['blue', 'green', 'red'])
plt.title('IQR Values for Deep, Light, REM Sleep Proportions by Gender')
plt.xlabel('Gender')
plt.ylabel('IQR Value')
plt.legend(['Deep Sleep', 'Light Sleep', 'REM Sleep'])
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\iqr_values_sleep_proportions_gender.png')
plt.show()

# Age: Wakeup Time and Bedtime Mean
wake_bed_mean = pd.DataFrame({
    'Wakeup Time Mean': [group['Wakeup time'].mean() for group in age_groups.values()],
    'Bedtime Mean': [group['Bedtime'].mean() for group in age_groups.values()]
}, index=age_groups.keys())
wake_bed_mean.plot(kind='bar', figsize=(10, 6), color=['blue', 'red'])
plt.title('Wakeup Time and Bedtime Mean by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Mean Value')
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\wakeup_bedtime_mean_age.png')
plt.show()

# Age: Wakeup Time and Bedtime Std Dev
wake_bed_std = pd.DataFrame({
    'Wakeup Time Std': [group['Wakeup time'].std() for group in age_groups.values()],
    'Bedtime Std': [group['Bedtime'].std() for group in age_groups.values()]
}, index=age_groups.keys())
wake_bed_std.plot(kind='bar', figsize=(10, 6), color=['blue', 'red'])
plt.title('Wakeup Time and Bedtime Std Dev by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Std Dev Value')
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\wakeup_bedtime_std_age.png')
plt.show()

# Age: IQR Values for Deep, Light, REM Sleep Proportions
iqr_values_age = data.groupby(pd.cut(data['Age'], bins=[0, 24, 45, 100], labels=['Young', 'Working', 'Old']))[['Deep sleep percentage', 'Light sleep percentage', 'REM sleep percentage']].quantile(0.75) - data.groupby(pd.cut(data['Age'], bins=[0, 24, 45, 100], labels=['Young', 'Working', 'Old']))[['Deep sleep percentage', 'Light sleep percentage', 'REM sleep percentage']].quantile(0.25)
iqr_values_age.plot(kind='bar', figsize=(10, 6), color=['blue', 'red', 'yellow'])
plt.title('IQR Values for Deep, Light, REM Sleep Proportions by Age Group')
plt.xlabel('Sleep Proportion')
plt.ylabel('IQR Value')
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\iqr_values_sleep_proportions_age.png')
plt.show()

# Physical Activity: Cumulative Relative Frequency Ogive for Wakeup Time
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=data[data['Exercise frequency'] == 0], x='Wakeup time', color='blue', label='No Exercise')
sns.ecdfplot(data=data[(data['Exercise frequency'] > 0) & (data['Exercise frequency'] <= 2)], x='Wakeup time', color='green', label='Light Exercise')
sns.ecdfplot(data=data[data['Exercise frequency'] > 2], x='Wakeup time', color='red', label='Regular Exercise')
plt.title('Cumulative Relative Frequency Ogive of Wakeup Time by Exercise Frequency')
plt.xlabel('Wakeup Time')
plt.ylabel('Cumulative Frequency')
plt.legend(title='Exercise Frequency')
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\wakeup_time_cumulative_frequency_exercise.png')
plt.show()

# Physical Activity: Bar Graph for Sleep Duration, Deep Sleep Fraction, Sleep Efficiency
data['Deep sleep fraction'] = data['Deep sleep percentage'] / 100
data['Exercise frequency group'] = pd.cut(data['Exercise frequency'], bins=[-1, 1, 3, 5], labels=['0-1', '2-3', '4-5'])
exercise_stats = data.groupby('Exercise frequency group')[['Sleep duration', 'Deep sleep fraction', 'Sleep efficiency']].std()
exercise_stats.plot(kind='bar', figsize=(10, 6), color=['blue', 'green', 'red'])
plt.title('Std Dev of Sleep Duration, Deep Sleep Fraction, Sleep Efficiency by Exercise Frequency')
plt.xlabel('Exercise Frequency Group')
plt.ylabel('Std Dev Value')
plt.savefig('c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Plots_Vinay\\sleep_stats_exercise_std.png')
plt.show()
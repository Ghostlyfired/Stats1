import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Sleep_Efficiency_no_dates_modified_wakeup.csv'
data = pd.read_csv(file_path)

# Extract the relevant columns
rem_sleep = data['REM sleep percentage'].dropna()
deep_sleep = data['Deep sleep percentage'].dropna()
light_sleep = data['Light sleep percentage'].dropna()

# Combine the data into a single DataFrame
sleep_data = pd.DataFrame({
    'REM Sleep': rem_sleep,
    'Deep Sleep': deep_sleep,
    'Light Sleep': light_sleep
})

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create box plots
sleep_data.boxplot(ax=ax, whis=[0, 100])

# Set titles and labels
ax.set_title('Sleep Composition Percentages')
ax.set_ylabel('Percentage')

# Save the plot
output_path = 'c:\\Users\\New\\Desktop\\College\\4th Sem\\Applied Stats\\Project\\Sleep Composition\\sleep_composition_boxplot.png'
plt.tight_layout()
plt.savefig(output_path)

# Show the plot
plt.show()
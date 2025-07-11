import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/Sleep_Efficiency_no_dates_modified_wakeup.csv')

# Calculate the correlation coefficient
correlation_coefficient = data['Sleep duration'].corr(data['Sleep efficiency'])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Sleep duration'], data['Sleep efficiency'], alpha=0.5)
plt.title('Scatter Plot of Sleep Duration vs Sleep Efficiency')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Sleep Efficiency')
plt.grid(True)

# Display the correlation coefficient on the plot
plt.text(0.05, 0.95, f'Correlation Coefficient: {correlation_coefficient:.2f}', transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

# Save the plot as an image file
plt.savefig('c:/Users/New/Desktop/College/4th Sem/Applied Stats/Project/sleep_duration_vs_efficiency.png')

# Show the plot
plt.show()
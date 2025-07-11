import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import norm

# Load the dataset
file_path = r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\archive\Sleep_Efficiency_no_dates_modified.csv'
data = pd.read_csv(file_path)

# Choose the variable of interest
variable = 'Sleep efficiency'

# Create directory for saving plots
output_dir = r'c:\Users\New\Desktop\College\4th Sem\Applied Stats\Project\CLT_sleep_efficiency\plots'
os.makedirs(output_dir, exist_ok=True)

# Inspect the original data distribution
plt.figure(figsize=(10, 6))
sns.histplot(data[variable].dropna(), kde=False)
plt.title(f'Distribution of Original Data ({variable})')
plt.xlabel(variable)
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'original_data_distribution.png'))
plt.show()

# Function to calculate sample means
def calculate_sample_means(data, variable, sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        sample = data[variable].dropna().sample(sample_size, replace=True)
        sample_means.append(sample.mean())
    return sample_means

# Parameters
sample_size = 50  # Increase sample size
num_samples = 2000  # Increase number of samples

# Calculate sample means
sample_means = calculate_sample_means(data, variable, sample_size, num_samples)

# Plot the distribution of sample means
plt.figure(figsize=(10, 6))
sns.histplot(sample_means, kde=False)
plt.title(f'Distribution of Sample Means ({variable})')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.savefig(os.path.join(output_dir, 'sample_means_distribution.png'))
plt.show()

# Plot the distribution of sample means with the normal distribution overlay
plt.figure(figsize=(10, 6))
sns.histplot(sample_means, kde=False, stat='density', label='Sample Means Distribution')
mean_sample_means = np.mean(sample_means)
std_sample_means = np.std(sample_means)
x = np.linspace(mean_sample_means - 4*std_sample_means, mean_sample_means + 4*std_sample_means, 1000)
plt.plot(x, norm.pdf(x, mean_sample_means, std_sample_means), 'r-', lw=2, label='Normal Distribution of Sample Means')
plt.title(f'Distribution of Sample Means with Normal Distribution Overlay ({variable})')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.legend()

# Add expected mean and standard deviation values
expected_mean = mean_sample_means
expected_std = std_sample_means * np.sqrt(sample_size) 
plt.axvline(expected_mean, color='k', linestyle='dashed', linewidth=1)
plt.text(expected_mean + expected_mean*0.02, plt.ylim()[1]*0.9, f'Expected Mean: {expected_mean:.2f}', color='k')
plt.text(expected_mean + expected_mean*0.02, plt.ylim()[1]*0.85, f'Expected SD: {expected_std:.2f}', color='k')

# Add actual mean and standard deviation values for the data
actual_mean = np.mean(data[variable].dropna())
actual_std = np.std(data[variable].dropna(), ddof=0)
plt.axvline(actual_mean, color='b', linestyle='dashed', linewidth=1)
plt.text(actual_mean + actual_mean*0.02, plt.ylim()[1]*0.8, f'Actual Mean: {actual_mean:.2f}', color='b')
plt.text(actual_mean + actual_mean*0.02, plt.ylim()[1]*0.75, f'Actual SD: {actual_std:.2f}', color='b')

plt.savefig(os.path.join(output_dir, 'sample_means_with_expected_and_actual_values.png'))
plt.show()
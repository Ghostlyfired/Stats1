import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Sleep_Efficiency_no_dates.csv')  # Ensure the file path is correct

# Specify the column you want to use for the pie chart
attribute_column = 'Awakenings'  # Replace with the actual column name

# Count the occurrences of each unique value in the column and sort it by index (i.e., the sleep duration values)
value_counts = df[attribute_column].value_counts().sort_index()  # Sort values by category

# Create the pie chart
plt.figure(figsize=(8, 8))  # Adjust figure size if needed
wedges, _, autotexts = plt.pie(
    value_counts, 
    labels=None,  # No labels on slices
    autopct='%1.1f%%',  # Show only percentages
    startangle=140, 
    wedgeprops={'edgecolor': 'black'}  # Add borders for better visibility
)

# Add a title
plt.title(f'Number of {attribute_column}')

# Add a sorted legend
plt.legend(wedges, value_counts.index, title=attribute_column, loc="best")

# Ensure the pie chart is a circle
plt.axis('equal')

# Show the chart
plt.show()

import pandas as pd
import numpy as np

# Create a sample DataFrame with some missing values
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': np.random.randn(5),
    'D': np.random.randn(5)
})

print("Initial DataFrame:\n", df)

# Descriptive Statistics

# Using describe() to get a summary of the statistics
# This includes count, mean, std, min, quartiles, and max
print("\nDescriptive Statistics:\n", df.describe())

# Calculate mean of each numeric column
print("\nMean of each column:\n", df.mean())

# Calculate median of each numeric column
print("\nMedian of each column:\n", df.median())

# Find the minimum value in each column
print("\nMinimum value in each column:\n", df.min())

# Find the maximum value in each column
print("\nMaximum value in each column:\n", df.max())

# Handling Missing Data

# Check for missing values in each column
print("\nMissing data in each column:\n", df.isnull().sum())

# Fill missing values with a specified value (e.g., the mean of the column)
df['A'].fillna(value=df['A'].mean(), inplace=True)
print("\nDataFrame after filling missing values in column 'A':\n", df)

# Alternatively, you could drop rows with missing data (commented out for demonstration)
df.dropna(inplace=True)

# This script demonstrates how to perform basic descriptive statistical analysis and handle missing data,
# which are essential tasks in data cleaning and preparation for further analysis.

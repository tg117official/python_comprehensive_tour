# Importing the Pandas library
import numpy as np
import pandas as pd

# Pandas Overview:
#   Pandas is a powerful library for data analysis and manipulation in Python.
#   It provides high-performance, easy-to-use data structures, and data analysis
#   tools.
#   Unlike NumPy which handles only numerical data,
#   Pandas supports heterogeneous data with its two primary data structures:
#   Series and DataFrame.

# Key Features of Pandas:

# 1. Handling of data in different formats: The ability to read and write data in many
# formats such as CSV, Excel, SQL databases, and HDF5 format.

# Example of reading from a CSV file
data = pd.read_csv('data/cr.txt')  # Ensure you have a file path or URL here
print(data)

# 2. Sophisticated Indexing: Offers indexed data manipulation.
# This includes support for automatic and explicit data alignment.
# Create a simple DataFrame
df = pd.DataFrame({
    'A': range(1, 5),
    'B': pd.date_range('20230101', periods=4),
    'C': pd.Series([3] * 4, dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

# Displaying the DataFrame
print(df)

# 3. Data alignment: Critical for data analysis and missing data handling.
# Pandas automatically aligns data based on labels.
# Create another DataFrame to demonstrate alignment
df2 = pd.DataFrame({
    'A': range(1, 6),
    'B': pd.date_range('20230101', periods=5)
})


# Using boolean indexing to find common dates
common_dates = df[df['B'].isin(df2['B'])]['B']

# Displaying the result
print("\nCommon dates between df and df2:\n", common_dates)


# 4. Powerful data manipulation tools for cleaning, filtering, and transforming data: Includes filling missing values, merging and joining data.
# Example of merging two DataFrames
merged_df = pd.merge(df, df2, on='A', how='inner')  # Merge based on column 'A'

# Display merged DataFrame
print("Merged DataFrame:\n", merged_df)

# This script serves as a basic introduction to what Pandas is and its essential capabilities,
# ideal for a brief overview in a teaching session.

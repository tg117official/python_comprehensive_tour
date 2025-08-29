import pandas as pd
import numpy as np

# Creating DataFrames from various sources

# 1. From a CSV file (commented for demonstration purposes, use an actual file path to test)
df_from_csv = pd.read_csv('path_to_file.csv')
print("DataFrame from CSV:\n", df_from_csv.head())

# 2. From a dictionary of lists (each list becomes a column in the DataFrame)
df_from_dict = pd.DataFrame({
    'A': range(1, 6),
    'B': pd.date_range('20230101', periods=5),
    'C': pd.Series(1, index=list(range(5)), dtype='float32'),
    'D': np.array([3] * 5, dtype='int32')
})
print("DataFrame from a dictionary of lists:\n", df_from_dict)

# 3. From a list of lists (each list becomes a row in the DataFrame)
df_from_list = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], columns=['X', 'Y', 'Z'])
print("DataFrame from a list of lists:\n", df_from_list)

# Viewing data using head() and tail()

# Display the first few rows of the DataFrame
print("First 3 rows of the DataFrame:\n", df_from_dict.head(3))

# Display the last few rows of the DataFrame
print("Last 2 rows of the DataFrame:\n", df_from_dict.tail(2))

# Accessing and selecting data

# Access a single column using column name
column_a = df_from_dict['A']
print("Column A:\n", column_a)

# Select multiple columns
multiple_columns = df_from_dict[['A', 'B']]
print("Multiple Columns (A and B):\n", multiple_columns)

# Access rows by integer location using iloc
row_at_index_2 = df_from_dict.iloc[2]
print("Row at index 2:\n", row_at_index_2)

# Access a slice of rows using iloc
slice_of_rows = df_from_dict.iloc[1:4]
print("Slice of rows from index 1 to 3:\n", slice_of_rows)

# Access a specific value using iloc
specific_value = df_from_dict.iloc[2, 1]  # Row 2, Column 1
print("Specific value at Row 2, Column 1:\n", specific_value)

# Access rows and columns by labels using loc
row_with_label = df_from_dict.loc[1, 'B']
print("Value at index 1 for column 'B':\n", row_with_label)

# This script showcases how to create DataFrames from various sources,
# view subsets of the data, and access specific elements efficiently,
# which are crucial for data manipulation and exploration in Pandas.

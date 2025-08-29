import pandas as pd
import numpy as np

# Introduction to Pandas Series:
# A Series is a one-dimensional array with axis labels, capable of holding any data type.

# Creating a Series from a list
series_from_list = pd.Series([1, 2, 3, 4, 5])
print("Series from a list:\n", series_from_list)

# Creating a Series from a dictionary
# The keys of the dictionary become the index labels of the Series.
series_from_dict = pd.Series({'a': 1, 'b': 2, 'c': 3})
print("Series from a dictionary:\n", series_from_dict)

# Creating a Series from a scalar value
# When creating from a scalar, an index must be provided to match the length.
series_from_scalar = pd.Series(5, index=[0, 1, 2, 3])
print("Series from a scalar value:\n", series_from_scalar)

# Introduction to Pandas DataFrame:
# A DataFrame is a two-dimensional, size-mutable, potentially heterogeneous tabular data structure.

# Creating a DataFrame from a list of dictionaries
# Each dictionary turns into a row in the DataFrame.
df_from_list_dict = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}])
print("DataFrame from a list of dictionaries:\n", df_from_list_dict)

# Creating a DataFrame from a dictionary of Series
# Each Series becomes a column in the DataFrame.
dict_of_series = {'one': pd.Series([1., 2., 3.]), 'two': pd.Series([1., 2., 3., 4.])}
df_from_dict_series = pd.DataFrame(dict_of_series)
print("DataFrame from a dictionary of Series:\n", df_from_dict_series)

# Creating a DataFrame from a 2D NumPy array
# Optionally, specific column names and index labels can be set.
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
df_from_2d_array = pd.DataFrame(array_2d, columns=['first', 'second', 'third'], index=['row1', 'row2'])
print("DataFrame from a 2D NumPy array:\n", df_from_2d_array)

# This script provides examples of how Pandas can be used to create Series and DataFrames from various types of data sources,
# demonstrating its flexibility and ease of use for data manipulation and analysis.

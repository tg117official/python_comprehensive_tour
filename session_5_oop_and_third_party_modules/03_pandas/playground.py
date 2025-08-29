import pandas as pd


# Set display option to show all columns
pd.set_option('display.max_columns', None)

# If you want to ensure that all rows are displayed as well, use:
# pd.set_option('display.max_rows', None)

# # Reset display options to default
# pd.reset_option('display.max_columns')
# # pd.reset_option('display.max_rows')  # To reset row display limit as well

# Task 1: Load the Excel file into a Pandas DataFrame
df = pd.read_excel('data/employee.xlsx')

print(df)
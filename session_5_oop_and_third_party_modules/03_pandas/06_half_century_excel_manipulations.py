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
# The above line reads the Excel file into a DataFrame.
# Make sure the file 'employee_data.xlsx' is in your working directory.

# Task 2: Display the first 5 rows of the DataFrame
print("First 5 rows of the DataFrame:\n", df.head())
# head() shows the first 5 rows by default.

# Task 3: Check for missing values in the DataFrame
print("\nMissing values in each column:\n", df.isnull().sum())
# isnull().sum() gives a count of missing values in each column.

# Task 4: Fill missing salary values with the median salary
df['salary'] = df['salary'].fillna(df['salary'].median())
# fillna() replaces missing values with the median value of the 'salary' column.

# Task 5: Convert the 'salary' column to integer type
df['salary'] = df['salary'].astype(int)
# astype(int) converts the 'salary' column to integer type.

# Task 6: Remove duplicate rows based on the 'email' column
df = df.drop_duplicates(subset=['email'])
# drop_duplicates() removes any duplicate rows based on the 'email' column.

# Task 7: Create a new column 'full_name' by concatenating 'first_name' and 'last_name'
df['full_name'] = df['first_name'] + ' ' + df['last_name']
# This creates a new column 'full_name' by concatenating 'first_name' and 'last_name' with a space in between.

# Task 8: Sort the DataFrame by 'salary' in descending order
df = df.sort_values(by='salary', ascending=False)
# sort_values() sorts the DataFrame by the 'salary' column in descending order.

# Task 9: Filter the DataFrame for employees with a salary greater than 50,000
high_salary_df = df[df['salary'] > 50000]
print("\nEmployees with salary greater than 50,000:\n", high_salary_df)
# This filters the DataFrame to include only rows where 'salary' is greater than 50,000.

# Task 10: Group the DataFrame by 'dept' and calculate the mean salary for each department
dept_salary_mean = df.groupby('dept')['salary'].mean()
print("\nMean salary by department:\n", dept_salary_mean)
# groupby() groups the DataFrame by 'dept', and mean() calculates the average salary in each department.

# Task 11: Add a new column 'tax' that is 10% of the 'salary'
df['tax'] = df['salary'] * 0.10
# This creates a new column 'tax' where each value is 10% of the corresponding 'salary'.

# Task 12: Rename the column 'dept' to 'department'
df = df.rename(columns={'dept': 'department'})
# rename() is used to change the name of the 'dept' column to 'department'.

# Task 13: Save the modified DataFrame to a new Excel file
df.to_excel('modified_employee_data.xlsx', index=False)
# to_excel() saves the DataFrame to a new Excel file called 'modified_employee_data.xlsx'.
# index=False prevents the DataFrame index from being saved to the file.

# Task 14: Calculate the total salary paid across all employees
total_salary = df['salary'].sum()
print("\nTotal salary paid to all employees:", total_salary)
# sum() calculates the total sum of the 'salary' column.

# Task 15: Create a pivot table that shows the average salary per department
pivot_table = df.pivot_table(values='salary', index='department', aggfunc='mean')
print("\nPivot table showing average salary per department:\n", pivot_table)
# pivot_table() creates a pivot table where the average salary is calculated for each department.

# Task 16: Count the number of employees in each department
dept_employee_count = df.groupby('department').size()
print("\nNumber of employees in each department:\n", dept_employee_count)
# groupby() and size() are used together to count the number of employees in each department.

# Task 17: Find the employee with the highest salary
highest_salary_employee = df[df['salary'] == df['salary'].max()]
print("\nEmployee with the highest salary:\n", highest_salary_employee)
# max() finds the maximum salary, and this is used to filter the DataFrame to find the corresponding employee.

# Task 18: Filter the DataFrame for employees whose first name starts with 'A'
employees_start_with_a = df[df['first_name'].str.startswith('A')]
print("\nEmployees whose first name starts with 'A':\n", employees_start_with_a)
# str.startswith() filters the DataFrame for rows where 'first_name' starts with 'A'.

# Task 19: Calculate the sum of salaries for each department
dept_salary_sum = df.groupby('department')['salary'].sum()
print("\nTotal salary by department:\n", dept_salary_sum)
# groupby() with sum() calculates the total salary paid in each department.

# Task 20: Filter out employees with a salary less than 30,000
df = df[df['salary'] >= 30000]
print("\nDataFrame after filtering out employees with salary less than 30,000:\n", df)
# This filters the DataFrame to keep only employees with a salary of 30,000 or more.

# Task 21: Add a new column 'bonus' where each employee gets 5% of their salary as a bonus
df['bonus'] = df['salary'] * 0.05
print("\nDataFrame with bonus column added:\n", df)
# A new column 'bonus' is added, calculated as 5% of the salary.

# Task 22: Order the DataFrame by 'full_name' alphabetically
df = df.sort_values(by='full_name')
print("\nDataFrame ordered by full_name:\n", df)
# sort_values() is used to order the DataFrame by 'full_name' alphabetically.

# Task 23: Reset the index of the DataFrame
df = df.reset_index(drop=True)
print("\nDataFrame with reset index:\n", df)
# reset_index(drop=True) resets the index to a default integer index, and drop=True avoids adding the old index as a column.

# Task 24: Calculate the average salary for employees with 'test' in their 'department' name
average_test_salary = df[df['department'].str.contains('test')]['salary'].mean()
print("\nAverage salary for 'test' department employees:\n", average_test_salary)
# str.contains() filters the DataFrame for rows where 'department' contains 'test', and then mean() calculates the average salary.

# Task 25: Create a new column 'salary_bracket' to categorize employees into 'Low', 'Medium', and 'High' salary brackets
df['salary_bracket'] = pd.cut(df['salary'], bins=[0, 40000, 60000, float('inf')], labels=['Low', 'Medium', 'High'])
print("\nDataFrame with salary_bracket column:\n", df)
# pd.cut() is used to categorize 'salary' into different brackets.

# Task 26: Group by 'salary_bracket' and calculate the average bonus for each bracket
bracket_bonus_mean = df.groupby('salary_bracket')['bonus'].mean()
print("\nAverage bonus by salary bracket:\n", bracket_bonus_mean)
# groupby() with mean() calculates the average bonus for each salary bracket.

# Task 27: Select only the 'full_name', 'email', and 'salary' columns
selected_columns = df[['full_name', 'email', 'salary']]
print("\nSelected columns (full_name, email, salary):\n", selected_columns)
# This selects specific columns from the DataFrame.

# Task 28: Find all employees with a bonus greater than 2000
high_bonus_employees = df[df['bonus'] > 2000]
print("\nEmployees with a bonus greater than 2000:\n", high_bonus_employees)
# This filters the DataFrame to find employees whose 'bonus' is greater than 2000.

# Task 29: Find the department with the most employees
dept_most_employees = dept_employee_count.idxmax()
print("\nDepartment with the most employees:", dept_most_employees)
# idxmax() finds the index of the maximum value in the series, which corresponds to the department with the most employees.

# Task 30: Rename the 'salary_bracket' column to 'income_bracket'
df = df.rename(columns={'salary_bracket': 'income_bracket'})
print("\nDataFrame with 'salary_bracket' renamed to 'income_bracket':\n", df)
# rename() changes the name of the 'salary_bracket' column to 'income_bracket'.


# Assuming you have already loaded the original employee DataFrame (df)
# and have completed the previous tasks

# Creating a second DataFrame (df2) that can be joined with the original DataFrame (df)
df2 = pd.DataFrame({
    'eid': [1, 2, 3, 4, 5, 6],  # Employee IDs
    'dept': ['HR', 'Finance', 'IT', 'Marketing', 'Finance', 'HR'],  # Department names
    'location': ['New York', 'San Francisco', 'Los Angeles', 'Boston', 'San Francisco', 'New York'],  # Office locations
    'manager_id': [101, 102, 103, 104, 102, 101]  # Manager IDs
})

print("Second DataFrame (df2):\n", df2)

# Join Exercises

# Task 31: Inner Join on 'eid'
inner_join = df.merge(df2, on='eid', how='inner')
print("\nInner join on 'eid':\n", inner_join)
# Inner join merges df and df2 on 'eid', keeping only rows where 'eid' is present in both DataFrames.

# Task 32: Left Join on 'eid'
left_join = df.merge(df2, on='eid', how='left')
print("\nLeft join on 'eid':\n", left_join)
# Left join merges df and df2 on 'eid', keeping all rows from df and filling with NaNs where df2 has no matching 'eid'.

# Task 33: Right Join on 'eid'
right_join = df.merge(df2, on='eid', how='right')
print("\nRight join on 'eid':\n", right_join)
# Right join merges df and df2 on 'eid', keeping all rows from df2 and filling with NaNs where df has no matching 'eid'.

# Task 34: Outer Join on 'eid'
outer_join = df.merge(df2, on='eid', how='outer')
print("\nOuter join on 'eid':\n", outer_join)
# Outer join merges df and df2 on 'eid', keeping all rows from both DataFrames and filling with NaNs where there are no matches.

# Task 35: Inner Join on 'dept'
inner_join_dept = df.merge(df2, on='dept', how='inner')
print("\nInner join on 'dept':\n", inner_join_dept)
# Inner join on 'dept' where rows are merged based on department names.

# Task 36: Left Join on 'dept'
left_join_dept = df.merge(df2, on='dept', how='left')
print("\nLeft join on 'dept':\n", left_join_dept)
# Left join on 'dept', keeping all rows from df.

# Task 37: Right Join on 'dept'
right_join_dept = df.merge(df2, on='dept', how='right')
print("\nRight join on 'dept':\n", right_join_dept)
# Right join on 'dept', keeping all rows from df2.

# Task 38: Outer Join on 'dept'
outer_join_dept = df.merge(df2, on='dept', how='outer')
print("\nOuter join on 'dept':\n", outer_join_dept)
# Outer join on 'dept', keeping all rows from both DataFrames.

# Task 39: Cross Join (Cartesian product)
cross_join = df.merge(df2, how='cross')
print("\nCross join (Cartesian product):\n", cross_join)
# Cross join combines each row of df with each row of df2.

# Task 40: Left Join on 'eid' with specific columns from df2
left_join_select = df.merge(df2[['eid', 'location']], on='eid', how='left')
print("\nLeft join on 'eid' with specific columns (eid, location) from df2:\n", left_join_select)
# Left join with only 'eid' and 'location' columns from df2.

# Task 41: Joining df2 with df on multiple keys ('eid' and 'dept')
multi_key_join = df.merge(df2, on=['eid', 'dept'], how='inner')
print("\nJoin on multiple keys ('eid' and 'dept'):\n", multi_key_join)
# Inner join using both 'eid' and 'dept' as keys.

# Task 42: Filter rows from the join where 'location' is 'New York'
filtered_join = inner_join[inner_join['location'] == 'New York']
print("\nFiltered rows from inner join where location is 'New York':\n", filtered_join)
# Filtering the result of an inner join to keep only rows where 'location' is 'New York'.

# Task 43: Join and calculate the average salary by department after the join
joined_avg_salary = df.merge(df2, on='dept', how='inner').groupby('dept')['salary'].mean()
print("\nAverage salary by department after join:\n", joined_avg_salary)
# Grouping the result of an inner join by 'dept' and calculating the average salary.

# Task 44: Adding a new column 'team_size' by counting the number of employees in each department
df2['team_size'] = df2.groupby('dept')['eid'].transform('count')
team_size_join = df.merge(df2[['dept', 'team_size']], on='dept', how='left')
print("\nAdding 'team_size' column and joining:\n", team_size_join)
# Adding a new column 'team_size' to df2 and joining it with df.

# Task 45: Left Join on 'eid' and fill missing 'location' with 'Unknown'
left_join_fillna = df.merge(df2[['eid', 'location']], on='eid', how='left').fillna({'location': 'Unknown'})
print("\nLeft join on 'eid' and fill missing 'location' with 'Unknown':\n", left_join_fillna)
# Filling missing 'location' values with 'Unknown' after a left join.

# Task 46: Join and create a new column 'is_manager' to indicate if 'eid' is a manager
df['is_manager'] = df['eid'].isin(df2['manager_id'])
print("\nDataFrame with 'is_manager' column:\n", df)
# Creating a new column 'is_manager' to indicate if 'eid' is a manager.

# Task 47: Join and calculate the total salary by location
total_salary_by_location = df.merge(df2, on='eid', how='inner').groupby('location')['salary'].sum()
print("\nTotal salary by location:\n", total_salary_by_location)
# Calculating the total salary paid in each location after the join.

# Task 48: Self-join df2 to find pairs of employees in the same department
self_join = df2.merge(df2, on='dept', how='inner', suffixes=('_emp1', '_emp2'))
print("\nSelf-join to find pairs of employees in the same department:\n", self_join)
# Self-join to find pairs of employees who are in the same department.

# Task 49: Join df and df2, then drop rows with missing 'manager_id'
inner_join_dropna = df.merge(df2, on='eid', how='inner').dropna(subset=['manager_id'])
print("\nInner join and drop rows with missing 'manager_id':\n", inner_join_dropna)
# Dropping rows with missing 'manager_id' after an inner join.

# Task 50: Join and reorder columns to bring 'location' and 'manager_id' to the front
reordered_columns = df.merge(df2, on='eid', how='inner')[['location', 'manager_id'] + df.columns.tolist()]
print("\nJoin and reorder columns to bring 'location' and 'manager_id' to the front:\n", reordered_columns)
# Reordering columns after the join to bring 'location' and 'manager_id' to the front.

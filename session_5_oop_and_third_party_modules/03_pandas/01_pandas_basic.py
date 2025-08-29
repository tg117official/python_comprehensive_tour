import pandas as pd

# Exercise 1: Creating a DataFrame
# Problem: Create a DataFrame with columns "Name", "Age", and "City" using a dictionary.
# Relevance: Learn how to create and view data in a tabular format.
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print("Exercise 1: Create a DataFrame")
print(df, "\n")

# Exercise 2: Filtering Rows
# Problem: Filter rows where "Age" is greater than 30.
# Relevance: Understand how to filter data based on conditions.
filtered_df = df[df["Age"] > 30]
print("Exercise 2: Filter rows where Age > 30")
print(filtered_df, "\n")

# Exercise 3: Adding a New Column
# Problem: Add a new column "Salary" with values [50000, 60000, 70000, 80000].
# Relevance: Modify and expand your DataFrame dynamically.
df["Salary"] = [50000, 60000, 70000, 80000]
print("Exercise 3: Add a new column 'Salary'")
print(df, "\n")

# Exercise 4: Sorting Data
# Problem: Sort the DataFrame by "Age" in descending order.
# Relevance: Learn how to organize data based on a column.
sorted_df = df.sort_values(by="Age", ascending=False)
print("Exercise 4: Sort DataFrame by Age (descending)")
print(sorted_df, "\n")

# Exercise 5: Handling Missing Data
# Problem: Replace the value of "City" for "Bob" with NaN, then fill it with "Unknown".
# Relevance: Handle missing or incomplete data in a dataset.
df.loc[1, "City"] = None
df["City"].fillna("Unknown", inplace=True)
print("Exercise 5: Handle missing data")
print(df, "\n")

# Exercise 6: Grouping and Aggregation
# Problem: Group by "City" and calculate the average "Age".
# Relevance: Perform group-level aggregations for data analysis.
grouped_df = df.groupby("City")["Age"].mean()
print("Exercise 6: Group by City and calculate average Age")
print(grouped_df, "\n")

# Exercise 7: Merging DataFrames
# Problem: Merge the current DataFrame with another DataFrame containing "Name" and "Department".
# Relevance: Combine datasets from multiple sources.
department_data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "Finance", "Marketing"]
})
merged_df = pd.merge(df, department_data, on="Name")
print("Exercise 7: Merge DataFrames on Name")
print(merged_df, "\n")

# Exercise 8: Dropping Columns
# Problem: Drop the "Salary" column from the DataFrame.
# Relevance: Learn how to remove unnecessary data from a DataFrame.
dropped_df = merged_df.drop(columns=["Salary"])
print("Exercise 8: Drop the 'Salary' column")
print(dropped_df, "\n")

# Exercise 9: Reading and Writing Files
# Problem: Write the DataFrame to a CSV file and read it back.
# Relevance: Save and load data for persistent storage.
df.to_csv("output.csv", index=False)
read_df = pd.read_csv("output.csv")
print("Exercise 9: Write and read DataFrame to/from CSV")
print(read_df, "\n")

# Exercise 10: Applying Functions
# Problem: Create a new column "Age Group" based on "Age" (e.g., "Young", "Mid", "Senior").
# Relevance: Apply custom functions to manipulate data.
def age_group(age):
    if age < 30:
        return "Young"
    elif age < 40:
        return "Mid"
    else:
        return "Senior"

df["Age Group"] = df["Age"].apply(age_group)
print("Exercise 10: Apply function to create Age Group column")
print(df, "\n")

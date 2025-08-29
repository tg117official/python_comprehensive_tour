import pandas as pd
import os

# Ensure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# Step 1: Define the initial data
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Department": ["HR", "IT", "Finance"]
}
df = pd.DataFrame(data)

# Step 2: Write DataFrame to CSV
csv_path = "data/data.csv"
df.to_csv(csv_path, index=False)
print(f"Data written to CSV: {csv_path}")

# Step 3: Create DataFrame from CSV and write to Excel
excel_path = "data/data.xlsx"
df_from_csv = pd.read_csv(csv_path)
df_from_csv.to_excel(excel_path, index=False)
print(f"Data written to Excel: {excel_path}")

# Step 4: Read Excel to create DataFrame and write to JSON
json_path = "data/data.json"
df_from_excel = pd.read_excel(excel_path)
df_from_excel.to_json(json_path, orient="records", lines=True)
print(f"Data written to JSON: {json_path}")

# Step 5: Read JSON to create DataFrame and write to Parquet
parquet_path = "data/data.parquet"
df_from_json = pd.read_json(json_path, orient="records", lines=True)
df_from_json.to_parquet(parquet_path, index=False)
print(f"Data written to Parquet: {parquet_path}")

# Step 6: Read Parquet to create DataFrame and write to Text
text_path = "data/data.txt"
df_from_parquet = pd.read_parquet(parquet_path)
df_from_parquet.to_csv(text_path, index=False, sep="|")
print(f"Data written to Text: {text_path}")

# Step 7: Read Text to create DataFrame and write to Pickle
pickle_path = "data/data.pkl"
df_from_text = pd.read_csv(text_path, sep="|")
df_from_text.to_pickle(pickle_path)
print(f"Data written to Pickle: {pickle_path}")

# Step 8: Read Pickle to create DataFrame
df_from_pickle = pd.read_pickle(pickle_path)
print("\nFinal DataFrame created from Pickle:")
print(df_from_pickle)


# pip install openpyxl
# pip install pyarrow
# pip install fastparquet



### Pickle in Python**

# What is Pickle?
# Pickle is a Python module used for **serializing** and **deserializing** Python objects, meaning it converts objects into a byte stream (serialization) for storage or transmission and reconstructs them back into Python objects (deserialization).
#
# ---
#
# Purpose:
# 1. Save complex Python objects (e.g., lists, dictionaries, DataFrames) to a file for later use.
# 2. Transfer Python objects between systems or over a network.
# 3. Store objects in a binary format, preserving their state.

#
# import pickle
#
# # Serialize
# with open("data.pkl", "wb") as f:
#     pickle.dump({"key": "value"}, f)
#
# # Deserialize
# with open("data.pkl", "rb") as f:
#     data = pickle.load(f)
# print(data)  # Output: {'key': 'value'}


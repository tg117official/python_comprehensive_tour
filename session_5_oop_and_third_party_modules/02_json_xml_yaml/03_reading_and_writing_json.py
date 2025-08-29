# Import the json module to work with JSON data
import json

# Define a Python dictionary that we want to write to a file.
data = {
    "name": "Bob",
    "age": 30,
    "is_student": False,
    "skills": ["Java", "Data Analysis"]
}

# Open a new file in write mode ('w') and name it 'data.json'
with open('data/my_json_data.json', 'w') as file:
    # Use json.dump() to write the dictionary to the file in JSON format.
    # We pass two arguments: the data to serialize and the file object.
    json.dump(data, file)

# Now, let's read the JSON data back into a Python dictionary.
# Open the file in read mode ('r') and read from 'data.json'
with open('data/my_json_data.json', 'r') as file:
    # Use json.load() to load the JSON data from the file and convert it into a Python dictionary.
    data_loaded = json.load(file)

# Print the data loaded from the file
print(data_loaded)

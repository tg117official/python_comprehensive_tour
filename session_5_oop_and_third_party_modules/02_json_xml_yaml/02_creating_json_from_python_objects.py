# Import the json module to work with JSON data
import json

# Define a Python dictionary. Dictionaries in Python are similar to objects in JSON.
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "skills": ["Python", "Machine Learning"]
}

# JSON serialization
# Use json.dumps() to convert the Python dictionary into a JSON string.
# The function dumps stands for "dump string".
json_string = json.dumps(data)

# Print the JSON string
print(json_string)

# JSON deserialization
# Use json.loads() to convert the JSON string back into a Python dictionary.
# The function loads stands for "load string".
python_dict = json.loads(json_string)

# Print the Python dictionary
print(python_dict)

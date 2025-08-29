# Import the json module to work with JSON data
import json

# Example of a Python object to be serialized
data = {
    "name": "Charlie",
    "age": "twenty-five",  # This is intentionally incorrect to demonstrate error handling
    "interests": ["Python", {"sports": "soccer"}]  # Nested data is fine
}

# Try to serialize the Python object to a JSON string
try:
    # Attempt to use json.dumps() to convert the Python dictionary into a JSON string
    json_string = json.dumps(data)
    print("Serialized Data:", json_string)
except TypeError as e:
    # Handle errors that occur if the object is not serializable (e.g., wrong data types)
    print("Serialization Error:", str(e))

# Define a JSON string with an error (missing a closing quote)
json_string_error = '{"name": "Charlie", "age": 25, "is_student": false'

# Try to deserialize the incorrect JSON string
try:
    # Attempt to use json.loads() to parse the JSON string
    result = json.loads(json_string_error)
    print("Deserialized Data:", result)
except json.JSONDecodeError as e:
    # Handle errors that occur if the JSON data is improperly formatted
    print("Decoding JSON Error:", str(e))


# Handling Serialization Errors:
#
# Purpose:
#   We try to convert a Python dictionary to a JSON string using json.dumps().
#   The dictionary contains a value that is not typically serializable
#   ("age": "twenty-five").

# Error Handling:
#   The except TypeError as e block catches and handles TypeError, which is raised
#   if an object is not serializable (like a custom object without a serialization
#   method).

# Output: If an error occurs during serialization, it will print an error message
# detailing why serialization failed.

# Handling Deserialization Errors:
#
# Purpose:
#   We attempt to parse an incorrectly formatted JSON string that lacks a closing
#   quote.
# Error Handling:
#   The except json.JSONDecodeError as e block catches and handles JSONDecodeError,
#   which is raised if the JSON string is not correctly formatted.
# Output:
#   If there's a formatting error in the JSON string, it prints an error message
#   explaining the issue.

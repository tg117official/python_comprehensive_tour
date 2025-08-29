# Import the json module to work with JSON data
import json

# Define a Python dictionary that we will convert to a JSON string.
# This dictionary is intentionally complex to demonstrate the effect of pretty printing.
data = {
    "name": "Diana",
    "age": 28,
    "is_student": False,
    "skills": ["Data Science", "Machine Learning", "Web Development"],
    "education": {
        "bachelor": "Computer Science",
        "master": "Data Science",
        "phd": "Artificial Intelligence"
    }
}

# Convert the dictionary to a JSON string using json.dumps(),
# setting 'indent' to 4 for better readability and 'sort_keys' to True to alphabetize the keys
pretty_json_string = json.dumps(data, indent=4, sort_keys=True)

# Print the prettily formatted JSON string
print(pretty_json_string)

#
# - Importing Module:
#       As always, we start by importing the `json` module to utilize its
#       functionality for handling JSON data.
# - Creating Data:
#       We create a complex dictionary representing a person with various attributes,
#       including nested data.
#       This complexity helps to showcase the benefits of pretty printing.
# - Pretty Printing:
#   - `json.dumps(data, indent=4, sort_keys=True)`:
#           This function call converts the dictionary into a JSON string.
#           The `indent` parameter is set to `4`, which means each level of hierarchy
#           in the JSON will be indented by four spaces, making it easier to read.
#           The `sort_keys` parameter is set to `True`, which sorts the dictionary
#           keys alphabetically before converting it to a JSON string.
# - Outputting Data:
#       The formatted JSON string is then printed out.
#       It will appear well-structured and easy to read, similar to this:
# {
#     "age": 28,
#     "education": {
#         "bachelor": "Computer Science",
#         "master": "Data Science",
#         "phd": "Artificial Intelligence"
#     },
#     "is_student": false,
#     "name": "Diana",
#     "skills": [
#         "Data Science",
#         "Machine Learning",
#         "Web Development"
#     ]
# }
#
#
# This script clearly illustrates how to use the `json.dumps()` function with the
# `indent` and `sort_keys` parameters to enhance the readability of JSON data.
# This technique is particularly useful for logging, debugging, and presenting
# JSON data in a human-friendly format.

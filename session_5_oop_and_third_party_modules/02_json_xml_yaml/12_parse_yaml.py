import yaml


# Define a function to load and parse the YAML file
def load_yaml_file(file_path):
    """
    Load and parse a YAML file safely using yaml.safe_load().

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed data from the YAML file.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Define the path to the YAML configuration file
yaml_file_path = 'data/config.yaml'

# Load the YAML file
config_data = load_yaml_file(yaml_file_path)

# Access and print the data from the YAML file
print("Application Name:", config_data['app']['name'])
print("Application Version:", config_data['app']['version'])
print("Database Host:", config_data['database']['host'])
print("Database Port:", config_data['database']['port'])
print("Database User:", config_data['database']['user'])
print("Enabled Features:", ", ".join(config_data['features']))

# Example output:
# Application Name: SampleApp
# Application Version: 1.0
# Database Host: localhost
# Database Port: 5432
# Database User: admin
# Enabled Features: authentication, logging, monitoring


# Define a function to load and parse the YAML file:
# The load_yaml_file function takes the path to the YAML file as an argument.
# It opens the file in read mode ('r') and uses yaml.safe_load() to parse the file content safely.
# The parsed data is returned as a dictionary.
#
# Load the YAML file:
# The load_yaml_file function is called with the YAML file path to load and parse the YAML file. The parsed data is stored in the config_data variable.
#
# Access and print the data from the YAML file:
# The script accesses various elements of the parsed YAML data (stored in the config_data dictionary) and prints them. The features list is joined into a single string for easier display.

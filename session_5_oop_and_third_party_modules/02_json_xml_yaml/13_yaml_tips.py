import yaml


# Define a function to load and parse the YAML file using safe_load
def load_yaml_file_safely(file_path):
    """
    Load and parse a YAML file safely using yaml.safe_load().

    Safe loading restricts the types of Python objects that can be created
    from the YAML data, providing protection against arbitrary code execution.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed data from the YAML file.
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Define a function to load and parse the YAML file using full_load
def load_yaml_file_fully(file_path):
    """
    Load and parse a YAML file using yaml.full_load().

    Full loading allows all YAML tags and data types to be processed,
    which can include creating arbitrary Python objects. Use with caution.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Parsed data from the YAML file.
    """
    with open(file_path, 'r') as file:
        data = yaml.full_load(file)
    return data


# Define the path to the YAML configuration file
yaml_file_path = 'config.yaml'

# Load the YAML file using safe_load
config_data_safe = load_yaml_file_safely(yaml_file_path)
print("Safe Load:")
print("Application Name:", config_data_safe['app']['name'])
print("Application Version:", config_data_safe['app']['version'])
print("Database Host:", config_data_safe['database']['host'])
print("Database Port:", config_data_safe['database']['port'])
print("Database User:", config_data_safe['database']['user'])
print("Enabled Features:", ", ".join(config_data_safe['features']))

# Load the YAML file using full_load
config_data_full = load_yaml_file_fully(yaml_file_path)
print("\nFull Load:")
print("Application Name:", config_data_full['app']['name'])
print("Application Version:", config_data_full['app']['version'])
print("Database Host:", config_data_full['database']['host'])
print("Database Port:", config_data_full['database']['port'])
print("Database User:", config_data_full['database']['user'])
print("Enabled Features:", ", ".join(config_data_full['features']))

# Tips on maintaining readability and managing large YAML files:
# 1. Use comments to explain complex configurations and document sections.
# 2. Use anchors (&) and aliases (*) to avoid duplication and manage repeated structures.
# 3. Break down large YAML files into multiple smaller files and use !include directives (with a custom loader).
# 4. Maintain consistent indentation and structure to enhance readability.

# Example of using anchors and aliases
extended_config_yaml = """
default_settings: &defaults
  timeout: 30
  retries: 5

app:
  <<: *defaults  # Merge default settings into app
  name: ExtendedApp
  version: 2.0
"""

# Parse the extended YAML configuration
extended_config = yaml.safe_load(extended_config_yaml)
print("\nExtended Config:")
print("Application Name:", extended_config['app']['name'])
print("Application Version:", extended_config['app']['version'])
print("Timeout:", extended_config['app']['timeout'])
print("Retries:", extended_config['app']['retries'])

# Example of breaking down a large YAML file (not executable in this code snippet)
# master_config.yaml
"""
base: !include base_config.yaml
development: !include dev_config.yaml
production: !include prod_config.yaml
"""

def print_details(name, age=None, job=None):
    """Prints details about a person, handling multiple scenarios.

    Args:
        name (str): The person's name.
        age (int, optional): The person's age. Defaults to None.
        job (str, optional): The person's job. Defaults to None.
    """
    details = f"Name: {name}"
    if age:
        details += f", Age: {age}"
    if job:
        details += f", Job: {job}"
    print(details)


# Example usage
print_details("Alice")  # Outputs: Name: Alice
print_details("Bob", age=25)  # Outputs: Name: Bob, Age: 25
print_details("Charlie", job="Engineer")  # Outputs: Name: Charlie, Job: Engineer
print_details("Dana", 34, "Doctor")  # Outputs: Name: Dana, Age: 34, Job: Doctor

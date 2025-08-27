def validate_numbers(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")
    return True

def validate_positive(value):
    if value < 0:
        raise ValueError("Value must be positive")
    return True

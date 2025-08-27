# Utility functions (defaults, *args, **kwargs, recursion, simple validation)
def banner():  # no params
    print("=== Welcome to EduMgr (Student Manager) ===")

def average(*nums):  # *args
    if not nums:
        return None
    total = 0
    for x in nums:
        total = total + x
    return total / len(nums)

def grade_for(avg, scale=(("A", 90), ("B", 75), ("C", 60))):  # default arg + tuple
    if avg >= scale[0][1]:
        return scale[0][0]
    elif avg >= scale[1][1]:
        return scale[1][0]
    elif avg >= scale[2][1]:
        return scale[2][0]
    else:
        return "F"

def full_name(**kwargs):  # **kwargs
    first = kwargs.get("first", "")
    middle = kwargs.get("middle", "")
    last = kwargs.get("last", "")
    title = kwargs.get("title", "")
    # simple concatenation (strings topic)
    name = (title + " " if title else "") + first + (" " + middle if middle else "") + (" " + last if last else "")
    return name.strip()

def factorial(n):  # recursion demo
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def validate_range(label, value, min_val=0, max_val=100):  # default args + raise
    if value < min_val or value > max_val:
        raise ValueError(f"{label} must be between {min_val} and {max_val}. Got {value}.")
    return value

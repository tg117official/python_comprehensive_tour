age = -3
try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Ex6: Age is", age)
except ValueError as e:
    print("Ex6:", e)















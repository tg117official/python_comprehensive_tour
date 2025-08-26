# ============================================================
# Exercise: Take input from user for different datatypes
# Problem:
# 1) Ask the user for:
#    - name (string)
#    - age (integer)
#    - height in meters (float)
#    - are you a student? (yes/no → boolean)
#    - favorite numbers as comma-separated values (e.g., 3,5,7) → list of ints
# 2) Convert each input into the correct datatype.
# 3) Print the collected values and also print their Python types to confirm.
# Notes:
# - input() always returns a string; we convert using int(), float(), etc.
# - For boolean, we'll accept yes/y/no/n (case-insensitive).
# - For the list, we'll split by "," and convert each piece to int.
# - Keep it simple; no loops are required to *use*—we'll use map() for conversion.
# ============================================================

# 1) Collect inputs (they arrive as strings)
name_str = input("Enter your name: ").strip()

age_str = input("Enter your age (e.g., 25): ").strip()
height_str = input("Enter your height in meters (e.g., 1.75): ").strip()
# Yes / yes / YES
student_str = input("Are you a student? (yes/no): ").strip().lower()

nums_str = input("Enter your favorite numbers (comma-separated, e.g., 3,5,7): ").strip()

# 2) Convert to target types
# String stays string
name = name_str

# Convert to int and float
age = int(age_str)            # e.g., "25" -> 25
height = float(height_str)    # e.g., "1.75" -> 1.75

# Convert to boolean based on yes/no
is_student = (student_str in ("y", "yes", "true", "t", "1"))

# Convert comma-separated to list of ints
# Split into pieces, strip spaces, then map to int
nums_pieces = [piece.strip() for piece in nums_str.split(",")] if nums_str else []
favorite_numbers = list(map(int, filter(None, nums_pieces)))  # removes empty pieces, converts to int

# 3) Print values and their types (confirmation)
print("\n--- Summary ---")
print(f"Name: {name} \t(Type: {type(name).__name__})")
print(f"Age: {age} \t(Type: {type(age).__name__})")
print(f"Height (m): {height} \t(Type: {type(height).__name__})")
print(f"Is Student: {is_student} \t(Type: {type(is_student).__name__})")
print(f"Favorite Numbers: {favorite_numbers} \t(Type: {type(favorite_numbers).__name__})")

# Optional: Simple derived output using the values
bmi_weight_example = 70.0  # pretend weight for demo
bmi_example = bmi_weight_example / (height ** 2)
print(f"\nExample BMI (with 70kg): {bmi_example:.1f}")

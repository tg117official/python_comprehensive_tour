# ===============================================
# Beginner Exercises — Variables Only (with solutions)
# ===============================================

# -------------------------------------------------
# Exercise 1: Full Name Greeting
# Problem: Create variables first_name and last_name, combine into full_name,
# and print: "Hello, <full_name>!"
# -------------------------------------------------
first_name = "Sandeep"
last_name = "Patil"
full_name = first_name + " " + last_name
print("Hello,", full_name)  # Expected: Hello, Sandeep Patil

# -------------------------------------------------
# Exercise 2: Age in the Future
# Problem: Store your current age in a variable. Create another variable that
# is your age after 5 years and print both.
# -------------------------------------------------
age_now = 28
age_in_5 = age_now + 5
print("Current age:", age_now)       # Expected: 28
print("Age after 5 years:", age_in_5)  # Expected: 33

# -------------------------------------------------
# Exercise 3: Rectangle Area
# Problem: Store length and width in variables. Create area = length * width.
# Print the area.
# -------------------------------------------------
length = 10
width = 4
area = length * width
print("Rectangle area:", area)  # Expected: 40

# -------------------------------------------------
# Exercise 4: Simple Shopping Total
# Problem: Store prices of items in variables (e.g., eggs, milk, bread).
# Add them to get total and print it.
# -------------------------------------------------
price_eggs = 60.0
price_milk = 45.5
price_bread = 40.0
total_bill = price_eggs + price_milk + price_bread
print("Total bill:", total_bill)  # Expected: 145.5

# -------------------------------------------------
# Exercise 5: Celsius to Fahrenheit
# Problem: Store a temperature in Celsius and convert to Fahrenheit using:
# F = (C * 9/5) + 32. Print both.
# -------------------------------------------------
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print("Celsius:", celsius)          # Expected: 30
print("Fahrenheit:", fahrenheit)    # Expected: 86.0

# -------------------------------------------------
# Exercise 6: Swap Two Variables (using a temporary variable)
# Problem: Given a = 5 and b = 9, swap their values using a third variable.
# Print before and after.
# -------------------------------------------------
a = 5
b = 9
print("Before swap -> a:", a, "b:", b)  # Expected: a: 5 b: 9
temp = a
a = b
b = temp
print("After swap  -> a:", a, "b:", b)  # Expected: a: 9 b: 5

# -------------------------------------------------
# Exercise 7: Running Counter (reassignment)
# Problem: Start counter at 0. Increase it step by step and print after each change.
# -------------------------------------------------
counter = 0
print("Counter:", counter)  # Expected: 0
counter = counter + 1
print("Counter:", counter)  # Expected: 1
counter = counter + 2
print("Counter:", counter)  # Expected: 3
counter = counter + 5
print("Counter:", counter)  # Expected: 8

# -------------------------------------------------
# Exercise 8: Multiple Assignment (Date)
# Problem: Put day=15, month="Aug", year=2025 in variables (in one line),
# then print a simple date string "15-Aug-2025".
# -------------------------------------------------
day, month, year = 15, "Aug", 2025
date_string = str(day) + "-" + month + "-" + str(year)
print("Date:", date_string)  # Expected: 15-Aug-2025

# -------------------------------------------------
# Exercise 9: Build a Message from Parts
# Problem: Create variables greeting, name, and punctuation,
# then combine them into one message and print it.
# -------------------------------------------------
greeting = "Good morning"
name = "Student"
punct = "!"
message = greeting + ", " + name + punct
print(message)  # Expected: Good morning, Student!

# -------------------------------------------------
# Exercise 10: Price with Tax (constants-style variable)
# Problem: Given BASE_PRICE and TAX_RATE, compute final_price = BASE_PRICE + (BASE_PRICE * TAX_RATE).
# Print final_price.
# -------------------------------------------------
BASE_PRICE = 1000.0  # uppercase to show it should not change (convention)
TAX_RATE = 0.18      # 18% tax
final_price = BASE_PRICE + (BASE_PRICE * TAX_RATE)
print("Final price with tax:", final_price)  # Expected: 1180.0

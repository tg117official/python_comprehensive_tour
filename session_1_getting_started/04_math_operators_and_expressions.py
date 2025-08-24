# ============================================================
# Short Notes — Math Operators & Expressions (Python)
# ------------------------------------------------------------
# +  addition          -  subtraction
# *  multiplication    /  true division (returns float)
# // floor division    %  modulus (remainder)
# ** exponent (power)  () parentheses control order
# Precedence (high → low): **, unary +/-, *, /, //, %, then +, -
# Tip: / always returns float; // floors toward -infinity; use round(x, 2) for 2 decimals.
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Add & Subtract
# Problem: Given a=15, b=4, print their sum and difference.
# ------------------------------------------------------------
a = 15
b = 4
sum_ab = a + b
diff_ab = a - b
print("Ex1:", sum_ab, diff_ab)  # Expected: 19 11


# ------------------------------------------------------------
# Exercise 2: Multiply & Divide
# Problem: Given x=12, y=5, print x*y and x/y.
# ------------------------------------------------------------
x = 12
y = 5
prod = x * y
quot = x / y
print("Ex2:", prod, quot)  # Expected: 60 2.4


# ------------------------------------------------------------
# Exercise 3: True vs Floor Division
# Problem: For n=7, print n/2 and n//2. Also show -7//2 to see flooring.
# ------------------------------------------------------------
n = 7
print("Ex3:", n / 2, n // 2, -7 // 2)  # Expected: 3.5 3 -4


# ------------------------------------------------------------
# Exercise 4: Modulus (Remainder) & Even Check
# Problem: For m=29 and k=6, print m%k. Also check if 28 is even using %.
# ------------------------------------------------------------
m = 29
k = 6
rem = m % k
is_even_28 = (28 % 2) == 0
print("Ex4:", rem, is_even_28)  # Expected: 5 True


# ------------------------------------------------------------
# Exercise 5: Exponent (Power)
# Problem: With base=3, print square and cube. Also print sqrt(16) using power.
# ------------------------------------------------------------
base = 3
square = base ** 2
cube = base ** 3
sqrt_16 = 16 ** 0.5
print("Ex5:", square, cube, sqrt_16)  # Expected: 9 27 4.0


# ------------------------------------------------------------
# Exercise 6: Operator Precedence vs Parentheses
# Problem: Compute 10 + 3 * 2 and (10 + 3) * 2; print both.
# ------------------------------------------------------------
p1 = 10 + 3 * 2
p2 = (10 + 3) * 2
print("Ex6:", p1, p2)  # Expected: 16 26


# ------------------------------------------------------------
# Exercise 7: Average of Three Scores
# Problem: For s1=80, s2=95, s3=88, print their average rounded to 2 decimals.
# ------------------------------------------------------------
s1, s2, s3 = 80, 95, 88
avg = (s1 + s2 + s3) / 3
print("Ex7:", round(avg, 2))  # Expected: 87.67


# ------------------------------------------------------------
# Exercise 8: Compound Assignment
# Problem: Start wallet=1000. Add 250, subtract 300, then add 10% (multiply by 1.10), then divide by 5.
# Print after each step.
# ------------------------------------------------------------
wallet = 1000
wallet += 250
print("Ex8 step1:", wallet)     # Expected: 1250
wallet -= 300
print("Ex8 step2:", wallet)     # Expected: 950
wallet *= 1.10
print("Ex8 step3:", wallet)     # Expected: 1045.0
wallet /= 5
print("Ex8 step4:", wallet)     # Expected: 209.0


# ------------------------------------------------------------
# Exercise 9: Convert Minutes to Hours & Minutes
# Problem: For total_minutes=135, compute hours (//60) and minutes (%60).
# ------------------------------------------------------------
total_minutes = 135
hours = total_minutes // 60
minutes = total_minutes % 60
print("Ex9:", hours, "hour(s)", minutes, "minute(s)")  # Expected: 2 hour(s) 15 minute(s)


# ------------------------------------------------------------
# Exercise 10: Percentage Discount
# Problem: price=999, discount=15 (%). Compute final price, rounded to 2 decimals.
# ------------------------------------------------------------
price = 999
discount = 15
final_price = price * (1 - discount / 100)
print("Ex10:", round(final_price, 2))  # Expected: 849.15

# ============================================================
# Short Notes — if / elif / else (Python)
# ------------------------------------------------------------
# Basic shape:
#   if condition1:
#       ...
#   elif condition2:
#       ...
#   else:
#       ...
#
# Nested if: an if-block inside another if/else.
# Truthy/Falsey: numbers (0 is False), empty strings "" are False, others True.
# Use comparison (==, !=, <, <=, >, >=) and boolean ops (and, or, not).
# ============================================================


# ------------------------------------------------------------
# Ex1: Basic if/else
# Problem: If age >= 18 print "Adult", else "Minor".
# ------------------------------------------------------------
age = 17
if age >= 18:
    print("Ex1:", "Adult")
else:
    print("Ex1:", "Minor")  # Expected with 17: Minor


# ------------------------------------------------------------
# Ex2: if/elif/else (sign of number)
# Problem: For n, print "Positive", "Zero", or "Negative".
# ------------------------------------------------------------
n = 0
if n > 0:
    print("Ex2:", "Positive")
elif n == 0:
    print("Ex2:", "Zero")      # Expected with 0: Zero
else:
    print("Ex2:", "Negative")


# ------------------------------------------------------------
# Ex3: Simple grading (if/elif/else)
# Problem: marks → A (>=90), B (>=75), C (>=60), else "Fail".
# ------------------------------------------------------------
marks = 76
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"   # Expected with 76: B
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"
print("Ex3:", grade)


# ------------------------------------------------------------
# Ex4: Nested if (email check)
# Problem: If email contains "@", then check it endswith ".com".
#          Print "Valid .com" or "Valid but not .com". If "@" missing → "Invalid".
# ------------------------------------------------------------
email = "user@example.org"
if "@" in email:
    if email.endswith(".com"):
        print("Ex4:", "Valid .com")
    else:
        print("Ex4:", "Valid but not .com")  # Expected with example.org
else:
    print("Ex4:", "Invalid")


# ------------------------------------------------------------
# Ex5: Compare two numbers
# Problem: Given a and b, print which is larger or if equal.
# ------------------------------------------------------------
a, b = 10, 10
if a > b:
    print("Ex5:", "a is greater")
elif a < b:
    print("Ex5:", "b is greater")
else:
    print("Ex5:", "a and b are equal")  # Expected with 10,10


# ------------------------------------------------------------
# Ex6: Tiered discount (if/elif/else)
# Problem: bill >= 1000 → 10% off; >= 500 → 5% off; else 0%. Print final.
# ------------------------------------------------------------
bill = 740.0
if bill >= 1000:
    disc = 0.10
elif bill >= 500:
    disc = 0.05    # Expected with 740: 5%
else:
    disc = 0.00
final_amount = bill * (1 - disc)
print("Ex6:", f"Discount={disc*100:.0f}%, Final={final_amount:.2f}")


# ------------------------------------------------------------
# Ex7: Nested if (even/odd and divisible by 4)
# Problem: If num is even, then check if also divisible by 4. Else "Odd".
# ------------------------------------------------------------
num = 14
if num % 2 == 0:
    if num % 4 == 0:
        print("Ex7:", "Even and divisible by 4")
    else:
        print("Ex7:", "Even but not divisible by 4")  # Expected with 14
else:
    print("Ex7:", "Odd")


# ------------------------------------------------------------
# Ex8: Simple password check (nested)
# Problem: If len(password) >= 8, then check if it contains "@".
#          Print "Strong", "Needs special char", or "Too short".
# ------------------------------------------------------------
password = "welcome1"
if len(password) >= 8:
    if "@" in password:
        print("Ex8:", "Strong")
    else:
        print("Ex8:", "Needs special char @")  # Expected with welcome1
else:
    print("Ex8:", "Too short")


# ------------------------------------------------------------
# Ex9: Ticket category (if/elif/else chain)
# Problem: age <12 -> Child, 12-17 -> Teen, 18-59 -> Adult, >=60 -> Senior.
# ------------------------------------------------------------
age2 = 61
if age2 < 12:
    cat = "Child"
elif age2 <= 17:
    cat = "Teen"
elif age2 <= 59:
    cat = "Adult"
else:
    cat = "Senior"  # Expected with 61: Senior
print("Ex9:", cat)


# ------------------------------------------------------------
# Ex10: Leap year (nested logic)
# Problem: Year is leap if divisible by 4, except centuries must be divisible by 400.
# ------------------------------------------------------------
year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Ex10:", "Leap year")   # Expected with 2000: Leap year
        else:
            print("Ex10:", "Not a leap year")
    else:
        print("Ex10:", "Leap year")
else:
    print("Ex10:", "Not a leap year")

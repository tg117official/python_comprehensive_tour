# ============================================================
# Short Notes — Printing & String Interpolation (Python)
# ------------------------------------------------------------
# print(values...)        : prints values with a space by default, then a newline.
# print(..., sep="|")     : custom separator between multiple values.
# print(..., end="")      : custom line ending (default "\n").
#
# String + variables (interpolation):
# f"...{var}..."          : f-strings (Python 3.6+). Fast, readable, allows inline expressions.
# "...{}...".format(x)    : str.format with positional or named placeholders.
# "%s %d %.2f" % (..)     : old-style printf formatting (still works, less recommended).
#
# Formatting helpers:
# f"{x:.2f}"              : 2 decimals; f"{n:,}" adds thousands separator.
# f"{txt:<10}"            : left-align in width 10; > right-align; ^ center.
# f"{var=}"               : quick debug form (Python 3.8+), prints "var=value".
# f"{obj!r}"              : use repr() (debug/raw view); !s uses str().
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Basic print — commas vs concatenation
# Problem: Print "Hello, Alice! You are 30." using (a) commas and (b) concatenation (+).
# ------------------------------------------------------------
name = "Alice"
age = 30
print("Ex1a:", "Hello,", name, "You are", age, ".")           # commas auto-add spaces
print("Ex1b:", "Hello, " + name + " You are " + str(age) + ".")  # + needs str() for numbers


# ------------------------------------------------------------
# Exercise 2: Custom separator (sep)
# Problem: Print the date values 2025, 8, 24 as "2025-8-24" using sep.
# ------------------------------------------------------------
year, month, day = 2025, 8, 24
print("Ex2:", year, month, day, sep="-")  # Expected: 2025-8-24


# ------------------------------------------------------------
# Exercise 3: Custom line ending (end)
# Problem: Print "Loading..." without moving to a new line, then print "done".
# ------------------------------------------------------------
print("Ex3:", end=" ")
print("Loading...", end="")   # no newline
print("done")                 # now newline happens after this


# ------------------------------------------------------------
# Exercise 4: f-strings (simple variables)
# Problem: Use an f-string to print "Hello, Bob! Score: 95".
# ------------------------------------------------------------
user = "Bob"
score = 95
print("Ex4:", f"Hello, {user}! Score: {score}")  # f-string


# ------------------------------------------------------------
# Exercise 5: f-strings with expressions & formatting
# Problem: price=999, discount=15; show final price with 2 decimals.
# ------------------------------------------------------------
price = 999
discount = 15
final_price = price * (1 - discount/100)
print("Ex5:", f"Final: ₹{final_price:.2f}")  # Expected: ₹849.15


# ------------------------------------------------------------
# Exercise 6: str.format — positional & named
# Problem: Print "X=10, Y=20" using (a) positional, (b) named placeholders.
# ------------------------------------------------------------
x, y = 10, 20
print("Ex6a:", "X={}, Y={}".format(x, y))
print("Ex6b:", "X={a}, Y={b}".format(a=x, b=y))


# ------------------------------------------------------------
# Exercise 7: Old-style % formatting
# Problem: Print "Alice is 30 years old." using %s and %d.
# ------------------------------------------------------------
print("Ex7:", "%s is %d years old." % (name, age))


# ------------------------------------------------------------
# Exercise 8: Number formatting — commas and decimals
# Problem: For n=1234567 and rate=0.075, print "1,234,567 at 7.50%".
# ------------------------------------------------------------
n = 1_234_567
rate = 0.075
print("Ex8:", f"{n:,} at {rate*100:.2f}%")  # thousands separator + 2 decimals


# ------------------------------------------------------------
# Exercise 9: Alignment in fixed width
# Problem: Print a tiny table: left-align name in 10 chars, right-align marks in 5.
# ------------------------------------------------------------
student = "Riya"
marks = 88
print("Ex9:", f"|{student:<10}|{marks:>5}|")   # |Riya      |   88|


# ------------------------------------------------------------
# Exercise 10: Debug prints — var= and !r
# Problem: Show variable names with values, and repr vs str of a string with \n.
# ------------------------------------------------------------
path = "C:\\new\nfolder"
print("Ex10a:", f"{path=}")        # prints: path='C:\\new\nfolder'
print("Ex10b:", f"repr: {path!r}") # explicit repr view (shows escapes)
print("Ex10c:", f"str : {path}")   # rendered with actual newline

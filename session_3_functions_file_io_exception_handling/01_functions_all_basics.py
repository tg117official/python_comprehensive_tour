# ============================================================
# Short Notes — Functions in Python
# ------------------------------------------------------------
# def name(...):         define a function
# return value           send a value back to the caller (default is None)
# Parameters:
#   • no parameters              def f():
#   • one/two parameters         def f(a), def g(a, b)
#   • default arguments          def f(a=10, b=2)
#   • variable args (*args)      def f(*nums)         # tuple of extra positional args
#   • keyword args (**kwargs)    def f(**opts)        # dict of extra keyword args
# Recursion: a function calling itself; MUST have a base case to stop.
# ============================================================


# ------------------------------------------------------------
# Ex1: No parameters — Welcome banner
# Problem: Make a function that prints a fixed welcome message.
# ------------------------------------------------------------
def welcome_banner():
    print("Ex1:", "Welcome to Python functions!")


welcome_banner()  # Expected: prints the message


# ------------------------------------------------------------
# Ex2: One parameter — Square of a number
# Problem: Return n squared.
# ------------------------------------------------------------
def square(n):
    return n * n


print("Ex2:", square(5))  # Expected: 25


# ------------------------------------------------------------
# Ex3: One parameter — Simple absolute value (no built-in abs)
# Problem: Return positive version of n using if/else.
# ------------------------------------------------------------
def my_abs(n):
    if n < 0:
        return -n
    else:
        return n


print("Ex3:", my_abs(-12), my_abs(7))  # Expected: 12 7


# ------------------------------------------------------------
# Ex4: Two parameters — Sum of two numbers
# Problem: Return a + b.
# ------------------------------------------------------------
def add(a, b):
    return a + b


print("Ex4:", add(10, 25))  # Expected: 35


# ------------------------------------------------------------
# Ex5: Two parameters — Maximum of two (no built-in max)
# Problem: Return the larger of a, b.
# ------------------------------------------------------------
def max_of_two(a, b):
    if a >= b:
        return a
    else:
        return b


print("Ex5:", max_of_two(3, 9), max_of_two(9, 3), max_of_two(5, 5))  # Expected: 9 9 5


# ------------------------------------------------------------
# Ex6: Default argument — Power with default exponent
# Problem: Return base**exp; default exp is 2.
# ------------------------------------------------------------
def power(base, exp=2):
    return base ** exp


print("Ex6:", power(5), power(2, 5))  # Expected: 25 32


# ------------------------------------------------------------
# Ex7: Default arguments — Wrap text with optional prefix/suffix
# Problem: Return prefix + text + suffix; defaults "[" and "]".
# ------------------------------------------------------------
def make_tag(text, prefix="[", suffix="]"):
    return prefix + text + suffix


print("Ex7:", make_tag("INFO"), make_tag("OK", "(", ")"))  # Expected: [INFO] (OK)


# ------------------------------------------------------------
# Ex8: *args (n parameters) — Average of any count of numbers
# Problem: Return average of all given numbers; if none, return None.
# ------------------------------------------------------------
def average(*nums):
    if len(nums) == 0:
        return None
    total = 0
    for x in nums:
        total = total + x
    return total / len(nums)


print("Ex8:", average(), average(10, 20, 30))  # Expected: None 20.0


# ------------------------------------------------------------
# Ex9: **kwargs — Format a person's name from parts
# Problem: Accept first, last, optional title and middle via keywords,
#          return a nicely formatted full name.
#          Unknown keys can be ignored.
# ------------------------------------------------------------
def full_name(**kwargs):
    first = kwargs.get("first", "")
    middle = kwargs.get("middle", "")
    last = kwargs.get("last", "")
    title = kwargs.get("title", "")
    # Build with simple spacing rules
    name = ""
    if title:
        name = title + " "
    name = name + first
    if middle:
        name = name + " " + middle
    if last:
        name = name + " " + last
    return name.strip()


print("Ex9:", full_name(first="Riya", last="Sharma"),
      "|", full_name(title="Dr.", first="A. P.", last="Singh", middle="K."))
# Expected: "Riya Sharma" | "Dr. A. P. K. Singh"


# ------------------------------------------------------------
# Ex10: Recursion — Factorial (n!)
# Problem: Compute n! with recursion. Base: 0! = 1, 1! = 1.
# ------------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    else:                     # recursive case
        return n * factorial(n - 1)

print("Ex10:", factorial(5))  # Expected: 120

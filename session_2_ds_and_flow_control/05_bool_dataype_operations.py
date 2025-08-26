# ============================================================
# Short Notes — Booleans in Python
# ------------------------------------------------------------
# • Booleans: True, False  (capitalized)
# • Produced by comparisons (==, !=, <, <=, >, >=) and operators (and, or, not).
# • Truthiness: bool(0), bool(0.0), bool(""), bool([]), bool(()) => False; most others => True.
# • and / or short-circuit and RETURN an operand (not always a pure bool):
#     A and B -> returns A if A is falsy else B
#     A or  B -> returns A if A is truthy else B
# • Precedence:  not  >  and  >  or   (use parentheses to be explicit)
# • Chaining:  10 < x <= 20  is valid and reads naturally.
# • Equality vs identity:  True == 1  (True), but  True is 1  (False).
# ============================================================


# ------------------------------------------------------------
# Ex1: Boolean literals & types
# Problem: Create t=True, f=False. Print them and their types.
# ------------------------------------------------------------
t = True
f = False
print("Ex1:", t, type(t).__name__, f, type(f).__name__)  # Expected: True bool False bool


# ------------------------------------------------------------
# Ex2: Comparisons produce booleans
# Problem: For x=10, y=7 print: x>y, x==y, x!=y, x<=10
# ------------------------------------------------------------
x, y = 10, 7
print("Ex2:", x > y, x == y, x != y, x <= 10)  # Expected: True False True True


# ------------------------------------------------------------
# Ex3: Chained comparison
# Problem: For n=15, check 10 < n <= 20.
# ------------------------------------------------------------
n = 15
in_range = 10 < n <= 20
print("Ex3:", in_range)  # Expected: True


# ------------------------------------------------------------
# Ex4: Logical operators (and, or, not)
# Problem: With p=True, q=False, print p and q, p or q, not p, not q.
# ------------------------------------------------------------
p, q = True, False
print("Ex4:", p and q, p or q, not p, not q)  # Expected: False True False True


# ------------------------------------------------------------
# Ex5: Truthiness & bool() conversion
# Problem: Show truthiness of 0, 1, "", "hi", [], [0].
# ------------------------------------------------------------
print("Ex5:",
      bool(0), bool(1), bool(""), bool("hi"), bool([]), bool([0]))
# Expected: False True False True False True


# ------------------------------------------------------------
# Ex6: and/or return operands (not just True/False)
# Problem: Demonstrate results without wrapping in bool().
# ------------------------------------------------------------
a = "" or "fallback"      # "" is falsy -> returns "fallback"
b = 0 and 5               # 0 is falsy -> returns 0
c = "hi" and 123          # "hi" truthy -> returns 123
print("Ex6:", a, b, c, type(a).__name__, type(b).__name__, type(c).__name__)
# Expected: fallback 0 123 str int int


# ------------------------------------------------------------
# Ex7: Operator precedence (not > and > or)
# Problem: Compare two expressions to see why parentheses matter.
# ------------------------------------------------------------
expr1 = not True and False or False     # evaluated as ((not True) and False) or False
expr2 = not (True and False) or False   # parentheses change grouping
print("Ex7:", expr1, expr2)             # Expected: False True


# ------------------------------------------------------------
# Ex8: Equality vs identity
# Problem: Show True == 1 and True is 1; also False == 0 and False is 0.
# ------------------------------------------------------------
print("Ex8:", True == 1, True is 1, False == 0, False is 0)
# Expected: True False True False


# ------------------------------------------------------------
# Ex9: De Morgan's Laws check
# Problem: For a=True, b=False, verify:
#   not(a and b) == (not a) or (not b)
#   not(a or b)  == (not a) and (not b)
# ------------------------------------------------------------
a, b = True, False
lhs1 = not (a and b)
rhs1 = (not a) or (not b)
lhs2 = not (a or b)
rhs2 = (not a) and (not b)
print("Ex9:", lhs1 == rhs1, lhs2 == rhs2)  # Expected: True True


# ------------------------------------------------------------
# Ex10: Simple boolean use cases
# Problem: Membership and prefix check produce booleans.
# ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
email = "user@example.com"
print("Ex10:", "apple" in fruits, email.endswith(".com"))
# Expected: True True

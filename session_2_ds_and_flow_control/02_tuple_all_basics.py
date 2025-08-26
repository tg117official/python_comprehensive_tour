# ============================================================
# Short Notes — Tuples (Python)
# ------------------------------------------------------------
# • A tuple is an ordered, immutable sequence: (1, 2, 3), ("a","b"), etc.
# • Immutability: you cannot change, add, or remove items in-place.
# • Indexing & slicing work like lists: t[0], t[-1], t[1:4], t[::-1]
# • Parentheses are optional: t = 1, 2, 3  ==  (1, 2, 3)
# • Single-element tuple needs a trailing comma: (5,) not (5)
# • Operators: + (concatenate), * (repeat), "x in t" (membership)
# • Methods: count(x), index(x)
# • You can store mutables inside a tuple (e.g., a list) and mutate that inner object.
# ============================================================


# ------------------------------------------------------------
# Ex1: Indexing (first, third, last)
# Problem: From nums = (10, 20, 30, 40, 50), print first, third, last.
# ------------------------------------------------------------
nums = (10, 20, 30, 40, 50)
first_val = nums[0]
third_val = nums[2]
last_val = nums[-1]
print("Ex1:", first_val, third_val, last_val)  # Expected: 10 30 50


# ------------------------------------------------------------
# Ex2: Basic Slicing
# Problem: From letters = ('a','b','c','d','e','f'), print ('b','c','d'), first 3, and from index 2 onward.
# ------------------------------------------------------------
letters = ('a', 'b', 'c', 'd', 'e', 'f')
mid = letters[1:4]        # b,c,d
first_three = letters[:3]
from_two = letters[2:]
print("Ex2:", mid, first_three, from_two)
# Expected: ('b','c','d') ('a','b','c') ('c','d','e','f')


# ------------------------------------------------------------
# Ex3: Step Slicing & Reverse
# Problem: For digits = (0,1,2,3,4,5,6,7,8,9), print every 2nd element and the reversed tuple.
# ------------------------------------------------------------
digits = (0,1,2,3,4,5,6,7,8,9)
every_second = digits[::2]
reversed_digits = digits[::-1]
print("Ex3:", every_second, reversed_digits)
# Expected: (0,2,4,6,8) (9,8,7,6,5,4,3,2,1,0)


# ------------------------------------------------------------
# Ex4: Immutability + "Modify" via New Tuple
# Problem: Change ('c','a','t') into ('b','a','t') by building a NEW tuple with slices.
# ------------------------------------------------------------
t = ('c','a','t')
new_t = ('b',) + t[1:]    # create a new tuple; original unchanged
print("Ex4:", "old:", t, "| new:", new_t)
# Note: t[0] = 'b' would raise a TypeError (tuples are immutable).


# ------------------------------------------------------------
# Ex5: Concatenation and Repetition
# Problem: Concatenate (1,2) with (3,4) and repeat ('ha',) three times.
# ------------------------------------------------------------
a = (1, 2)
b = (3, 4)
combined = a + b
laughs = ('ha',) * 3
print("Ex5:", combined, laughs)
# Expected: (1,2,3,4) ('ha','ha','ha')


# ------------------------------------------------------------
# Ex6: Membership & Length
# Problem: In fruits, check membership of 'apple' and print length of the tuple.
# ------------------------------------------------------------
fruits = ('apple', 'banana', 'cherry', 'banana', 'date')
has_apple = 'apple' in fruits
length = len(fruits)
print("Ex6:", has_apple, length)  # Expected: True 5


# ------------------------------------------------------------
# Ex7: count() and index()
# Problem: Count 'banana' and find its first index.
# ------------------------------------------------------------
banana_count = fruits.count('banana')
banana_first_idx = fruits.index('banana')  # safe here because 'banana' exists
print("Ex7:", banana_count, banana_first_idx)  # Expected: 2 1


# ------------------------------------------------------------
# Ex8: Single-Element Tuple vs Parentheses
# Problem: Show the difference between (5) and (5,) by printing their types.
# ------------------------------------------------------------
not_tuple = (5)     # just the integer 5 in parentheses
single_tuple = (5,) # a 1-element tuple
print("Ex8:", type(not_tuple).__name__, type(single_tuple).__name__)
# Expected: int tuple


# ------------------------------------------------------------
# Ex9: Packing & Unpacking (and Swapping)
# Problem: Unpack t = ('x','y','z') into three variables; then swap two variables using tuple assignment.
# ------------------------------------------------------------
t2 = ('x','y','z')     # packing
x, y, z = t2           # unpacking
print("Ex9 step1:", x, y, z)   # Expected: x y z
a1, a2 = 100, 200
a1, a2 = a2, a1        # swap using tuple assignment
print("Ex9 step2:", a1, a2)    # Expected: 200 100


# ------------------------------------------------------------
# Ex10: Tuples can hold mutables (inner list can change)
# Problem: Given mix = (1, [2, 3], 4), append 99 to the inner list and show the tuple changed inside.
# ------------------------------------------------------------
mix = (1, [2, 3], 4)
mix[1].append(99)   # allowed: we mutate the inner list, not the tuple structure
print("Ex10:", mix)
# Expected: (1, [2, 3, 99], 4)

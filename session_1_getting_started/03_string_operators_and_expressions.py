# ============================================================
# Short Notes — String Operators & Expressions (Python)
# ------------------------------------------------------------
# Strings are immutable sequences of characters.
# Key operators:
#   +  : concatenation ("a" + "b" -> "ab")
#   *  : repetition ("ha" * 3 -> "hahaha")
#   [] : indexing (s[0], s[-1])
#   [:]: slicing (s[1:4], s[:], s[::2], s[::-1])
#   in / not in : membership ("py" in "python" -> True)
#   ==, !=, <, <=, >, >= : lexicographic comparison (case-sensitive)
# Tip: You can’t change a string in place; build a new one using slices + concatenation.
# ============================================================

# Basics

# "Hello", 'World' !!!
print(""""Hello", 'World' !!! """)
print('''"Hello", 'World' !!! ''')
print('"Hello"', ",'World' !!!")
print("\"Hello\", 'Word' !!!")
print('"Hello", \'Word\' !!!')

# ------------------------------------------------------------
# Exercise 1: Basic Concatenation
# Problem: Join first_name and last_name with a space using + and print it.
# ------------------------------------------------------------
first_name = "Sandeep"
last_name  = "Patil"
full_name = first_name + " " + last_name
print("Ex1:", full_name)  # Expected: Sandeep Patil


# ------------------------------------------------------------
# Exercise 2: Repetition
# Problem: Make a small divider line using "*" repeated 20 times and print it.
# ------------------------------------------------------------
divider = "-" * 20
print("Ex2:", divider)  # Expected: --------------------


# ------------------------------------------------------------
# Exercise 3: Build a Message with +=
# Problem: Start with msg = "" and keep appending parts using += then print.
# ------------------------------------------------------------
msg = ""
msg += "Hello"
msg += ", "
msg += "Python"
msg += " learner!"
print("Ex3:", msg)  # Expected: Hello, Python learner!


# ------------------------------------------------------------
# Exercise 4: Membership Test (in / not in)
# Problem: Check if "py" is in "python" and if "Java" is not in "python".
# Print both boolean results.
# ------------------------------------------------------------
text = "python"
print("py" in text)
print("Java" not in text)  # Expected: True True


# ------------------------------------------------------------
# Exercise 5: Indexing (first, middle, last)
# Problem: From the string "abcdef", print first char, third char, and last char.
# ------------------------------------------------------------
s = "abcdef"
first_char = s[0]
third_char = s[2]
last_char = s[-1]
print("Ex5:", first_char, third_char, last_char)  # Expected: a c f


# ------------------------------------------------------------
# Exercise 6: Basic Slicing
# Problem: For "Hello, World!", print "Hello", "World", and the whole string via slice.
# ------------------------------------------------------------
t = "Hello, World!"
hello_part = t[0:5]     # up to but not including index 5
world_part = t[7:12]
whole_copy = t[:]
print("Ex6:", hello_part, world_part, whole_copy)
# Expected: Hello World Hello, World!


# ------------------------------------------------------------
# Exercise 7: Step Slicing & Reverse
# Problem: For "0123456789", print every second character and the reversed string.
# ------------------------------------------------------------
digits = "0123456789"
every_second = digits[::2]
reversed_digits = digits[::-1]
print("Ex7:", every_second, reversed_digits)
# Expected: 02468 9876543210


# ------------------------------------------------------------
# Exercise 8: "Modify" a String via Slices (+ immutability trick)
# Problem: Change "cat" to "bat" by creating a new string using slices and +.
# ------------------------------------------------------------
animal = "cat"
new_animal = "b" + animal[1:]    # replace first char by building a new string
print("Ex8:", new_animal)  # Expected: bat


# ------------------------------------------------------------
# Exercise 9: Comparisons (lexicographic, case-sensitive)
# Problem: Compare "apple" and "banana", then "Zoo" and "apple".
# Print the booleans for < and == cases.
# ------------------------------------------------------------
print("apple" < "banana")
print("apple" == "banana")  # Expected: True False
print("Zoo" < "apple")  # Expected: True (because 'Z' (90) < 'a' (97))


# ------------------------------------------------------------
# Exercise 10: Compose with +, *, and slices
# Problem: From greet="Hello", name="Bob", and exclamations=3, build "Hello, Bob!!!"
# using + and * (no methods). Use slicing greet[:].
# ------------------------------------------------------------
greet = "Hello"
name = "Bob"
exclamations = 3
sentence = greet[:] + ", " + name + "!" * exclamations
print("Ex10:", sentence)  # Expected: Hello, Bob!!!

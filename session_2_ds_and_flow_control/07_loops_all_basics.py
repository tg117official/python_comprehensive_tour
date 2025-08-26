# ============================================================
# Short Notes — Loops in Python
# ------------------------------------------------------------
# for loop:   for item in iterable: ...
# while loop: while condition: ...
# range():    range(stop) or range(start, stop[, step]) for number sequences
# break:      exit the nearest loop immediately
# continue:   skip the rest of the current loop iteration
# for-else:   else runs if the loop wasn't ended by 'break'
# Tip: Keep while-loops safe by changing the condition inside the loop!
# ============================================================


# ------------------------------------------------------------
# Ex1: for over a list (print items)
# Problem: Print each fruit from the list one per line.
# ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Ex1:", fruit)
# Expected lines: apple, banana, cherry


# ------------------------------------------------------------
# Ex2: range basics
# Problem: Print numbers 1 to 5 using range.
# ------------------------------------------------------------
for n in range(1, 6):
    print("Ex2:", n)
# Expected: 1 2 3 4 5 (on separate lines)


# ------------------------------------------------------------
# Ex3: range with step (even numbers)
# Problem: Print even numbers from 0 to 10.
# ------------------------------------------------------------
for n in range(0, 11, 2):
    print("Ex3:", n)
# Expected: 0 2 4 6 8 10


# ------------------------------------------------------------
# Ex4: Summation with a for-loop
# Problem: Compute the sum of nums without using sum().
# ------------------------------------------------------------
nums = [4, 8, 15, 16, 23, 42]
total = 0
for x in nums:
    total = total + x
print("Ex4 total:", total)   # Expected: 108


# ------------------------------------------------------------
# Ex5: Count vowels in a string
# Problem: Count 'a', 'e', 'i', 'o', 'u' (lowercase) in the text.
# ------------------------------------------------------------
text = "hello world"
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count = count + 1
print("Ex5 vowels:", count)  # Expected: 3 (e, o, o)


# ------------------------------------------------------------
# Ex6: break + for-else (search)
# Problem: Find first number > 50. If found, print it; else print "not found".
# ------------------------------------------------------------
numbers_a = [10, 20, 30]       # try with none found
for n in numbers_a:
    if n > 50:
        print("Ex6A found:", n)
        break
else:
    print("Ex6A:", "not found")  # Expected: not found

numbers_b = [10, 60, 40]       # try with a match
for n in numbers_b:
    if n > 50:
        print("Ex6B found:", n)  # Expected: 60
        break
else:
    print("Ex6B:", "not found")


# ------------------------------------------------------------
# Ex7: continue (skip multiples of 3)
# Problem: Print numbers 1..10 but skip those divisible by 3.
# ------------------------------------------------------------
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print("Ex7:", n)
# Expected: 1 2 4 5 7 8 10


# ------------------------------------------------------------
# Ex8: while-loop countdown
# Problem: Print 5 down to 1, then "Go!".
# ------------------------------------------------------------
k = 5
while k >= 1:
    print("Ex8:", k)
    k = k - 1
print("Ex8:", "Go!")
# Expected: 5 4 3 2 1 then Go!


# ------------------------------------------------------------
# Ex9: Factorial with while (5!)
# Problem: Compute 5! = 1*2*3*4*5 using a while-loop.
# ------------------------------------------------------------
n = 5
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("Ex9 5! =", fact)   # Expected: 120



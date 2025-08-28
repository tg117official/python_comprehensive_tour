# ============================================================
# Short Notes — Python Lists (Basics)
# ------------------------------------------------------------
# A list is an ordered, mutable sequence: [1, 2, 3], ["a", "b"], etc.
# Indexing:    l[0] first, l[-1] last (negative indexes count from the end)
# Slicing:     l[start:stop]  (stop is excluded), l[start:stop:step], l[::-1] reverse copy
# Copy:        l2 = l[:] or list(l)  (NOT l2 = l, which is the same object)
# Operators:   + (concatenate), * (repeat), "x in l" (membership)
# Methods:     append(x), extend(iterable), insert(i, x),
#              remove(x) [first match], pop([i]) [default last],
#              clear(), index(x), count(x),
#              sort() [in-place], reverse() [in-place]
# Built-ins:   len(l), sum(l), min(l), max(l), sorted(l) [new list]
# ============================================================


# ------------------------------------------------------------
# Ex1: Indexing (first, third, last, negative indexing)
# Problem: From nums = [10, 20, 30, 40, 50], print first, third, last using indexes.
# ------------------------------------------------------------
nums = [10, 20, 30, 40, 50]
first_val = nums[0]
third_val = nums[2]
last_val = nums[-1]
print("Ex1:", first_val, third_val, last_val)  # Expected: 10 30 50


# ------------------------------------------------------------
# Ex2: Basic Slicing
# Problem: From letters = ['a','b','c','d','e','f'], print "['b','c','d']", "first 3", and "from index 2 onward".
# ------------------------------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f']
mid = letters[1:4]      # b,c,d
first_three = letters[:3]
from_two = letters[2:]
print("Ex2:", mid, first_three, from_two)
# Expected: ['b','c','d'] ['a','b','c'] ['c','d','e','f']


# ------------------------------------------------------------
# Ex3: Step Slicing & Reverse
# Problem: For digits = [0,1,2,3,4,5,6,7,8,9], print every 2nd element and the reversed list.
# ------------------------------------------------------------
digits = [0,1,2,3,4,5,6,7,8,9]
every_second = digits[::2]
reversed_digits = digits[::-1]
print("Ex3:", every_second, reversed_digits)
# Expected: [0,2,4,6,8] [9,8,7,6,5,4,3,2,1,0]


# ------------------------------------------------------------
# Ex4: Copy vs Alias
# Problem: Show difference between aliasing (same object) and copying (new object).
# ------------------------------------------------------------
base = [1, 2, 3]
alias = base            # same object
copy1 = base[:]         # new object (shallow copy)
base.append(99)         # modifies base (and alias), not copy1
print("Ex4:", "base:", base, "| alias:", alias, "| copy1:", copy1)
# Expected: base and alias have 99; copy1 does not


# ------------------------------------------------------------
# Ex5: Concatenation and Repetition
# Problem: Add elements using +, and repeat a short list using *.
# ------------------------------------------------------------
start = [1, 2]
combined = start + [3, 4] + [5]
laughs = ["ha"] * 3
print("Ex5:", combined, laughs)
# Expected: [1,2,3,4,5] ['ha','ha','ha']


# ------------------------------------------------------------
# Ex6: Membership, index(), count()
# Problem: In fruits list, check membership of 'apple', count 'banana', and find first index of 'banana'.
# ------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "banana", "date"]
has_apple = "apple" in fruits
banana_count = fruits.count("banana")
banana_first_idx = fruits.index("banana")   # safe here because banana exists
print("Ex6:", has_apple, banana_count, banana_first_idx)
# Expected: True 2 1


# ------------------------------------------------------------
# Ex7: append() vs extend() vs insert()
# Problem: Show difference between appending a list, extending by its elements, and inserting at a position.
# ------------------------------------------------------------
l = [10, 20]
l.append([30, 40])      # appends as a single element (nested list)
print("Ex7 step1:", l)  # Expected: [10, 20, [30, 40]]
l = [10, 20]
l.extend([30, 40])      # adds each element
print("Ex7 step2:", l)  # Expected: [10, 20, 30, 40]
l.insert(1, 15)         # insert 15 at index 1
print("Ex7 step3:", l)  # Expected: [10, 15, 20, 30, 40]


# ------------------------------------------------------------
# Ex8: remove() and pop()
# Problem: Remove the first 2 and then pop last and index-1 items; print each result.
# ------------------------------------------------------------
vals = [1, 2, 3, 2, 4]
vals.remove(2)          # removes first occurrence of 2
last_item = vals.pop()  # pops last
idx1_item = vals.pop(1) # pops element at index 1
print("Ex8:", vals, "| popped:", last_item, idx1_item)
# Expected final list and popped values accordingly


# ------------------------------------------------------------
# Ex9: sort()/reverse() vs sorted()
# Problem: Show difference between in-place sort and new sorted list.
# ------------------------------------------------------------
nums2 = [5, 3, 9, 1, 7]
sorted_copy = sorted(nums2)  # new list
print("Ex9 step1:", "original:", nums2, "| sorted_copy:", sorted_copy)
nums2.sort()                 # in-place sort
print("Ex9 step2:", "after sort():", nums2)
nums2.reverse()              # in-place reverse
print("Ex9 step3:", "after reverse():", nums2)


# ------------------------------------------------------------
# Ex10: Useful built-in functions on lists
# Problem: For data = [4, 8, 15, 16, 23, 42], print len, sum, min, max.
# ------------------------------------------------------------
data = [4, 8, 15, 16, 23, 42]
print("Ex10:", "len:", len(data), "sum:", sum(data), "min:", min(data), "max:", max(data))
# Expected: len: 6 sum: 108 min: 4 max: 42


######################### List Comprehension #####################


# Generate list
# process list data

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = []
for num in l1 :
    squares.append(num*num)
print(squares)

squares = [num*num for num in l1]
print(squares)

squares = [num*num for num in l1 if num % 2 == 0]
print(squares)

squares = [num*num if num % 2 == 0 else num+num for num in l1]
print(squares)

squares = [num if num in (2, 3, 5, 7)
            else num*num if num % 2 == 0
            else num + num
           for num in l1]
print(squares)

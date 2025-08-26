# ============================================================
# Short Notes — Sets (Python)
# ------------------------------------------------------------
# • A set is an unordered collection of UNIQUE items: {1, 2, 3}
# • Unordered => no indexing/slicing (s[0] is invalid)
# • Mutable: you can add/remove elements; but elements must be hashable (immutable)
# • Common ops: union(|), intersection(&), difference(-), symmetric diff(^)
# • Useful methods: add, remove, discard, pop, clear, copy,
#                   issubset(<=), issuperset(>=), isdisjoint
# • frozenset: an immutable set (no add/remove), still supports set algebra
# ============================================================


# ------------------------------------------------------------
# Ex1: Set creation + automatic de-duplication
# Problem: Create a set with duplicates and show it contains only unique items.
# ------------------------------------------------------------
s1 = {1, 2, 2, 3, 3, 3}
print("Ex1:", s1, "len:", len(s1))  # Expected: {1, 2, 3} len: 3


# ------------------------------------------------------------
# Ex2: Membership tests
# Problem: Check if 2 is in the set and 99 is not.
# ------------------------------------------------------------
print("Ex2:", 2 in s1, 99 not in s1)  # Expected: True True


# ------------------------------------------------------------
# Ex3: add(), remove(), discard()
# Problem: Start with {1,2,3}. Add 4, remove 2, discard 99 (no error if missing).
# ------------------------------------------------------------
s2 = {1, 2, 3}
s2.add(4)        # {1,2,3,4}
s2.remove(2)     # {1,3,4} (remove raises error if absent; here it's present)
s2.discard(99)   # no error; does nothing
print("Ex3:", s2)  # Expected: {1, 3, 4}


# ------------------------------------------------------------
# Ex4: Union and Intersection
# Problem: For a={1,2,3} and b={3,4,5}, print union and intersection.
# ------------------------------------------------------------
a = {1, 2, 3}
b = {3, 4, 5}
print("Ex4 union:", a | b)  # Expected: {1,2,3,4,5}
print("Ex4 inter:", a & b)  # Expected: {3}

print("Ex4 union:", a.union(b))  # Expected: {1,2,3,4,5}
print("Ex4 inter:", a.intersection(b))  # Expected: {3}

# ------------------------------------------------------------
# Ex5: Difference and Symmetric Difference
# Problem: Using the same a and b, print a-b and a^b.
# ------------------------------------------------------------
print("Ex5 diff  :", a - b)   # Expected: {1,2}
print("Ex5 symdiff:", a ^ b)  # Expected: {1,2,4,5}


# ------------------------------------------------------------
# Ex6: Subset, Superset, Disjoint
# Problem: Check subset/superset and disjoint relationships.
# ------------------------------------------------------------
small = {1, 2}
big = {1, 2, 3}
other = {7, 8}
print("Ex6 subset :", small <= big)          # True
print("Ex6 superset:", big >= small)         # True
print("Ex6 disjoint:", big.isdisjoint(other))# True


# ------------------------------------------------------------
# Ex7: De-duplicate a list using set
# Problem: Turn a list with repeats into a unique list (order arbitrary).
# ------------------------------------------------------------
lst = [4, 4, 1, 2, 2, 3, 3, 3]
unique_set = set(lst)
unique_list = sorted(unique_set)  # sorted for a neat, predictable display
print("Ex7:", unique_set, "->", unique_list)
# Expected: unique_set has {1,2,3,4}; unique_list [1,2,3,4]


# ------------------------------------------------------------
# Ex8: copy() vs aliasing
# Problem: Show that alias points to same object but copy() makes a new one.
# ------------------------------------------------------------
base = {10, 20}
alias = base            # same object
cpy = base.copy()       # new set
base.add(99)            # affects base and alias, not cpy
print("Ex8 base :", base)
print("Ex8 alias:", alias)
print("Ex8 copy :", cpy)


# ------------------------------------------------------------
# Ex9: pop() and clear()
# Problem: pop an arbitrary element, then clear the set.
# ------------------------------------------------------------
s3 = {10, 20, 30}
popped = s3.pop()   # removes and returns an arbitrary element
print("Ex9 popped:", popped, "remaining:", s3)  # element order not guaranteed
s3.clear()
print("Ex9 cleared:", s3)  # Expected: set()


# ------------------------------------------------------------
# Ex10: frozenset (immutable set) basics
# Problem: Create a frozenset, show membership, and do a union with a normal set.
# ------------------------------------------------------------
fs = frozenset([1, 2, 3])
normal = {3, 4}
# fs.add(5)  #  would raise AttributeError (frozenset is immutable)
print("Ex10 type:", type(fs).__name__)      # Expected: frozenset
print("Ex10 member:", 2 in fs)              # True
print("Ex10 union :", fs | normal)          # Expected: {1,2,3,4}

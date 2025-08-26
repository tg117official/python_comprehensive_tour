# ============================================================
# Short Notes — Dictionaries (Python)
# ------------------------------------------------------------
# • A dictionary maps keys → values: {"name": "Riya", "age": 21}
# • Keys must be hashable (immutable types like str, int, tuple); values can be anything.
# • Access: d[key]; safe access: d.get(key, default)
# • Add/Update: d[key] = value; bulk update: d.update(other)
# • Remove: d.pop(key[, default]), d.popitem() (removes last), del d[key], d.clear()
# • Views: d.keys(), d.values(), d.items() (dynamic “live” views)
# • Copy: alias = d (same object), c = d.copy() (shallow copy), deep copy needed for nested structures.
# • Merge (no loops): {**a, **b} or a.update(b) (b overwrites clashes)
# ============================================================


# ------------------------------------------------------------
# Ex1: Create & Access
# Problem: Make a dict person with name="Sandeep", age=30. Print name and age.
# ------------------------------------------------------------
person = {"name": "Sandeep", "age": 30}
print("Ex1:", person["name"], person["age"])  # Expected: Sandeep 30


# ------------------------------------------------------------
# Ex2: Add & Modify
# Problem: Add city="Pune"; change age to 31. Print dict.
# ------------------------------------------------------------
person["city"] = "Pune"   # add
person["age"] = 31        # modify
print("Ex2:", person)     # Expected: {'name':'Sandeep','age':31,'city':'Pune'}


# ------------------------------------------------------------
# Ex3: Safe Access with get()
# Problem: Try to read person['email'] safely with a default "NA".
# ------------------------------------------------------------
email = person.get("email", "NA")
print("Ex3:", email)  # Expected: NA


# ------------------------------------------------------------
# Ex4: Remove Keys: pop() and popitem()
# Problem: Pop "city" (return its value), then pop the last item with popitem().
# ------------------------------------------------------------
popped_city = person.pop("city", None)    # returns value or None
last_key, last_val = person.popitem()     # removes LAST inserted item
print("Ex4:", popped_city, (last_key, last_val), person)
# Note: popitem() removes ('age', 31) in current insertion order (Python 3.7+ preserves order).


# ------------------------------------------------------------
# Ex5: Keys, Values, Items (live views)
# Problem: Show keys/values/items; then add a key and show that the views reflect it.
# ------------------------------------------------------------
d = {"a": 1, "b": 2}
kview = d.keys()
vview = d.values()
iview = d.items()
print("Ex5 before:", list(kview), list(vview), list(iview))
d["c"] = 3
print("Ex5 after :", list(kview), list(vview), list(iview))


# ------------------------------------------------------------
# Ex6: Merge Dictionaries
# Problem: Merge a={"x":1,"y":2} and b={"y":99,"z":3} two ways; show y is overwritten.
# ------------------------------------------------------------
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}
merged_unpack = {**a, **b}     # new dict, b wins for 'y'
a_update = a.copy(); a_update.update(b)  # new dict via copy+update
print("Ex6:", merged_unpack, a_update)   # Expected: {'x':1,'y':99,'z':3} (both)


# ------------------------------------------------------------
# Ex7: Nested Dictionary Access & Update
# Problem: Access "Python" beginner level and update it to "intermediate".
# ------------------------------------------------------------
skills = {
    "programming": {"Python": "beginner", "Java": "none"},
    "tools": {"Git": "basic"}
}
level_before = skills["programming"]["Python"]
skills["programming"]["Python"] = "intermediate"
print("Ex7:", level_before, "->", skills["programming"]["Python"])


# ------------------------------------------------------------
# Ex8: setdefault() for Defaults
# Problem: Ensure key "country" exists with default "India" without overwriting.
# ------------------------------------------------------------
profile = {"name": "Asha"}
existing = profile.setdefault("country", "India")  # inserts if missing
again = profile.setdefault("country", "UK")        # does NOT overwrite
print("Ex8:", profile, existing, again)  # Expected: {'name':'Asha','country':'India'} India India


# ------------------------------------------------------------
# Ex9: Copy vs Alias (Shallow Copy)
# Problem: Show that alias reflects changes; shallow copy is independent at top-level.
# ------------------------------------------------------------
base = {"k1": 1, "k2": [10, 20]}
alias = base              # same object
shallow = base.copy()     # new dict; inner list still shared (shallow)
base["k1"] = 999          # top-level change
base["k2"].append(30)     # mutate inner list (shared)
print("Ex9 base  :", base)
print("Ex9 alias :", alias)    # same as base
print("Ex9 shallow:", shallow) # k1 old, but k2 mutated due to shallow copy


# ------------------------------------------------------------
# Ex10: Handy Built-ins & Membership
# Problem: For d2={'a':10,'c':5,'b':8}, print len, check key membership,
#          and show sorted keys and items without loops.
# ------------------------------------------------------------
d2 = {"a": 10, "c": 5, "b": 8}
print("Ex10 len:", len(d2))               # Expected: 3
print("Ex10 'a' in d2?", "a" in d2)       # membership checks keys
print("Ex10 sorted keys:", sorted(d2))    # ['a','b','c']
print("Ex10 sorted items:", sorted(d2.items()))  # [('a',10),('b',8),('c',5)]

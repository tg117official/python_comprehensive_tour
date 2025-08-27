# ============================================================
# Short Notes — Binary File I/O with pickle
# ------------------------------------------------------------
# • What is pickle?  A Python module to serialize (save) and deserialize (load)
#   Python objects to/from BYTES (binary). Great for Python-native data like
#   lists/dicts/sets/tuples, and even simple custom classes.
#
# • SECURITY: Never unpickle data from an untrusted source. Unpickling can
#   execute arbitrary code. Only open pickle files you created or fully trust.
#
# • Core API:
#     import pickle
#     pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)  # to binary file
#     obj = pickle.load(file)                                   # from binary file
#     b = pickle.dumps(obj, protocol=...)                       # to bytes in memory
#     obj = pickle.loads(b)                                     # from bytes
#
# • File modes (binary!): "wb" (write/overwrite), "rb" (read), "ab" (append)
# • Protocols: use pickle.HIGHEST_PROTOCOL for best speed/size on your Python.
# • Multiple objects in one file: write several dumps; when reading, call
#   load() repeatedly until EOFError (end of file).
# ============================================================

import pickle

# ------------------------------------------------------------
# Ex1: Dump & load a list (basic round-trip)
# Problem: Save a list of numbers to 'nums.pkl' and load it back.
# ------------------------------------------------------------
nums = [1, 2, 3, 5, 8, 13]
with open("nums.pkl", "wb") as f:
    pickle.dump(nums, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("nums.pkl", "rb") as f:
    nums_back = pickle.load(f)

print("Ex1:", nums_back)  # Expected: [1, 2, 3, 5, 8, 13]


# ------------------------------------------------------------
# Ex2: Dump & load a dictionary (with highest protocol)
# Problem: Save a small student dict and read it back.
# ------------------------------------------------------------
student = {"name": "Riya", "age": 21, "skills": ["Python", "Git"], "score": 92.5}
with open("student.pkl", "wb") as f:
    pickle.dump(student, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("student.pkl", "rb") as f:
    student_back = pickle.load(f)

print("Ex2:", student_back["name"], student_back["score"])  # Expected: Riya 92.5


# ------------------------------------------------------------
# Ex3: Append multiple objects and read them all
# Problem: Write two separate dumps into the same file, then load until EOF.
# ------------------------------------------------------------
with open("multi.pkl", "wb") as f:
    pass  # create/clear file

# append two objects
with open("multi.pkl", "ab") as f:
    pickle.dump({"id": 1, "item": "book", "price": 199}, f)
    pickle.dump({"id": 2, "item": "pen", "price": 25}, f)

# read them all back (loop until EOFError)
loaded_multi = []
with open("multi.pkl", "rb") as f:
    while True:
        try:
            loaded_multi.append(pickle.load(f))
        except EOFError:
            break

print("Ex3:", loaded_multi)
# Expected: [{'id':1,'item':'book','price':199},{'id':2,'item':'pen','price':25}]


# ------------------------------------------------------------
# Ex4: In-memory bytes round-trip (dumps/loads)
# Problem: Serialize to BYTES (not a file) and back.
# ------------------------------------------------------------
payload = {"hello": "नमस्ते", "nums": (1, 2, 3)}
blob = pickle.dumps(payload, protocol=pickle.HIGHEST_PROTOCOL)  # bytes
restored = pickle.loads(blob)
print("Ex4 bytes len:", len(blob), "| restored:", restored)


# ------------------------------------------------------------
# Ex5: Complex object (tuple with mixed types)
# Problem: Pickle a tuple containing text, set, list, and float.
# ------------------------------------------------------------
complex_obj = ("data", {"a", "b"}, [10, 20], 3.14159)
with open("complex.pkl", "wb") as f:
    pickle.dump(complex_obj, f, protocol=pickle.HIGHEST_PROTOCOL)
with open("complex.pkl", "rb") as f:
    complex_back = pickle.load(f)
print("Ex5:", complex_back)


# ------------------------------------------------------------
# Ex6: Mini “gradebook” save & load
# Problem: Save a nested dict of marks, then load and print average.
# ------------------------------------------------------------
gradebook = {
    "Riya": {"Math": 90, "English": 82},
    "Aman": {"Math": 76, "English": 88},
}
with open("gradebook.pkl", "wb") as f:
    pickle.dump(gradebook, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("gradebook.pkl", "rb") as f:
    gb_back = pickle.load(f)

avg_riya = (gb_back["Riya"]["Math"] + gb_back["Riya"]["English"]) / 2
print("Ex6 Riya avg:", avg_riya)  # Expected: 86.0


# ------------------------------------------------------------
# Ex7: Protocol size comparison (ASCII protocol 0 vs highest)
# Problem: Compare serialized sizes for the same object.
# ------------------------------------------------------------
obj = {"k": list(range(20)), "msg": "hello"}
b_proto0 = pickle.dumps(obj, protocol=0)  # older, ASCII-ish text format
b_high   = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
print("Ex7 sizes:", len(b_proto0), "(proto0) vs", len(b_high), "(highest)")


# ------------------------------------------------------------
# Ex8: Tiny “index” file — names → scores
# Problem: Save a dict, then load and print sorted (by name) pairs.
# ------------------------------------------------------------
index_map = {"Sia": 84, "Aman": 91, "Riya": 88}
with open("index.pkl", "wb") as f:
    pickle.dump(index_map, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("index.pkl", "rb") as f:
    idx_back = pickle.load(f)

sorted_items = sorted(idx_back.items())  # list of (name, score)
print("Ex8:", sorted_items)  # Expected: [('Aman',91), ('Riya',88), ('Sia',84)]


# ------------------------------------------------------------
# Ex9: Handling bad data (UnpicklingError)
# Problem: Show safe handling when bytes are not valid pickle data.
# ------------------------------------------------------------
bad = b"not a pickle at all"
try:
    pickle.loads(bad)
except pickle.UnpicklingError as e:
    print("Ex9: UnpicklingError caught:", str(e))


# ------------------------------------------------------------
# Ex10: Pickle a simple custom class instance
# Problem: Save and load an object of a user-defined class (same script).
# ------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

p = Point(10, 20)
with open("point.pkl", "wb") as f:
    pickle.dump(p, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("point.pkl", "rb") as f:
    p_back = pickle.load(f)

print("Ex10:", p_back, "| coords:", p_back.x, p_back.y)  # Expected: Point(...) | 10 20

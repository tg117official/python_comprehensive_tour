# -*- coding: utf-8 -*-
"""
pickle_notes.py
Simple notes for beginners: Binary data, the pickle module, and pickle protocols.

You can just read this file like a mini-handbook. Running it is optional.
"""

# =============================================================================
# 1) BINARY DATA (WHAT IT IS)
# =============================================================================
# • Text (str) = human-readable characters, like "hello" or "नमस्ते".
# • Binary (bytes) = raw byte values (0–255). Not meant to be read as text.
# • In Python:
#     - bytes: immutable sequence of bytes. Example: b"ABC" or b"\x41\x42\x43"
#     - bytearray: like bytes, but mutable (you can change its contents).
# • Why this matters: pickle saves data as BYTES, not as text.
# • When working with files:
#     - Text mode  : open("file.txt",  "w", encoding="utf-8")  -> read/write str
#     - Binary mode: open("file.bin", "wb")                    -> read/write bytes
#
# Tip: Always open files in binary mode ('wb' to write, 'rb' to read) for pickle.


# =============================================================================
# 2) WHAT IS PICKLE? (PURPOSE)
# =============================================================================
# • Pickle is Python’s built-in way to "serialize" and "deserialize" Python objects.
#   - Serialize (pickle/dump): turn a Python object into bytes.
#   - Deserialize (unpickle/load): turn those bytes back into the original object.
#
# • PURPOSE (when to use it):
#   - Save and load Python objects (lists, dicts, custom classes, etc.) quickly.
#   - Share data between Python programs you control (same team, same environment).
#   - Make a quick cache or checkpoint of in-memory objects.
#
# • When NOT to use pickle:
#   - Never unpickle data from an untrusted source (security risk).
#   - Not good for sharing with other languages (format is Python-specific).
#   - Not the best for public, long-term archives (format may change over time).
#
# • Alternatives (use the right tool for the job):
#   - JSON: human-readable, good for simple data types (strings, numbers, lists, dicts).
#   - CSV/Parquet/Arrow: for tabular or analytics data.
#   - NumPy .npy/.npz, joblib: for arrays and scientific data.
#   - SQLite: small, simple database for structured data.


# =============================================================================
# 3) CORE PICKLE FUNCTIONS (JUST KNOW THE NAMES)
# =============================================================================
# • pickle.dump(obj, file, protocol=None)   -> write bytes to an open binary file.
# • pickle.load(file)                       -> read from an open binary file.
# • pickle.dumps(obj, protocol=None)        -> return bytes (in memory).
# • pickle.loads(bytes_obj)                 -> turn bytes back into an object.
#
# • protocol=None uses the default protocol for your Python version.
#   For best speed/size on your system, you can use protocol=pickle.HIGHEST_PROTOCOL.
#   For broad compatibility across most Python 3 versions, protocol=4 is a safe choice.


# =============================================================================
# 4) SAFETY WARNING (VERY IMPORTANT)
# =============================================================================
# • Unpickling can run code during loading.
# • If someone gives you a malicious pickle, it can be dangerous.
# • Rule: Only unpickle data you created yourself or from a source you fully trust.
# • If data is from outside or the internet, use a safer format (e.g., JSON).


# =============================================================================
# 5) PICKLE PROTOCOLS (WHAT THEY ARE + SIMPLE MEANINGS)
# =============================================================================
# “Protocol” = the version/format of the pickle byte stream.
# Newer protocols are usually faster and smaller, but older Python may not read them.
#
# Common protocols you’ll see in Python 3:
#
# • Protocol 0: Text (ASCII) format. Oldest, human-readable, biggest size. Rare today.
# • Protocol 1: Old binary format (Python 2 era). Mostly for legacy.
# • Protocol 2: Adds support for “new-style” classes (very old need). Legacy.
# • Protocol 3: Python 3 only; better handling of bytes objects. Older Py3 compatibility.
# • Protocol 4: Modern “default” in many Python 3 versions.
#               Supports large objects and more types. Good all-around choice.
# • Protocol 5: Python 3.8+ feature. Adds “out-of-band buffers” for big binary data
#               (helps when moving large byte arrays with less copying).
#
# Quick choices:
# • Don’t know what to pick and want wide Python 3 compatibility?  -> use protocol=4.
# • Want best speed/size on your current Python?                    -> use pickle.HIGHEST_PROTOCOL (often 5).
# • Teaching/demo and want something human-readable (not recommended for real use)? -> protocol=0.
#
# Notes on Protocol 5 (simple view):
# • Helps handle very large binary blobs efficiently (like big arrays).
# • Useful in multiprocessing or shared memory scenarios.
# • Only available on Python 3.8 and above.


# =============================================================================
# 6) WHAT PICKLE CAN/CAN’T HANDLE (BEGINNER VIEW)
# =============================================================================
# • Usually works fine with: numbers, strings, lists, dicts, sets, tuples,
#   and many user-defined classes.
# • Hard/problematic cases:
#   - Open file handles, active network connections, threads, database cursors.
#   - Big external resources need custom handling.
# • Classes can customize how they’re pickled by defining:
#   - __getstate__(self)  -> returns a dict-like “state” to save
#   - __setstate__(self, state) -> rebuild the object from saved state
#   (This is an advanced topic—just know it exists.)


# =============================================================================
# 7) BEST PRACTICES (CHEAT SHEET)
# =============================================================================
# • Safety first:
#   - Only unpickle trusted data.
# • Files:
#   - Always open files in binary mode for pickle: 'wb' for writing, 'rb' for reading.
# • Versioning:
#   - If sharing pickles with others, document the Python version + protocol used.
#   - For most Python 3 environments, protocol=4 is a good default.
#   - If everyone uses modern Python (3.8+), HIGHEST_PROTOCOL is fine.
# • Performance and size:
#   - Higher protocols usually give smaller/faster pickles.
#   - If file size matters, compress the pickle file (gzip/bz2/lzma) at the cost of CPU.
# • Interoperability:
#   - If you need to share data with non-Python tools, prefer formats like JSON, CSV, Parquet, or Arrow.


# =============================================================================
# 8) TINY REFERENCE (HOW A FILE SAVE/LOAD *WOULD* LOOK)
# =============================================================================
# (Shown for completeness—no need to run this if you’re just reading notes.)
#
# import pickle
#
# data = {"name": "Alice", "scores": [95, 88, 92]}
#
# # Save
# with open("data.pkl", "wb"):  # binary write
#     pickle.dump(data, open("data.pkl", "wb"), protocol=4)  # or pickle.HIGHEST_PROTOCOL
#
# # Load
# with open("data.pkl", "rb") as f:  # binary read
#     again = pickle.load(f)
#
# print(again)
#
# Keep in mind: Only load files you trust.


# =============================================================================
# OPTIONAL: PRINT YOUR PYTHON’S DEFAULTS (if you run this file)
# =============================================================================
if __name__ == "__main__":
    import pickle, sys
    print("Python version        :", sys.version.split()[0])
    print("DEFAULT_PROTOCOL      :", pickle.DEFAULT_PROTOCOL)
    print("HIGHEST_PROTOCOL      :", pickle.HIGHEST_PROTOCOL)
    print("Tip: Use protocol=4 for broad Python 3 compatibility,")
    print("     or pickle.HIGHEST_PROTOCOL for best results on this Python.")

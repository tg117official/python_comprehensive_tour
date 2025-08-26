# ============================================================
# Short Notes — Text File I/O (Python)
# ------------------------------------------------------------
# open(path, mode, encoding="utf-8")
#   Modes: "r" read (default), "w" write (overwrite/create),
#          "a" append (create if missing), "x" create new (error if exists),
#          "r+" read/write (file must exist)
# Use WITH so files auto-close:
#   with open("file.txt", "r", encoding="utf-8") as f:
#       data = f.read()
# Reading:
#   f.read() -> whole file (string)
#   f.readline() -> one line (keeps '\n')
#   f.readlines() -> list of lines
#   for line in f: ...  -> iterate lines efficiently
# Writing:
#   f.write("text\n")
#   f.writelines(["a\n", "b\n"])   # you must include '\n' yourself
# Paths:
#   Windows raw string: r"C:\data\notes.txt"  (backslashes literal)
#   Use UTF-8 for Unicode (emoji/हिंदी/etc.).
# ============================================================


# ------------------------------------------------------------
# Ex1: Write a new text file (overwrite/create)
# Problem: Create "notes.txt" with three lines of text.
# ------------------------------------------------------------
notes_file = "notes.txt"
with open(notes_file, "w", encoding="utf-8") as f:
    f.write("Welcome to file I/O.\n")
    f.write("This is line two.\n")
    f.write("End of notes.\n")
print("Ex1: wrote", notes_file)


# ------------------------------------------------------------
# Ex2: Read entire file at once
# Problem: Read notes.txt with read() and print the content.
# ------------------------------------------------------------
with open(notes_file, "r", encoding="utf-8") as f:
    content = f.read()
print("Ex2 content:\n" + content)


# ------------------------------------------------------------
# Ex3: Read line by line (iteration)
# Problem: Print notes.txt line numbers and text (strip the trailing newline).
# ------------------------------------------------------------
with open(notes_file, "r", encoding="utf-8") as f:
    line_no = 1
    for line in f:
        print("Ex3:", line_no, line.rstrip("\n"))
        line_no = line_no + 1


# ------------------------------------------------------------
# Ex4: Append to an existing file
# Problem: Append one more line to notes.txt, then show the last line back.
# ------------------------------------------------------------
with open(notes_file, "a", encoding="utf-8") as f:
    f.write("Appended line.\n")
# Read back last line quickly
with open(notes_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("Ex4 last line:", lines[-1].rstrip("\n"))  # Expected: Appended line.


# ------------------------------------------------------------
# Ex5: Create new file only if it doesn't exist
# Problem: Use mode "x" to create "log.txt"; if it exists, write to "log.txt" in append mode.
# ------------------------------------------------------------
log_file = "log.txt"
created = False
try:
    with open(log_file, "x", encoding="utf-8") as f:
        f.write("LOG START\n")
        created = True
except FileExistsError:
    # Fall back to append
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Log continues…\n")
print("Ex5:", "created" if created else "appended", log_file)


# ------------------------------------------------------------
# Ex6: readlines() and stripping whitespace
# Problem: Read all lines from notes.txt into a clean list without '\n'.
# ------------------------------------------------------------
with open(notes_file, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()
clean_lines = [ln.rstrip("\n") for ln in raw_lines]
print("Ex6 cleaned lines:", clean_lines)


# ------------------------------------------------------------
# Ex7: Count characters and words
# Problem: Show character count and word count of notes.txt.
# ------------------------------------------------------------
with open(notes_file, "r", encoding="utf-8") as f:
    text = f.read()
char_count = len(text)
word_count = len(text.split())
print("Ex7 chars:", char_count, "| words:", word_count)


# ------------------------------------------------------------
# Ex8: Simple CSV-like write & read (still plain text)
# Problem: Write "data.csv" with three records (name,age). Read it back and print names only.
# ------------------------------------------------------------
csv_file = "data.csv"
with open(csv_file, "w", encoding="utf-8") as f:
    f.write("name,age\n")
    f.write("Riya,21\n")
    f.write("Aman,25\n")
    f.write("Sia,19\n")

with open(csv_file, "r", encoding="utf-8") as f:
    header = f.readline()              # "name,age\n"
    line1 = f.readline().rstrip("\n")  # "Riya,21"
    line2 = f.readline().rstrip("\n")
    line3 = f.readline().rstrip("\n")

name1 = line1.split(",")[0]
name2 = line2.split(",")[0]
name3 = line3.split(",")[0]
print("Ex8 names:", name1, name2, name3)  # Expected: Riya Aman Sia


# ------------------------------------------------------------
# Ex9: Copy a text file (manual)
# Problem: Copy notes.txt to notes_copy.txt using read() then write().
# ------------------------------------------------------------
copy_file = "notes_copy.txt"
with open(notes_file, "r", encoding="utf-8") as src:
    data = src.read()
with open(copy_file, "w", encoding="utf-8") as dst:
    dst.write(data)
print("Ex9: copied to", copy_file)


# ------------------------------------------------------------
# Ex10: Unicode write/read with explicit encoding
# Problem: Write Hindi/emoji to unicode.txt and read it back.
# ------------------------------------------------------------
uni_file = "unicode.txt"
with open(uni_file, "w", encoding="utf-8") as f:
    f.write("नमस्ते 😊\n")
    f.write("Python loves Unicode!\n")

with open(uni_file, "r", encoding="utf-8") as f:
    u = f.read()
print("Ex10 content:\n" + u)

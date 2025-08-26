# ============================================================
# Mini Project: Student Gradebook & Report (CLI + Inputs)
# ------------------------------------------------------------
# Problem Statement:
# Build a command-line tool that:
# 1) Takes a comma-separated list of subjects and optional pass/full marks.
# 2) Asks the user for student details (name, roll, email).
# 3) Prompts marks for each subject and computes:
#    • per-subject pass/fail
#    • total, average, highest & lowest
#    • overall letter grade using simple thresholds
# 4) Prints a clean, formatted report showing all details using:
#    • string concatenation, repetition, membership checks
#    • f-strings, str.format(), and % formatting
#    • print(..., sep=..., end=...), alignment
# 5) Demonstrates basic containers: list (subjects), dict (marks),
#    set (unique subjects), tuple (grade scale).
#
# How to run (examples):
#   python gradebook.py --subjects "Math,English,Science" --pass-mark 40 --full-mark 100 --title "TG117 Report"
#   python gradebook.py --subjects "DS,DBMS,OS"
# ============================================================

import argparse

# ---------- Parse CLI ----------
parser = argparse.ArgumentParser(description="Student Gradebook & Report")
parser.add_argument("--subjects", type=str, default="Math,English,Science",
                    help="Comma-separated subjects (e.g., 'Math,English,Science')")
parser.add_argument("--pass-mark", type=int, default=40, dest="pass_mark",
                    help="Pass mark per subject (default: 40)")
parser.add_argument("--full-mark", type=int, default=100, dest="full_mark",
                    help="Full mark per subject (default: 100)")
parser.add_argument("--title", type=str, default="Student Grade Report",
                    help="Report title")
args = parser.parse_args()

# ---------- Prepare subjects (list + set demo) ----------
raw_subjects = args.subjects.split(",")
subjects = []
for s in raw_subjects:
    s = s.strip()
    if s != "":
        subjects.append(s)

unique_subjects = set(subjects)  # de-dup preview (we still keep original order list)
# tuple grade thresholds (letter, min average)
grade_scale = (("A", 90), ("B", 75), ("C", 60))  # else Fail

# ---------- Collect student details (inputs) ----------
student_name = input("Student name: ").strip()
roll_str = input("Roll number (integer): ").strip()
roll_no = int(roll_str)  # basic type conversion
email = input("Email: ").strip()

# Basic email flags (booleans + membership)
has_at = ("@" in email)
is_dotcom = email.endswith(".com")

# Demonstrate raw string (Windows-like path) + Unicode symbols
save_path = r"C:\Reports\TG117\2025"
tick = "✓"  # Unicode check mark
cross = "✗" # Unicode cross

# ---------- Marks input (dict + loops + math) ----------
marks = {}        # subject -> score
total = 0
i = 0
while i < len(subjects):
    sub = subjects[i]
    prompt = f"Marks for {sub} (out of {args.full_mark}): "
    m_int = int(input(prompt).strip())
    marks[sub] = m_int
    total = total + m_int
    i = i + 1

count = len(subjects)
average = total / count

# Highest & lowest (loop over list to preserve order)
# Initialize with first subject
first_subject = subjects[0]
max_subject, max_score = first_subject, marks[first_subject]
min_subject, min_score = first_subject, marks[first_subject]

for sub in subjects:
    sc = marks[sub]
    if sc > max_score:
        max_subject, max_score = sub, sc
    if sc < min_score:
        min_subject, min_score = sub, sc

# Overall letter grade (if/elif/else + tuples info available above)
if average >= grade_scale[0][1]:
    letter = grade_scale[0][0]
elif average >= grade_scale[1][1]:
    letter = grade_scale[1][0]
elif average >= grade_scale[2][1]:
    letter = grade_scale[2][0]
else:
    letter = "F"

# Pass/fail check (booleans via loop)
all_passed = True
for sub in subjects:
    if marks[sub] < args.pass_mark:
        all_passed = False

# Extra nested-if message about email validity (just for demo)
email_msg = ""
if has_at:
    if is_dotcom:
        email_msg = "Valid .com"
    else:
        email_msg = "Valid but not .com"
else:
    email_msg = "Invalid (missing @)"

# ---------- Pretty print report (strings, formatting, print options) ----------
line = "=" * 64
dash = "-" * 64

print(line)
print(args.title.center(64))
print(line)

# Mix of formatting styles
print("Student:", student_name, "| Roll:", roll_no, "| Email:", email, sep=" ")
print("Save Path (raw string):", save_path)
print("Subjects (list):", ", ".join(subjects))
print("Unique subjects (set):", unique_subjects)  # order not guaranteed
print("Grade scale (tuple):", grade_scale)
print(dash)

# Header with alignment
print(f"|{'Subject':<20}|{'Marks':>10}|{'Out of':>10}|{'Pass?':>10}|")
print(dash)

for sub in subjects:
    sc = marks[sub]
    passed = (sc >= args.pass_mark)
    symbol = tick if passed else cross
    # str.format demo:
    row = "|{s:<20}|{m:>10}|{fm:>10}|{pf:>10}|".format(
        s=sub, m=sc, fm=args.full_mark, pf=symbol
    )
    print(row)

print(dash)
# old-style % formatting for one line:
print("Total: %d   Average: %.2f   Highest: %s=%d   Lowest: %s=%d" %
      (total, average, max_subject, max_score, min_subject, min_score))

# f-strings with alignment and booleans
print(f"All subjects passed? {all_passed}")
print(f"Overall Letter Grade: {letter}")

# Use print end/sep variations
print(dash)
print("Email check:", end=" ")
print(email_msg)
print("Summary:", "Name", student_name, "Roll", roll_no, sep=" | ")

# Tiny final box
print(line)
title_box = f"Result: {(tick if all_passed else cross)}  Grade={letter}"
print(title_box.center(64))
print(line)

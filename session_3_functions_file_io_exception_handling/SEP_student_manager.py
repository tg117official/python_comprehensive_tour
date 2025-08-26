# ============================================================
# Mini Project: “Student Manager” (CLI + Inputs + Files)
# ------------------------------------------------------------
# Problem Statement
# Build a simple tool that:
# 1) Takes a list of subjects via CLI; validates pass/full marks.
# 2) Asks user for student info; records marks per subject.
# 3) Computes totals/average/highest/lowest, pass/fail, letter grade.
# 4) Prints a neat receipt-style report (various string/print techniques).
# 5) Saves a human-readable report (text file) and a binary Gradebook (pickle).
# 6) Demonstrates: lists/tuples/sets/dicts, booleans, loops, conditions,
#    functions (no params, params, defaults, *args, **kwargs, recursion),
#    raw path + Unicode, math ops, and exception handling.
# ============================================================

import argparse
import pickle

# ---------- Functions (covering the requested variants) ----------
def banner():  # no parameters
    print("=== Welcome to Student Manager ===")

def percent(numerator, denominator):  # two parameters
    return (numerator / denominator) * 100

def average(*nums):  # *args (n parameters)
    if len(nums) == 0:
        return None
    total = 0
    for x in nums:
        total = total + x
    return total / len(nums)

def grade_for(avg, scale=(("A", 90), ("B", 75), ("C", 60))):  # default argument + tuple use
    if avg >= scale[0][1]:
        return scale[0][0]
    elif avg >= scale[1][1]:
        return scale[1][0]
    elif avg >= scale[2][1]:
        return scale[2][0]
    else:
        return "F"

def full_name(**kwargs):  # **kwargs
    first = kwargs.get("first", "")
    middle = kwargs.get("middle", "")
    last = kwargs.get("last", "")
    title = kwargs.get("title", "")
    name = (title + " " if title else "") + first + (" " + middle if middle else "") + (" " + last if last else "")
    return name.strip()

def factorial(n):  # recursion
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def validate_range(label, value, min_val=0, max_val=100):  # defaults + raise
    if value < min_val or value > max_val:
        raise ValueError(f"{label} must be between {min_val} and {max_val}. Got {value}.")
    return value

# ---------- CLI ----------
parser = argparse.ArgumentParser(description="Student Manager")
parser.add_argument("--subjects", type=str, default="Math,English,Science",
                    help="Comma-separated subjects, e.g. 'Math,English,Science'")
parser.add_argument("--pass-mark", type=int, default=40, dest="pass_mark",
                    help="Pass mark per subject (default 40)")
parser.add_argument("--full-mark", type=int, default=100, dest="full_mark",
                    help="Full mark per subject (default 100)")
parser.add_argument("--load", action="store_true", help="Load existing gradebook.pkl if present")
args = parser.parse_args()

# Validate CLI numbers (exception + raise)
try:
    validate_range("Pass mark", args.pass_mark, 0, args.full_mark)
except ValueError as e:
    print("CLI Error:", e)
    # Keep going with defaults to keep the demo simple
    args.pass_mark = 40
    args.full_mark = max(args.full_mark, 40)

# ---------- Start ----------
banner()

# Raw path demo + Unicode symbols
save_dir = r"C:\TG117\Reports"      # raw string (backslashes literal)
tick, cross, rupee = "✓", "✗", "₹"  # Unicode symbols

# Subjects (list) + Set de-dup + Slicing/Step demo
subjects_input = [s.strip() for s in args.subjects.split(",") if s.strip()]
unique_subjects = set(subjects_input)            # set
subjects = list(unique_subjects)                 # keep it simple; order may change
subjects_preview = subjects[:2]                  # slicing
subjects_reversed = subjects[::-1]               # step slicing (reverse)

# Student inputs
print("\nEnter student details")
first = input("First name: ").strip()
last = input("Last name: ").strip()
roll_str = input("Roll number (integer): ").strip()
email = input("Email: ").strip()

# Basic conversions + booleans
try:
    roll_no = int(roll_str)
except ValueError:
    print("Roll number invalid; defaulting to 0.")
    roll_no = 0
has_at = "@" in email
is_dotcom = email.endswith(".com")
batch_guess = roll_no // 100  # floor division (math)

# Build a canonical name using **kwargs
student_name = full_name(first=first, last=last)

# Collect marks (dict + loops + try/except)
marks = {}  # dict: subject -> score
print("\nEnter marks (out of", args.full_mark, ")")
for sub in subjects:
    raw = input(f"  {sub}: ").strip()
    try:
        score = int(raw)
        validate_range(f"{sub} marks", score, 0, args.full_mark)
    except ValueError as e:
        print("  Warning:", e, "| Using 0.")
        score = 0
    marks[sub] = score

# Compute totals/average/highest/lowest (lists/loops/if)
scores_list = [marks[s] for s in subjects]       # list
total = 0
for sc in scores_list:
    total = total + sc
avg = average(*scores_list) or 0                 # *args
letter = grade_for(avg)                          # default arg function

# Highest/Lowest
max_sub, max_score = subjects[0], marks[subjects[0]]
min_sub, min_score = subjects[0], marks[subjects[0]]
for sub in subjects:
    sc = marks[sub]
    if sc > max_score:
        max_sub, max_score = sub, sc
    if sc < min_score:
        min_sub, min_score = sub, sc

# Pass/fail (booleans + if/else)
all_passed = True
for sc in scores_list:
    if sc < args.pass_mark:
        all_passed = False

# Tiny nested-if demo for email message
if has_at:
    if is_dotcom:
        email_msg = "Valid .com"
    else:
        email_msg = "Valid but not .com"
else:
    email_msg = "Invalid email (missing @)"

# A tiny recursion use: factorial of subject count (just to show recursion)
sub_fact = factorial(len(subjects))

# ---------- Pretty console report (string ops/interpolation/print controls) ----------
line = "=" * 64
dash = "-" * 64
print("\n" + line)
print("STUDENT REPORT".center(64))
print(line)

# Mix of comma-sep printing + sep/end
print("Name:", student_name, "| Roll:", roll_no, "| Batch guess:", batch_guess, sep=" ")
print("Email:", email, "|", email_msg)
print("Save directory (raw path):", save_dir)
print("Subjects preview:", subjects_preview, "| reversed:", subjects_reversed)

# Different interpolation styles
print(dash)
print(f"|{'Subject':<20}|{'Marks':>10}|{'Out of':>10}|{'Pass?':>8}|")
print(dash)
for sub in subjects:
    sc = marks[sub]
    symbol = tick if sc >= args.pass_mark else cross
    print("|{:<20}|{:>10}|{:>10}|{:>8}|".format(sub, sc, args.full_mark, symbol))
print(dash)
print("Total: %d   Average: %.2f   Highest: %s=%d   Lowest: %s=%d" %
      (total, avg, max_sub, max_score, min_sub, min_score))
print(f"Overall: {'PASSED' if all_passed else 'FAILED'}  Grade={letter}  (subjects! = {sub_fact})")
print(f"Fees sample: {rupee}{(total/len(subjects)):.2f} per subject (illustration)")
print(line)

# ---------- Save human-readable report (TEXT) with try/except/else/finally ----------
report_name = f"report_{roll_no}.txt"
f = None
try:
    f = open(report_name, "w", encoding="utf-8")
    f.write(line + "\n")
    f.write(f"Report for {student_name} (Roll {roll_no})\n")
    f.write(line + "\n")
    for sub in subjects:
        f.write(f"{sub:<20} : {marks[sub]:>3}/{args.full_mark}\n")
    f.write(dash + "\n")
    f.write(f"Total={total}  Average={avg:.2f}  Grade={letter}\n")
    f.write(f"Email check: {email_msg}\n")
except OSError as e:
    print("File write error:", e)
else:
    print(f"Report saved to {report_name}")
finally:
    if f is not None:
        f.close()
        print("Report file closed?", f.closed)

# ---------- Save Gradebook (PICKLE) with try/except/else/finally ----------
gradebook_file = "gradebook.pkl"
# Try to load existing (if --load), else start fresh
if args.load:
    try:
        with open(gradebook_file, "rb") as rf:
            gradebook = pickle.load(rf)
    except FileNotFoundError:
        gradebook = {}
else:
    gradebook = {}

# Update gradebook (dict of roll -> record)
record = {
    "name": student_name,
    "email": email,
    "subjects": subjects,
    "marks": marks,
    "total": total,
    "average": avg,
    "grade": letter,
    "all_passed": all_passed,
}
gradebook[roll_no] = record

pf = None
try:
    pf = open(gradebook_file, "wb")
    pickle.dump(gradebook, pf, protocol=pickle.HIGHEST_PROTOCOL)
except OSError as e:
    print("Pickle save error:", e)
else:
    print(f"Gradebook updated -> {gradebook_file} ({len(gradebook)} students)")
finally:
    if pf is not None:
        pf.close()

# ---------- Tiny post-checks (dict/list/set/tuple basics) ----------
print("\nQuick checks:")
print("Keys in gradebook:", list(gradebook.keys()))
print("First 2 subjects (slice):", subjects[:2], "| Reverse:", subjects[::-1])
print("Unique subject count (set):", len(set(subjects)))
print("Grade scale (tuple) used:", (("A", 90), ("B", 75), ("C", 60)))

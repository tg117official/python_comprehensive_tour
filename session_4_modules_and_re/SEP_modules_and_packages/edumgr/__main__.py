import argparse
from . import patterns, utils, report, storage


# Sample run command
# # 1) Put these files in a folder (shown below)
# # 2) From the parent folder, run:
# python -m edumgr --subjects "Math, English, Science" --pass-mark 40 --full-mark 100 --title "Midterm Report"
def main():
    # ---------- CLI ----------
    ap = argparse.ArgumentParser(description="EduMgr — Student Manager (regex + files)")
    ap.add_argument("--subjects", type=str, default="Math, English, Science")
    ap.add_argument("--pass-mark", type=int, default=40, dest="pass_mark")
    ap.add_argument("--full-mark", type=int, default=100, dest="full_mark")
    ap.add_argument("--title", type=str, default="Student Report")
    ap.add_argument("--gradebook", type=str, default="gradebook.pkl")
    ap.add_argument("--load", action="store_true", help="Load existing gradebook first")
    args = ap.parse_args()

    # ---------- Start ----------
    utils.banner()

    # Raw string + Unicode (strings topic)
    save_dir = r"C:\EduMgr\Reports"   # raw path example (prints literally)
    tick, cross, rupee = "✓", "✗", "₹"

    # Validate basic numeric ranges (exceptions + raise)
    try:
        utils.validate_range("Pass mark", args.pass_mark, 0, args.full_mark)
    except ValueError as e:
        print("CLI Warning:", e, "| Using defaults 40/100.")
        args.pass_mark, args.full_mark = 40, max(100, args.full_mark)

    # ---------- Subjects via regex split (lists/sets/tuples/strings) ----------
    subjects = patterns.split_subjects(args.subjects)
    if not subjects:
        subjects = ["Math", "English", "Science"]
    # De-dup with set (order may change; okay for demo)
    subjects = list(set(subjects))
    subjects_preview = subjects[:2]
    subjects_rev = subjects[::-1]

    # ---------- Inputs ----------
    print("\nEnter student details")
    first = input("First name: ").strip()
    last  = input("Last name: ").strip()
    roll_str = input("Roll number (digits only): ").strip()
    email = input("Email: ").strip()

    # Regex validation (regular expressions!)
    if not patterns.is_valid_roll(roll_str):
        print("Note: Roll looks invalid; defaulting to 0.")
        roll_no = 0
    else:
        roll_no = int(roll_str)

    email_msg = "Valid .com"
    if not patterns.is_valid_email(email):
        email_msg = "Invalid email"
    elif not email.endswith(".com"):
        email_msg = "Valid but not .com"

    # ---------- Marks (dict + loops + regex parse + exceptions) ----------
    marks = {}
    print(f"\nEnter marks (out of {args.full_mark}). You may type '90' or '90/{args.full_mark}'.")
    total = 0
    for sub in subjects:
        raw = input(f"  {sub}: ").strip()
        try:
            score, out_of = patterns.parse_mark(raw)
            if out_of is not None and out_of != args.full_mark:
                print(f"  Note: you typed out_of={out_of}; using CLI full_mark={args.full_mark}.")
            score = utils.validate_range(f"{sub} marks", score, 0, args.full_mark)
        except ValueError as e:
            print("  Warning:", e, "| Using 0.")
            score = 0
        marks[sub] = score
        total = total + score

    # ---------- Stats (math, lists, tuples, booleans, functions) ----------
    scores_list = [marks[s] for s in subjects]
    avg = utils.average(*scores_list) or 0.0
    letter = utils.grade_for(avg)

    # Highest / Lowest
    max_sub, max_score = subjects[0], marks[subjects[0]]
    min_sub, min_score = subjects[0], marks[subjects[0]]
    for sub in subjects:
        sc = marks[sub]
        if sc > max_score:
            max_sub, max_score = sub, sc
        if sc < min_score:
            min_sub, min_score = sub, sc

    all_passed = True
    for sc in scores_list:
        if sc < args.pass_mark:
            all_passed = False

    # Recursion cameo (factorial of subject count)
    fact_subjects = utils.factorial(len(subjects))

    # Full name via **kwargs
    student_name = utils.full_name(first=first, last=last)

    # Simple fee sample using rupee symbol (unicode)
    sample_fee = f"{rupee}{(total/len(subjects)):.2f}"

    # ---------- Console output (printing & formatting) ----------
    line = "=" * 64
    dash = "-" * 64
    print("\n" + line)
    print(args.title.center(64))
    print(line)
    print("Name:", student_name, "| Roll:", roll_no, "| Email:", email, sep=" ")
    print("Save directory (raw):", save_dir)
    print("Subjects preview:", subjects_preview, "| reversed:", subjects_rev)

    table = report.make_console_table(subjects, marks, args.full_mark, args.pass_mark, tick, cross)
    print(table)
    print(report.summary_line(total, avg, (max_sub, max_score), (min_sub, min_score)))
    print(f"Overall: {'PASSED' if all_passed else 'FAILED'}   Grade={letter}   subj!={fact_subjects}")
    print("Sample fee per subject:", sample_fee)
    print(line)

    # ---------- Text report (file I/O with try/except/else/finally) ----------
    body_lines = [
        f"Subjects: {', '.join(subjects)}",
        f"Total={total}  Average={avg:.2f}  Grade={letter}",
        f"Highest: {max_sub}={max_score}  Lowest: {min_sub}={min_score}",
        f"All Passed? {all_passed}",
    ]
    txt = report.build_text_report(student_name, roll_no, email_msg, [table, *body_lines])
    report_path = f"report_{roll_no}.txt"
    storage.write_text(report_path, txt)

    # ---------- Gradebook (pickle I/O with safety) ----------
    gradebook = storage.load_gradebook(args.gradebook) if args.load else {}
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
    storage.save_gradebook(args.gradebook, gradebook)

if __name__ == "__main__":
    main()

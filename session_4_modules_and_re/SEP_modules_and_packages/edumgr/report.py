# Pretty console/text report formatting (strings & interpolation)
def make_console_table(subjects, marks, full_mark, pass_mark, tick="✓", cross="✗"):
    line = "=" * 64
    dash = "-" * 64
    rows = []
    rows.append(line)
    rows.append(f"|{'Subject':<20}|{'Marks':>10}|{'Out of':>10}|{'Pass?':>8}|")
    rows.append(dash)
    for sub in subjects:
        sc = marks[sub]
        passed = tick if sc >= pass_mark else cross
        rows.append("|{:<20}|{:>10}|{:>10}|{:>8}|".format(sub, sc, full_mark, passed))
    rows.append(dash)
    return "\n".join(rows)

def summary_line(total, avg, max_pair, min_pair):
    # old-style % formatting just to demonstrate:
    return "Total: %d   Average: %.2f   Highest: %s=%d   Lowest: %s=%d" % (
        total, avg, max_pair[0], max_pair[1], min_pair[0], min_pair[1]
    )

def build_text_report(student_name, roll_no, email_msg, body_lines):
    line = "=" * 64
    parts = []
    parts.append(line)
    parts.append(f"Report for {student_name} (Roll {roll_no})")
    parts.append(line)
    parts.extend(body_lines)
    parts.append(f"Email check: {email_msg}")
    parts.append(line)
    return "\n".join(parts)

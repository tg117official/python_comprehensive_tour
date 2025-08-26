# ============================================================
# Short Notes — Exception Handling in Python
# ------------------------------------------------------------
# try:       put risky code here
# except X:  handle exception type X (use specific types when possible)
# else:      runs if NO exception happened in the try block
# finally:   runs ALWAYS (success or failure) — great for cleanup/closing
# raise E:   create/throw an exception (e.g., raise ValueError("bad"))
#
# Tips:
# • Catch specific exceptions (ValueError, ZeroDivisionError, FileNotFoundError).
# • Avoid bare 'except:'; prefer 'except Exception as e:' only at top-level.
# • Use 'else' for the success path; use 'finally' for releasing resources.
# • You can re-raise the current exception with just 'raise'.
# ============================================================


# ------------------------------------------------------------
# Ex1: Basic try/except (ValueError while converting to int)
# Problem: Convert strings to int; on error, print a friendly message.
# ------------------------------------------------------------
good = "42"
bad  = "42x"
try:
    a = int(good)
    b = int(bad)  # This will raise ValueError
    print("Ex1:", a, b)  # won't reach here for 'bad'
except ValueError as e:
    print("Ex1: Could not convert to int ->", str(e))


# ------------------------------------------------------------
# Ex2: Division with ZeroDivisionError
# Problem: Divide 100 by a denominator; catch divide-by-zero.
# ------------------------------------------------------------
num = 100
den = 0
try:
    ans = num / den
    print("Ex2:", ans)
except ZeroDivisionError as e:
    print("Ex2: Cannot divide by zero:", e)


# ------------------------------------------------------------
# Ex3: Multiple except blocks (specific handling)
# Problem: Convert input to float and divide 50 by it.
# ------------------------------------------------------------
raw = "five"  # try changing to "10" or "0"
try:
    val = float(raw)
    print("Ex3:", 50 / val)
except ValueError:
    print("Ex3: Please enter a number (e.g., 10).")
except ZeroDivisionError:
    print("Ex3: Denominator cannot be zero.")


# ------------------------------------------------------------
# Ex4: try/except/else (use else for success path)
# Problem: Parse "3.14". If success, print "Parsed OK" in else.
# ------------------------------------------------------------
text = "3.14"
try:
    pi = float(text)
except ValueError:
    print("Ex4: Not a float.")
else:
    print("Ex4: Parsed OK ->", pi)


# ------------------------------------------------------------
# Ex5: finally for cleanup (close a file even on errors)
# Problem: Open a file, read first line, ensure it closes in finally.
# ------------------------------------------------------------
fname = "sample.txt"
# prepare a small file
with open(fname, "w", encoding="utf-8") as wf:
    wf.write("hello\nworld\n")

f = None
try:
    f = open(fname, "r", encoding="utf-8")
    first = f.readline()
    print("Ex5: first line =", first.rstrip("\n"))
    # Force an error to prove 'finally' still runs:
    _ = 1 / 0
except ZeroDivisionError:
    print("Ex5: Oops, math error (simulated).")
finally:
    if f is not None:
        f.close()
    print("Ex5: file closed? ->", f.closed)


# ------------------------------------------------------------
# Ex6: raise for validation (custom message)
# Problem: Validate age >= 0; otherwise raise ValueError with message.
# ------------------------------------------------------------
age = -3
try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Ex6: Age is", age)
except ValueError as e:
    print("Ex6:", e)


# ------------------------------------------------------------
# Ex7: Custom exception class + handling
# Problem: Raise a custom error if withdrawal exceeds balance.
# ------------------------------------------------------------
class InsufficientFundsError(Exception):
    pass

balance = 500
withdraw = 700
try:
    if withdraw > balance:
        raise InsufficientFundsError(f"Need ₹{withdraw - balance} more.")
    balance = balance - withdraw
    print("Ex7: New balance =", balance)
except InsufficientFundsError as e:
    print("Ex7:", e)


# ------------------------------------------------------------
# Ex8: Re-raising exceptions (log then propagate)
# Problem: Catch ValueError, log it, re-raise, and catch again outside.
# ------------------------------------------------------------
def to_int(s):
    try:
        return int(s)
    except ValueError as e:
        print("Ex8(inner): logging ->", e)
        raise  # re-raise the SAME exception

try:
    _ = to_int("12a")
except ValueError as outer:
    print("Ex8(outer): caught re-raised ->", outer)


# ------------------------------------------------------------
# Ex9: IndexError handling with else
# Problem: Safely access an index; if OK, print the value in else.
# ------------------------------------------------------------
arr = [10, 20, 30]
idx = 5
try:
    val = arr[idx]
except IndexError as e:
    print("Ex9:", "Bad index:", idx, "|", e)
else:
    print("Ex9: Value =", val)


# ------------------------------------------------------------
# Ex10: KeyError handling vs safe .get()
# Problem: Show difference between dict[key] and dict.get(key, default).
# ------------------------------------------------------------
user = {"name": "Asha", "city": "Pune"}
try:
    phone = user["phone"]  # will raise KeyError
except KeyError as e:
    print("Ex10: Missing key ->", e)

phone_safe = user.get("phone", "NA")
print("Ex10: Safe get ->", phone_safe)  # Expected: NA

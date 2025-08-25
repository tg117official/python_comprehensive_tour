# ============================================================
# Mini Project: Simple Receipt Builder (CLI + Input)
# ------------------------------------------------------------
# Problem Statement:
# Build a command-line tool that:
# 1) Accepts item prices (one or more) and optional --discount and --tax.
# 2) Asks the user for customer details via input(): name, city, and email.
# 3) Computes Subtotal, Discount, After-Discount, Tax, and Total.
# 4) Prints a clean, well-formatted receipt demonstrating:
#    - string concatenation (+) and repetition (*)
#    - f-strings / .format / % formatting
#    - print(..., sep=..., end=...) and alignment
#    - Unicode (₹) and a raw string example (Windows-like path)
#
# Examples:
#   python receipt.py 199.99 349 49.5 --discount 10 --tax 18
#   python receipt.py 799 --tax 5
#   python receipt.py 120 80 60 --discount 15
#
# Notes:
# - Uses only features discussed in this chat.
# - No loops or custom functions; just straight-line code.
# ============================================================

import argparse

# ---------- Parse Command-Line Parameters ----------
parser = argparse.ArgumentParser(description="Build a simple receipt from prices.")
parser.add_argument("prices", nargs="+", type=float, help="Item prices (one or more).")
parser.add_argument("--discount", type=float, default=0.0, help="Discount % (e.g., 10).")
parser.add_argument("--tax", type=float, default=0.0, help="Tax % after discount (e.g., 18).")
args = parser.parse_args()

# ---------- Collect Basic Customer Inputs ----------
customer_name = input("Enter customer name: ").strip()
customer_city = input("Enter city: ").strip()
customer_email = input("Enter email: ").strip()

# ---------- Core Calculations (Math Operators) ----------
subtotal = sum(args.prices)
discount_amount = subtotal * (args.discount / 100.0)
after_discount = subtotal - discount_amount
tax_amount = after_discount * (args.tax / 100.0)
total = after_discount + tax_amount

# ---------- Formatting Helpers (Strings & Interpolation) ----------
line = "=" * 46
dash = "-" * 46
currency_symbol = "₹"  # Unicode (works in Python 3 strings)

# Compose a joined string of item prices using formatting
items_str = ", ".join(f"{p:.2f}" for p in args.prices)  # (generator expression only)

# Demonstrate raw string (no special meaning for backslashes)
save_path = r"C:\Receipts\TG117\2025"

# Quick email checks using string operators (no conditions, just booleans)
has_at = ("@" in customer_email)
ends_common = (customer_email.endswith(".com"))  # simple method use, no branching

# ---------- Print Receipt (Different Printing Styles) ----------
print(line)
print("RECEIPT".center(46))
print(line)

# Using commas + sep
print("Customer:", customer_name, "| City:", customer_city, "| Email:", customer_email, sep=" ")

# f-strings for inline expressions
print(f"Items: {items_str}")

# Old-style % formatting (still valid)
print("Subtotal: %s%.2f" % (currency_symbol, subtotal))

# str.format with named placeholders
print("Discount ({d:.2f}%): -{c}{amt:.2f}".format(d=args.discount, c=currency_symbol, amt=discount_amount))

# f-string again
print(f"After Discount: {currency_symbol}{after_discount:.2f}")
print(f"Tax ({args.tax:.2f}%):    +{currency_symbol}{tax_amount:.2f}")
print(dash)
print(f"Total:          {currency_symbol}{total:.2f}")

# Alignment demo
print(dash)
print(f"|{'Field':<18}|{'Value':>25}|")
print(dash)
print(f"|{'Currency':<18}|{currency_symbol:>25}|")
print(f"|{'Email has @?':<18}|{str(has_at):>25}|")
print(f"|{'Ends with .com?':<18}|{str(ends_common):>25}|")

# print(..., end=...) to keep same line, then newline
print(dash)
print("Save Path:", end=" ")
print(save_path)  # raw string printed as typed (backslashes literal)

# Another small demo: custom date print with sep
year, month, day = 2025, 8, 25
print("Generated on:", year, month, day, sep="-")  # 2025-8-25

print(line)
print(f"Thank you, {customer_name}!".center(46))
print(line)
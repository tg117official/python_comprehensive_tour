# ============================================================
# Short Notes — Python String Types (Normal, Raw & Unicode)
# ------------------------------------------------------------
# Normal strings: interpret escape sequences like \n (newline), \t (tab), \" (quote), \\ (backslash).
# Raw strings (prefix r"..."): backslashes are taken literally (no escapes). Great for paths/regex.
#   - Still must escape the quote if it matches the string delimiter.
#   - Cannot end with a single backslash (syntax error), e.g., r"foo\"  # ❌
# Unicode strings: In Python 3, ALL strings are Unicode by default (they can store characters from any language).
#   - Use .encode("utf-8") to get bytes for saving/sending; .decode("utf-8") to get back text from bytes.
#   - The u"..." prefix is allowed in Python 3 but is identical to "..." (both are Unicode).
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Normal String — Newline & Tab
# Problem: Create a normal string that includes a newline and a tab, then print it.
# ------------------------------------------------------------
s1 = "Line1\nLine2\tTabbed"
print(s1)  # Expected: "Line1" then a newline, then "Line2    Tabbed"


# ------------------------------------------------------------
# Exercise 2: Raw String — Show Literal Backslashes
# Problem: Create a Windows-style path both as a normal string and as a raw string; print both.
# ------------------------------------------------------------
path_normal = "C:\new\test"        # \n ⇒ newline, \t ⇒ tab (not literal backslashes)
path_raw = r"C:\new\test"          # backslashes stay as-is
print("Normal path:", path_normal)
print("Raw path   :", path_raw)


# ------------------------------------------------------------
# Exercise 3: Unicode Greeting (Multilingual)
# Problem: Store a greeting with non-English characters and print it.
# ------------------------------------------------------------
greet = "नमस्ते, 世界"   # Hindi + Chinese characters
print(greet)  # Expected: The exact multilingual text


# ------------------------------------------------------------
# Exercise 4: Characters vs Bytes (UTF-8)
# Problem: For the word "café", print the character count and the byte count when UTF-8 encoded.
# ------------------------------------------------------------
word = "café"
chars = len(word)
bytes_len = len(word.encode("utf-8"))
print("Chars:", chars)          # Expected: 4
print("UTF-8 bytes:", bytes_len)  # Expected: 5 (é takes 2 bytes in UTF-8)


# ------------------------------------------------------------
# Exercise 5: Raw String for a Regex-like Pattern
# Problem: Create a raw string for a pattern that contains backslashes and print it.
# ------------------------------------------------------------
pattern_raw = r"\d+\s\w+"
print("Pattern:", pattern_raw)  # Expected: \d+\s\w+ (backslashes shown literally)


# ------------------------------------------------------------
# Exercise 6: Escaping Quotes (Normal vs Raw)
# Problem: Write a string that includes double quotes inside. Do it once as normal, once as raw.
# ------------------------------------------------------------
quoted_normal = "He said, \"hello\""
quoted_raw = r"He said, \"hello\""   # quotes still need escaping in raw strings
print(quoted_normal)
print(quoted_raw)


# ------------------------------------------------------------
# Exercise 7: Multiline String (Triple Quotes)
# Problem: Create a normal triple-quoted string spanning multiple lines and print it.
# ------------------------------------------------------------
multi = """First line
Second line
Third line"""
print(multi)


# ------------------------------------------------------------
# Exercise 8: Unicode Prefix u"..." in Python 3
# Problem: Use u"..." and show it behaves like a normal string (both are Unicode).
# ------------------------------------------------------------
u_text = u"हिंदी"
normal_text = "हिंदी"
print(u_text, normal_text)            # Same visual
print(isinstance(u_text, str))        # Expected: True
print(isinstance(normal_text, str))   # Expected: True


# ------------------------------------------------------------
# Exercise 9: Encode and Decode Roundtrip
# Problem: Create a string with a currency symbol, encode to UTF-8 bytes, then decode back to text.
# ------------------------------------------------------------
price_text = "Total: ₹1500"
price_bytes = price_text.encode("utf-8")
restored = price_bytes.decode("utf-8")
print(price_bytes)  # Expected: b'...' (byte sequence)
print(restored)     # Expected: "Total: ₹1500"


# ------------------------------------------------------------
# Exercise 10: Emoji Length vs Bytes
# Problem: Create a string with two emojis, print character length and UTF-8 byte length.
# ------------------------------------------------------------
faces = "🙂🙂"
print("Chars:", len(faces))                 # Expected: 2
print("UTF-8 bytes:", len(faces.encode("utf-8")))  # Expected: 8 (each emoji is 4 bytes in UTF-8)

import re

text = """Alice was born on 1990-05-20 in New York.
Bob's email is bob@example.com.
The project deadline is approaching: 2024-07-31.
John's phone numbers are 321-555-4321, 123.555.1234
, 123*555*1234
, 800-555-1234
, 900-555-1234.
cat
mat
pat
bat
Mr. John
Mr James
Mr Sunder
Mr. Satya
Ms Dibya
Mrs. Ashwini
Mr. A

emails = 
thisIsSample@gmail.com
IamStudent@university.edu
my-117-business@my-work.net

https://www.google.com
http://technologicalgeeks.in
https://youtube.com
https://www.nasa.gov

"""
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'at')
matches = pattern.finditer(text)

for match in matches :
    print(match)

# Study Drills :
# 1. Match all three digits : r'\d\d\d'
# 2. Match all phone numbers : r'\d\d\d.\d\d\d.\d\d\d\d'
# 3. Match all phone numbers with . and - as separator : r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d'
# 4. Match all phone numbers starting with 800 or 900 : r'[89]00[-.]\d\d\d[-.]\d\d\d\d'
# 5. Match all numbers in range 1 to 5 : r[1-5]
# 6. Match all lowercase a to z : r[a-z]
# 7. Match all lowercase and uppercase a to z : r[a-zA-Z]
# 8. Match everything which is not lowercase or uppercase a to z : r'[^a-zA-Z]' | caret here works like negation
# 9. Write Regular Expression to match cat,pat except bat : r'[^b]at'
# 10. Use {} quantifier to match the phone numbers : r'\d{3}.\d{3}.\d{4}'
# 11. Match all Mr. in the text : r'Mr\.'
# 12. Match all Mr and Mr. in the text : r'Mr\.?'
# 13. Match all Mr, Mr. and Initial capital letter in front of it : r'Mr\.?\s[A-Z]'
# 14. Match all Mr, Mr. and name in front of it (except single char name) : r'Mr.\?\s[A-Z]\w+'
# 15. Match all Mr, Mr. and name in front of it (except single char name) : r'Mr.\?\s[A-Z]\w*'
# 16. Match all Mr, Mr., Mrs., Mrs, Ms, Ms. and name in front of it : r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'
# 17. Match all emails with small and capital letters , @ , letters , .com : r'[a-zA-Z]+@[a-zA-Z]+\.com'
# 18. Allow . in first part of email : r'[a-zA-Z.]+@[a-zA-Z]+\.com'
# 19. Allow .edu as the last part of email : r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)'
# 20. Allow 0-9 digits and - in first part of email and domain and .net as extension: r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)'
# 21. Match all email ids with domain name length raning from 3 to 5 characters : r'\w+@\w+\.[a-z]{3,5}'
# 22. Write regular expression to match the URLs : r'https?://(www\.)?(\w+)(\.\w+)'
# 23. Print group(0), group(1), group(2), group(3)

# ============================================================
# REGEX QUESTIONS WITH FULL ELEMENT-BY-ELEMENT NOTES
# ============================================================

# 1. Match all three digits
# Pattern: r'\d\d\d'
#   \d   → digit (0–9)
#   \d   → second digit
#   \d   → third digit
# Place: matches exactly 3 consecutive digits anywhere.

# 2. Match all phone numbers (any single-char separator)
# Pattern: r'\d\d\d.\d\d\d.\d\d\d\d'
#   \d\d\d   → 3 digits (first block)
#   .        → any single character (separator)
#   \d\d\d   → 3 digits (second block)
#   .        → separator again
#   \d\d\d\d → 4 digits (last block)
# Place: matches phone-like patterns with any separator.

# 3. Phone numbers with only - or . as separator
# Pattern: r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d'
#   \d\d\d   → 3 digits
#   [-.]     → dash or dot (char class)
#   \d\d\d   → 3 digits
#   [-.]     → dash or dot again
#   \d\d\d\d → 4 digits
# Place: stricter phone numbers allowing only - or . separators.

# 4. Phone numbers starting with 800 or 900
# Pattern: r'[89]00[-.]\d\d\d[-.]\d\d\d\d'
#   [89]     → first digit must be 8 or 9
#   00       → literal 00
#   [-.]     → dash or dot
#   \d\d\d   → 3 digits
#   [-.]     → separator
#   \d\d\d\d → 4 digits
# Place: matches numbers like 800-xxx-xxxx or 900.xxx.xxxx.

# 5. Digits 1 to 5
# Pattern: r'[1-5]'
#   [ ]      → character class
#   1-5      → any digit from 1 to 5
# Place: matches a single digit in that range.

# 6. Lowercase a to z
# Pattern: r'[a-z]'
#   [ ]      → character class
#   a-z      → range from a to z
# Place: matches one lowercase letter.

# 7. Lowercase + Uppercase letters
# Pattern: r'[a-zA-Z]'
#   a-z      → lowercase
#   A-Z      → uppercase
# Place: matches a single alphabet letter.

# 8. Non-letters
# Pattern: r'[^a-zA-Z]'
#   [ ]      → character class
#   ^        → negation inside [] (not a-zA-Z)
# Place: matches characters that are NOT letters.

# 9. Match 'cat', 'pat' but not 'bat'
# Pattern: r'\b(?:cat|pat)\b'
#   \b          → word boundary
#   (?:cat|pat) → non-capturing group: either 'cat' or 'pat'
#   \b          → word boundary
# Place: matches whole words 'cat' and 'pat' only.

# 10. Phone numbers using {n} quantifiers
# Pattern: r'\d{3}[-.*]\d{3}[-.*]\d{4}'
#   \d{3}     → 3 digits
#   [-.*]     → separator (dash, dot, or star)
#   \d{3}     → 3 digits
#   [-.*]     → separator
#   \d{4}     → 4 digits
# Place: matches phone numbers like 123-456-7890, 123.456.7890, 123*456*7890.

# 11. Literal 'Mr.'
# Pattern: r'Mr\.'
#   Mr        → literal
#   \.        → literal dot
# Place: matches exactly "Mr.".

# 12. Match 'Mr' and 'Mr.'
# Pattern: r'Mr\.?'
#   Mr        → literal
#   \.?       → optional dot
# Place: matches "Mr" or "Mr.".

# 13. 'Mr' or 'Mr.' followed by single capital
# Pattern: r'Mr\.?\s[A-Z]'
#   Mr\.?     → Mr or Mr.
#   \s        → whitespace
#   [A-Z]     → capital letter
# Place: captures title + single capital initial.

# 14. 'Mr' or 'Mr.' + proper name (≥2 chars)
# Pattern: r'Mr\.?\s[A-Z]\w+'
#   Mr\.?     → Mr or Mr.
#   \s        → space
#   [A-Z]     → capital start
#   \w+       → one or more word chars
# Place: ensures at least two-letter names.

# 15. 'Mr' or 'Mr.' + name (even 1 char)
# Pattern: r'Mr\.?\s[A-Z]\w*'
#   Mr\.?     → Mr or Mr.
#   \s        → space
#   [A-Z]     → capital start
#   \w*       → zero or more chars
# Place: allows names like "Mr A".

# 16. Titles Mr/Ms/Mrs + name
# Pattern: r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'
#   (Mr|Ms|Mrs) → group for title
#   \.?         → optional dot
#   \s          → space
#   [A-Z]\w*    → capital + word chars
# Place: matches "Mr John", "Ms Dibya", etc.

# 17. Emails with only letters, .com
# Pattern: r'[a-zA-Z]+@[a-zA-Z]+\.com'
#   [a-zA-Z]+  → local part (letters only)
#   @          → literal
#   [a-zA-Z]+  → domain (letters only)
#   \.com      → literal extension
# Place: matches like abc@xyz.com.

# 18. Allow '.' in local part
# Pattern: r'[a-zA-Z.]+@[a-zA-Z]+\.com'
#   [a-zA-Z.]+ → letters and dots allowed in local
# Place: matches first.last@domain.com.

# 19. Allow .com or .edu
# Pattern: r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)'
#   (com|edu) → alternation
# Place: allows two extensions.

# 20. Allow digits, '-', '.' in local and domain; TLD = com|edu|net
# Pattern: r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)'
#   [a-zA-Z0-9.-]+ → local part with digits, ., -
#   [a-zA-Z-]+     → domain
#   (com|edu|net)  → allowed endings
# Place: more general email structure.

# 21. Emails with TLD length 3–5
# Pattern: r'\w+@\w+\.[a-z]{3,5}'
#   \w+       → local part
#   @\w+      → domain
#   \.[a-z]{3,5} → TLD between 3–5 chars
# Place: matches .com, .info, .email (rejects .c, .company).

# 22. Match URLs (http/https, optional www, host, TLDs)
# Pattern: r'https?://(www\.)?([A-Za-z0-9-]+)((?:\.[A-Za-z]{2,})+)'
#   https?    → http or https
#   ://       → literal
#   (www\.)?  → optional www.
#   ([A-Za-z0-9-]+) → hostname
#   ((?:\.[A-Za-z]{2,})+) → TLD(s), e.g. .com, .co.in
# Place: structured URL match.

# 23. Print groups for URL
#   group(0) → full URL
#   group(1) → www. (if present)
#   group(2) → hostname
#   group(3) → TLD(s)

# 24. Dates YYYY-MM-DD
# Pattern: r'\b\d{4}-\d{2}-\d{2}\b'
#   \d{4} → year
#   -     → literal dash
#   \d{2} → month
#   -     → dash
#   \d{2} → day
# Place: matches 2024-07-31.

# 25. Words ending with 'at'
# Pattern: r'\b\w*at\b'
#   \b     → word boundary
#   \w*    → zero or more letters
#   at     → literal
#   \b     → boundary
# Place: matches cat, hat, mat.

# 26. Only 'cat' or 'pat'
# Pattern: r'\b[cp]at\b'
#   [cp]   → c or p
#   at     → literal
# Place: only cat/pat.

# 27. Titles at start of line
# Pattern: r'^(?:Mr|Ms|Mrs)\.?.*$'
#   ^      → line start
#   (?: )  → group without capture
#   Mr|Ms|Mrs → titles
#   \.?    → optional dot
#   .*     → rest of line
#   $      → line end
# Place: matches lines beginning with titles.

# 28. Capture groups for phone numbers
# Pattern: r'(\d{3})[-.*](\d{3})[-.*](\d{4})'
#   (\d{3}) → group1 area code
#   [-.*]   → separator
#   (\d{3}) → group2 prefix
#   [-.*]   → separator
#   (\d{4}) → group3 line number
# Place: splits number into parts.

# 29. Named groups for URLs
# Pattern: r'https?://(?:www\.)?(?P<host>[A-Za-z0-9-]+)(?P<tlds>(?:\.[A-Za-z]{2,})+)'
#   (?P<host> … ) → named group host
#   (?P<tlds> … ) → named group tlds
# Place: allows you to refer groups by name.

# 30. Non-greedy capture between born on ... in
# Pattern: r'born on (.*?) in (.*?)\.'
#   (.*?)   → capture minimal content
# Place: extracts date + city.

# 31. Case-insensitive match of alice/bob
# Pattern: r'\b(?:alice|bob)\b' (re.IGNORECASE)
#   (?: )   → non-capturing group
# Place: matches Alice, ALICE, bob, etc.

# 32. Anchors: match Start...end
# Pattern: r'^Start.*end$'
#   ^       → start
#   Start   → literal
#   .*      → anything
#   end     → literal
#   $       → end
# Place: full-line check.

# 33. Negative lookahead: exclude 800/900
# Pattern: r'^(?![89]00[-.*])\d{3}[-.*]\d{3}[-.*]\d{4}$'
#   ^       → start
#   (?! )   → negative lookahead
#   [89]00  → blocks 800/900
# Place: matches all except 800/900 numbers.

# 34. Standalone 'Mr'
# Pattern: r'\bMr\b'
#   \b   → boundary
# Place: avoids matching 'Mrs'.

# 35. Match literal dot
# Pattern: r'\.'
#   \.   → literal dot
# Place: finds '.' characters.

# 36. Greedy vs non-greedy emails
# Pattern: r'^(.+)@(.+)$'
#   (.+) → greedy local part
#   @    → literal
#   (.+) → greedy domain part
# Place: captures whole line split at '@'.

# 37. Simplified email regex
# Pattern: r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
#   [..]+  → local part
#   @      → literal
#   [..]+  → domain
#   \.[A-Za-z]{2,} → TLD at least 2 chars
# Place: general email.

# 38. Title + Name groups
# Pattern: r'\b(Mr|Ms|Mrs)\.?\s([A-Z]\w+)\b'
#   (Mr|Ms|Mrs) → group1 title
#   \.?         → optional dot
#   \s          → space
#   ([A-Z]\w+)  → group2 name
# Place: extracts title + name separately.

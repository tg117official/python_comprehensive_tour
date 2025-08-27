import re

def main():
    # Sample text
    text = "The quick brown fox jumps over the lazy dog."
    # 1. Matching whole words consisting of one or more alphabetic characters
    word_pattern = r'\b[A-Za-z]+\b'
    print("1. Matching whole words consisting of one or more alphabetic characters:")
    print(re.findall(word_pattern, text))
    print()

    # 2. Matching a phone number in the format XXX-XXX-XXXX
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    phone_text = "Call me at 123-456-7890 or 987-654-3210"
    print("2. Matching phone numbers in the format XXX-XXX-XXXX:")
    print(re.findall(phone_pattern, phone_text))
    print()

    # 3. Matching a five-digit ZIP code
    zip_pattern = r'^\d{5}$'
    zip_codes = ["12345", "456789", "9876", "123456"]
    print("3. Matching five-digit ZIP codes:")
    for code in zip_codes:
        if re.match(zip_pattern, code):
            print(code)
    print()

    # 4. Matching an email address
    email_pattern = r'^\w+@\w+\.\w+$'
    emails = ["example@example.com", "invalid-email.com", "test@123.abc"]
    print("4. Matching email addresses:")
    for email in emails:
        if re.match(email_pattern, email):
            print(email)
    print()

    # 5. Matching comma-separated integers with optional thousands separators
    num_pattern = r'\b\d{1,3}(,\d{3})*\b'
    numbers = ["1,000", "10,000", "100,000", "1,000,000"]
    print("5. Matching comma-separated integers with optional thousands separators:")
    for number in numbers:
        if re.match(num_pattern, number):
            print(number)
    print()

    # 6. Matching capitalized words
    cap_pattern = r'\b[A-Z][a-z]*\b'
    cap_text = "The Quick Brown Fox Jumps Over The Lazy Dog."
    print("6. Matching capitalized words:")
    print(re.findall(cap_pattern, cap_text))
    print()

    # 7. Matching dates in the format mm/dd/yyyy or m/d/yy
    date_pattern = r'\b\d{1,2}/\d{1,2}/\d{2,4}\b'
    dates = ["12/25/2022", "1/1/22", "15/02/2023", "02/30/2024"]
    print("7. Matching dates in the format mm/dd/yyyy or m/d/yy:")
    for date in dates:
        if re.match(date_pattern, date):
            print(date)
    print()

    # 8. Matching US phone numbers in various formats
    phone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    phones = ["(123) 456-7890", "123-456-7890", "123.456.7890", "1234567890"]
    print("8. Matching US phone numbers in various formats:")
    for phone in phones:
        if re.match(phone_pattern, phone):
            print(phone)
    print()

    # 9. Matching the word "python" case-insensitively
    python_pattern = r'(?i)python'
    python_text = "Python is a powerful programming language."
    print("9. Matching the word 'python' case-insensitively:")
    print(re.findall(python_pattern, python_text))
    print()

    # 10. Matching a password that contains at least one digit, one lowercase letter,
    # one uppercase letter, one non-word character, and is at least eight characters
    # long
    password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$'
    passwords = ["Password123!", "weakpassword", "Strong!"]
    print("10. Matching passwords with specific criteria:")
    for password in passwords:
        if re.match(password_pattern, password):
            print(password)
    print()


if __name__ == "__main__":
    main()

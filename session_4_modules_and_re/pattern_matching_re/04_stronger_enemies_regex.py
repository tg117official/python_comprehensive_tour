import re

def regex_operations_example():
    # Sample text
    text = "The quick brown fox jumps over the lazy dog."

    # Basic Search
    search_pattern = r'fox'
    search_match = re.search(search_pattern, text)
    if search_match:
        print("Basic search:", search_match.group())

    # Basic Match
    match_pattern = r'\bfox\b'
    # \b    :   This is a word boundary anchor in regular expressions.
    #           It matches a position where a word character
    #           (like a letter or digit) is not followed or preceded by another
    #           word character.
    #           In other words, it matches the empty string at the beginning or end of
    #           a word.
    #           Here, \b ensures that the word "fox" is matched as a whole word, not as part
    #           of another word.
    # fox   : This is the literal string "fox" that we want to match.
    # \b    : This is another word boundary anchor, ensuring that "fox" is matched as
    #           a whole word.

    match_match = re.match(match_pattern, text)
    if match_match:
        print("Basic match:", match_match.group())
    else:
        print("No match found.")

    # Substitution
    sub_pattern = r'\bfox\b'
    sub_text = re.sub(sub_pattern, 'cat', text)
    print("Substitution:", sub_text)

    # Splitting
    split_pattern = r'\s+'
    # '\s+' : This is the regular expression pattern itself. Let's break it
    #         down further:
    # \s    : This is a special character class in regular expressions that matches
    #         any whitespace character, such as space, tab, newline, etc.
    # +     : This is a quantifier that matches one or more occurrences of the
    #         preceding element (in this case, whitespace characters).
    #         So, \s+ matches one or more whitespace characters.
    split_text = re.split(split_pattern, text)
    print("Splitting:", split_text)

    # Flags (case-insensitive matching)
    flags_pattern = r'quick'
    flags_match = re.search(flags_pattern, text, re.IGNORECASE)
    if flags_match:
        print("Flags (case-insensitive) match:", flags_match.group())

    # Finding all matches
    findall_pattern = r'\b\w{3}\b'
    # `\b`  : This is a word boundary anchor in regular expressions. It matches a
    #         position where a word character (like a letter or digit) is not followed
    #         or preceded by another word character. In other words, it matches the
    #         empty string at the beginning or end of a word.
    #
    # `\w`  : This is a shorthand character class in regular expressions that matches
    #         any word character. Word characters include letters (both uppercase and
    #         lowercase), digits, and underscores.
    #
    # `{3}` : This is a quantifier that matches exactly three occurrences of the
    #         preceding element (in this case, `\w`). So, `\w{3}` matches exactly three
    #         word characters.
    #
    # `\b`  : This is another word boundary anchor, ensuring that the three-word
    #         characters matched by `\w{3}` are surrounded by word boundaries. It
    #         ensures that we match whole words that are exactly three characters
    #         long.
    findall_matches = re.findall(findall_pattern, text)
    print("Finding all matches:", findall_matches)

if __name__ == "__main__":
    regex_operations_example()

# Import the re module for regular expressions
import re

# Define a function to demonstrate regex operations
def regex_operations_example():
    # Sample text
    text = "The quick brown fox jumps over the lazy dog."

    # Literal Characters
    # Define a pattern to match the literal string "fox"
    literal_pattern = r'fox'
    # Search for the pattern in the text
    literal_match = re.search(literal_pattern, text)
    # If a match is found, print the matched text
    if literal_match:
        print("Literal match found:", literal_match.group())
    # group(): Returns the string matched by the regular expression.
    # start(): Returns the starting index of the match.
    # end(): Returns the ending index of the match.
    # span(): Returns a tuple containing the (start, end) indices of the match.
    # groups(): Returns a tuple containing all the subgroups of the match.

    # find all occurences of r'fox'
    literal_matches = re.findall(literal_pattern, text)
    print(literal_matches)

    # Character Classes
    # Define a pattern to match any vowel
    char_class_pattern = r'[aeiou]'
    # Search for the pattern in the text
    char_class_match = re.search(char_class_pattern, text)
    # Find all matches of the pattern in the text
    char_class_matches = re.findall(char_class_pattern, text)
    # If a match is found, print the matched text
    if char_class_match:
        print("Character class match found:", char_class_match.group())
    if char_class_matches:
        print("Character class matches found:", char_class_matches)


    # Quantifiers
    # Define a pattern to match words with exactly 5 characters
    quantifier_pattern = r'\b\w{5}\b'
    # Search for the pattern in the text
    quantifier_match = re.search(quantifier_pattern, text)
    # If a match is found, print the matched text
    if quantifier_match:
        print("Quantifier match found:", quantifier_match.group())
    # findall
    quantifier_matches = re.findall(quantifier_pattern, text)
    print("Quantifier matches found:", quantifier_matches)



    # Anchors
    # Define a pattern to match the word "The" at the beginning of the text(caret)
    anchor_pattern = r'^The'
    # Search for the pattern in the text
    anchor_match = re.search(anchor_pattern, text)
    # If a match is found, print the matched text
    if anchor_match:
        print("Anchor match found:", anchor_match.group())

    # Wildcards
    # Define a pattern to match "lazy" followed by any character
    wildcard_pattern = r'lazy.'
    # lazy  : This part of the pattern matches the literal string "lazy".
    # .     : This part of the pattern matches any single character except a newline.
    # this pattern will match strings like "lazy ", "lazy!", "lazy?", "lazy5", etc.,
    # where the last character can be anything except a newline character.

    # Search for the pattern in the text
    wildcard_match = re.search(wildcard_pattern, text)
    # If a match is found, print the matched text
    if wildcard_match:
        print("Wildcard match found:", wildcard_match.group())
    wildcard_matches = re.findall(wildcard_pattern, text)
    print(wildcard_matches)

    # Escape Characters
    # Define a pattern to match a period (escaped with '\')
    escape_pattern = r'\.'
    # \.    : This is a literal period (dot) character. In regular expressions,
    #         the period (.) has a special meaning; it matches any single character
    #         except newline. However, by preceding the dot with a backslash (\),
    #         we are escaping it, which means we are treating it as a literal dot
    #         character that needs to be matched exactly.

    # Search for the pattern in the text
    escape_match = re.search(escape_pattern, text)
    # If a match is found, print the matched text
    if escape_match:
        print("Escape match found:", escape_match.group())

    # Alternation
    # Define a pattern to match either "fox" or "dog"
    alternation_pattern = r'fox|dog'
    # Search for the pattern in the text
    alternation_match = re.search(alternation_pattern, text)
    # If a match is found, print the matched text
    if alternation_match:
        print("Alternation match found:", alternation_match.group())
    alternation_matches = re.findall(alternation_pattern, text)
    print(alternation_matches)

    # Grouping
    # Define a pattern to capture groups of words
    grouping_pattern = r'(\b\w{5}\b).*?(\b\w{3}\b)'
    #  `(`: This parenthesis starts a capturing group. Capturing groups allow you
    #       to capture and extract substrings that match certain parts of the pattern.
    #
    # `\b`: This is a word boundary anchor in regular expressions. It matches
    #       a position where a word character (like a letter or digit) is not
    #       followed or preceded by another word character. In other words, it
    #       matches the empty string at the beginning or end of a word.
    #
    # `\w{5}`: This matches exactly five word characters. `\w` is a shorthand
    #          character class in regular expressions that matches any word character
    #          (letters, digits, and underscores), and `{5}` is a quantifier that
    #          specifies the exact number of occurrences to match.
    #
    # `\b`: Another word boundary anchor, ensuring that the five-word characters
    #       matched by `\w{5}` are surrounded by word boundaries. It ensures that
    #       we match whole words that are exactly five characters long.
    #
    # `)`: This parenthesis ends the first capturing group.
    #
    # `.*?`: This matches any characters (except newline) zero or more times,
    #        as few times as possible.
    #       - .: The dot (.) in a regular expression matches any single character
    #            except newline.
    #       - *: The asterisk (*) is a quantifier that specifies that the preceding
    #            element (in this case, .) can be matched zero or more times. So,
    #            .* matches any sequence of characters of any length, including an
    #            empty string.
    #       - ?: This is a non-greedy quantifier, which makes the preceding
    #            quantifier (* in this case) match as few times as possible, as
    #            opposed to the default behavior of matching as many times as
    #            possible (greedy behavior).
    #
    # `\b`: This is a word boundary anchor, matching the empty string at
    #       the beginning or end of a word.
    #
    # `\w{3}`: This matches exactly three word characters.
    #
    # `\b`: Another word boundary anchor, ensuring that the three-word characters
    #       matched by `\w{3}` are surrounded by word boundaries.
    #
    # `)`: This parenthesis ends the second capturing group.
    #
    # So, the regular expression pattern `r'(\b\w{5}\b).*?(\b\w{3}\b)'` captures
    # two groups of word characters: one group that is exactly five characters long
    # and another group that is exactly three characters long, with any characters
    # in between.

    # Search for the pattern in the text
    grouping_match = re.search(grouping_pattern, text)
    # If a match is found, print the captured groups
    if grouping_match:
        print("Grouping match found:")
        print("Group 1:", grouping_match.group(1))
        print("Group 2:", grouping_match.group(2))

    # Character Escapes
    # Define a pattern to match digits
    escape_chars_pattern = r'\d+'
    # `\d`: This is a shorthand character class in regular expressions that matches
    #       any digit character. It's equivalent to the character class `[0-9]`,
    #       which matches any character from 0 to 9.
    #
    # `+`: This is a quantifier that matches one or more occurrences of the preceding
    #      element (in this case, `\d`). So, `\d+` matches one or more digit
    #      characters in a row.
    #
    # So, the regular expression pattern `r'\d+'` matches one or more consecutive
    # digit characters in a text. It can match numbers like "0", "123", "456789", etc.

    # Text with numbers
    escape_chars_text = "The price is $50."
    # Search for the pattern in the text
    escape_chars_match = re.search(escape_chars_pattern, escape_chars_text)
    # If a match is found, print the matched text
    if escape_chars_match:
        print("Escape characters match found:", escape_chars_match.group())

# Execute the function if the script is run directly
if __name__ == "__main__":
    regex_operations_example()

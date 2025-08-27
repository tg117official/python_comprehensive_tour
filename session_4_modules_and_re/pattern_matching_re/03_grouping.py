grouping_pattern = r'(\b\w{5}\b).*?(\b\w{3}\b)'
# 1. `(\b\w{5}\b)`:
#    - `\b` - This asserts a word boundary, meaning it matches positions where a
#             word character is next to a non-word character or at the start/end
#             of a string. It ensures the pattern matches whole words.
#    - `\w{5}` - The `\w` matches any word character (equivalent to `[a-zA-Z0-9_]`),
#                and `{5}` specifies exactly 5 occurrences of `\w`. Thus, `\w{5}` matches
#                any sequence of exactly 5 word characters.
#    - `\b` - Another word boundary, ensuring the word has exactly 5 characters with no
#             more letters attached.
#
#    This whole group `(\b\w{5}\b)` captures a whole word of exactly 5 characters long.
#
# 2. `.*?`:
#    - `.*?` - The `.` matches any character (except for a newline), and `*` quantifier
#              means "0 or more times". The `?` after the `*` makes the quantifier lazy
#              (non-greedy), meaning it matches as few characters as possible while still
#              allowing the overall pattern to match.
#    - This part tries to find the shortest sequence of any characters (including none)
#      until the next part of the pattern is found.
#
# 3. `(\b\w{3}\b)`:
#    - This is structured like the first group but matches exactly 3 word characters.
#    - This group captures a whole word of exactly 3 characters long.
#
# ### Putting It All Together
#
# The entire pattern `r'(\b\w{5}\b).*?(\b\w{3}\b)'` looks for two words in a text:
# - The first word must be exactly 5 characters long.
# - The second word must be exactly 3 characters long.
# - There may be any characters (as few as possible) between these two words.
#
# ### Example Texts This Pattern Will Match
#
# 1. Text: "Those birds are flying."
#    - Matches: "Those" (5 characters) and "are" (3 characters)
#    - Explanation: The first group captures "Those", then skips "birds" which is neither
#                   5 nor 3 characters long, and finally, the second group captures "are".
#
# 2. Text: "Every great story deserves retelling."
#    - Matches: "Every" (5 characters) and "story" (3 characters, but won't be matched
#                due to position)
#    - Explanation: Here, "Every" is captured by the first group, but since "story" has
#                   more than 3 characters, and no other suitable 3-character word follows,
#                   this wouldn't fully match unless you consider "ret" part of "retelling"
#                   , but "retelling" itself isn't a match.
#
# 3. Text: "Happy days are here."
#    - Matches: "Happy" (5 characters) and "are" (3 characters)
#    - Explanation: The pattern captures "Happy" first and then finds "are", ignoring
#      "days" and "here" because they don't fit the required lengths.

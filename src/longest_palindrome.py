"""Find the longest palindrome in a string."""


def longest_palindrome(s):
    """Return the len of longest palindrome."""
    longest_substr = ''
    for start_idx in range(len(s)):
            for len_substr in range(len(s) - start_idx + 1):
                substr = s[start_idx:start_idx + len_substr]
                if len_substr > len(longest_substr) and substr == substr[::-1]:
                    longest_substr = substr
    return len(longest_substr)

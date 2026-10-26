"""Checks whether a string contains a palindromic substring."""

def contains_palindrome(s):
    """Returns True if any substring of s (case-insensitive) is a palindrome.

    Note: single characters count as palindromes, so any non-empty string
    returns True.
    """
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                return True
    return False


# Example usage
INPUT_STRING = "racecar and aca are a palindrome"
RESULT = contains_palindrome(INPUT_STRING)
print(f"Is there a palindrome in the input string? {RESULT}")

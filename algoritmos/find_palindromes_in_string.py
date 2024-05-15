
def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                return True
    return False


# Example usage
input_string = "racecfar and aca are a palindrome"
result = is_palindrome(input_string)
print(f"Is there a palindrome in the input string? {result}")
#print(f"if so, how many? {}")
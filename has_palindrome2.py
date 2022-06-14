"""
input a string and determine if it has a palindrome.
"""
def has_palindrome(num):
   if not isinstance(num, int) or num < 0:
      return "Not valid"
   snum = str(num)
   for i in range(1, len(snum)):
     if snum[i - 1] == snum[i] or (i < len(snum) - 1 and snum[i - 1] == snum[i + 1]):
      return True
   return False


if __name__ == "__main__":
    assert has_palindrome(868) is True
    assert has_palindrome("868") == "Not valid"
    assert has_palindrome(2) is False
    assert has_palindrome(22) is True
    assert has_palindrome(-22) == "Not valid"
    assert has_palindrome(12345321) is False
    assert has_palindrome(1221) is True
    assert has_palindrome("NEUQUEN") == "Not valid"
    assert has_palindrome("33>22") == "Not valid"
    print("All test passed!")

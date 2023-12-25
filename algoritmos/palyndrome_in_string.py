def is_palindrome(s):
    return s == s[::-1]


def find_palindromes(i_string):
    palindromes = []
    words = i_string.split()

    for word in words:
        if is_palindrome(word):
            palindromes.append(word)

    return palindromes


input_string = input("Enter a sentence or paragraph: ")
palindromes_found = find_palindromes(input_string)

if palindromes_found:
    print("Palindromes found:")
    for palindrome in palindromes_found:
        print(palindrome)
else:
    print("No palindromes found in the input.")

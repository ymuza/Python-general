
def find_palindromes_in_sub_string(any_input, j, k):
  count = 0
  while j >= 0 and k < len(any_input):
    if any_input[j] != any_input[k]:
      break
    print(any_input[j: k + 1])
    count += 1

    j -= 1
    k += 1

  return count


def find_all_palindrome_substrings(any_input):
  count = 0
  for i in range(0, len(any_input)):
    count += find_palindromes_in_sub_string(any_input, i - 1, i + 1)
    count += find_palindromes_in_sub_string(any_input, i, i + 1)

 # return count


s = "aabbbaa"
#print("Total palindrome substrings: ", find_all_palindrome_substrings(s))
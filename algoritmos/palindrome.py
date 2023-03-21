def has_palindrome(num):
    total_length = len(str(num))
    if type(num) is not str and num > 10:
        for n in range(0, total_length):
            if str(n) == str(n)[::-1]:
                return True

            else:
                return False

    else:
        print("is invalid")


print(has_palindrome(124))

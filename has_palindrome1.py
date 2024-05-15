def has_palindrome(num):
    i = 0
    j = 0
    if type(num) is not str and num > 10:
        for n in range(1, len(str(num))):
            i = n - 1
            j = n + 1
            print(j)
        while i >= 0 and j < len(str(num)):
            if str(num)[i] != str(num)[j]:
                return True
            i -= 1
            j += 1
        else:
            return False
    else:
        print("invalid")


print(has_palindrome(121))

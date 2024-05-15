def has_palindrome(num):
    #total_length = len(str(num))
    if type(num) is not str and num > 10:
        for _ in str(num):
            if str(num) == str(num)[::-1]:

                return True

            else:
                return False

    else:
        print("is invalid")


print(has_palindrome(101))
#print(str(122)[::-1])


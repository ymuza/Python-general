def test_primeNumber(n):
    if n == 1:
        return False
    elif n == 2:
        return True;
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


print(test_primeNumber(13))


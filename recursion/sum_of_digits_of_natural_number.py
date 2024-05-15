"""
recursive case - flow
---------------------
example => 10

10/10 = 1 . The remaining  = 0
54/10 = 5 . The remaining  = 4

112/10 = 11 . The remaining = 2 . Now if we do 11/10 , the remains are 1.
so:
    f(n) = n%10 + f(n/10) => the remains + f(n/10)
"""


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        if n < 0 and isinstance(n, int) :
            raise ValueError("n is not a natural number")
        else:
            return int(n%10) + sum_of_digits(int(n/10))


print(sum_of_digits(20002))

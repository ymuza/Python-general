"""Prints the prime numbers in a range using a for/else loop."""

START = 25
END = 50
print("Prime numbers between", START, "and", END, "are:")

for num in range(START, END + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
